from help_functions import *

ALL_PLAYERS = {
    "Rémi": 1,
    "Aimeric": 1,
    "Rudy": 1,
    "Titou": 1,
    "Léo": 2,
    "Hugo": 2,
    "Thomas": 2,
    "Vincent": 2,
    "Emma": 3,
    "Anna": 3,
    "Nils": 3,
    "Guillaume": 3,
    "Pro 1": 1,
    "Pro 2": 1,
    "Pro 3": 1,
    "Pro 4": 1,
    "Inter 1": 2,
    "Inter 2": 2,
    "Inter 3": 2,
    "Inter 4": 2,
    "Debut 1": 3,
    "Debut 2": 3,
    "Debut 3": 3,
    "Debut 4": 3,
}
selected_names = list(ALL_PLAYERS.keys())
players = [(name, ALL_PLAYERS[name], 0) for name in selected_names]

# players = list(ALL_PLAYERS.items())
random.shuffle(players)
L1 = [p for p in players if p[1] == 1]
L2 = [p for p in players if p[1] == 2]
L3 = [p for p in players if p[1] == 3]

# appel moteur
matches, rest = build_matches(L1, L2, L3, 4)
print(matches, rest)
print_matches_and_rest(matches, rest)
# print(L1, L2, L3)
