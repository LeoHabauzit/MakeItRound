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

    st.sidebar.header("Configuration niveaux")
    # round_ = st.sidebar.selectbox("Choisir le round", [1, 2, 3, 4])
    # women_round = st.sidebar.selectbox("Mettre round féminin", ["oui", "non"])
    st.sidebar.write("1 -> pro")
    st.sidebar.write("2 -> Intermédiaire")
    st.sidebar.write("3 -> Débutant")


def generate_rounds():
    st.sidebar.header("Configuration des rounds")

    # Nombre total de rounds
    number_of_rounds = st.sidebar.number_input(
        "Nombre de rounds",
        min_value=1,
        value=1,
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
            value=1,
            step=1,
            key=f"round_type_{round_number}",
        )

        rounds.append(round_type)

    st.sidebar.header("Configuration")
    st.sidebar.write("1 → Mix pro/inter")
    st.sidebar.write("2 → Mix pro/débutants")
    st.sidebar.write("3 → Mix inter/débutants")
    st.sidebar.write("4 → Mix au minimum")
    st.sidebar.divider()
    return rounds
