def check_substring():
    string = input("Enter the main string: ")
    substring = input("Enter the substring: ")
    if substring in string:
        print("Substring is present.")
    else:
        print("Substring is not present.")

check_substring()