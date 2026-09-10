from help_functions import *
import streamlit as st
import pandas as pd


df = pd.read_excel("alpes_roundnet.xlsx")

ALL_PLAYERS = {
    row["Nom"]: {
        "level": row["level"],
        "sex": row["sex"],
    }
    for _, row in df.iterrows()
}

st.title("Make it round")

st.sidebar.header("Configuration")
round_ = st.sidebar.selectbox("Choisir le round", [1, 2, 3, 4])
women_round = st.sidebar.selectbox("Mettre round féminin", ["oui", "non"])
st.sidebar.info("1 -> Mix pro/inter")
st.sidebar.info("2 -> Mix pro/debutants")
st.sidebar.info("3 -> Mix inter/debutants")
st.sidebar.info("4 -> Mix au minimum")

# =========================================================
# SELECTION JOUEURS
# =========================================================


selected_names = st.multiselect(
    "Sélectionne les joueurs présents à l'entraînement", list(ALL_PLAYERS.keys())
)

players = [
    (name.title(), ALL_PLAYERS[name]["level"], ALL_PLAYERS[name]["sex"])
    for name in selected_names
]
random.shuffle(players)


# =========================================================
# GENERATION MATCHS
# =========================================================

if st.button("🚀 Générer les matchs"):
    if len(players) < 4:
        st.warning("Il faut au moins 4 joueurs pour générer un match")
        st.stop()

    matches = []
    rest = []
    if women_round == "oui":
        women_players = [p for p in players if p[2] == "w"]
        players = [p for p in players if p[2] == "m"]
        L1_w, L2_w, L3_w = get_level_list_players(women_players)
        print("levels : ", L1_w, L2_w, L3_w)
        matches, rest = build_matches(L1_w, L2_w, L3_w, round_, matches, rest)
    # appel moteur
    L1, L2, L3 = get_level_list_players(players)
    matches, rest = build_matches(L1, L2, L3, round_, matches, rest)
    print(matches)
    # =====================================================
    # AFFICHAGE MATCHS
    # =====================================================

    # st.subheader("Matchs")

    if not matches:
        st.info("Aucun match généré")
    else:
        for i, m in enumerate(matches, 1):
            print(i)
            st.markdown(f"### Match {i}")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("#### 🟦 Team A")
                for p in m["teamA"]:
                    st.write(f"{p[0]} (lvl {p[1]})")

            with col2:
                st.markdown("#### 🟥 Team B")
                for p in m["teamB"]:
                    st.write(f"{p[0]} (lvl {p[1]})")

            st.divider()

    # =====================================================
    # RESTE
    # =====================================================
    if len(rest) >= 4:
        best_match, rest = find_best_rest_match(rest)
        if not best_match:
            st.info("Aucun match généré")
        else:
            st.markdown(f"### Match bonus")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### 🟦 Team A")
                for p in best_match["teamA"]:
                    st.write(f"{p[0]} (lvl {p[1]})")
            with col2:
                st.markdown("### 🟥 Team B")
                for p in best_match["teamB"]:
                    st.write(f"{p[0]} (lvl {p[1]})")

    st.subheader("🟡 Joueurs en pause")
    if rest:
        for p in rest:
            st.write(f"{p[0]} (lvl {p[1]})")
    else:
        st.success("Aucun joueur en pause 🎉")
