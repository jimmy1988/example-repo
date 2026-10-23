#Import the statistics module
import statistics

#Initialize the numbers list
numbers_list = []

#Initialize the input_number
input_number = 0

#How many times to repeat
repeat = 10

#loop around and repeat until all numbers are given
for i in range(repeat):
    input_number = float(input("Enter a number: ")) #Get the users input
    numbers_list.append(input_number) #append the number onto the numbers list


print(f"The sum of all the numbers is: {sum(numbers_list)}") #Get the sum of all the numbers and output
print(f"The index of the largest number is: {numbers_list.index(max(numbers_list))}") #Get the index of the largest number and output
print(f"The index of the smallest number is: {numbers_list.index(min(numbers_list))}") #Get the index of the smallest number and output

average = statistics.mean(numbers_list) # Find the mean (average)
print(f"The average of the numbers is: {round(average, 2)}") #output the mean

median = statistics.median(numbers_list) #find the mean number
print(f"The median of the numbers is: {round(median, 2)}") #output the mean