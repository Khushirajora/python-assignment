def count_occurrences():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    element = int(input("Enter the element to count: "))
    print(f"The element {element} occurs {numbers.count(element)} times.")

count_occurrences()
