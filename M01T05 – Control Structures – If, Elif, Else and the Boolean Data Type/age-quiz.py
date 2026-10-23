#Instantiate the age variable and give it a default value of 0
age = 0
#Loop will continue until a valid age above 1 is given
while age <= 0:
    #Get the users input
    age = input("Please enter a valid age: ")

    #if the input is blank, default to 0 and re-enter the loop
    if age == "":
        age = 0
        continue

    #else if the age is less than 0, default back to 0 and re-enter the loop
    elif int(age) < 0:
        age = 0
        continue
    else:
        #else assign age and then break from the loop
        age = int(age)
        break

#Evaluate age and print out the correct responses as output
if age > 100:
    print("Sorry, you're dead.") #if the users age is above 100
elif 65 <= age <= 100:
    print("Enjoy your retirement!") #if the users age is between 65 and 100
elif 40 <= age < 65:
    print("You're over the hill.") #if the users age is between 40 and 64
elif age == 21:
    print("Congrats on your 21st!") #if the users age is 21
elif age <= 13:
    print("You qualify for the kiddie discount.") # if the users age is 13 or below
else:
    print("Age is just a number") #all other ages