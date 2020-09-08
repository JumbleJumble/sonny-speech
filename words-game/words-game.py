import json
import click
import random
from colorama import Fore, Style, init
from os import system


class Pool:
    def __init__(self, words, count):
        super().__init__()
        self.words = words
        self.count = count


def play_game(players, pools):
    turn = random.randrange(len(players))
    game_over = False

    while not game_over:
        words = []
        for pool in pools:
            for i in range(pool.count):
                word = random.choice(pool.words)
                pool.words.remove(word)
                words.append(word)

            if len(pool.words) < pool.count:
                game_over = True

        print(f"{Fore.GREEN}{players[turn]}:")
        for word in words:
            print(f"{Fore.YELLOW}{word}")

        input()
        turn = (turn + 1) % len(players)

    print(f"{Fore.RED}Game over!")


@click.command()
@click.option('--game', prompt="Which game?")
def main(game):
    init(autoreset=True)
    system('cls')

    gamedef = {}
    with open('gamedef.json') as gamedef_file:
        gamedef = json.load(gamedef_file)

    players = gamedef["players"]

    try:
        rules = gamedef["games"][game]
    except KeyError:
        print(f"Could not find game {game}")
        return

    selections = []
    for rule in rules.items():
        selections.append(Pool(gamedef["word-lists"][rule[0]], rule[1]))

    play_game(players, selections)


if __name__ == "__main__":
    main()
