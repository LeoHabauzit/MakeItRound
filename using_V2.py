from help_functions import *
import random


players = generate_players(7, 7, 7)
print(players)

L1 = get_level_i_players(players, 1)
L2 = get_level_i_players(players, 2)
L3 = get_level_i_players(players, 3)
print("Round 1")
matches, rest = build_matches(L1, L2, L3, round=1)
print_matches_and_rest(matches, rest)
random.shuffle(players)
print("Round 2")
matches, rest = build_matches(L1, L2, L3, round=2)
print_matches_and_rest(matches, rest)
random.shuffle(players)
print("Round 3")
matches, rest = build_matches(L1, L2, L3, round=3)
print_matches_and_rest(matches, rest)

print("Round 4")
matches, rest = build_matches(L1, L2, L3, round=4)
print_matches_and_rest(matches, rest)
