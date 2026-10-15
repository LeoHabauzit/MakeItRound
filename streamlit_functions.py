import random

import streamlit as st


# =========================================================
# AJOUT TEMPORAIRE D'UN JOUEUR
# =========================================================
def add_temporary_player(list_players):
    st.sidebar.subheader("Ajouter un joueur")

    with st.sidebar.form("add_player_form", clear_on_submit=True):
        new_name = st.text_input("Nom")

        new_level = st.selectbox("Niveau", [1, 2, 3])

        new_sex = st.selectbox("H/F", ["m", "w"])

        add_player = st.form_submit_button("Ajouter temporairement")

        if add_player:
            if not new_name.strip():
                st.error("Veuillez renseigner un nom.")

            elif new_name in list_players:
                st.warning("Ce joueur existe déjà.")

            else:
                st.session_state.temporary_players[new_name] = {
                    "level": new_level,
                    "sex": new_sex,
                }

                st.success(f"{new_name} ajouté temporairement.")

                # Force le script à se relancer
                st.rerun()
    with st.sidebar.expander("Signification des niveaux"):
        # round_ = st.sidebar.selectbox("Choisir le round", [1, 2, 3, 4])
        # women_round = st.sidebar.selectbox("Mettre round féminin", ["oui", "non"])
        st.write("1 -> pro")
        st.write("2 -> Intermédiaire")
        st.write("3 -> Débutant")
    st.sidebar.divider()


def generate_rounds():
    st.sidebar.header("Configuration des rounds")

    # Nombre total de rounds
    number_of_rounds = st.sidebar.number_input(
        "Nombre de rounds",
        min_value=1,
        value=4,
        step=1,
        key="number_of_rounds",
    )
    st.sidebar.divider()
    rounds = []
    # Configuration de chaque round
    for round_number in range(1, number_of_rounds + 1):
        round_type = st.sidebar.number_input(
            f"Round {round_number}",
            min_value=1,
            max_value=4,
            value=round_number,
            step=1,
            key=f"round_type_{round_number}",
        )

        rounds.append(round_type)
    with st.sidebar.expander("Signification des configurations"):
        st.caption("1 → Mix pro/inter")
        st.caption("2 → Mix pro/débutants")
        st.caption("3 → Mix inter/débutants")
        st.caption("4 → Mix au minimum")

    return rounds


def generate_lvl_bye(rounds, players):
    st.sidebar.header("Configuration lvl des byes")

    n_bye = len(players) % 4
    bye_rounds = []

    for round_number in range(len(rounds)):
        st.sidebar.subheader(f"Round {round_number + 1}")

        round_byes = []

        if n_bye > 0:
            cols = st.sidebar.columns(n_bye)

            for i in range(n_bye):
                with cols[i]:
                    bye_person = st.number_input(
                        f"Bye {i + 1}",
                        min_value=1,
                        max_value=3,
                        value=random.randint(1, 3),
                        step=1,
                        key=f"round_type_{round_number}_{i}",
                    )

                    round_byes.append(bye_person)

        bye_rounds.append(round_byes)

    st.sidebar.divider()
    return bye_rounds
