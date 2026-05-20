 # This file contains the solutions to the exercises in ExerciseXP Day02. 
 # Each exercise is separated by a comment line for clarity.


# Exercise 1: Converting Lists into Dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dict = dict(zip(keys, values))
print(my_dict)


#------------------------------------------------------------------------------

# Exercise 2: Cinemax #2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

def ticket_price(age):
    if age < 3:
        return 0
    if age <= 12:
        return 10
    return 15

def main():
    prix_total = 0

    ajouter = input("Voulez-vous ajouter un membre de la famille? ").strip().lower()
    while ajouter == 'o':
        nom = input("Nom: ").strip()
        try:
            âge = int(input("Âge: ").strip())
        except ValueError:
            print("Âge invalide, veuillez entrer un nombre.")
            continue
        family[nom] = âge
        ajouter = input("Ajouter un autre membre? (o/n) ").strip().lower()

    for nom, âge in family.items():
        prix = ticket_price(âge)
        prix_total += prix
        print(f"{nom}: {prix} $")

    print(f"Prix total: {prix_total} $")

if __name__ == '__main__':
    main()


#-------------------------------------------------------------------------------------



# Exercise 3: Zara

# Create a dictionary called brand with the provided data.
brand = {
    'name': 'Zara',
    'creation_date': '1975',
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': 'men, women, children, home',
    'international_competitors': 'Gap, H&M, Benetton',
    'number_stores': '7000',
    'major_color': {
        'France': 'blue',
        'Spain': 'red',
        'US': 'white'
    }
}

# Change the value of number_stores to 2.
brand['number_stores'] = '2'
print(f"Number of stores: {brand['number_stores']}")

# Print a sentence describing Zara’s clients using the type_of_clothes key.
print(f"Zara's clients are: {brand['type_of_clothes']}.")

#Add a new key country_creation with the value Spain.
add = brand['country_creation'] = 'Spain'
print(f"new key add is : {brand['country_creation']}")

# Check if international_competitors exists and, if so, add “Desigual” to the list.
if 'international_competitors' in brand:
    competitors = brand['international_competitors'].split(', ')
    competitors.append('Desigual')
    brand['international_competitors'] = ', '.join(competitors)

# Delete the creation_date key.
del brand['creation_date']

# Print the last item in international_competitors.
print(f"Last international competitor: {brand['international_competitors'].split(', ')[-1]}")

#Print the major colors in the US.
print (f'Major color in the US: {brand["major_color"]["US"]}')

# Print the number of keys in the dictionary.
print(f"Number of keys in the brand dictionary: {len(brand)}")

# Print all keys of the dictionary.*
print(f"Keys in the brand dictionary: {list(brand.keys())}")


# Create another dictionary called more_on_zara with creation_date and number_stores. 
# Merge this dictionary with the original brand dictionary and print the result.

more_on_zara = {
    'creation_date': '1975',
    'number_stores': '7000'
}

brand.update(more_on_zara)
print(f"Updated brand dictionary: {brand}")


#-------------------------------------------------------------------------------------------



# Exercise 4 : Some Geography

# Step 1: Define a Function with Parameters
def describe_city(city, country= "Unknown"):
    # Step 2: Print a Message
    print(f"{city} is in {country}.")
    
# Step 3: Call the Function
describe_city("Reykjavik", "Iceland")
describe_city("Paris")


#-------------------------------------------------------------------------------------

# Exercise 5 : Random

# Step 1: Import the random Module
import random

# Step 2: Define a Function with a Parameter
def random_number(n):
    # Step 3: Generate a Random Number
    return random.randint(0, n)

# Get a valid number from the user
def get_user_number():
    while True:
        try:
            number = int(input("Enter a number between 0 and 100: "))
            if 0 <= number <= 100:
                return number
            print("Please enter a number between 0 and 100.")
        except ValueError:
            print("Please enter a valid integer.")

# Compare the user's number with a random number
def main():
    your_number = get_user_number()
    n = random_number(100)

    if your_number == n:
        print("Success! You guessed the number.")
    else:
        print(f"Fail! Your number: {your_number}, Random number: {n}.")

if __name__ == "__main__":
    main()


#--------------------------------------------------------------------------------------


# Exercise 6 : Let’s create some personalized shirts 

# Step 1: Define a Function with Parameters
def make_shirt(size , text) :
    # Step 2: Print a Message
    print(f"The size of the shirt is {size} and the text is {text}.")

# Step 3: Call the Function
# make_shirt()

# Step 4: Modify the Function with Default Values
# The function now uses default values for size and text.
make_shirt("Large", "I love Python")

# Step 5: Call the Function with Default and Custom Values
make_shirt("Medium", "I love Python")
make_shirt("Small", "Custom message")


# Step 6 (Bonus): Keyword Arguments
make_shirt(text="Hello!", size="Small")


# -------------------------------------------------------------------------------

# Exercise 7 : Temperature Advice

# Step 1: Create the get_random_temp() Function
import random

def get_random_temp():
    return random.randint(-10, 40)

# Step 2: Create the main() Function
def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")
    
    # Step 3: Provide Temperature-Based Advice
    if temp < 0 :
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp < 16 :
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= temp < 23 :
        print("Nice weather.")
    elif 24 <= temp < 32 :
        print("A bit warm, stay hydrated.")
    else :
        print("It’s really hot! Stay cool.")

if __name__ == "__main__":
    main()

# Step 4: Floating-Point Temperatures (Bonus)
def get_random_temp():
    return (random.uniform(-10, 40), 1)

# Step 5: Month-Based Seasons (Bonus)
month = int(input("Enter the month number (1-12): "))

def get_random_temp(month):
    if month in [12, 1, 2]:  # Winter
        print("It's winter! Expect cold temperatures.")
    elif month in [3, 4, 5]:  # Spring
        print("It's spring! Expect mild temperatures.")
    elif month in [6, 7, 8]:  # Summer
        print("It's summer! Expect warm temperatures.")
    elif month in [9, 10, 11]:  # Autumn
       print("It's autumn! Expect cool temperatures.")
    else:
        raise ValueError("Invalid month number. Please enter a number between 1 and 12.")
get_random_temp(month)

# --------------------------------------------------------------------------------------


# Exercise 8: Pizza Toppings
menu = []
while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping.lower() == 'quit':
        print("Finished adding toppings.")
        break
    else:
        print(f"Adding {topping} to your pizza.")
        menu.append(topping)

# Display toppings and calculate total price
base_price = 10
topping_price = 2.50
total_price = base_price + (len(menu) * topping_price)

print("\nYour pizza toppings:")
for topping in menu:
    print(f"- {topping}")

print(f"\nBase price: ${base_price:.2f}")
print(f"Number of toppings: {len(menu)}")
print(f"Total price: ${total_price:.2f}")

