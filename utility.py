import time
import random
import ingame_contents
import OOP
import random_module


cases = ingame_contents.cases
cause_of_death = ingame_contents.cause_of_death
evidence_map1 = ingame_contents.evidence_map1
evidence_map11 = ingame_contents.evidence_map11
rep=OOP.G_State()

#DITO NA KAYO
def case():
    
    while True:
        print(f"\n{"*" * 10}Main Menu{"*" * 10}\n\n")

        print("REPUTATION: ", rep.reputation)

        print(f"""
                1. CASE 1
                2. CASE 2
                3. Exit
              
               """)
        
        try:
            choose = int(input("Enter your guess (1-4):"))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if choose == 1:
            print("""\n
            Detective 1882 – Sherlock Swagman Case
            A murder has occurred at Angel’s Share restaurant...""")
        
            time.sleep(2.5)

            menu()
            
        elif choose == 2:
            pass
        elif choose == 3: 
            break



def menu():

    while True:
        print(f"\n{"*" * 10}Main Menu{"*" * 10}\n")
        print("You are now in the crime scene!!")
        print("\n\nVictim: Robert")
        print("Cause of Death: Anaphylaxis due to poisoning")
        print("Location: Angel’s Share Kitchen\n")
        print("You arrive at the crime scene...")

        print("REPUTATION: ", rep.reputation)

        print(f"""
                1. Investigate Evidence
                2. Interrogate Suspect
                3. Accuse
                4. Exit
              
               """)
        
        try:
            choose = int(input("Enter your guess (1-4):"))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if choose == 1:
            Investigate1()
            
        elif choose == 2:
            Interogate1()
        elif choose == 3: 
            Accuse1()
        elif choose == 4:
            break
            
        
def hint(proof):
    print(f"\n\n\n{"*"*10}EVIDENCE{"*"*10}")
    for case in proof:
        print("\n", case["HINT"], "\n")
        for evidence, description in case["HINTS"].items():
            print(evidence)
            print(description)


def play_case(case, evidence_map1):
    victim = case["victim"]

    print(f"\n{case['name']}")
    print(f"Victim: {victim['name']}, {victim['age']}, {victim['career']}")
    print(f"Location: {case['location']}\n\n")



    # STEP 1: Evidence
    evidences = list(evidence_map1.keys())
    evidence_hint = evidence_map11
    while True:

        print("BASED ON THE REPORT:")
        for i, c in enumerate(evidence_hint):
            print(f"{i+1}. {c}")
            time.sleep(1.5)

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
            print("\n\nWrong!! Reputation Decreased\n\nWalang Bitaw ya!\n")
            lost = random_module.reputation()
            rep.reputation -= lost
            print(f"REPUTATION DECREASED BY: {lost} ")
            print(f"REPUTATION: {rep.reputation} \n")
            continue

        print("\nPossible causes:")
        for i, c in enumerate(choices):
            print(f"{i+1}. {c}")


        answer = int(input("\nChoose cause of death: ")) - 1

        return choices[answer] == victim["cause_of_death"]


def generate_choices(correct_answer, possible_causes):

    
    wrong = [c for c in cause_of_death if c not in possible_causes]

    wrong_choices = random.sample(wrong, 4)

    choices = wrong_choices + [correct_answer]
    random.shuffle(choices)

    return choices


def Investigate1():
    
    hint(ingame_contents.evidence2)
    time.sleep(3)

    evidences = list(evidence_map1.keys())

    for case in cases:
        correct = play_case(case, evidence_map1)

    if correct:
        gained= random_module.reputation()
        rep.reputation += gained
        print(f"\n\nCorrect! Reputation Increase by {gained}")
        return 

    else:
        print("\n\nWrong!! Reputation Decreased")
        lost = random_module.reputation()
        rep.reputation -= lost
        print(f"REPUTATION DECREASED BY: {lost} REPUTATION: {rep.reputation} \n")

    if rep.reputation < 5:
        print("\n\nYou've lost all your reputation. No one trusts you now!\n\n")
    
    time.sleep(3)
    

        
def Interogate1():
        melvin = OOP.MELVIN("MELVIN","WAITER")
        jen = OOP.JENNSKY("JENNSKY","KITCHEN STUFF")
        francon = OOP.FRANCO("FRANCO", "HEAD CHEF")

        print(f"\n{"*" * 10}INTEROGATE{"*" * 10}\n\n")
        print(f"\n{"*" * 10}SUSPECT{"*" * 10}\n") 
    
       
        suspects = (jen, melvin, francon)

        for i, e in enumerate(suspects):
            print(f"{i+1}. {e.name}")

        try:
            choose = int(input("\nChoose suspect to interrogate: "))-1
        except ValueError:
            print("Invalid input.")
            return

    
        print("\nWhere are you? Are you the killer?\n")
        suspects[choose].speak()
        time.sleep(3)

def Accuse1():
    melvin = OOP.MELVIN("MELVIN","WAITER")
    jen = OOP.JENNSKY("JENNSKY","KITCHEN STUFF")
    franco = OOP.FRANCO("FRANCO", "HEAD CHEF")


    print(f"\n{"*" * 10}WHO IS THE CRIMANAL{"*" * 10}\n\n")
    print(f"\n{"*" * 10}SUSPECT{"*" * 10}\n") 

    suspects = (jen, melvin, franco)

    for i, e in enumerate(suspects):
        print(f"{i+1}. {e.name}")

    try:
        choose = int(input("\nChoose suspect to interrogate: "))-1
    except ValueError:
        print("Invalid input.")
        return
    
    selected = suspects[choose]

    if selected.name == "FRANCO":
        print("\n\nCORRECT!! Case Solved!")
        selected.accuse()
        rep.reputation += 20
        print(f"\n\nCorrect! Reputation Increase by 20")
        time.sleep(1.5)
    else:
        selected.accuse()
        rep.reputation -= 15
        print("REPUTATION DECREASED BY: 15 \n")

        time.sleep(2)

