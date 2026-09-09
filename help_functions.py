import random


def generate_players(l1, l2, l3):
    players = []
    pid = 1

    for _ in range(l1):
        players.append((f"P{pid}", 1, 0))
        pid += 1

    for _ in range(l2):
        players.append((f"P{pid}", 2, 0))
        pid += 1

    for _ in range(l3):
        players.append((f"P{pid}", 3, 0))
        pid += 1

    random.shuffle(players)

    return players


def fill_matches(A, matches, rest):
    "Optimise les matchs de même niveau"
    i = 0
    while i + 3 < len(A):
        p1, p2, p3, p4 = A[i : i + 4]

        matches.append({"teamA": [p1, p2], "teamB": [p3, p4]})

        i += 4

    rest += A[i:]
    print(rest)
    # if A[i:] == []:
    #     rest = None
    # else:
    #     rest.append(A[i:])
    # print("après", rest)
    return matches, rest


def get_level_i_players(players, i):
    return [p for p in players if p[1] == i]


#     return matches, rest
def build_matches(L1, L2, L3, round):
    matches = []
    rest = []

    if round == 1:
        "Round Intermédiaire ensembles"
        A = L2
        B = L1
        C = L3

    elif round == 2:
        "Round Débutants ensembles"
        A = L3
        B = L1
        C = L2

    elif round == 3:
        "Round Pro Ensembles"
        A = L1
        B = L2
        C = L3
    elif round == 4:
        "Round minimiser le mix de niveaux"
        for level in [L1, L2, L3]:
            matches, rest = fill_matches(level, matches, rest)
            # matches.append(matche_lvl)
            # rest.append(rest_lvl)

        while len(rest) > 4:
            last_matches, last_rest = find_best_rest_match(rest)

            matches.append(last_matches)
            rest = last_rest
        return matches, rest

    matches, rest = fill_matches(A, matches, rest)

    i, j = 0, 0

    while i + 1 < len(B) and j + 1 < len(C):
        p1 = B[i]
        p2 = C[j]
        p3 = B[i + 1]
        p4 = C[j + 1]

        matches.append({"teamA": [p1, p2], "teamB": [p3, p4]})

        i += 2
        j += 2

    rest += B[i:] + C[j:]
    print(rest)
    last_match, last_rest = find_best_rest_match(rest)
    if last_match is not None:
        matches.append(last_match)

    return matches, last_rest


def print_matches_and_rest(matches, rest):
    print("\n================ MATCHS ================\n")

    for i, m in enumerate(matches, 1):
        teamA = m["teamA"]
        teamB = m["teamB"]

        print(f"Match {i}")

        print("  Team A :", " | ".join([f"{p[0]} (lvl {p[1]})" for p in teamA]))
        print("  Team B :", " | ".join([f"{p[0]} (lvl {p[1]})" for p in teamB]))

        print("-" * 40)

    print("\n============== PAUSE ==============\n")

    if not rest:
        print("Aucun joueur en pause 🎉")
    else:
        for p in rest:
            print(f"{p[0]} (lvl {p[1]})")

    print("\n====================================\n")


import itertools


def score_match(teamA, teamB):
    """
    score = différence de niveau entre les deux équipes
    plus c'est proche de 0, mieux c'est
    """
    return abs(sum(p[1] for p in teamA) - sum(p[1] for p in teamB))


import itertools


def find_best_rest_match(rest):
    """
    rest = [(id, level), ...]
    retourne :
        - le meilleur match 2v2
        - les joueurs restants après ce match
    """

    if len(rest) < 4:
        return None, rest

    best_match = None
    best_score = float("inf")
    best_used = None
    print(itertools.combinations(rest, 4))
    for combo in itertools.combinations(rest, 4):
        for teamA_idx in itertools.combinations(range(4), 2):
            print(teamA_idx)
            teamA = [combo[i] for i in teamA_idx]
            teamB = [combo[i] for i in range(4) if i not in teamA_idx]

            score = score_match(teamA, teamB)
            # print(score)
            if score < best_score:
                print("aaa")
                best_score = score
                best_match = {"teamA": teamA, "teamB": teamB}

                best_used = set(combo)

    new_rest = [p for p in rest if p not in best_used]
    print("best match : ", best_match)

    return best_match, new_rest
