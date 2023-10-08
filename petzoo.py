class Animal: # This is the base class for all animals in the zoo. 
    def __init__(self, name, age, species, health_status, happiness_level):
        self.name = name
        self.age = age
        self.species = species
        self.health_status = health_status
        self.happiness_level = happiness_level

    def feed(self, food_type): #  method adjusts the health_status of the animal based on the type of food it's given
        if food_type == "meat":
            self.health_status -= 5
        elif food_type == "vegetables":
            self.health_status -= 3
        else:
            print("The animal does not like the type of food given")

    def play(self, game): # method adjusts the happiness_level based on the type of game played.
        if game == "fetch":
            self.happiness_level += 5
        elif game == "chase_tail":
            self.happiness_level += 3
        else:
            print("The animal does not enjoy the game")
# These classes inherit from the Animal class. They have their own __init__ methods that call the parent class's __init__ method using super()
class Panda(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Herbivore", 100, 70)

class Elephant(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Herbivore", 100, 60)

class Monkey(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Herbivore", 100, 90)

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Carnivore", 100, 50)

class Bear(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Carnivore", 100, 50)

class Zoo: # This class represents the zoo. 
# initilizes an empty list to store the animal instances in the zoo.
    def __init__(self):
        self.animals = []

    def add_animal(self, animal): #Adds an animal instance to the list of animals in the zoo.
        self.animals.append(animal)

    def remove_animal(self, animal_name): #  Removes an animal by name from the list of animals and prints a message if the animal has already been adopted
        for animal in self.animals:
            if animal.name == animal_name:
                self.animals.remove(animal)
                print(f"{animal_name} has already been adopted hence not in the zoo.")
                return
        print(f"{animal_name} not found in the zoo.")

    def check_animal_status(self, animal_name): #Prints the status (name, age, happiness level, and health status) of a specific animal based on its name.
        for animal in self.animals:
            if animal.name == animal_name:
                print(f"Animal: {animal.name}")
                print(f"Age: {animal.age} years")
                print(f"Happiness Level: {animal.happiness_level}")
                print(f"Health Status: {animal.health_status}")
                return
        print(f"{animal_name} not found in the zoo.")

    def display_zoo_status(self): # Prints the status of all animals in the zoo.
        print("\nZoo Status:")
        for animal in self.animals:
            print(f"{animal.name} - {animal.species}:")
            print(f"Age: {animal.age} years")
            print(f"Happiness Level: {animal.happiness_level}")
            print(f"Health Status: {animal.health_status}")

# create some animals
panda = Panda("Po", 5)
elephant = Elephant("Elp", 10)
monkey = Monkey("Tinny", 3)
cat = Cat("Whiskers", 4)
bear = Bear("Teddy", 8)

# create an instance of the zoo
my_zoo = Zoo()

# add animals to the zoo
my_zoo.add_animal(panda)
my_zoo.add_animal(elephant)
my_zoo.add_animal(monkey)
my_zoo.add_animal(cat)
my_zoo.add_animal(bear)
# main menu loop enters a loop that displays a menu of options for interacting with the animals in the zoo. 
while True:
    print("\nZoo Menu:")
    print("1. Feed the animals") #  the feed method of each animal adjusts their health status accordingly.
    print("2. Play with the animals") #  the play method of each animal adjusts their happiness level.
    print("3. Check animal status")
    print("4. Quit")

    choice = input("Enter your choice: ") # handling user choices

    if choice == "1":
        food_type = input("Enter food type (meat/vegetables): ")
        for animal in my_zoo.animals:
            animal.feed(food_type)
        my_zoo.display_zoo_status()

    elif choice == "2":
        game = input("Enter game to play (fetch/chase_tail): ")
        for animal in my_zoo.animals:
            animal.play(game)
        my_zoo.display_zoo_status()

    elif choice == "3":
        animal_name = input("Enter animal name to check status: ")
        my_zoo.check_animal_status(animal_name)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
