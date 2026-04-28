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
        "role": "{self.job}", 
        "dialogue" : “No… I was there because the hitman’s call came to me—I answered, stayed on the line during the struggle, and now my phone makes it look like I was involved, but I didn’t kill him.””""")
        

    def speak_3(self):
        print(f"""
        "name": {self.name}:,
        "role": "{self.job}",
        "dialogue": "I prepared the tea as usual. Everything was fine when I left it" """)
        

    def accuse(self):
        print("SKILL ISSUE")
    
    def correct(self):
        print("MAY BITAW KA MAN")
    

class TWO(Suspect):
    def speak(self):
        print(f"""
        "name": {self.name}:,
        "role": "{self.job}",
        "dialogue": “I… I prepared all the dishes personally before service. No one else touched the final plating." """)
    
    def speak_2(self):
        print(f"""
        "name": {self.name}:,
        "role": "{self.job}",
        "dialogue": “That’s… a strange question, detective. I cook. I serve. I clean. That’s all people ever see. If I wanted someone dead, don’t you think I’d be more… careful? """)
    

        #killer
    def speak_3(self):
        print(f"""
        "name": {self.name}:,
        "role": "{self.job}",
        "dialogue": “I was around before the gathering… but I wasn’t involved in anything important.” """)


    def accuse(self):
        print(f"KULANG KA PA SA KANIN YAH")

    def correct(self):
        print("MAY BITAW KA MAN")

class THREE(Suspect):
    def speak(self):
        print(f"""
        "name": {self.name}:,
        "role": "{self.job}",
        "dialogue": "I only serve the dishes, I don’t touch the kitchen!" """)

    def speak_2(self):
        print(f"""
        "name": {self.name}:,
        "role": "{self.job}",
        "dialogue": "If I were, Mr. Stank wouldn’t still be breathing. My job is to take bullets, not fire them. Whoever did this knew Tony’s schedule but they didn’t expect me." """)



    def speak_3(self):
        print(f"""
        "name": {self.name}:,
        "role": "{self.job}",
        "dialogue": “I just followed instructions during service. Nothing more.” """)



    def accuse(self):
        print("ARE YOU STUPID?")

    def correct(self):
        print("IKAW BA YAN DETECTIVE CONAN")
