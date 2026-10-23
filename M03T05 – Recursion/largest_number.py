
def largest_number(numbers) -> int:

    """
    Find the largets number in the list
    Args:
        numbers(list): A list of integers:

    Returns:
        int: The largest integer in the list

    """

    if len(numbers) == 0:
        return 0 # return 0 if the length of the list is 0

    elif len(numbers) == 1:
        return numbers[0] # if there is 1 element in the list just return this

    else:

        max_number = largest_number(numbers[1:]) # check for the larget number

    # return the maximum  number
    return numbers[0] if numbers[0] > max_number else max_number

print(largest_number([1, 4, 5, 3])) #prints 5
print(largest_number([3, 1, 6, 8, 2, 4, 5])) # prints 8