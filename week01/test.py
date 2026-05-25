# Exercise 2 : Custom List Class
import random

class MyList:
    def __init__(self, letters):
        self.letter = letters
    
    def inverse(self):
        return self.letter[::-1]
    
    def sorted_list(self):
        return sorted(self.letter)
    
    def random_list(self):
        return [random.randint(0, 100) for _ in range(len(self.letter))]
    

req = MyList(["sinon", "bakary"])
print(req.inverse())

a = "Python"
print(a[2:5])