# Challenge 1
number = int(input("Entrez un nombre : "))
length = int(input("Entrez une longueur : "))

multiple = []
current = 1

while len(multiple) < length:
    if current % number == 0:
        multiple.append(current)
    current += 1

print(multiple)

######################## Challenge 1 end #########################




# Challenge 2
UserText = input("Entrer un text : ")
if UserText:
    result = [UserText[0]]
    for ch in UserText[1:]:
        if ch != result[-1]:
            result.append(ch)
    new_text = "".join(result)
else:
    new_text = ""

print(new_text)

########################## Challenge 2 end #########################