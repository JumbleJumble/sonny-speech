import json
import click
import random
from colorama import Fore, Style, init

def play_game(players, selections):
    turn = 0
    game_over = False

    while not game_over:
        words = []
        for sel in selections:
            wordlist = sel[0]
            wordcount = sel[1]

            for i in range(wordcount):
                word = random.choice(wordlist)
                wordlist.remove(word)
                if len(sel[0]) < wordcount:
                    game_over = True
                words.append(word)

        print(f"{Fore.GREEN}{players[turn]}'s {Style.RESET_ALL}turn!")
        for word in words:
            print(f"{Fore.YELLOW}{word}")

        input()
        turn = (turn + 1) % len(players)

    print(f"{Fore.RED}Game over!")


@click.command()
@click.option('--game', default='ch-words')
def main(game):
    init(autoreset=True)

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
        selections.append((gamedef["word-lists"][rule[0]], rule[1]))

    play_game(players, selections)
    

if __name__ == "__main__":
    main()