import streamlit as st


# =========================================================
# AJOUT TEMPORAIRE D'UN JOUEUR
# =========================================================
def add_temporary_player(list_players):
    st.sidebar.subheader("Ajouter un joueur")

    with st.sidebar.form("add_player_form", clear_on_submit=True):
        new_name = st.text_input("Nom")

        new_level = st.selectbox("Niveau", ["pro", "inter", "debutant"])

        new_sex = st.selectbox("Sexe", ["M", "F"])

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


def generate_rounds():
    st.sidebar.header("Configuration des rounds")
    rounds = []

    for round_number in [1, 2, 3, 4]:
        count = st.sidebar.number_input(
            f"Round {round_number}",
            min_value=0,
            value=0,
            step=1,
            key=f"round_count_{round_number}",
        )

        rounds.extend([round_number] * count)

    st.sidebar.header("Configuration")
    # round_ = st.sidebar.selectbox("Choisir le round", [1, 2, 3, 4])
    # women_round = st.sidebar.selectbox("Mettre round féminin", ["oui", "non"])
    st.sidebar.write("1 -> Mix pro/inter")
    st.sidebar.write("2 -> Mix pro/debutants")
    st.sidebar.write("3 -> Mix inter/debutants")
    st.sidebar.write("4 -> Mix au minimum")
    return rounds
