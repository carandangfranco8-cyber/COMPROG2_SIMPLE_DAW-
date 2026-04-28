import random
import ingame_contents

suspect = ["JENNSKY","MELVIN", "IAN", "FRANCO", "DANIEL"]

def reputation():
    return random.randint(5, 10) 

def culprit():
    return random.choice(ingame_contents.suspect)
    
def name():
    return random.choice(suspect)