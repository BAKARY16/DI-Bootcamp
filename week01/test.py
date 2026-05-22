# Step 1: Create the Person Class

class Person():
    def __init__(self, first_name, age, last_name=""):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def is_18(self):
        return self.age >= 18

# Étape 2 : Créer la Familyclasse

class Family():
    def __init__(self, last_name, members=None):
        self.last_name = last_name
        self.members = members if members is not None else []

    def born(self, first_name, age):
        new_member = Person(first_name, age, self.last_name)
        self.members.append(new_member)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print("Person not found in the family.")

    def family_presentation(self):
        print(f"Family last name: {self.last_name}")
        for member in self.members:
            print(f"{member.first_name}, {member.age} years old")



renzo_family = Family("Renzo")

results = renzo_family.check_majority("Renzo")
print(results)