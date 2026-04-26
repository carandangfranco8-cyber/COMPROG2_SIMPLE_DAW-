import time
import random
import random_module
import ingame_contents
import OOP



cases = ingame_contents.cases
cause_of_death = ingame_contents.cause_of_death
evidence_map1 = ingame_contents.evidence_map1



def run_game(starting_reputation, character):
    case_index = 0

    while True:
        global rep
        rep = starting_reputation
        print(f"\n{'='*40}")
        print(f"  INVESTIGATION — CASE {case_index + 1}")
        print(f"  Reputation: {rep}")
        print(f"{'='*40}\n")
        time.sleep(1)

        case_solved = menu(starting_reputation, character)

        # --- End of investigation check ---
        if rep < 5:
            print("\n" + "="*40)
            print("  INVESTIGATION FAILED!")
            print("  Your reputation is too low.")
            print("  You have LOST YOUR JOB.")
            print("="*40)
            time.sleep(3)
            case_index = 0          # reset back to first case
            input("\nPress Enter to try again...\n")
            import main2  # restart the game
            main2.run_game(starting_reputation)
            break               

        if case_solved:
            case_index += 1
            print(f"\n{'='*40}")
            print(f"  Case solved! Advancing to Case {case_index + 1}...")
            print(f"{'='*40}")
            time.sleep(2)
            if case_index == 2:
                print("\nYou've solved ALL cases! You are a Master Detective!")
                break
        else:
            print("\nInvestigation ended. Goodbye, Detective.")
            break


def menu(rep,character):
    global reputation
    reputation = rep
    print("\t\t","*" * 30)
    print("""
        \t\tYou are now in the crime scene!!""")

    print(f"""\n
            Detective 1882 – Sherlock Swagman Case
            A murder has occurred at Angel’s Share restaurant...
        
                    Playing as: {character}
                    Reputation: {reputation}
                    """)
        
    time.sleep(2)

    print("\n\nVictim: Robert")
    print("Cause of Death: Anaphylaxis due to poisoning")
    print("Location: Angel’s Share Kitchen\n")

    print("You arrive at the crime scene...")

    while True:
        print(f"\n\n{"*" * 10}Main Menu{"*" * 10}\n")

        print(f"REPUTATION: {reputation}")

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
            Investigate(reputation)
            
        elif choose == 2:
            Interogate()
            continue
        elif choose == 3: 
            result = Accuse(reputation)
            if result == True:
                return True
            else:
                continue
        elif choose == 4:
            return False
            
           
        
def hint(proof):
    print(f"\n\n\n{"*"*10}EVIDENCE{"*"*10}")
    for case in proof:
        print("\n", case["HINT"], "\n")
        for evidence, description in case["HINTS"].items():
            print(evidence)
            print(description)


def play_case(case, evidence_map1, rep):
    victim = case["victim"]

    print(f"\n{case['name']}")
    print(f"Victim: \n\tName: {victim['name']},\n\tAge: {victim['age']},\n\tCareer: {victim['career']}")
    print(f"Location: {case['location']}")

    # STEP 1: Evidence
    evidences = list(evidence_map1.keys())

    while True:

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
            rep -= lost
            print(f"REPUTATION DECREASED BY: {lost} ")
            print(f"REPUTATION: {rep} \n")
        
            if rep < 0:
                print("\n" + "="*40)
                print("  INVESTIGATION FAILED!")
                print("  Your reputation is too low.")
                print("  You have LOST YOUR JOB.")
                print("="*40)
                time.sleep(3)
                case_index = 0          # reset back to first case
                input("\nPress Enter to try again...\n")
                import main2  # restart the game
                main2
                break               
                
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

    if correct:
        print("\n\nCorrect! Reputation Increase")
        reputation += 10
        return True

    else:
        print("\n\nWrong!! Reputation Decreased")
        reputation -= 15

    if reputation < 0:
        print("\n" + "="*40)
        print("  INVESTIGATION FAILED!")
        print("  Your reputation is too low.")
        print("  You have LOST YOUR JOB.")
        print("="*40)
        time.sleep(3)
        case_index = 0          # reset back to first case
        input("\nPress Enter to try again...\n")
        import main2  # restart the game
        main2
                    

    
    time.sleep(3)
    

        
def Interogate():
        melvin = OOP.THREE("MELVIN","WAITER")
        jen = OOP.ONE("JENNSKY","KITCHEN STUFF")
        francon = OOP.TWO("FRANCO", "HEAD CHEF")

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

def Accuse(rep):
    global reputation
    reputation = rep
    melvin = OOP.THREE("MELVIN","WAITER")
    jen = OOP.ONE("JENNSKY","KITCHEN STUFF")
    franco = OOP.TWO("FRANCO", "HEAD CHEF")


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
        reputation += 20
        time.sleep(1.5)
        return True
        

    else:
        selected.accuse()
        reputation -= 15
        time.sleep(2)
        return False
       

