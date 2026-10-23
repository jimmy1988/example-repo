def adding_up_to(numbers, max_index) -> int:

    """
    Adds up all the numbers from a list to the given index
    Args:
        numbers (list): A list of integers:
        max_index (int): The index of the element to be added:

    Returns:
        int: The sum of the elements in the list
    """
    if max_index < 0:
        return 0

    return numbers[max_index] + adding_up_to(numbers, max_index - 1)


print(adding_up_to([1, 4, 5, 3, 12, 16], 4)) #prints 25

print(adding_up_to([4, 3, 1, 5], 1)) # prints 7