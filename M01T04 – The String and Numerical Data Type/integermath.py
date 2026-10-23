#Ask the user for 3 different integers

#Ask for the first number
num1 = 0
while num1 <= 0:
    num1 = int(input("Enter your first number: "))


#Ask for the second number
#Ensures that the second number is not a duplicate of the first number
num2 = 0
while num2 <= 0:
    num2 = int(input("Enter your second number: "))
    if num2 == num1:
        print("Your second number cannot be equal to your first number")
        num2 = 0

#Ask fr the third number
#Ensures that the third number is not a duplicate of the first or second numbers
num3 = 0
while num3 <= 0:
    num3 = int(input("Enter your third number: "))
    if num3 == num1:
        print("Your third number cannot be equal to your first number")
        num3 = 0

    if num3 == num2:
        print("Your third number cannot be equal to your second number")
        num3 = 0

total = sum([num1, num2 , num3]) #Find the total of all three numbers
print(total) #output the total
print(num1 - num2) #subtract the first number from the second number
print(num3 * num1) #multiply the third number by the first number
print(total / num3) #divide the sum of all the number