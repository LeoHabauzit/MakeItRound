from help_functions import *
from streamlit_functions import *
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
# Initialisation des joueurs temporaires
if "temporary_players" not in st.session_state:
    st.session_state.temporary_players = {}
if "paused_players" not in st.session_state:
    st.session_state.paused_players = []

paused_players = st.session_state.paused_players

# Ajouter les joueurs temporaires à la liste générale
ALL_PLAYERS.update(st.session_state.temporary_players)

st.title("Make it round")
# =========================================================
# CONFIGURATION DES ROUNDS
# =========================================================

rounds = generate_rounds()


# =========================================================
# AJOUT TEMPORAIRE D'UN JOUEUR
# =========================================================
add_temporary_player(ALL_PLAYERS)

# =========================================================
# SELECTION JOUEURS
# =========================================================


selected_names = st.multiselect(
    "Sélectionne les joueurs présents à l'entraînement",
    list(ALL_PLAYERS.keys()),
    key="selected_players",
)


number_of_players = len(selected_names)

# st.metric(label="Nombre de joueurs sélectionnés", value=number_of_players)

players = [
    (name.title(), ALL_PLAYERS[name]["level"], ALL_PLAYERS[name]["sex"])
    for name in selected_names
]
L1, L2, L3 = get_level_list_players(players)
st.write(
    f"Nombre de joueurs : {number_of_players} ({len(L1)} pro /{len(L2)} Intermédiaire / {len(L3)} Débutants)"
)
random.shuffle(players)


# =========================================================
# GENERATION MATCHS
# =========================================================

if st.button("🚀 Générer les matchs"):
    n_round = 0
    # paused_players = []
    for round_ in rounds:
        n_round += 1
        n_match = 0
        random.shuffle(players)
        matches = []
        rest = []
        st.subheader(f"Round {n_round} - type {round_}")

        if len(players) < 4:
            st.warning("Il faut au moins 4 joueurs pour générer un match")
            st.stop()

        paused_players, playing_players, this_round_bye_players = get_playing_players(
            players, paused_players
        )
        # if women_round == "oui":
        #     women_players = [p for p in players if p[2] == "w"]
        #     players = [p for p in players if p[2] == "m"]
        #     L1_w, L2_w, L3_w = get_level_list_players(women_players)
        #     matches, rest = build_matches(L1_w, L2_w, L3_w, round_, matches, rest)

        L1, L2, L3 = get_level_list_players(playing_players)
        matches, rest = build_matches(L1, L2, L3, round_, matches, rest)
        # =====================================================
        # AFFICHAGE MATCHS
        # =====================================================

        if not matches:
            st.write("⚠️ Aucun match du round possible")
        else:
            for i, m in enumerate(matches, 1):
                st.write(
                    f"Match {i} :",
                    "🟥",
                    " / ".join(
                        f"{m['teamA'][j][0]} (l{m['teamA'][j][1]})" for j in [0, 1]
                    ),
                    "vs 🟦 :",
                    " / ".join(
                        f"{m['teamB'][j][0]} (l{m['teamB'][j][1]})" for j in [0, 1]
                    ),
                )
                n_match = i

        # =====================================================
        # RESTE
        # =====================================================

        while len(rest) >= 4:
            best_match, rest = find_best_rest_match(rest)
            n_match += 1
            if not best_match:
                st.write("⚠️ Aucun match généré")
            else:
                st.write(
                    f"Match (r) {n_match} :",
                    "🟥",
                    " / ".join(
                        f"{best_match['teamA'][j][0]} (l{best_match['teamA'][j][1]})"
                        for j in [0, 1]
                    ),
                    "vs 🟦 :",
                    " / ".join(
                        f"{best_match['teamB'][j][0]} (l{best_match['teamB'][j][1]})"
                        for j in [0, 1]
                    ),
                )
        if this_round_bye_players:
            st.write(
                "🟡 Byes : ",
                " / ".join(f"{p[0]} (l{p[1]})" for p in this_round_bye_players),
            )
        else:
            st.write("🟡 Pas de joueurs en pause🎉")
        st.divider()
