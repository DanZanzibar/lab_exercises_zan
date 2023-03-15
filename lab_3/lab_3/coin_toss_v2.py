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
    return p1_win, p2_win


def round():
    p1_round_score, p2_round_score = 0, 0
    for _ in range(4):
        subround_result = subround()
        if subround_result[0]:
            p1_round_score += 1
        if subround_result[1]:
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


def main():
    round()


main()