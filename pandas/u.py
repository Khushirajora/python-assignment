def sum_of_list():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(f"The sum of the list is: {sum(numbers)}")

sum_of_list()
