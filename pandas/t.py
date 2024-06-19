import string

def remove_punctuation():
    text = input("Enter a string: ")
    result = text.translate(str.maketrans("", "", string.punctuation))
    print(f"The string without punctuation is: {result}")

remove_punctuation()
