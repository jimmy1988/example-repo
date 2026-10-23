
def binarySearch(arr, targetVal):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == targetVal:
      return mid

    if arr[mid] < targetVal:
      left = mid + 1
    else:
      right = mid - 1

  return -1

def insertion_sort(the_list):

    n = len(the_list)
    for i in range(1, n):
        insert_index = i
        current_value = the_list.pop(i)

        for j in range(insert_index-1, -1, -1):

            if the_list[j] > current_value:
                insert_index = j

        the_list.insert(insert_index, current_value)

    return the_list

def linear_search(array, find) -> int:

    """
        Find the index of the first occurrence of `find` in `array`
    Args:
        array (list): A list of integers:
        find (int): The function finds the index of the element in the list:

    Returns:
        int: The index of the element in the list

    """

    output = -1
    for i, value in enumerate(array):
        if value == find:
            output = i
            break
        else:
            continue

    return output


"""
I would use a linear search algorithm to find the index of the first occurrence of `find` in `array`
This is because the list is not sorted, so i would have to scan each value in the list to find the index of the first instance
of find
"""
number_to_find = 9
numbers = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
print(linear_search(numbers, number_to_find))

print()

numbers_new = insertion_sort(numbers)
print(numbers_new)

print()

"""
The binary search could be used on records returned back from a database where all records are sorted on their
primary keyS
"""

print(binarySearch(numbers_new, number_to_find))