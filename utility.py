import time
import random
import random_module
import ingame_contents
import OOP


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


#CASE 3
cases3 = ingame_contents.cases3
evidence_map3 = ingame_contents.evidence_map3
evidence_map44 = ingame_contents.evidence_map44
cause_of_death_3 = ingame_contents.cause_of_death_3



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


        rep2,case_solved = menu(rep, character)
        

        # --- End of investigation check ---

        if case_solved == True and rep2 >= 5:
            case_index += 1

        elif case_solved == False:
            print("\nInvestigation ended. Goodbye, Detective.")
            case_index = 0 
            return False
        

        if case_index == 1:
            print(f"\n{'='*40}")
            print(f"  Case solved! Advancing to Case {case_index + 1}...")
            print(f"\n{'='*40}")
            print(f"  INVESTIGATION — CASE {case_index + 1}")
            print(f"  Reputation: {rep2}")
            print(f"{'='*40}\n")
            time.sleep(1)
            ch = character
            rep3,case_solved2 = menu2(rep2, ch)
            print(f"{'='*40}")
            time.sleep(2)
        else:
            break

        if case_solved2 == True and rep3 > 0:
                case_index += 1

        elif case_solved2 == False and rep3 < 0:
                print("\n\nYou failed. Goodbye, Detective.")
                time.sleep(2)
                case_index = 0 
                return False
        
        if case_index == 2:
            print(f"\n{'='*40}")
            print(f"  Case solved! Advancing to Case {case_index + 1}...")
            print(f"\n{'='*40}")
            print(f"  INVESTIGATION — CASE {case_index + 1}")
            print(f"  Reputation: {rep2}")
            print(f"{'='*40}\n")
            time.sleep(1)
            ch = character
            rep4,case_solved3 = menu3(rep3, ch)
            print(f"{'='*40}")
            time.sleep(2)
        else:
            break

        if case_solved3 == True and rep4 > 0:
            print("\n" + "="*40)
            print("  INVESTIGATION COMPLETE!")
            print("  Your reputation is {rep}")
            print("  CONGRATS MA SANA BINABASA MO")
            print("="*40)
            time.sleep(3)
            return True

        elif case_solved3 == False and rep4 < 0:
                print("\n\nYou failed. Goodbye, Detective.")
                time.sleep(2)
                case_index = 0 
                return False


       
def menu(rep,character):
    global reputation
    reputation = rep
    print("\t\t","*" * 30)
    print("""
        \t\tYou are now in the crime scene!!""")

    print(f"""\n
            Detective 1882 – {character} Case
            A murder has occurred at Angel’s Share restaurant...
        
                    Playing as: {character}
                    Reputation: {reputation}
                    """)
        
    time.sleep(2)

    print("\n\nVictim: Robert")
    print("Cause of Death: Unknown")
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
            reputation, result = Investigate(reputation)  
            if reputation > 0 and result == True:
                continue
            elif reputation < 0:
                return reputation, False
            else:
                continue 
        elif choose == 2:
            Interogate()
            continue
        elif choose == 3: 
            reputation, result = Accuse(reputation)
            if reputation < 0 and result == False:
                return reputation,False
            elif reputation > 0 and result == True :
                return reputation, True
        elif choose == 4:
            break
        
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
            print("\n\nWrong!! Reputation Decreased\n\nWalang Bitaw ya!\n")
            lost = random_module.reputation()
            rep -= lost
            print(f"REPUTATION DECREASED BY: {lost} ")
            print(f"REPUTATION: {rep} \n")
        
            if rep < 0:    # reset back to first case
                return rep, False
                        
            else:
                continue

        print("\nPossible causes:")
        for i, c in enumerate(choices):
            print(f"{i+1}. {c}")


        answer = int(input("\nChoose cause of death: ")) - 1

        f_ans = choices[answer] == victim["cause_of_death"]

        if f_ans:
            return rep, True
        else:
            print("\n\nWrong!! Reputation Decreased")
            print(f"REPUTATION DECREASED BY: 15 ")
            rep -= 15
            return rep, False


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
        reputation,correct = play_case(case, evidence_map1, rep)

    if correct:
        print("\n\nCorrect! Reputation Increase")
        reputation += 10
        print(f"REPUTATION INCREASED BY: 10 ")
        return reputation, True

    elif reputation > 0:
        return reputation, True
        

    if reputation < 0:
        print("\n" + "="*40)
        print("  INVESTIGATION FAILED!")
        print("  Your reputation is too low.")
        print("  You have LOST YOUR JOB.")
        print("="*40)
        time.sleep(3)
        case_index = 0          # reset back to first case
        input("\nPress Enter to try again...\n")
        return reputation, False

    
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
        print(f"\nREPUTATION INCREASED BY: 20 ")
        selected.correct()
        reputation += 20

        time.sleep(1.5)
        return reputation,True
        

    else:
        selected.accuse()
        reputation -= 15
        print(f"\nREPUTATION DECREASED BY: 15 ")
        time.sleep(2)

        if reputation < 0:
            print("\n" + "="*40)
            print("  INVESTIGATION FAILED!")
            print("  Your reputation is too low.")
            print("  You have LOST YOUR JOB.")
            print("="*40)
            time.sleep(3)
            input("\nPress Enter to try again...\n")
            return reputation, False
        else:
            return reputation, False
            

#####################################################################

def generate_choices2(correct_answer, possible_causes):
    
    wrong = [c for c in cause_of_death_2 if c not in possible_causes]

    wrong_choices = random.sample(wrong, 2)

    choices = wrong_choices + [correct_answer]
    random.shuffle(choices)

    return choices

def Interogate2():
        melvin = OOP.THREE("JENSKY","BODYGUARD")
        jen = OOP.ONE("DANIEL","CUSTOMER")
        francon = OOP.TWO("IAN", "ANGEL STAFF")

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
        suspects[choose].speak_2()
        time.sleep(3)

def Accuse2 (rep):
    global reputation
    reputation = rep
    melvin = OOP.THREE("FRANCO","BODYGUARD")
    jen = OOP.ONE("MELVIN","BYSTANDER")
    franco = OOP.TWO("IAN", "KITCHEN STAFF")


    print(f"\n{"*" * 10}WHO IS THE CRIMANAL{"*" * 10}\n\n")
    print(f"\n{"*" * 10}SUSPECT{"*" * 10}\n") 

    suspects = (franco,jen, melvin)
    
    for i, e in enumerate(suspects):
        print(f"{i+1}. {e.name}")

    try:
        choose = int(input("\nChoose suspect to interrogate: "))-1
    except ValueError:
        print("Invalid input.")
        return
    
    selected = suspects[choose]

    if selected.name == "MELVIN":
        print("\n\nCORRECT!! Case Solved!")
        selected.correct()
        reputation += 20
        time.sleep(1.5)
        return reputation,True       

    else:
        selected.accuse()
        reputation -= 15
        print(f"\nREPUTATION DECREASED BY: 15 ")
        time.sleep(2)

        if reputation < 0:
            print("\n" + "="*40)
            print("  INVESTIGATION FAILED!")
            print("  Your reputation is too low.")
            print("  You have LOST YOUR JOB.")
            print("="*40)
            time.sleep(3)
            input("\nPress Enter to try again...\n")
            return reputation, False
        else:
            return reputation, False

def hint2(case):
    print(f"\n\n\n{'*'*10} EVIDENCE {'*'*10}")
    
    print("\n", case["HINT"], "\n")
    
    for evidence, description in case["HINTS"].items():
        print(evidence)
        print(description)

def play_case2(case, evidence_map2, rep):
    victim = case["victim"]

    print(f"\n{case['name']}")
    print(f"Victim: \n\tName: {victim['name']},\n\tAge: {victim['age']},\n\tCareer: {victim['career']}")
    print(f"Location: {case['location']}")

    # STEP 1: Evidence
    evidences = list(evidence_map2.keys())
    evidence_hint = evidence_map22

    while True:

        print("\nPossible Causes of Accident:")
        for i, e in enumerate(evidences):
            print(f"{i+1}. {e}")
            time.sleep(1)

        try:
            choice = int(input("\nSelect Possible Cause: "))-1
        except ValueError, IndexError:
            print("Please enter a valid number.")
            continue
        
        if choice > len(evidences):
            print("INVALID")
            continue

        selected_evidence = evidences[choice]

        if selected_evidence == "Victim Misidentified":
            possible_causes = evidence_map2[selected_evidence]
            choices = generate_choices2(victim["cause_of_death"], possible_causes)
        else:
            time.sleep(1)
            print("\n\nWrong!! Reputation Decreased\n\nWalang Bitaw ya!\n")
            lost = random_module.reputation()
            rep -= lost
            print(f"REPUTATION DECREASED BY: {lost} ")
            print(f"REPUTATION: {rep} \n")
        
            if rep < 0:
                return rep, False           
                
            else:
                continue

        print("\nPossible causes:")
        for i, c in enumerate(choices):
            print(f"{i+1}. {c}")


        answer = int(input("\nChoose cause of the old Man death: ")) - 1
    
        f_ans = choices[answer] == victim["cause_of_death"]

        if f_ans == True:
            return rep, True
        else:
            print("\n\nWrong!! Reputation Decreased")
            print(f"REPUTATION DECREASED BY: 15 ")
            rep -= 15
            return rep, False


def Investigate2(rep):
    global reputation
    reputation = rep

    hint2(ingame_contents.evidence_2)
    time.sleep(1.5)

    evidences = list(evidence_map2.keys())

    for case in cases2:
        reputation,correct = play_case2(case, evidence_map2, rep)

    if correct:
        print("\n\nCorrect! Reputation Increase")
        reputation += 10
        print(f"REPUTATION INCREASED BY: 10 ")
        return reputation, True
    
    elif reputation >= 0:
        return reputation, True

    if reputation < 0:
        print("\n" + "="*40)
        print("  INVESTIGATION FAILED!")
        print("  Your reputation is too low.")
        print("  You have LOST YOUR JOB.")
        print("="*40)
        time.sleep(3)
        case_index = 0          # reset back to first case
        input("\nPress Enter to try again...\n")
        return reputation, False
                    

    
    time.sleep(3)

def menu2(rep,character):
    global reputation
    reputation = rep
    print("\t\t","*" * 30)
    print("""
        \t\tYou are now in the crime scene!!""")

    print(f"""\n
            Detective 1882 – {character} Case
         After a suspicious death, someone flees and an old man dies instead. At another location, 
         a phone is found, left behind with a cryptic clue raising more questions than answers.
        
                    Playing as: {character}
                    Reputation: {reputation}
                    """)
        
    time.sleep(2)

    print("\n\nVictim: Unnamed Old Man")
    print("Cause of Death: UNKNOWN")
    print("Location: Angel’s Staff\n")

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
            reputation, result = Investigate2(reputation)  
            if reputation > 0 and result == True:
                continue
            elif reputation < 0 and result == False:
                return reputation, False
            else:
                continue 
        elif choose == 2:
            Interogate2()
            continue
        elif choose == 3: 
            reputation, result = Accuse2(reputation)
            if reputation < 0 and result == False:
                return reputation,False
            elif reputation > 0 and result == True :
                return reputation, True
        elif choose == 4:
            break
        elif choose == 4:
            print("\n" * 10, "THANK YOU FOR PLAYING","\n" * 10 )
            break
        

####################################################

def menu3(rep,character):

    global reputation
    reputation = rep
    print("\t\t","*" * 30)
    print("""
        \t\tYou are now in the crime scene!!""")

    print(f"""\n
            Detective 1882 – {character} Case
           After a gathering, a diplomat is found dead inside his room, and all guests become suspects. 
           With conflicting statements and unclear events, the truth behind what happened remains uncertain.
        
                    Playing as: {character}
                    Reputation: {reputation}
                    """)
        
    time.sleep(2)

    print("\n\nVictim: Myles")
    print("Cause of Death: Unknown")
    print("Location: Diplomat residence\n")

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
            reputation, result = Investigate3(reputation)  
            if reputation > 0 and result == True:
                continue
            elif reputation < 0 and result == False:
                return reputation, False
            else:
                continue 
        elif choose == 2:
            Interogate3()
            continue
        elif choose == 3: 
            reputation, result = Accuse3(reputation)
            if reputation < 0 and result == False:
                return reputation,False
            elif reputation > 0 and result == True :
                return reputation, True
        elif choose == 4:
            break
        elif choose == 4:
            print("\n" * 10, "THANK YOU FOR PLAYING","\n" * 10 )
            break
        
def hint3(proof):
    print(f"\n\n\n{"*"*10}EVIDENCE{"*"*10}")
    for case in proof:
        print("\n", case["HINT"], "\n")
        for evidence, description in case["HINTS"].items():
            print(evidence)
            print(description)


def play_case3(case, evidence_map3, rep):
    victim = case["victim"]

    print(f"\n{case['name']}")
    print(f"Victim: \n\tName: {victim['name']},\n\tAge: {victim['age']},\n\tCareer: {victim['career']}")
    print(f"Location: {case['location']}")

    # STEP 1: Evidence
    evidences = list(evidence_map3.keys())
    evidence_hint = ingame_contents.evidence_map44

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


        if selected_evidence == "Tea":
            possible_causes = evidence_map3[selected_evidence]
            choices = generate_choices(victim["cause_of_death"], possible_causes)
        else:
            time.sleep(1)
            print("\n\nWrong!! Reputation Decreased\n\nWalang Bitaw ya!\n")
            lost = random_module.reputation()
            rep -= lost
            print(f"REPUTATION DECREASED BY: {lost} ")
            print(f"REPUTATION: {rep} \n")
        
            if rep < 0:
                return rep, False       
                
            else:
                continue

        print("\nPossible causes:")
        for i, c in enumerate(choices):
            print(f"{i+1}. {c}")


        answer = int(input("\nChoose cause of death: ")) - 1

        f_ans = choices[answer] == victim["cause_of_death"]

        if f_ans == True:
            return rep, True
        else:
            print("\n\nWrong!! Reputation Decreased")
            print(f"REPUTATION DECREASED BY: 15 ")
            rep -= 15
            return rep, False


def generate_choices3(correct_answer, possible_causes):
    
    wrong = [c for c in cause_of_death_3 if c not in possible_causes]

    wrong_choices = random.sample(wrong, 2)

    choices = wrong_choices + [correct_answer]
    random.shuffle(choices)

    return choices


def Investigate3(rep):
    global reputation
    reputation = rep

    hint3(ingame_contents.evidence_3)
    time.sleep(1.5)


    for case in cases3:
        reputation,correct = play_case3(case, evidence_map3, rep)

    if correct:
        print("\n\nCorrect! Reputation Increase")
        reputation += 10
        print(f"REPUTATION INCREASED BY: 10 ")
        return reputation, True
    
    elif reputation >= 0:
        return reputation, True

    if reputation < 0:
        print("\n" + "="*40)
        print("  INVESTIGATION FAILED!")
        print("  Your reputation is too low.")
        print("  You have LOST YOUR JOB.")
        print("="*40)
        time.sleep(3)
        case_index = 0          # reset back to first case
        input("\nPress Enter to try again...\n")
        return reputation, False

                    

    
    time.sleep(3)
    
def Interogate3():

        melvin = OOP.THREE("JENNSKY","ASSISTANT")
        francon = OOP.TWO("IAN", "BUSINESS PARTNER")
        jen = OOP.ONE("DANIEL","CHEF")

        print(f"\n{"*" * 10}INTEROGATE{"*" * 10}\n\n")
        print(f"\n{"*" * 10}SUSPECT{"*" * 10}\n") 
    
       
        suspects = (melvin, francon, jen)

        for i, e in enumerate(suspects):
            print(f"{i+1}. {e.name}")

        try:
            choose = int(input("\nChoose suspect to interrogate: "))-1
        except ValueError:
            print("Invalid input.")
            return

    
        print("\nAre you the killer?\n")
        suspects[choose].speak_3()
        time.sleep(3)

def Accuse3(rep):
    global reputation
    reputation = rep

    melvin = OOP.THREE("JENNSKY","ASSISTANT")
    francon = OOP.TWO("IAN", "BUSINESS PARTNER")
    jen = OOP.ONE("DANIEL","CHEF")


    print(f"\n{"*" * 10}WHO IS THE CRIMANAL{"*" * 10}\n\n")
    print(f"\n{"*" * 10}SUSPECT{"*" * 10}\n") 

    suspects = (melvin, francon, jen)
    
    for i, e in enumerate(suspects):
        print(f"{i+1}. {e.name}")

    try:
        choose = int(input("\nChoose suspect to interrogate: "))-1
    except ValueError:
        print("Invalid input.")
        return
    
    selected = suspects[choose]

    if selected.name == "IAN":
        print("\n\nCORRECT!! Case Solved!")
        selected.correct()
        reputation += 20
        time.sleep(1.5)
        return reputation,True
        

    else:
        selected.accuse()
        reputation -= 15
        print(f"\nREPUTATION DECREASED BY: 15 ")
        time.sleep(2)

        if reputation < 0:
            print("\n" + "="*40)
            print("  INVESTIGATION FAILED!")
            print("  Your reputation is too low.")
            print("  You have LOST YOUR JOB.")
            print("="*40)
            time.sleep(3)
            input("\nPress Enter to try again...\n")
            return reputation, False
        else:
            return reputation, False