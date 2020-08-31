import random

words = [
    "its", "ants", "bats", "cats", "dots", "hats", "kits", "lots", "nuts", "pets", 
    "boots", "boats", "goats", "notes", "notes", "roots", "sheets", "lights", "weights",
    "back hurts", "foot hurts", "tummy hurts", "thumb hurts", "martial arts", "darts", 
    "pants", "pints", "floats", "fruits", "plates", "paints", "carrots", "nuggets", "puppets", 
    "rabbits"]

players = ["Richard", "Sonny"]

game_over = False
turn = 0

while not game_over:
    print(f"Player: {players[turn]}")

    first_word = random.choice(words)
    words.remove(first_word)

    second_word = random.choice(words)
    words.remove(second_word)

    game_over = len(words) < 2

    print(f"First word: {first_word}\nSecond word: {second_word}")

    turn = (turn + 1) % len(players)

    input()

print("Game over!")
