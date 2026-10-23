name = input("Enter your name: ") #store the users name
age = input("Enter your age: ") # store the users age
house_number = input("Enter your house number: ") # store the users house number
street_name = input("Enter your street name: ") #store the users street name

#print the output - this formats the output and substitutes in the variables with their values using interpolation
print(f"This is {name}. He is {age} years old and lives at house number {house_number} on {street_name}")