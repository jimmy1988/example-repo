# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.


print("Welcome to the error program") #Missing parenthesis
print("\n") #Missing parenthesis and indentation

# Variables declaring the user's age, casting the str to an int, and printing the result

#Indentation
#Removed double equals
#Removed "years old"
#Converted to an int
# Removed age_str as it is pointless

age = 24
print("I'm " + str(age) + " years old.") #convert age to a string and added a space after i'm and before years

# Variables declaring additional years and printing the total years of age
years_from_now = "3.5" #added .5 to the 3 months as 6 months is half a year
total_years = age + float(years_from_now) # cast years_from_now to an int

# Add the parenthesis
#Variable needs replacing and casting to a string

print("The total number of years:" + str(total_years))

# Variable to calculate the total number of months from the given number of years and printing the result
#total is an undefined variable
#replaced with total_years
total_months = total_years * 12

#Added parenthesis
#cast total_months to a string
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")

#HINT, 330 months is the correct answer

