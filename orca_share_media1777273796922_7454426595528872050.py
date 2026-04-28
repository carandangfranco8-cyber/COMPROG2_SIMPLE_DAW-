# CASE 3 MODULE

import random

# DATA MODULE

characters = [
    "Diplomat (Victim)",
    "Guest A (Chef)",
    "Guest B (Assistant)",
    "Guest C (Business Partner)",
    "Detective"
]

suspects = [
    "Guest A (Chef)",
    "Guest B (Assistant)",
    "Guest C (Business Partner)"
]

rooms = [
    "Dining Area",
    "Kitchen",
    "Study Room",
    "Hallway"
]

clues = [
    "Cup of tea near the victim",
    "No signs of forced entry",
    "Strange timing of tea serving",
    "Poison detected in drink",
    "Witness inconsistent statements"
]



# OOP MODULE

class Character:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Detective(Character):
    def investigate(self):
        return "Analyzing the crime scene..."


class Suspect(Character):
    def alibi(self):
        return f"{self.name} gives an alibi."


class Witness(Character):
    def clue(self):
        return "I saw something suspicious..."


# UTILITY MODULE


player_score = 0
inventory = []

def add_score(points):
    global player_score
    player_score += points


def add_item(item):
    inventory.append(item)


def check_win(correct_suspect, guess):
    return correct_suspect == guess


def game_status():
    if player_score >= 10:
        return "WIN"
    return "CONTINUE"

# RANDOMIZER MODULE


def random_suspect():
    return random.choice(suspects)


def random_clues():
    return random.sample(clues, 3)


def shuffle_rooms():
    temp = rooms[:]
    random.shuffle(temp)
    return temp


def random_event():
    events = [
        "A witness suddenly collapses",
        "Phone call interrupts investigation",
        "New clue discovered in kitchen",
        "Suspect changes statement"
    ]
    return random.choice(events)

# CASE 3 STORY ENGINE

def case3_game():
    print("\nCASE 3: THE DIPLOMAT MURDER CASE\n")

    detective = Detective("Detective")
    killer = random_suspect()
    scene_clues = random_clues()
    room_order = shuffle_rooms()

    print("A diplomat was found dead inside the Study Room.")
    print("Cause of death: Poisoning.\n")

    print("Initial clues discovered:")
    for c in scene_clues:
        print("-", c)

    print("\nRooms investigated order:")
    for r in room_order:
        print("-", r)

    print("\nUnexpected event:", random_event())

    print("\nSuspects:")
    for s in suspects:
        print("-", s)

    guess = input("\nWho is the killer? (type exact name): ")

    if check_win(killer, guess):
        add_score(10)
        add_item("Case File Evidence")
        print("\nCorrect! You solved the case.")
    else:
        print("\nWrong suspect. The real culprit escapes justice.")

    print("\nFinal Score:", player_score)
    print("Inventory:", inventory)

    if game_status() == "WIN":
        print("CASE CLEARED SUCCESSFULLY!")
    else:
        print("CASE INCOMPLETE.")


# Run case (for testing only)
if __name__ == "__main__":
    case3_game()
