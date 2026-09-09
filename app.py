import streamlit as st
from help_functions import *
# ⚠️ toutes tes fonctions sont importées ailleurs
# from engine import build_matches, find_best_rest_match


# =========================================================
# BASE JOUEURS
# =========================================================

ALL_PLAYERS = {
    "Alice": 1,
    "Bob": 2,
    "Charlie": 3,
    "David": 1,
    "Emma": 2,
    "Fred": 3,
    "George": 2,
    "Hugo": 1,
}


# =========================================================
# UI
# =========================================================

st.title("🏐 Roundnet Match Generator")

st.sidebar.header("Configuration")

round_ = st.sidebar.selectbox("Choisir le round", [1, 2, 3, 4])


# =========================================================
# SELECTION JOUEURS
# =========================================================

st.subheader("👥 Joueurs présents")

selected_names = st.multiselect(
    "Sélectionne les joueurs présents à l'entraînement", list(ALL_PLAYERS.keys())
)


# transformation en format moteur
players = [(name, ALL_PLAYERS[name], 0) for name in selected_names]


st.write("### Joueurs sélectionnés")
st.write(players)


# =========================================================
# GENERATION MATCHS
# =========================================================

if st.button("🚀 Générer les matchs"):
    if len(players) < 4:
        st.warning("Il faut au moins 4 joueurs pour générer un match")
        st.stop()

    # split par niveau
    L1 = [p for p in players if p[1] == 1]
    L2 = [p for p in players if p[1] == 2]
    L3 = [p for p in players if p[1] == 3]

    # appel moteur
    matches, rest = build_matches(L1, L2, L3, round_)

    # =====================================================
    # AFFICHAGE MATCHS
    # =====================================================

    st.subheader("📊 Matchs générés")

    if not matches:
        st.info("Aucun match généré")
    else:
        for i, m in enumerate(matches, 1):
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

    # =====================================================
    # MATCH DES RESTES
    # =====================================================

    st.subheader("⚡ Match des restes (optimisé)")

    if len(rest) >= 4:
        best_match, new_rest = find_best_rest_match(rest)

        if best_match:
            st.markdown("### Team A")
            for p in best_match["teamA"]:
                st.write(f"{p[0]} (lvl {p[1]})")

            st.markdown("### Team B")
            for p in best_match["teamB"]:
                st.write(f"{p[0]} (lvl {p[1]})")

            st.write("### Restants finaux")
            st.write(new_rest)

    elif rest:
        st.info("Pas assez de joueurs pour un match des restes")
