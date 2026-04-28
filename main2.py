import utility
import time
import os
import subprocess
import ingame_contents
import random_module
import random
import textwrap
import shutil

def clear():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

#start up menu
random_module.reputation()
print("\t\t\t\t\t","*" * 110)
print("\n\t\t\t\t\t\t\t\t\t\tWELCOME TO Detective 1882 – Text Game!!\n")
print("\t\t\t\t\t","*" * 110)
time.sleep(2)
print("\n\n\t\t\t\t\t\t\t\t\tTo start, first roll a character to set your reputation")
time.sleep(1)


characters = {"Detective Daniel":10, 
              "Detective Marc":8, 
              "Detective Melvin":14,
              "Detective Ian":5}

#centered title
print("CHARACTERS:".center(200))

#print names in column
for name in characters:
    print(name.center(50), end="")
print()

#print scores in column under names
for score in characters.values():
    print(str(score).center(50), end="")
print()

input("\nPress Enter to roll the dice...")
print("\n🎲 ROLLING DICE", end="")
for i in range(15):
    print(".", end="", flush=True)
    time.sleep(0.15)
print(" 🎲\n")

chosen_character = random.choice(list(characters.keys()))
starting_reputation = characters[chosen_character]

# Dramatic reveal
print(f"\nYOU ROLLED: {chosen_character}!.".center(400))
print(f"Starting Reputation: {starting_reputation}".center(200))
print(f"\n{'='*195}")
time.sleep(1.5)
print("CONGRATULATIONS! You are now a detective, ready to solve your first case!")
input("\nPress Enter to continue...")
#start game


utility.run_game(starting_reputation,chosen_character)





