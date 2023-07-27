class Pokemon:
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack
 
    # One instance method
    def description(self):
        return f"{self.name} favorite attack is {self.attack}"
 
    # A second instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"