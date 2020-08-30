import random

s_words = ["sit", "sand", "sock", "soap", "sun", "seal", "sand", "sink", "soup", "sing",
           "suitcase", "sick", "saw", "salt", "same", "soda", "say", "see", "sew", "sidewalk"]

j_words = ["jelly beans", "jacket", "jingle bells", "jacks", "jelly", "juice", "jam", "jump", "Jupiter",
           "Jack 'o lantern", "jet ski", "jog", "jump rope", "jewellery", "janitor", "July", "jeep", "J", "joker", "jail"]

players = ["Richard", "Sonny"]

game_over = False
turn = 0

while not game_over:
    print(f"Player: {players[turn]}")

    s_word = random.choice(s_words)
    s_words.remove(s_word)

    j_word = random.choice(j_words)
    j_words.remove(j_word)

    game_over = len(s_words) == 0

    print(f"{s_word} {j_word}")

    turn = (turn + 1) % len(players)

    input()

print("Game over!")

