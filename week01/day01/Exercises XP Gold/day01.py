# Exercise 1: What is the Season?
my_month = int(input("saisir un mois de 1 à 12 : "))

for month in range(1, 13):
    if my_month == month :
        if month in [3,5]:
            print("it's spring")
        elif month in [6,8]:
            print("it's summer")
        elif month in [9, 11]:
            print("it's autumn")
        else :
            print("it's winter")

##################### Exercise 1 end #########################



# Exercise 2: For Loop
for i in range(1, 21):
    print(i)

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

##################### Exercise 2 end #########################



# Exercise 3: While Loop
name = input("What is your name? :")
myname = "Bakary"

while name != "":
    if name == myname:
        print("Welcome, " + name + "!")
        break
    else:
        print("Sorry, I don't know you.")
        name = input("What is your name? : ")

##################### Exercise 3 end #########################



# Exercise 4: Check the index
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

username = input("Enter a name : ")

if username in names :
    index = names.index(username)
    print("The name " + username + " is at index " + str(index))

##################### Exercise 4 end #########################

# Exercise 5: Greatest Number

number1 = int(input("Enter the first number : "))
number2 = int(input("Enter the second number : "))
number3 = int(input("Enter the third number : "))

if number1 > number2 and number1 > number3 :
    print("The greatest number is : " + str(number1))
elif number2 > number1 and number2 > number3 :
    print("The greatest number is : " + str(number2))
else :
    print("The greatest number is : " + str(number3))

##################### Exercise 5 end #########################



# Exercise 6: Random number
nbre = int(input("Enter a number between 1 and 10 : "))
import random
random_number = random.randint(1, 10)

if nbre == random_number :
    print("Congratulations! You guessed the number.")
else :
    print ("Better luck next time!")