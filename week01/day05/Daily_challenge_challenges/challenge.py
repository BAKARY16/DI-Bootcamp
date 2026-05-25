# Challenge 1 : Sorting

def get_user_input():
    user_input = input("Enter a comma-separated sequence of words: ")
    # use list comprehension to strip whitespace from each word
    req = [w.strip() for w in user_input.split(",")] if user_input else []
    return req

def print_sorted_sequence(sequence):
    sorted_sequence = sorted(sequence)
    print(",".join(sorted_sequence))

if __name__ == "__main__":
    seq = get_user_input()
    if seq:
        print_sorted_sequence(seq)


# Challenge 2 : Longest Word

def longest_sentence(longest_input):

    sentence = longest_input.split()

    if not sentence:
        ""
    req = max(sentence, key=len)
    return req

longest_input = input("Enter a sentence : ")

result = longest_sentence(longest_input)

print(f"The sentence is : {result}")