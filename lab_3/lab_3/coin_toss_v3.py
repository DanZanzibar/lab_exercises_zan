# A simple coin toss game.

import random


with open('instructions.txt') as file:
    print(file.read())


def toss_coin():
    toss = random.randint(0, 1)
    return 'H' if toss == 0 else 'T'


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


def count_subsequence(subsequence, sequence):
    sub_len, seq_len = len(subsequence), len(sequence)
    count = 0
    for index in range(seq_len - sub_len + 1):
        if sequence[index:index + sub_len] == subsequence:
            count += 1
    return count


def round():
    p1_round_score, p2_round_score = 0, 0
    p1_tosses, p2_tosses = [], []

    for _ in range(4):
        p1_subround, p2_subround = subround()
        p1_subround_win, p1_toss = p1_subround
        p2_subround_win, p2_toss = p2_subround

        p1_tosses.append(p1_toss)
        p2_tosses.append(p2_toss)
        if p1_subround_win:
            p1_round_score += 1
        if p2_subround_win:
            p2_round_score += 1

    if p1_round_score > p2_round_score:
        round_winner = 'Player 1'
    elif p2_round_score > p1_round_score:
        round_winner = 'Player 2'
    else:
        round_winner = None

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


def main():
    round()


main()