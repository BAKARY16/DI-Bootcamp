# This file contains the code for the exercises XP of the day3. 
# Each exercise is separated by a comment line for clarity.


# Exercise 1: Cats
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects
# cat1 = create the object
cat1 = Cat("bilou", 3)
cat2 = Cat("lilou", 10)
cat3 = Cat("milou", 5)

# Step 2: Create a function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    # ... code to find and return the oldest cat ...
    if cat1.age > cat2.age and cat1.age > cat3.age :
        print("The oldest cat is {} and it is {} years old.".format(cat1.name, cat1.age))
    elif cat2.age > cat1.age and cat2.age > cat3.age :
        print("The oldest cat is {} and it is {} years old.".format(cat2.name, cat2.age))
    else :
        print("The oldest cat is {} and it is {} years old.".format(cat3.name, cat3.age))
     

# Step 3: Print the oldest cat's details
find_oldest_cat(cat1, cat2, cat3)


# -----------------------------------------------------------------

# Exercise 2 : Dogs

# Step 1: Create the Dog Class
class Dog():
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print("{} goes woof!".format(self.name))

    def jump(self):
        jump_height = self.height * 2
        print("{} jumps {} cm high!".format(self.name, jump_height))

# Step 2: Create Dog Objects
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Buddy", 40)

# Step 3: Print Dog Details and Call Methods
print(davids_dog.name)
print(davids_dog.height)
davids_dog.bark()
davids_dog.jump()

print(sarahs_dog.name)
print(sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()

# Step 4: Compare Dog Sizes
if davids_dog.height > sarahs_dog.height :
    print("{} is bigger than {}.".format(davids_dog.name, sarahs_dog.name))
elif davids_dog.height < sarahs_dog.height :
    print("{} is bigger than {}.".format(sarahs_dog.name, davids_dog.name))


# -----------------------------------------------------------------


# Exercise 3 : Who’s the song producer

# Step 1: Create the Song Class
class Song :
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self) :
        for line in self.lyrics :
            print(line)

stairway = Song(["There’s a lady who's sure", 
                 "all that glitters is gold",
                  "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()


# ------------------------------------------------------------------


# exercise 4 : The Zoo
# Step 1: Define the Zoo Class
# Create a class called Zoo.
class Zoo:
    #  Implement the __init__() method
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    # Add a method add_animal(new_animal)
    def add_animal(self, *new_animals):
        for new_animal in new_animals:
            if new_animal not in self.animals:
                self.animals.append(new_animal)
            else:
                print("{} is already in the zoo.".format(new_animal))
    
    # Add a method get_animals()
    def get_animals(self):
        print("The animals in {} are : {}.".format(self.name, self.animals))

    # Add a method sell_animal(animal_sold)
    def sell_animal(self, animal_sold) :
        if animal_sold in self.animals :
            self.animals.remove(animal_sold)
    
    # Add a method sort_animals()
    def sort_animals(self) :
        sorted_animals = {}
        for animal in sorted(self.animals):
            first_letter = animal[0].upper()
            sorted_animals.setdefault(first_letter, []).append(animal)
        self.groups = sorted_animals
        return sorted_animals

    # # Add a method get_groups()
    def get_groups(self) :
        groups = getattr(self, 'groups', None)
        if groups is None:
            groups = self.sort_animals()
        for key in sorted(groups):
            print("{}: {}".format(key, groups[key]))

# Step 2: Create a Zoo Object
safari_zoo = Zoo("Safari Zoo")

# Step 3: Call the Zoo Methods
safari_zoo.add_animal("Giraffe", "Cat", "Cougar", "Lion")
safari_zoo.add_animal("Bear", "Zbra")
safari_zoo.add_animal("Baboon")
safari_zoo.get_animals()
safari_zoo.sell_animal("Bear")
safari_zoo.get_animals()
safari_zoo.sort_animals()
safari_zoo.get_groups()

