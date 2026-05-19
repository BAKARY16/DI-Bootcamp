# Exercise 1: Hello World

print("Hello word \n"*4)

#########################


# Exercise 2: Some Math

result = (99**3)*8
print(result)


# Exercise 3: What is the output?

print(5 < 3) #False
print(3 == 3) #True
print(3 == "3") #False
# print("3" > 3) TypeError
print("Hello" == "hello") #False



# Exercise 4: Your computer brand
computer_brand = "samsung"
print(f"I have a {computer_brand} computer.")



# Exercise 5: Your information
name = "Bakary"
age = 26
shoe_size = 42
info = f"je m'appelle {name}, j'ai {age} ans et je chausse le numéro {shoe_size}"

print(info)


# Exercice 6 : A et B
a = 10
b = 5

if a > b :
    print("Hello World")



# Exercise 7: Odd or Even
nombre = int(input("Entrer un nombre: "))

if nombre % 2 == 0:
    print("Le nombre est pair")
else:
    print("Le nombre est impair")



# Exercise 8: What’s your name?
your_name = input("Quel est votre nom ?: ")
my_name = "Bakary"

if your_name == my_name :
    print("Vous êtes mon homonyme")
else :
    print("Bye, vous n'est pas mon homonyme")




# Exercise 9: Tall enough to ride a roller coaster
height = int(input("Veuillez reseigner votre taille: "))
height_max = 145 

if height > height_max :
    print(f"Taille {height} cm, vous êtes assez grand pour monter à bord")
else:
    print("Vous devez grandir encore pour pouvoir monter à cheval")