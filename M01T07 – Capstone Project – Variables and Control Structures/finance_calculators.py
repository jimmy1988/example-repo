#Import the math module
import math

# Using the strip method ona all inputs, ensures that we get clean input from the user and not a pile of garbage!


# Ask the user for their finance type
# Stripping the input of whitespace and converting tat string into a lowercase string, to be evaluated
finance_type = input("Enter either “investment” or “bond” from the menu above to proceed: ").strip().lower()

# Determine the path based on the finance type provided
if finance_type == "investment":

    # Get the amount initially deposited
    # Then, convert it to a float for pounds and pence
    deposit = float(input("What is The amount of money that they are depositing?(£) : ").strip())

    # Get the interest rate, float is used as some interest rates are not whole numbers
    interest_rate = float(input("What is The interest rate?(%) : ").strip())

    # Convert the interest rate from a percentage to a decimal
    # Code is here and not on the output for readability purposes
    # Code sits before the if, because we are using it in both cases, this is prevent repetition
    interest_rate = interest_rate / 100

    # Get the term, this is an integer as people invest in whole term and not part term
    # If part term was a factor, this would be a float
    term = int(input("How many years are you investing for? : ").strip())

    # Get the interest method, no type conversion here as string already provided
    # Strip out whitespace and convert to lowercase for evaluation
    interest_method = input("What is The interest method? “simple” or “compound”: ").strip().lower()



    if interest_method == "simple":

        # Work out the final amount
        # First work out what 1 times the interest, times the term is
        # The multiply it by the initial amount (deposit)
        # Round the number to the nearest number, to 2 decimal places
        final_amount = round(deposit * (1 + interest_rate * term), 2)

        # print the final amount
        # Nice fancy format, so the output means something to the user
        print(f"The final amount you will have (with simple interest) is £{final_amount}")

    elif interest_method == "compound":

        # Work out the final amount
        # Work out 1 plus the interest rate
        # Then, multiply that by the initial amount
        # Then, multiply that amount by the power of the number of term
        # Round the number to the nearest number, to 2 decimal places
        final_amount = round(deposit * math.pow(1 + interest_rate, term), 2)

        # print the final amount
        # Nice fancy format, so the output means something to the user
        print(f"The final amount you will have (with compound interest) is £{final_amount}")

    else:
        print("Investment type not recognized") #Fallback in case an invalid interest method is given

elif finance_type == "bond":

    #Get the value of the house
    #Convert to float
    #Would have converted to integer but this is just to accommodate for pound and pence
    house_value = float(input("What is the value of the house?(£) : ").strip())

    # Get the interest rate, float is used as some interest rates are not whole numbers
    interest_rate = float(input("What is The interest rate?(%) : ").strip())

    # Convert the interest rate from a percentage to a decimal, then divide by 12
    # Code is here and not on the output for readability purposes
    # Code sits before the if, because we are using it in both cases, this is prevent repetition
    interest_rate = (interest_rate / 100) / 12

    # Get the term, this is an integer as people invest in whole term and not part term
    # If part term was a factor, this would be a float
    term = int(input("How many months will you be paying the bond for? : ").strip())

    # Calculate the repayment
    # Value 1 - multiply the house value by the interest rate
    # Value 2 - Add 1 to the interest rate
    # Value 3 - find the exponent for Value 2, with a negative term
    # Minus 1 from the total
    # Divide the two values together
    # Round to the nearest number, to 2 decimal places
    repayment = round( ( interest_rate * house_value ) / ( 1 - ( 1 + interest_rate ) ** (-term) ), 2)

    # print the final amount
    # Nice fancy format, so the output means something to the user
    print(f"The total to repay is {repayment}")

else:
    print("Investment type not recognized") #Prints if the user gives a financial type not being asked for