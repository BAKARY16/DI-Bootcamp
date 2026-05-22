
# -----------------------------------------------

# Exercise 1: Pets

# Step 1: Create the Siamese Class

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
# Step 1: Create the Siamese Class
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Step 2: Create a List of Cat Instances
all_cats = [Cat("bobby", 3), Bengal("lilou", 10), Chartreux("milou", 5), Siamese("sylvester", 7)]

# Step 3: Create a Pets Instance
sara_pets = Pets(all_cats)

# Step 4: Take Cats for a Walk
sara_pets.walk()


# -------------------------------------------------------------------------------


# Exercise 2: Dogs

# Step 1: Create the Dog Class
class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight= weight      
    
    def bark(self):
        print("{} goes woof!".format(self.name))
    
    def run_speed(self) :
        speed = self.weight / self.age * 10
        return speed
    
    def fight(self, other_dog) :
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight :
            print("{} wins the fight.".format(self.name))
        elif self.run_speed() * self.weight < other_dog.run_speed() * other_dog.weight :
            print("{} wins the fight.".format(other_dog.name))
        else :
            print("It's a tie between {} and {}.".format(self.name, other_dog.name))


# Step 2: Create Dog Instances
dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Buddy", 3, 15)
Cesar_dog = Dog("Cesar", 4, 25)

# Step 3: Test dog methods
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))

# ------------------------------------------------------

# Exercise 3: Dogs Domesticated

# The code for this exercise is in ExerciseDog.py, 
# which imports the Dog class from this file.

# ----------------------------------------------------------

# Exercise 4: Family and Person Classes

# Step 1: Create the Person Class

class Person():
    def __init__(self, first_name, age, last_name=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def is_18(self):
        if self.age >= 18:
            return True
        else :
            return False

# Étape 2 : Créer la Familyclasse