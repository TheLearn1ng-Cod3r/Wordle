# Couldn't work out rich so I'm using emojis
import random

with open("Word List.txt","r") as file:
    words : list = file.read().split()
# print(words)

target : str = random.choice(words)
geuss : str = ""
geusses : list = []
attempts : int = 0

print("Welcome to Wordle! You have 5 attempts to guess the 5 letter word.")
print("🟩 = correct letter in correct position")
print("🟨 = correct letter in wrong position")
print("⬛ = incorrect letter")
start : str = input("Press Enter to start the game...")


def game_loop():
    """ Main game loop between geussing, and checking geusses."""
    print("Please enter your first guess:")
    while (geuss != target) and (attempts < 5):
        geuss = input(">> ").lower()
        try:
            if len(geuss) != 5:
                raise IndexError
            
            for i in range(len(geuss)):
                if geuss[i] == target[i]:
                    print("🟩", end=" ")
                elif geuss[i] in target:
                    print("🟨", end=" ")
                else:
                    print("⬛", end=" ")
                geusses.append(geuss)

        except IndexError:
            print("Please enter a 5 letter word")

        attempts += 1
        print()
        print(geuss.upper())

    if target in geusses:
        return True
    else:
        return False



if game_loop():
    print("You have guessed the word correctly")
else:
    print("You have used all your guesses. The correct word was:", target)