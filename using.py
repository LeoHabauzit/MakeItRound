from test2 import *
import numpy as np
import random


def generate_players(l1, l2, l3):
    players = []
    pid = 1

    # niveau 1
    for _ in range(l1):
        players.append((f"P{pid}", 1))
        pid += 1

    # niveau 2
    for _ in range(l2):
        players.append((f"P{pid}", 2))
        pid += 1

    # niveau 3
    for _ in range(l3):
        players.append((f"P{pid}", 3))
        pid += 1
    random.shuffle(players)

    return players


# def build_li_matches(L):
#     """
#     L2 = [(id, 2), ...]
#     retourne des matchs 2v2 uniquement avec lvl2
#     """

#     matches = []

#     # on prend les joueurs par groupe de 4
#     i = 0
#     while i + 3 < len(L2):
#         p1 = L2[i]
#         p2 = L2[i + 1]
#         p3 = L2[i + 2]
#         p4 = L2[i + 3]

#         match = {"teamA": [p1, p2], "teamB": [p3, p4]}

#         matches.append(match)

#         i += 4

#     # joueurs restants
#     rest = L2[i:]

#     return matches, rest


players = generate_players(4, 5, 3)


def get_level_i_players(players, i):
    return [p for p in players if p[1] == i]


def build_matches(L1, L2, L3, mode):
    """
    mode:
        "L2"   -> matchs 2v2 avec lvl2
        "L1L3" -> matchs (1,3) vs (1,3)
    """

    matches = []

    # -----------------------
    # MODE L2
    # -----------------------
    if mode == "L2":
        i = 0
        while i + 3 < len(L2):
            p1, p2, p3, p4 = L2[i : i + 4]

            matches.append({"teamA": [p1, p2], "teamB": [p3, p4]})

            i += 4

        rest = L2[i:]
        return matches, rest

    # -----------------------
    # MODE L1 + L3
    # -----------------------
    if mode == "L1L3":
        i, j = 0, 0

        while i + 1 < len(L1) and j + 1 < len(L3):
            p1 = L1[i]
            p2 = L3[j]
            p3 = L1[i + 1]
            p4 = L3[j + 1]

            matches.append({"teamA": [p1, p2], "teamB": [p3, p4]})

            i += 2
            j += 2

        rest = L1[i:] + L3[j:]
        return matches, rest

    return [], L1 + L2 + L3


L1 = get_level_i_players(players, 1)
L2 = get_level_i_players(players, 2)
L3 = get_level_i_players(players, 3)

matches_l2, rest_l2 = build_matches([], L2, [], "L2")
matches_l1l3, rest_l1l3 = build_matches(L1, [], L3, "L1L3")

print(matches_l2, rest_l2)
print(matches_l1l3, rest_l1l3)

# matches, remaining = build_matches(players)

# for i, m in enumerate(matches):
#     print(f"\nMatch {i + 1}")

#     print("Team A:", m["teamA"])
#     print("Team B:", m["teamB"])

# print("\nRestants:", remaining)
