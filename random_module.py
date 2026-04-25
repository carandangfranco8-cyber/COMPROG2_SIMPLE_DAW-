import random
import ingame_contents


def reputation():
    reputation = random.randint(1, 10)
    return reputation   

def culprit():
    culprit = random.choice(ingame_contents.suspect)
    return