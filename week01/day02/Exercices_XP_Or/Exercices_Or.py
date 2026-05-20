# Exercise 1: Birthday Look-up
birthdays = {
    "Alice": "2000-01-15",
    "Bob": "1995-05-30",
    "Charlie": "1988-12-10",
    "David": "1992-07-20",
    "Eve": "1998-03-25" 
}
print(f"Welcome to the birthday look-up. You can look up the birthdays of the people in the list: \n {',\n '.join(birthdays.keys())}.")
person = input("what's the name of the person you want to look up? :")

if person in birthdays :
    print(f"{person}'s birthday is {birthdays[person]}.")
else :
    print(f"Sorry, we don't have the birthday information for {person}.") 