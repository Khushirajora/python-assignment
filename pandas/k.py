def sum_of_digits():
    num = int(input("Enter a number: "))
    total = sum(int(digit) for digit in str(num))
    print(f"The sum of the digits is: {total}")

sum_of_digits()
