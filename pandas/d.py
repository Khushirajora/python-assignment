def write_to_file():
    text = input("Enter some text: ")
    with open("output.txt", "w") as file:
        file.write(text)

write_to_file()