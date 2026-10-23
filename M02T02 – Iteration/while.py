number = 0
numbers_list = []
while number >= 0:
    number = int(input("Enter a number: (-1 to exit) ").strip())
    if number == -1:
        break
    elif number > 0:
        numbers_list.append(number)

average = round(sum(numbers_list) / len(numbers_list), 2)
print(average)