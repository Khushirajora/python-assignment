def min_max_list():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(f"The minimum value is: {min(numbers)}")
    print(f"The maximum value is: {max(numbers)}")

min_max_list()
