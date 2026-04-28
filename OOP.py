class G_State:
    def __init__(self):
        self.reputation = 10





class Suspect:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def speak(self):
        print(f"{self.name}: What!? I dont know")

    def speak_2(self):
        print(f"{self.name}: What!? I dont know")

class ONE(Suspect):
    def speak(self):
        print(f"""
        "name": {self.name}:,
        "role": "{self.job}",
        "dialogue": "I was just preparing food... I did nothing wrong!""")

    def speak_2(self):
        print(f"""
        "name": {self.name}:,
        "role": "{self.job}", """)
        print("DIALOGUE: “Everything happened too fast… I only remember the old man falling.” ")
        

    def accuse(self):
        print("SKILL ISSUE")
    

class TWO(Suspect):
    def speak(self):
        print(f"""
        "name": {self.name}:,
        "role": "{self.job}",
        "dialogue": “I… I prepared all the dishes personally before service. No one else touched the final plating." """)
    
    def speak_2(self):
        print(f"""
        "name": {self.name}:,
        "role": "{self.job} STATUS (DEAD)", """)
        print("DIALOGUE: “Wait—why are you sending me to Angel’s Staff instead of the agreed drop point?” ")


    def accuse(self):
        print(f"Justice has been served.")

class THREE(Suspect):
    def speak(self):
        print(f"""
        "name": {self.name}:,
        "role": "{self.job}",
        "dialogue": "I only serve the dishes, I don’t touch the kitchen!" """)
    def speak_2(self):
        print(f"""
        "name": {self.name}:,
        "role": "{self.job}" """)
        print("DIALOGUE: ”“And about the old man… Mistakes happen in crowded environments. Wrong place, wrong timing. That’s all it is.” ")


    def accuse(self):
        print("ARE YOU STUPID?")

     #OOP MODULE

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