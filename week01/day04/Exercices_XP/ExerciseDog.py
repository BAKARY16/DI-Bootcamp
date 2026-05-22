
# ---------------------------------------------
# Exercise 3: Dogs Domesticated

# Step 1: Import the Dog Clas
from Exercices import Dog
import random

# Step 2: Create the PetDog Class
class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False
    
    # dImplement a train() method that prints the output of bark() and sets trained to True
    def train(self):
        self.bark()
        self.trained = True

    def play(self, *args):
        print("{} is playing with {}.".format(args[0].name, ", ".join([dog.name for dog in args[1:]])))

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")
        else:
            print(f"{self.name} is not trained yet")

# Step 3: Test PetDog Methods
my_dog = PetDog("Fido", 2, 10)
friend_dog = PetDog("Buddy", 3, 12)

my_dog.train()
my_dog.play(friend_dog)
my_dog.do_a_trick()
