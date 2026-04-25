import random
import ingame_contents

print("You are now in the crime scene!!")

cases = ingame_contents.cases
cause_of_death = ingame_contents.cause_of_death
evidence_map1 = ingame_contents.evidence_map1

def generate_choices(correct_answer, possible_causes):
    wrong = [c for c in cause_of_death if c not in possible_causes]

    wrong_choices = random.sample(wrong, 2)

    choices = wrong_choices + [correct_answer]
    random.shuffle(choices)

    return choices


def play_case(case, evidence_map1):
    victim = case["victim"]

    print(f"\n{case['name']}")
    print(f"Victim: {victim['name']}, {victim['age']}, {victim['career']}")
    print(f"Location: {case['location']}")

    # STEP 1: Evidence
    evidences = list(evidence_map1.keys())

    print("\nChoose Evidence:")
    for i, e in enumerate(evidences):
        print(f"{i+1}. {e}")

    choice = int(input("Select evidence: ")) - 1
    selected_evidence = evidences[choice]

    # STEP 2: Get possible causes
    possible_causes = evidence_map1[selected_evidence]

    # STEP 3: Generate choices
    choices = generate_choices(victim["cause_of_death"], possible_causes)

    print("\nPossible causes:")
    for i, c in enumerate(choices):
        print(f"{i+1}. {c}")

    answer = int(input("Choose cause of death: ")) - 1

    return choices[answer] == victim["cause_of_death"]


reputation = 10

for case in cases:
  correct = play_case(case, evidence_map1)

  if correct:
    print("Correct! Reputation Increase")
    reputation += 10

  else:
    print("Wrong!! Reputation Decreased")
    reputation -= 15

  if reputation < 5:
    print("You've lost all your reputation. No one trusts you now!")
    break


