#History file name declared at the top as it is shared by 2 functions
#Saves repetition
history_file = "equations.txt"

def convert_float_to_integer(num) -> float | int:
    """"
        Converts a whole number into an integer, otherwise keep it as a float
        e.g.
        1.0 or 1.00 will become 1
        1 will remain as 1
        1.52 will remain as 1.52

        Args:
            num (float | int) : Number to convert

        Returns:
            float | int : Converted number
    """

    #If the number inside the float is a whole number convert to integer
    if num.is_integer():
        num = int(num)

    #return the final type of the number
    return num

def perform_calculations() -> None:

    """"
        Gets 2 numbers and an operator and performs the calculations, then stores the calculation in a file to be read later

        Returns:
            None
    """

    #Get the first number
    #Loop until a number is given, this could be a float or an integer
    while True:
        try:
            # Get the first number, strip off any whitespace
            # Convert to a float
            # Then convert to its correct type
            num1 = convert_float_to_integer(float(input("Type the first number: ").strip()))
            break # if a number is given, break out of the loop
        except ValueError:
            #If a value os given and its type is anything other than a float, then display a message and loop again
            print("Invalid input. Please enter a valid numerical value.")


    valid_ops = ["+", "-", "*", "/", "%"] #List of valid operators
    #get the operator, loop until a valid operator is supplied by the user
    while True:

        try:
            #Get the operator and strip off any whitespace
            op = input(f"Type the operator ({', '.join(valid_ops)}): ").strip()

            #if the operator is in the list of valid operators then break out of the loop
            if op in valid_ops:

                #if num1 is 0 and the operator supplied is divide, then display a message to prevent a division by 0 error
                #Ask for another operator
                if op == "/" and num1 == 0:
                    print("Error: Division by zero is not allowed. Try another operator.")
                    continue

                break
            else:
                #Display message if an operator is invalid and loop again until a valid operator is supplied
                print(f"Invalid operation. Please choose from {', '.join(valid_ops)}")

        except ValueError:
            #If a value error exception is thrown, handle it here by displaying a message
            print("Please enter an operator")

    #Get the second number
    while True:

        try:
            #Get the second number and strip off any whitespace
            # Convert to a float
            # Then convert to its correct type
            num2 = convert_float_to_integer(float(input("Type the second number: ").strip()))

            #If the operator is division and the 2nd number is equal to 0 then ask for another number to avoid a division by 0 error
            if op == "/" and num2 == 0:
                print("Error: Division by zero is not allowed. Try another number.")
                continue

            break
        except ValueError:
            #value Error caught here in case a string that cannot be converted is supplied
            print("Please enter a number")



    result = 0  # Initialize the result
    equation_string = "" # initialize the equation string

    # start the equations
    # convert to the appropriate type
    # Build the string to put into the file
    if op == "+":
        result = convert_float_to_integer(num1 + num2)
        equation_string = f"{num1} + {num2} = {result}"
    elif op == "-":
        result = convert_float_to_integer(num1 - num2)
        equation_string = f"{num1} - {num2} = {result}"
    elif op == "*":
        result = convert_float_to_integer(num1 * num2)
        equation_string = f"({num1} * {num2}) = {result}"
    elif op == "/":
        result = convert_float_to_integer(num1 / num2)
        equation_string = f"{num1} / {num2} = {result}"
    elif op == "%":
        result = convert_float_to_integer(num1 % num2)
        equation_string = f"{num1} % {num2} = {result}"

    # print the result
    print(result)

    try:
        #open the history file in append mode
        file_handle = open(history_file, "a")
        file_handle.write(equation_string + "\n") # write the history to the file

    except FileNotFoundError, IOError:
        #If an exception is raised, handle it here
        print("File not found: " + history_file)

    finally:
        # Cloise the file, if it exists
        if file_handle:
            file_handle.close()

    return True # Return True to loop for the next instruction






def display_history() -> None:

    """
    Displays all the equations from the history file

    Returns:
        None
    """

    try:
        # Open the file in read mode
        file_handle = open(history_file,"r")
        history = file_handle.read() # read file contents

        history = history.split('\n') # split the file contents into a list, separating by a new line

        # test if the history file is empty, no history to display
        if not history:
            print("Equation history is empty")

        else:
            #output each line
            for line in history:
                if line != "":
                    print(line)

    except FileNotFoundError:
        print("File not found") # Message is file is not found

    finally:
        # if the file is open, then close it
        if file_handle:
            file_handle.close()

        # print message to say that all contents have been read
        print("End of history")

#Start of the main program
#repeats everytime an action is taken until the user type q to quit or terminate
while True:
    #Get the users response as to what they want to do
    response = input("Type (1) to perform calculations or (2) to display calculation history or (q) to quit: ")

    if response == "1":
        perform_calculations() # perform the calculations

    elif response == "2":
        display_history() # display history

    elif response == "q":
        break # quit or terminate the application