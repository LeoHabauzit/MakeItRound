from help_functions import *

ALL_PLAYERS = {
    "pro 1": {
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
    "pro 4": {
        "level": 1,
        "sex": "m",
    },
    "inter 1": {
        "level": 2,
        "sex": "m",
    },
    "inter 2": {
        "level": 2,
        "sex": "w",
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
        "sex": "w",
    },
    "debut 2": {
        "level": 3,
        "sex": "w",
    },
    "debut 3": {
        "level": 3,
        "sex": "w",
    },
    # "debut 4": {
    #     "level": 3,
    #     "sex": "m",
    # },
}
# ALL_PLAYERS = {
#     # "Rémi": 1,
#     # "Aimeric": 1,
#     # "Rudy": 1,
#     # "Titou": 1,
#     # "Léo": 2,
#     # "Hugo": 2,
#     # "Thomas": 2,
#     # "Vincent": 2,
#     # "Emma": 3,
#     # "Anna": 3,
#     # "Nils": 3,
#     # "Guillaume": 3,
#     "Pro 1": 1,
#     "Pro 2": 1,
#     "Pro 3": 1,
#     # "Pro 4": 1,
#     "Inter 1": 2,
#     "Inter 2": 2,
#     "Inter 3": 2,
#     # "Inter 4": 2,
#     "Debut 1": 3,
#     "Debut 2": 3,
#     "Debut 3": 3,
#     # "Debut 4": 3,
# }
# names = ALL_PLAYERS.keys()
# params = ALL_PLAYERS.items()
# random.shuffle(ALL_PLAYERS)
# print(params["sex"])

# level_2_players = {
#     name: player for name, player in ALL_PLAYERS.items() if player["level"] == 2
# }
# print(level_2_players)
# selected_names = list(ALL_PLAYERS.keys())
# # print(selected_names)
# players = [(name, ALL_PLAYERS[name], 0) for name in selected_names]
# params = ALL_PLAYERS.items()
# print(params["level"])
# players = list(ALL_PLAYERS.items())
# random.shuffle(players)

# En dictionnaire
# level_1_players = {
#     name: player for name, player in ALL_PLAYERS.items() if player["level"] == 1
# }
# level_2_players = {
#     name: player for name, player in ALL_PLAYERS.items() if player["level"] == 2
# }
# level_3_players = {
#     name: player for name, player in ALL_PLAYERS.items() if player["level"] == 3
# }
players = [
    (name.title(), player["level"], player["sex"])
    for name, player in ALL_PLAYERS.items()
]
random.shuffle(players)
# print(players)

# # Pour avoir la liste des noms de joueurs :
# level_1_players = [name for name, player in ALL_PLAYERS.items() if player["level"] == 1]
# level_2_players = [name for name, player in ALL_PLAYERS.items() if player["level"] == 2]
# level_3_players = [name for name, player in ALL_PLAYERS.items() if player["level"] == 3]
women_match = True
round = 4
matches = []
rest = []
if women_match == True:
    women_players = [p for p in players if p[2] == "w"]
    players = [p for p in players if p[2] == "m"]
    L1_w, L2_w, L3_w = get_level_list_players(women_players)
    matches, rest = build_matches(L1_w, L2_w, L3_w, round)
# print(players)

L1, L2, L3 = get_level_list_players(players)
# # L1 = [p for p in players if p[1] == 1]
# # L2 = [p for p in players if p[1] == 2]
# # L3 = [p for p in players if p[1] == 3]
# # print(women)
# # print(level_1_players)
# # appel moteur
matches, rest = build_matches(L1, L2, L3, 4, matches, rest)
# print(matches, rest)
print_matches_and_rest(matches, rest)
# print(L1, L2, L3)
