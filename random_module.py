import random
import ingame_contents


def reputation():
    return random.randint(5, 10) 

def culprit():
    return random.choice(ingame_contents.suspect)
    
