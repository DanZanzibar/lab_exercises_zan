# Zan's answer to the race game.

import random


starting_lane = ['*', '', '', '', '', '', '', '']

def roll_die(active_player):
    print(f'Player {active_player} press enter to roll!')
    roll = random.randint(1, 6)
    print(f'Player {active_player} rolled a {roll}')
    print('************************************')
    return roll


def player_index(player, lane):
    if lane == starting_lane:
        return 0
    else:
        return lane.index(player)
    

def opponent(player):
    return 'x' if player == 'o' else 'o'


def print_lane(lane):

    # Frank - is there an easier way to unpack this to use to print to the f string?
    print('update: {} {} {} {} {} {} {} {}'.format(*lane))


def update_position(player, lane, roll):

    # Get indexes for players, including potential new index for active player.
    index_active = player_index(player, lane)
    index_opponent = player_index(opponent(player), lane)
    new_index = index_active + roll

    # Change lane list to reflect new positions, checking if rolling too high (not moving) or bumping the opponent to start.
    if new_index > 7:
        print(f'The roll was too high, player {player} stays in this position')
        print('************************************')
        return lane
    else:
        lane[new_index] = player
        if new_index == index_opponent:
            lane[0] = opponent(player)
        print('************************************')
        return lane


def check_game_over():



def opponent(player):
    return 'x' if player == 'o' else 'o'


def main():
    lane = starting_lane
    active_player = 'x'
    print('Players begin in the starting position')
    print('************************************')
    print_lane(lane)
    print('************************************')


    while True:
        roll = roll_die()
        lane = update_position(active_player, lane, roll)
        if check_game_over(lane):
            print(f'Player {active_player} has won!')

