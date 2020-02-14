def min_max(numbers):
    smallest = largest = numbers[0]
    for item in numbers:
        if item > largest:
            largest = item
        elif item < smallest:
            smallest = item
    return smallest, largest


smallest, largest = min_max([1, 2, 5, 3, 7, 9, 4])

print("smallest value : ", smallest)

print("largest value : ", largest)