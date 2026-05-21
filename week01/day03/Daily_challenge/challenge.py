# --------- Daily challenge: Old MacDonald’s Farm -----------

# Step 1: Create the Farm Class

class Farm:
    # Step 2: Implement the __init__ Method
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    # Step 3: Implement the add_animal Method
    def add_animal(self, animal_type=None, count=1, **animals):
        if animal_type:
            self.animals[animal_type] = self.animals.get(animal_type, 0) + count
        for animal, qty in animals.items():
            self.animals[animal] = self.animals.get(animal, 0) + qty

    # Step 4: Implement the get_info Method
    def get_info(self):
        lines = [f"{self.name}'s farm", ""]
        for animal, count in self.animals.items():
            lines.append(f"{animal} : {count}")
        lines.append("")
        lines.append("    E-I-E-I-0!")
        return "\n".join(lines)

    # Step 6: Implement the get_animal_types Method
    def get_animal_types(self):
        return sorted(self.animals.keys())

    # Step 7: Implement the get_short_info Method
    def get_short_info(self):
        types = []
        for animal in self.get_animal_types():
            count = self.animals[animal]
            label = animal + ('s' if count > 1 else '')
            types.append(label)
        if not types:
            animal_list = ''
        elif len(types) == 1:
            animal_list = types[0]
        elif len(types) == 2:
            animal_list = f"{types[0]} et {types[1]}"
        else:
            animal_list = ", ".join(types[:-1]) + f" et {types[-1]}"
        return f"La ferme de {self.name} possède des {animal_list}."


macdonald = Farm('McDonald')
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep', 12)
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_short_info())
