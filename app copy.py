import streamlit as st
from help_functions import *
# ⚠️ toutes tes fonctions sont importées ailleurs
# from engine import build_matches, find_best_rest_match


# =========================================================
# BASE JOUEURS
# =========================================================


# ALL_PLAYERS = {
#     "Rémi": 1,
#     "Aimeric": 1,
#     "Rudy": 1,
#     "Titou": 1,
#     "Léo": 2,
#     "Hugo": 2,
#     "Thomas": 2,
#     "Vincent": 2,
#     "Emma": 3,
#     "Anna": 3,
#     "Nils": 3,
#     "Guillaume": 3,
#     "Pro 1": 1,
#     "Pro 2": 1,
#     "Pro 3": 1,
#     "Pro 4": 1,
#     "Inter 1": 2,
#     "Inter 2": 2,
#     "Inter 3": 2,
#     "Inter 4": 2,
#     "Debut 1": 3,
#     "Debut 2": 3,
#     "Debut 3": 3,
#     "Debut 4": 3,
# }
ALL_PLAYERS = {
    "pro 1 F": {
        "level": 1,
        "sex": "w",
    },
    "pro 2": {
        "level": 1,
        "sex": "m",
    },
    "pro 3": {
        "level": 1,
        "sex": "m",
    },
    "pro 4 F": {
        "level": 1,
        "sex": "w",
    },
    "inter 1": {
        "level": 2,
        "sex": "m",
    },
    "inter 2": {
        "level": 2,
        "sex": "m",
    },
    "inter 3": {
        "level": 2,
        "sex": "m",
    },
    # "inter 4": {
    #     "level": 2,
    #     "sex": "m",
    # },
    "debut 1": {
        "level": 3,
        "sex": "m",
    },
    "debut 2 f": {
        "level": 3,
        "sex": "w",
    },
    "debut 3 f": {
        "level": 3,
        "sex": "w",
    },
    # "debut 4": {
    #     "level": 3,
    #     "sex": "m",
    # },
}

# selected_names = st.multiselect(
#     "Sélectionne les joueurs présents à l'entraînement", list(ALL_PLAYERS.keys())
# )

# =========================================================
# UI
# =========================================================

st.title("Make it round")

st.sidebar.header("Configuration")

round_ = st.sidebar.selectbox(
    "Choisir le round", ["Mix pro/deb", "Mix pro/int", "Mix int/deb", "No Mix"]
)
women_round = st.sidebar.selectbox("Mettre round féminin", ["oui", "non"])


# =========================================================
# SELECTION JOUEURS
# =========================================================

st.subheader("👥 Joueurs présents")

selected_names = st.multiselect(
    "Sélectionne les joueurs présents à l'entraînement", list(ALL_PLAYERS.keys())
)


# transformation en format moteur
players = [
    (name.title(), ALL_PLAYERS[name]["level"], ALL_PLAYERS[name]["sex"])
    for name in selected_names
]

# players = list(ALL_PLAYERS.items())
random.shuffle(players)

# ALL_PLAYERS = dict(players)
# st.write("### Joueurs sélectionnés")
# st.write(players)


# =========================================================
# GENERATION MATCHS
# =========================================================

if st.button("🚀 Générer les matchs"):
    if len(players) < 4:
        st.warning("Il faut au moins 4 joueurs pour générer un match")
        st.stop()

    # split par niveau

    # print("levels2 : ", L1, L2, L3)

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

    st.subheader("📊 Matchs générés")

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

    st.subheader("🟡 Joueurs en pause")

    if rest:
        for p in rest:
            st.write(f"{p[0]} (lvl {p[1]})")
    else:
        st.success("Aucun joueur en pause 🎉")

    # # =====================================================
    # # MATCH DES RESTES
    # # =====================================================

    # st.subheader("⚡ Match des restes (optimisé)")

    # if len(rest) >= 4:
    #     best_match, new_rest = find_best_rest_match(rest)

    #     if best_match:
    #         st.markdown("### Team A")
    #         for p in best_match["teamA"]:
    #             st.write(f"{p[0]} (lvl {p[1]})")

    #         st.markdown("### Team B")
    #         for p in best_match["teamB"]:
    #             st.write(f"{p[0]} (lvl {p[1]})")

    #         st.write("### Restants finaux")
    #         st.write(new_rest)

    # elif rest:
    #     st.info("Pas assez de joueurs pour un match des restes")
