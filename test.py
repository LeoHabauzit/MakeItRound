# def calc_cost_comb(v):
import itertools

weights = {
    1: 1.0,
    2: 1.0,
    3: 0.7,  # on "boost" les lvl3
}


def score_match(match):
    
def score_match(match, weights):
    x1, x2, x3 = match
    players = [1]*x1 + [2]*x2 + [3]*x3
    
    best_score = float("inf")
    
    for team_a_idx in itertools.combinations(range(4), 2):
        team_b_idx = [i for i in range(4) if i not in team_a_idx]
        
        team_a = [players[i] for i in team_a_idx]
        team_b = [players[i] for i in team_b_idx]
        
        # équilibre des équipes
        diff = abs(sum(team_a) - sum(team_b))
        
        # bonus/malus selon niveaux utilisés
        weight_score = sum(weights[p] for p in players)
        
        total_score = diff + weight_score
        
        if total_score < best_score:
            best_score = total_score
    

    print(
        (players[best_split[0][0]], players[best_split[0][1]]),
        (players[best_split[1][0]], players[best_split[1][1]]),
    )
    return best_diff, best_split


def generate_match_types():
    match_types = []
    for x1 in range(5):
        for x2 in range(5):
            for x3 in range(5):
                if x1 + x2 + x3 == 4:
                    match_types.append((x1, x2, x3))
    return match_types


def expand_match(match):
    x1, x2, x3 = match
    return tuple([1] * x1 + [2] * x2 + [3] * x3)


def find_match_reste(j1, j2, j3):
    match_types = generate_match_types()
    # print(match_types)

    matches = []

    while True:
        possible = []

        for m in match_types:
            x1, x2, x3 = m

            if x1 <= j1 and x2 <= j2 and x3 <= j3:
                possible.append(m)

        if not possible:
            break

        # choisir le plus équilibré
        best = min(possible, key=score_match)

        matches.append(expand_match(best))

        x1, x2, x3 = best
        j1 -= x1
        j2 -= x2
        j3 -= x3

    return matches, (j1, j2, j3)


score_match((2, 2, 3))
