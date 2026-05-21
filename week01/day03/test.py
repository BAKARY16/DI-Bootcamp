

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