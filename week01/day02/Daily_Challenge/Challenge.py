
# The following code contains two challenges. 
# Each exercise is separated by a comment line for clarity.


# Challenge 1: Letter Index Dictionary
#  User Input:
user_input = input("Please enter a string: ")

# Creating the Dictionary:
letter_index_dict = {}
for index, letter in enumerate(user_input):
    if letter not in letter_index_dict:
        letter_index_dict[letter] = []
    letter_index_dict[letter].append(index)
# Output the Dictionary:
print(letter_index_dict)
 

# -----------------------------------------------------------------



# Challenge 2: Affordable Items

#  Store Data:
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

# Data Cleaning:
cleaned_items = {}
for item, price in items_purchase.items():
    cleaned_price = price.replace("$", "").replace(",", "")
    cleaned_items[item] = int(cleaned_price)


# Determining Affordable Items:
basket = []
wallet_amount = int(wallet.replace("$", ""))

for item, price in cleaned_items.items():
    if price <= wallet_amount:
        basket.append(item)
        wallet_amount -= price

if not basket:
    print("Nothing")
else:
    basket.sort()
    print(basket)

