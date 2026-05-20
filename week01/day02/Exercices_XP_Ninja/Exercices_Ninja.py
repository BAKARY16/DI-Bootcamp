# Exercise 1: Cars
# Volkswagen, Toyota, Ford Motor, Honda, Chevrolet
# convert the list of car brands into a python list
car = []
car.append("Volkswagen")
car.append("Toyota" )
car.append("Ford Motor")
car.append("Honda")
car.append("Chevrolet")

print(car)

# Print out a message saying how many manufacturers/companies are in the list.
print(f"There are {len(car)} manufacturers/companies in the list.")

# Imprimer la liste des fabricants en ordre inverse/décroissant (ZA)
car.reverse()
print(car)