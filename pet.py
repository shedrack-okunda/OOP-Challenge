class Pet:
    def __init__(self, name):
        """
        Initializes a new Pet object.
        
        Args:
            name (str): The name of the pet.
        """
        self.name = name
        self.hunger = 10
        self.energy = 5
        self.happiness = 5
        self.tricks = []
        
    def eat(self):
        """
        Reduces hunger by 3 points and increases happiness by 1.
        """
        print(f"{self.name} is eating...")
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        
    def sleep(self):
        """
        Increases energy by 5 points.
        """
        print(f"{self.name} is sleeping...")
        self.energy = min(10, self.energy + 5)
        
    def play(self):
        """
        Decreases energy by 2, increases happiness by 2, and increases hunger by 1.
        """
        
        if self.energy < 2:
            print(f'{self.name} is too tired to play.')
        else:
            print(f"{self.name} is playing...")
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            
    def get_status(self):
        """
        Prints the current state of the pet.
        """
        print(f"{self.name}'s current status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        print(f"Tricks: {self.tricks}")
        
    def train(self, trick):
        """
        Teaches the pet a new trick.


        Args:
            trick (str): The name of the trick.
        """
        self.tricks.append(trick)
        print(f"{self.name} has learned {trick}!")
        
    def show_tricks(self):
        """
        Prints all learned tricks.
        """
        print(f"{self.name} knows the following tricks:")
        for trick in self.tricks:
            print(trick)