class G_State:
    def __init__(self):
        self.reputation = 10



<<<<<<< HEAD


=======
>>>>>>> bb415bafaf0a98a7513bc318c4cd0280b7e2c3dd
class Suspect:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def speak(self):
        print(f"{self.name}: What!? I dont know")

class JENNSKY(Suspect):
    def speak(self):
        print(f"""
        "name": {self.name}:,
        "role": "{self.job}",
        "dialogue": "I was just preparing food... I did nothing wrong!""")

    def accuse(self):
        print("SKILL ISSUE")
    

class FRANCO(Suspect):
    def speak(self):
        print(f"""
        "name": {self.name}:,
        "role": "{self.job}",
        "dialogue": “I… I prepared all the dishes personally before service. No one else touched the final plating." """)

    def accuse(self):
        print(f"Justice has been served.")

class MELVIN(Suspect):
    def speak(self):
        print(f"""
        "name": {self.name}:,
        "role": "{self.job}",
        "dialogue": "I only serve the dishes, I don’t touch the kitchen!" """)

    def accuse(self):
        print("ARE YOU STUPID?")