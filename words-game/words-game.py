import json
import click
import random
from colorama import Fore, init
from os import system


class Pool:
    def __init__(self, words, count):
        super().__init__()
        self.words = words
        self.count = count


def play_game(players, pools, max_words):
    turn = random.randrange(len(players))
    game_over = False

    while not game_over:
        random.shuffle(pools)
        words = []
        for pool in pools:
            if len(words) < max_words:
                for _ in range(pool.count):
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

    ruleset = {}
    with open('gamedef.json') as gamedef_file:
        ruleset = json.load(gamedef_file)

    players = ruleset["players"]

    try:
        gamedef = ruleset["games"][game]
    except KeyError:
        print(f"Could not find game {game}")
        return

    pools = []
    try:
        max_words = int(gamedef["max-words"])
    except KeyError:
        max_words = 999

    pooldef = gamedef["pool"]
    for pool in pooldef.items():
        pools.append(Pool(ruleset["word-lists"][pool[0]], pool[1]))

    play_game(players, pools, max_words)


if __name__ == "__main__":
    main()
