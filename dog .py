class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is a dog who is {self.age} years old.")

    def get_info(self):
        print(f"{self.name} has a {self.coat_color} coat.")

class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def hunt(self):
        print(f"{self.name} is a skilled hunter.")

    def playfulness(self):
        print(f"{self.name} is very playful and energetic.")

class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def strength(self):
        print(f"{self.name} is a strong and powerful dog.")

    def loyalty(self):
        print(f"{self.name} is very loyal to its owner.")

# Create objects
dog1 = Dog("Buddy", 5, "brown")
dog2 = JackRussellTerrier("Riley", 3, "white")
dog3 = Bulldog("Charlie", 7, "black")

# Call methods on objects
dog1.description()
dog1.get_info()

dog2.description()
dog2.get_info()
dog2.hunt()
dog2.playfulness()

dog3.description()
dog3.get_info()
dog3.strength()
dog3.loyalty()