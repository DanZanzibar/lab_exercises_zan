# A simple coin toss game.

import random


def toss_coin():

    toss = random.randint(0, 1)
    return 'H' if toss == 0 else 'T'


# A single toss of the coin per player. Returns whether each player won and their toss.
def subround():

    p1_toss, p2_toss = toss_coin(), toss_coin()
    print(f'Player 1 has tossed {p1_toss}')
    print(f'Player 2 has tossed {p2_toss}')

    user_call = input('Heads or Tails ? Type H or T >').upper()
    p1_win, p2_win = p1_toss == user_call, p2_toss == user_call

    if p1_win:
        print('Player 1 wins')
    if p2_win:
        print('Player 2 wins')
    return (p1_win, p1_toss), (p2_win, p2_toss)


# Defined a function to count overlapping subsequences.
def count_subsequence(subsequence, sequence):

    sub_len, seq_len = len(subsequence), len(sequence)
    count = 0
    for index in range(seq_len - sub_len + 1):
        if sequence[index:index + sub_len] == subsequence:
            count += 1
    return count


def round():

    # Initialize round score and list of tosses.
    p1_round_score, p2_round_score = 0, 0
    p1_tosses, p2_tosses = [], []

    for _ in range(4):
        # Unpacking subround info: who won and their tosses.
        p1_subround, p2_subround = subround()
        p1_subround_win, p1_toss = p1_subround
        p2_subround_win, p2_toss = p2_subround

        # Adding tosses to list and adding score to round.
        p1_tosses.append(p1_toss)
        p2_tosses.append(p2_toss)
        if p1_subround_win:
            p1_round_score += 1
        if p2_subround_win:
            p2_round_score += 1

    # Determining winner of round.
    if p1_round_score > p2_round_score:
        round_winner = 'Player 1'
    elif p2_round_score > p1_round_score:
        round_winner = 'Player 2'
    else:
        round_winner = None

    # Printing round summary, including subsequence counting.
    print('ROUND STATS')
    if round_winner:
        print(f'{round_winner} wins this round')
    else:
        print('Tie Game')
    print(f'Player 1 points {p1_round_score}')
    print(f'Player 2 points {p2_round_score}')
    print(f'Player 1 tossed {p1_tosses}')
    print(f'Player 2 tossed {p2_tosses}')

    p1_HH_subsequence = count_subsequence(['H', 'H'], p1_tosses)
    p2_HH_subsequence = count_subsequence(['H', 'H'], p2_tosses)
    print(f'H H found in the player 1 sequence {p1_HH_subsequence} times')
    print(f'H H found in the player 2 sequence {p2_HH_subsequence} times')

    return round_winner


def main():

    # Print initial instructions
    with open('instructions.txt') as file:
        print(file.read())

    ties = 0
    p1_wins = 0
    p2_wins = 0

    while True:
        # Tracking multi-round scoring.
        round_winner = round()
        if round_winner == 'Player 1':
            p1_wins += 1
        elif round_winner == 'Player 2':
            p2_wins += 1
        else:
            ties += 1
        another_round = input('Do you want to play another round? y/n >')
        if another_round.lower() != 'y':
            break

    # Printing final multi-round scores.
    print('SUMMARY STATS')
    print(f'number of ties {ties}')
    print(f'number of player 1 wins {p1_wins}')
    print(f'number of player 2 wins {p2_wins}')

main()