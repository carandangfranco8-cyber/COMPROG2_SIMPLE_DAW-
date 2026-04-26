import utility
import time
import os
import subprocess
import ingame_contents
import random_module
import random

def clear():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

#start up menu
random_module.reputation()
print("\t\t","*" * 50)
print("\n\t\t\tWELCOME TO Detective 1882 – Text Game!!\n")
print("\t\t","*" * 50)
time.sleep(2)
print("\n\n\t\tTo start, first roll a character to set your reputation")
time.sleep(1)
print("CHARACTERS:")
characters = {"Detective Daniel":10, "Detective Marc":8, "Detective Melvin":14,"Detective Ian":5}
for key in characters.keys():
    print(f"{key:<{15}}", end="\t")
print()
for value in characters.values():
    print(f"{value:<{15}}", end="\t\t")
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
print(f"\nYOU ROLLED: {chosen_character}!")
print(f"Starting Reputation: {starting_reputation}")
print(f"\n{'='*50}")
time.sleep(1.5)
print("CONGRATULATIONS! You are now a detective, ready to solve your first case!")
input("\nPress Enter to continue...")

#start game
utility.case(starting_reputation)




print(f"""
        {"\n" * 20}
        THANK YOU {"\n" * 10}""")

