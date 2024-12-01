from Game import Game

if __name__ == '__main__':
    f = open('input.txt')
    possible_games = []
    powers = []
    for line in f.readlines():
        game = Game(line)

        if game.is_possible_with_bag(14,13,12):
            possible_games.append(game.id)

        powers.append(game.get_power())
        
    print(f'Problem 1: {sum(possible_games)}')
    print(f'Problem 2: {sum(powers)}')

