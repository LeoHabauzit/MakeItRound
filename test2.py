import itertools
import random
from collections import defaultdict


# ---------------------------
# 1. génération des paires possibles (2v2)
# ---------------------------


def all_team_splits(players):
    """retourne toutes les façons de faire 2 équipes de 2"""
    splits = []

    for teamA_idx in itertools.combinations(range(len(players)), 2):
        teamB_idx = [i for i in range(len(players)) if i not in teamA_idx]

        teamA = [players[i] for i in teamA_idx]
        teamB = [players[i] for i in teamB_idx]

        splits.append((teamA, teamB))

    return splits


# ---------------------------
# 2. score d'un match
# ---------------------------


def score_match(teamA, teamB, played_count):
    """
    score = équilibre + équité
    """

    # équilibre
    sumA = sum(lvl for _, lvl in teamA)
    sumB = sum(lvl for _, lvl in teamB)
    balance_score = abs(sumA - sumB)

    # équité (favorise joueurs peu utilisés)
    usage_score = 0
    for p, lvl in teamA + teamB:
        usage_score += played_count[p]

    return balance_score + 0.3 * usage_score


# ---------------------------
# 3. choisir le meilleur match parmi 4 joueurs
# ---------------------------


def best_match_from_players(players, played_count):
    best = None
    best_score = float("inf")

    for teamA, teamB in all_team_splits(players):
        s = score_match(teamA, teamB, played_count)

        if s < best_score:
            best_score = s
            best = (teamA, teamB)

    return best


# ---------------------------
# 4. algo principal (construction des matchs)
# ---------------------------


def build_matches(players):
    """
    players = [(id, level), ...]
    """

    played_count = defaultdict(int)
    remaining = players[:]

    matches = []

    while len(remaining) >= 4:
        # prendre 4 joueurs (heuristique simple)
        # on pourrait améliorer avec selection intelligente
        group = remaining[:4]

        match = best_match_from_players(group, played_count)

        if match is None:
            break

        teamA, teamB = match

        matches.append({"teamA": teamA, "teamB": teamB})

        # update joueurs joués
        for p, lvl in teamA + teamB:
            played_count[p] += 1

        # retirer ces joueurs
        used_ids = {p for p, _ in teamA + teamB}
        remaining = [p for p in remaining if p[0] not in used_ids]

    return matches, remaining
