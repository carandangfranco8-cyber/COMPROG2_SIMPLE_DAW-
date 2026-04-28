import time
import random
import random_module
import ingame_contents
import OOP


import textwrap
import shutil

import textwrap
import shutil


#CASE 1
cases = ingame_contents.cases
cause_of_death = ingame_contents.cause_of_death
evidence_map1 = ingame_contents.evidence_map1
evidence_map11 = ingame_contents.evidence_map11

#CASE 2
cases2 = ingame_contents.cases2
cause_of_death2 = ingame_contents.cause_of_death_2
evidence_map2 = ingame_contents.evidence_map2
evidence_map22 = ingame_contents.evidence_map22
cause_of_death_2 = ingame_contents.cause_of_death_2




def print_columns(left_text, right_text=""):
    width = shutil.get_terminal_size().columns

    # auto switch: 1 column if too small
    if width < 80:
        for line in textwrap.wrap(left_text, width):
            print(line)
        if right_text:
            for line in textwrap.wrap(right_text, width):
                print(line)
        print()
        return

    # 2 column mode
    left_lines = textwrap.wrap(left_text, width=width // 2 - 3)
    right_lines = textwrap.wrap(right_text, width=width // 2 - 3)

    max_lines = max(len(left_lines), len(right_lines))

    for i in range(max_lines):
        l = left_lines[i] if i < len(left_lines) else ""
        r = right_lines[i] if i < len(right_lines) else ""
        print(f"{l:<{width//2}} | {r}")



def run_game(starting_reputation, character):
    case_index = 0

    while True:
        global rep
        rep = starting_reputation
        print(f"\n{'='*195}")
        print(f"  INVESTIGATION — CASE {case_index + 1}".center(200))
        print(f"  Reputation: {rep}".center(200))
        print(f"{'='*195}\n")
        time.sleep(1)


        rep2,case_solved = menu(rep, character)
        

        # --- End of investigation check ---
        if rep2 < 5:
            print("\n" + "="*40)
            print("  INVESTIGATION FAILED!")
            print("  Your reputation is too low.")
            print("  You have LOST YOUR JOB.")
            print("="*40)
            time.sleep(3)
            case_index = 0          # reset back to first case
            input("\nPress Enter to try again...\n")
            break               

        if case_solved:
            case_index += 1
            print(f"\n{'='*195}")
            print(f"  Case solved! Advancing to Case {case_index + 1}...".center(200))
            print(f"\n{'='*195}")
            print(f"  INVESTIGATION — CASE {case_index + 1}".center(200))
            print(f"  Reputation: {rep2}".center(200))
            print(f"{'='*195}\n")
            time.sleep(1)
            ch = character
            case_solved = menu2(rep2, ch)
            print(f"{'='*40}")
            time.sleep(2)
            if case_index == 2:
                case_solved = menu3(rep2, character)
                break

       # Go to Case 2
            rep3, case_solved2 = menu2(rep2, character)
            print(f"{'='*40}")
            time.sleep(2)

            if case_solved2:
                case_index += 1  # Now becomes 2 after Case 2 triggers menu3
                print(f"\n{'='*195}")
                print(f"  Case solved! Advancing to Case {case_index + 1}...".center(200))
                print(f"\n{'='*195}")
                print(f"  INVESTIGATION — CASE {case_index + 1}".center(200))
                print(f"  Reputation: {rep3}".center(200))
                print(f"{'='*195}\n")
                time.sleep(1)

                #RUN MENU3
                if case_index == 2:
                    rep4, case_solved3 = menu3(rep3, character)
                    
                    if case_solved3:
                        print("\n" + "="*40)
                        print("  CONGRATULATIONS!")
                        print("  You have solved all the cases!")
                        print(f"  Your reputation: {rep4}")
                        print("="*40)
                        time.sleep(3)
                    break
            
        else:
            print("\nInvestigation ended. Goodbye, Detective.")
            break


def menu(rep,character):
    global reputation
    reputation = rep
    print("*".center(10) * 60)
    print("You are now in the crime scene!!".center(200))

    print("\n".join(
        line.center(180)for line in f"""\n
                Detective 1882 – {character} Case
                A murder has occurred at Angel’s Share restaurant...
        
                    Playing as: {character}
                    Reputation: {reputation}
                    """.split("\n")
    ))      
    time.sleep(2)

    print("=" * 195)
    print("Victim: Robert".center(200))
    print("Cause of Death: Unknown".center(200))
    print("Location: Angel’s Share Kitchen\n".center(200))
    print("=" * 195)

    print("You arrive at the crime scene...".center(200))

    while True:
        print(f"{"*" * 10}Main Menu{"*" * 10}\n".center(200), end="")

        print(f"REPUTATION: {reputation}".center(30))

        print("\n".join(
        line.center(180)for line in f"""
                1. Investigate Evidence
                2. Interrogate Suspect
                3. Accuse
                4. Exit
              
               """.split("\n")
        ))
        
        try:
            choose = int(input("Enter your guess (1-4):"))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if choose == 1:
            Investigate(reputation)
            
        elif choose == 2:
            Interogate()
            continue
        elif choose == 3: 
            reputation, result = Accuse(reputation)
            if reputation < 5:
                print(f"\nYour reputation is now {reputation}. Too low!")
                return reputation, False
            if result == True:
                return reputation,True
            else:
                continue
        elif choose == 4:
            print("\nInvestigation ended. Goodbye, Detective.")
            print("*".center(10) * 60)
            print("GOOD GAME".center(200))
            return reputation,False
        
def hint(proof):
    print((" EVIDENCE ").center(195))
    
    for case in proof:
        print("\t\t\t\t\t\t\n", case["HINT"] + "\n")

        items = list(case["HINTS"].items())

        for i in range (0, len(items), 2):
            left = items[i]

            right = items[i + 1] if i + 1 < len(items) else ("", "")

            left_text = f"{left[0]} : {left[1]}"
            right_text = f"{right[0]} : {right[1]}"

            print(f"{left_text:<40}           {right_text:<40}")
        print("=" * 195)


def play_case(case, evidence_map1, rep):
    victim = case["victim"]

    print(f"\n{case['name']}")

    width = 200

    lines = [
        "Victim:",
        f"Name: {victim['name']}",
        f"Age: {victim['age']}",
        f"Career: {victim['career']}",
        f"Location: {case['location']}"
]

# find longest line
    max_len = max(len(line) for line in lines)

    for line in lines:
        print(line.ljust(max_len).center(width))


    # STEP 1: Evidence
    evidences = list(evidence_map1.keys())
    evidence_hint = evidence_map11

    while True:

        print("\nBASED ON THE REPORT:\n")
        for i, c in enumerate(evidence_hint):
            print(f"{i+1}. {c}")
            time.sleep(1)

        print("\nChoose Evidence:")
        for i, e in enumerate(evidences):
            print(f"{i+1}. {e}")

        try:
            choice = int(input("\nSelect evidence: ")) - 1
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if choice > len(evidences):
            print("INVALID")
            continue

        selected_evidence = evidences[choice]

        if selected_evidence == "Soup":
            possible_causes = evidence_map1[selected_evidence]
            choices = generate_choices(victim["cause_of_death"], possible_causes)
        else:
            time.sleep(1)
            
            print("\n")
            lost = random_module.reputation()
            rep -= lost
            for line in [
            "Wrong!! Reputation Decreased",
            "walang bitaw ya!"
            ]:
                print(line.center(width))
            print()

            lost = random_module.reputation()
            rep -= lost
            
            width = shutil.get_terminal_size().columns

            print(f"REPUTATION DECREASED BY: {lost}".center(width))
            print(f"REPUTATION: {rep}".center(width))

            if rep < 0:
                width = shutil.get_terminal_size().columns

                print("\n" + "=" * width)
                print("INVESTIGATION FAILED!".center(width))
                print("Your reputation is too low.".center(width))
                print("You have LOST YOUR JOB.".center(width))
                print("=" * width)

                time.sleep(3)
                case_index = 0          # reset back to first case
                input("\nPress Enter to try again...\n".center(200))
                return rep, False          
                
            else:
                continue

        print("\nPossible causes:")
        for i, c in enumerate(choices):
            print(f"{i+1}. {c}")


        answer = int(input("\nChoose cause of death: ")) - 1

        return choices[answer] == victim["cause_of_death"]


def generate_choices(correct_answer, possible_causes):
    
    wrong = [c for c in cause_of_death if c not in possible_causes]

    wrong_choices = random.sample(wrong, 2)

    choices = wrong_choices + [correct_answer]
    random.shuffle(choices)

    return choices


def Investigate(rep):
    global reputation
    reputation = rep

    hint(ingame_contents.evidence_1)
    time.sleep(1.5)

    evidences = list(evidence_map1.keys())

    for case in cases:
        correct = play_case(case, evidence_map1, rep)

    width = 200
    if correct:
        print("\n\nCorrect! Reputation Increase".center(width))
        reputation += 10
        return True

    else:
        print("\n\nWrong!! Reputation Decreased".center(width))
        reputation -= 15

    if reputation < 0:
        print("\n" + "="*195)
        print("  INVESTIGATION FAILED!".center(200))
        print("  Your reputation is too low.".center(200))
        print("  You have LOST YOUR JOB.".center(200))
        print("="*195)
        time.sleep(3)
        case_index = 0          # reset back to first case
        input("\nPress Enter to try again...\n".center(200))
        return reputation, False  

    
    time.sleep(3)
    
def Interogate():
        width = 200
        melvin = OOP.THREE("MELVIN","WAITER")
        jen = OOP.ONE("JENNSKY","KITCHEN STUFF")
        francon = OOP.TWO("FRANCO", "HEAD CHEF")

        text = """
        INTERROGATE
        SUSPECT
        """

        width = shutil.get_terminal_size().columns

        print(f"{'*' * 10} WHO IS THE CRIMINAL {'*' * 10}".center(width))
        print(f"{'*' * 10} SUSPECT {'*' * 10}".center(width))

        suspects = (jen, melvin, francon)

        for i, e in enumerate(suspects):
            print(f"{i+1}. {e.name}".center(width))



        try:
            choose = int(input("\nChoose suspect to interrogate: "))-1
        except ValueError:
            print("Invalid input.")
            return reputation, False

    
        print("\nWhere are you? Are you the killer?\n")
        suspects[choose].speak()
        time.sleep(3)

def Accuse(rep):
    global reputation
    reputation = rep
    melvin = OOP.THREE("MELVIN","WAITER")
    jen = OOP.ONE("JENNSKY","KITCHEN STUFF")
    franco = OOP.TWO("FRANCO", "HEAD CHEF")


    width = shutil.get_terminal_size().columns

    print(f"{'*' * 10} WHO IS THE CRIMINAL {'*' * 10}".center(width))
    print(f"{'*' * 10} SUSPECT {'*' * 10}".center(width))

    suspects = (jen, melvin, franco)

    for i, e in enumerate(suspects):
        print(f"{i+1}. {e.name}".center(width))


    try:
        choose = int(input("\nChoose suspect to interrogate: "))-1
    except ValueError:
        print("Invalid input.")
        return reputation,False
    
    selected = suspects[choose]

    if selected.name == "FRANCO":
        print("\n\nCORRECT!! Case Solved!".center(200))
        selected.accuse()
        reputation += 20
        time.sleep(1.5)
        return reputation,True
        

    else:
        selected.accuse()
        reputation -= 15
        time.sleep(2)
        return reputation, False
       

def generate_choices2(correct_answer, possible_causes):
    
    wrong = [c for c in cause_of_death_2 if c not in possible_causes]

    wrong_choices = random.sample(wrong, 2)

    choices = wrong_choices + [correct_answer]
    random.shuffle(choices)

    return choices

def Interogate2():
    melvin = OOP.THREE("MELVIN","Business partner of the victim")
    ian = OOP.ONE("IAN","Diner manager")
    Daniel = OOP.TWO("DANIEL", "Former employee")

    width = shutil.get_terminal_size().columns

    print(f"{'*' * 10} WHO IS THE CRIMINAL {'*' * 10}".center(width))
    print(f"{'*' * 10} SUSPECT {'*' * 10}".center(width))

    suspects = (ian, melvin, Daniel)

    for i, e in enumerate(suspects):
        print(f"{i+1}. {e.name}".center(width))

    try:
        choose = int(input("\nChoose suspect to interrogate: "))-1
    except ValueError:
        print("Invalid input.")
        return reputation, False

    for i, e in enumerate(suspects):
        print("\nWhere were you? Are you the killer?\n")
    suspects[choose].speak_2()
    time.sleep(3)

def Accuse2 (rep):
    global reputation
    reputation = rep
    melvin = OOP.THREE("MELVIN","Business partner of the victim")
    ian = OOP.ONE("IAN","Diner manager")
    Daniel = OOP.TWO("DANIEL", "Former employee")

    width = shutil.get_terminal_size().columns

    print(f"{'*' * 10} WHO IS THE CRIMINAL {'*' * 10}".center(width))
    print(f"{'*' * 10} SUSPECT {'*' * 10}".center(width))

    suspects = (ian, melvin, Daniel)

    for i, e in enumerate(suspects):
        print(f"{i+1}. {e.name}".center(width))

    try:
        choose = int(input("\nWHO HIRED THE HITMAN?: "))-1
   
    except ValueError:
        print("Invalid input.")
        return reputation, False
    
    selected = suspects[choose]

    if selected.name == "Daniel":
        print("\n\nCORRECT!! Case Solved!".center(200))
        selected.accuse()
        reputation += 20
        time.sleep(1.5)
        return reputation,True
        

    else:
        selected.accuse()
        reputation -= 15
        time.sleep(2)
        return reputation,False

def hint2(case):
    print(f"\n\n\n{'*'*10} EVIDENCE {'*'*10}".center(200))
    
    print("\n", case["HINT"], "\n")
    
    for evidence, description in case["HINTS"].items():
        print(evidence)
        print(description)

def play_case2(case, evidence_map2, rep):
    victim = case["victim"]

    width = 200

    lines = [
     "Victim:",
        f"Name: {victim['name']}",
        f"Age: {victim['age']}",
        f"Career: {victim['career']}",
        f"Location: {case['location']}"
]

# find longest line
    max_len = max(len(line) for line in lines)

    for line in lines:
        print(line.ljust(max_len).center(width))


    # STEP 1: Evidence
    evidences = list(evidence_map2.keys())
    evidence_hint = evidence_map22

    while True:

        print("\nPossible Causes of Accident:")
        for i, e in enumerate(evidences):
            print(f"{i+1}. {e}")

        try:
            choice = int(input("\nSelect Possible Cause: "))-1
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if choice < 1 or choice > len(evidences):
            print("INVALID")
            continue

        selected_evidence = evidences[choice]
        width = 200

        if selected_evidence == "Victim Misidentified":
            possible_causes = evidence_map2[selected_evidence]
            choices = generate_choices2(victim["cause_of_death"], possible_causes)
        else:
            time.sleep(1)
            
            print("\n")
            lost = random_module.reputation()
            rep -= lost
            for line in [
            "Wrong!! Reputation Decreased",
            "walang bitaw ya!"
            ]:
                print(line.center(width))
            print()
        
            if rep < 0:
                print("\n" + "="*195)
                print("  INVESTIGATION FAILED!".center(width))
                print("  Your reputation is too low.".center(width))
                print("  You have LOST YOUR JOB.".center(width))
                print("="*195)
                time.sleep(3)
                case_index = 0          # reset back to first case
                input("\nPress Enter to try again...\n")
                return rep, False 
                break               
                
            else:
                continue

        print("\nPossible causes:")
        for i, c in enumerate(choices):
            print(f"{i+1}. {c}")


        answer = int(input("\nChoose cause of the old Man death: ")) - 1

        return choices[answer] == victim["cause_of_death"]

def Investigate2(rep):
    global reputation
    reputation = rep

    hint2(ingame_contents.evidence_2)
    time.sleep(1.5)

    evidences = list(evidence_map2.keys())
    width = 200
    for case in cases2:
        correct = play_case2(case, evidence_map2, rep)

    if correct:
        print("\n\nCorrect! Reputation Increase".center(width))
        reputation += 10
        return True

    else:
        print("\n\nWrong!! Reputation Decreased".center(width))
        reputation -= 15

    if reputation < 0:
        print("\n" + "="*40)
        print("  INVESTIGATION FAILED!".center(width))
        print("  Your reputation is too low.".center(width))
        print("  You have LOST YOUR JOB.".center(width))
        print("="*40)
        time.sleep(3)
        case_index = 0          # reset back to first case
        input("\nPress Enter to try again...\n".center(width))
        return reputation, False   
        

    
    time.sleep(3)

def menu2(rep,character):
    global reputation
    reputation = rep

    width = 200

    print(("*" * 30).center(width))
    print("You are now in the crime scene!!".center(width))
    case_text = f"""
Detective 1882 – {character} Case
A murder has occurred at Angel’s Share restaurant...

Playing as: {character}
Reputation: {reputation}
"""

    print("\n".join(line.center(width) for line in case_text.split("\n")))
        
    time.sleep(2)

    print("Victim: Unnamed Old Man".center(width))
    print("Cause of Death: Unknown".center(width))
    print("Location: Angel’s Staff".center(width))

    print("You arrive at the crime scene...".center(width))

    while True:
        print(("*" * 10 + " Main Menu " + "*" * 10).center(width))

        print(f"REPUTATION: {reputation}".center(width))

        menu_text = """
        1. Investigate Evidence
        2. Interrogate Suspect
        3. Accuse
        4. Exit
        """

        print("\n".join(line.center(width) for line in menu_text.split("\n")))
        
        try:
            choose = int(input("Enter your guess (1-4):"))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if choose == 1:
            Investigate2(reputation)
            
        elif choose == 2:
            Interogate2()
            continue
        elif choose == 3: 
            reputation, result = Accuse2(reputation)
            if reputation < 5:
                print(f"\nYour reputation is now {reputation}. Too low!")
                return reputation, False
            if result == True:
                return reputation,True
            else:
                continue
        elif choose == 4:
            print("\nInvestigation ended. Goodbye, Detective.")
            print("*".center(10) * 60)
            print("GOOD GAME".center(200))
            return reputation, False
        



    #########################CASE 3#########################
def menu3(rep3, character):
    ...
    global reputation
    reputation = rep3
    print("\t\t","*" * 30)
    print("""
        \t\tYou are now in the crime scene!!""")            
    print(f"""\n
            Detective 1882 – {character} Case
            A murder has occurred at Angel’s Share restaurant...""")
