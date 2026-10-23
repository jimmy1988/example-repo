from __future__ import annotations
import subprocess
import sys
import shutil
from typing import Final, IO, Optional, Any, Self

"""
Footnotes:

I have decided to treat the file and the object as two separate entities
I have created the file object so i can encapsulate all the file functionality in one class, the same is done on the shoe class


In set methods the current object is returned for statement chaining
In get methods the value of the property is returned
In none getters and setters, if it executes an operation, then true or false is returned, otherwise a value is returned

In the functions true or false is returned to determine whether the operation was successful or not
"""

#START OF THE FILE CLASS
class File:

    # Core Text Modes
    READ_TEXT: Final[str] = "r"  # Read only (default). File must exist.
    WRITE_TEXT: Final[str] = "w"  # Write only. Overwrites existing or creates new.
    APPEND_TEXT: Final[str] = "a"  # Append only. Writes to end of file or creates new.
    CREATE_TEXT = "x"  # Exclusive creation. Fails if file already exists.

    # Combined Text Modes (Read + Write)
    READ_WRITE_TEXT: Final[str] = "r+"  # Read/Write. File must exist; starts at beginning.
    WRITE_READ_TEXT: Final[str] = "w+"  # Write/Read. Overwrites existing or creates new.
    APPEND_READ_TEXT: Final[str] = "a+"  # Append/Read. Reads from start, appends to end.

    __file_name = "inventory.txt" # The file name and path to target
    __file_handle: Optional[IO] = None # The placeholder for the open file
    __file_contents = [] # A list of all the lines in the file
    __mode = "r" # The mode we are using to access the file

    def __init__(self, file_name = "inventory.txt", mode = READ_TEXT):

        """
        Initialize the object, set the file name, set the mode and load the file and the contents into the class
        Args:
            file_name (str): The name of the file
            mode (str): The mode of the file
        """
        (
            self.set_file_name(file_name)
            .set_mode(mode)
            .load_file()
        )

    def set_file_name(self, file_name = "inventory.txt") -> Self:

        """
        Sets the file name
        Args:
            file_name (str): The name of the file:

        Returns:
            File: The current object

        """

        if file_name == "":
            print("Please enter a file name")
        else:
            self.__file_name = str(file_name).strip()

        return self

    def get_file_name(self) -> str:

        """
        Gets the file name
        Returns:
            str: The file name
        """

        return self.__file_name

    def __set_file_handle(self) -> Self:

        """
        Sets up the file handle by opening the file in the selected mode
        Returns:
            File: The current object

        """

        try:
            self.__file_handle = open(self.get_file_name(), self.get_mode())

        except FileNotFoundError:
            # Handle the file not found exception
            print("File not found")
            self.__file_handle = None

        return self

    def get_file_handle(self) -> IO[Any]|None :
        """
        Gets the current file handle
        Returns:
            IO|None: Returns the buffer as the handle or None if it hasnt been set up yet
        """

        return self.__file_handle

    def __set_file_contents(self) -> Self:

        """
        Reads the file from the file handle and imports each line into the file contents
        Returns:
            File: The current object
        """

        # Check for a file handle
        if self.get_file_handle():

            # Read the file
            contents = self.get_file_handle().read().split("\n")

            max_line_length = 0 # Check so that each line matches the length of the headers
            for i, line in enumerate(contents):
                # Do not import the headers
                if i == 0:
                    max_line_length = len(line.strip().split(",")) # Set the max line length based on the headers
                    continue

                line = line.strip().split(",") # Split the line into its columns

                # Loop over each column and clean the data
                for j, column in enumerate(line):
                    line[j] = column.strip()

                # Make sure we skip over blank lines and any lines that exceed the amount of headers we have
                if len(line) > 0 and len(line) == max_line_length:
                    self.__file_contents.append(line)

        else:
            # Set an empty contents list in case the file handle is empty
            self.__file_contents = []

        return self

    def get_file_contents(self) -> list:

        """
        Returns a list of each line in the file
        Returns:
            list: The contents of each line in the file
        """

        return self.__file_contents

    def set_mode(self, mode = "r") -> Self:

        """
        Sets the access mode for the file
        Args:
            mode (str): The mode in which we are accessing the file in

        Returns:
            File: The current object
        """

        self.__mode = str(mode)
        return self

    def get_mode(self) -> str:

        """
        Returns the access mode for the file
        Returns:
            str: The access mode for the file
        """

        return self.__mode

    def close_file(self) -> Self:

        """
        Closes the file after processing
        Returns:
            File: The current object
        """

        if self.get_file_handle():
            self.get_file_handle().close()

        return self

    def load_file(self) -> Self:

        """
        Sets up the file handle, populates the file contents and closes down the file

        Returns:
            File: The current object
        """

        self.__set_file_handle().__set_file_contents().close_file()
        return self

    def __update_file(self) -> bool:

        """
        Updates the file from the current state of the file contents

        Returns:
            bool: Whether the operation was successful or not
        """

        self.__set_file_handle() # Set the file handle as the mode may have changed at this point

        success = True # Default for success

        # Check for file handle
        if self.get_file_handle():
            file_update = self.get_file_handle() # save file handle
            file_update.truncate() # Empty the contents of the file
            file_update.write("Country,Code,Product,Cost,Quantity\n") # Write the headers

            # Loop around the file contents and write each line to the file
            for i, line in enumerate(self.__file_contents):
                file_output = f"" # reset the output (starts a fresh output on every iteration)

                # Get each column and format it back to the original but with updated values
                for j, column in enumerate(line):
                    file_output += f"{column.strip()}" # output the data in the column

                    # output a comma on every column except for the last column
                    if j != len(line) - 1:
                        file_output += ","

                # Place a new line character on every line except for the last one
                if i < len(self.__file_contents) - 1:
                    file_output += "\n"

                # if the write was successful
                success = True if file_update.write(f"{file_output}") > 0 else False

                # break operation on failure
                if not success:
                    break

            self.close_file() # close the file

        else:
            success = False

        return success

    def add_row(self, row=None) -> bool:

        """
        Add a row to the end of the file
        Args:
            row (list): The row to added to the file

        Returns:
            bool: Whether the operation was successful or not
        """

        if row is None:
            row = []
        self.__file_contents.append(row) # Update file contents
        self.set_mode(self.WRITE_TEXT) # Set the new mode
        success = self.__update_file() # Update the file
        return success


    def update_row(self, row = 0, values=None) -> bool:

        """
        Updates a row in the file
        Args:
            row (int): The index of the row to update
            values (list): The full line to update

        Returns:
            bool: Whether the operation was a success or not
        """

        if values is None:
            values = []
        self.__file_contents[row] = values
        self.set_mode(self.WRITE_TEXT)
        success = self.__update_file()
        return success


    def delete_row(self, row = 0, return_row = False) -> bool:

        """
        Deletes a row from the file

        This is to complete the CRUD cycle within a file
        Args:
            row (int): The index of the row to be deleted
            return_row (bool): Whether to return the row or not

        Returns:
            bool|list: Whether the operation was successful or not, list for the row that was deleted
        """

        removed_row = self.__file_contents.pop(row) # remove the row
        success = self.__update_file() # update the file

        if return_row:
            return removed_row # return the removed row
        else:
            return success

#END OF THE FILE CLASS


#START OF THE SHOE CLASS
class Shoe:

    #Access modifiers are private, so that if the properties are modified that they are converted to the correct type before assignment
    __country = ""
    __code = ""
    __product = ""
    __cost = 0.0
    __quantity = 0

    def __init__(self, country = "", code = "", product = "", cost = 0.0, quantity = 0):

        #Statement chain here, to set everything up in one line
        (
            self.set_country(country)
            .set_code(code)
            .set_product(product)
            .set_cost(cost)
            .set_quantity(quantity)
        )

    def set_country(self, country = "") -> Self:

        """
        Set the country of the shoe
        Args:
            country (str): The country of the shoe.:

        Returns:
            Shoe
        """

        self.__country = str(country).strip().title()
        return self

    def get_country(self):

        """
        Return the country of the shoe
        Returns:
            str: The country of the shoe

        """

        return self.__country

    def set_code(self, code = "") -> Self:

        """
        Sets the code of the show
        Args:
            code (str): The code of the show:

        Returns:
            Shoe
        """

        self.__code = str(code).strip().upper()
        return self

    def get_code(self) -> str:

        """
        Return the code of the show
        Returns:
            str: The code of the show

        """

        return self.__code

    def set_product(self, product = "") -> Self:

        """
        Sets the product of the shoe
        Args:
            product (str): The product of the shoe:

        Returns:
            Shoe
        """

        self.__product = str(product).strip().title()
        return self

    def get_product(self) -> str:

        """
        Returns the product of the shoe
        Returns:
            str: The product of the shoe
        """

        return self.__product

    def set_cost(self, cost = 0.0) -> Self:

        """
        Sets the cost of the show
        Args:
            cost (float|int): The cost of the show

        Returns:
            Shoe

        """

        try:
            cost = float(cost)

        except ValueError:
            print("Cost must be an integer or float")

        else:
            self.__cost = float(cost)

        return self



    def get_cost(self):

        """
        Gets the cost of the show
        Returns:
            float: The cost of the shoe

        """

        return self.__cost

    def set_quantity(self, quantity = 0) -> Self:

        """
        Sets the quantity of the shoe
        Args:
            quantity (int): The quantity

        Returns:
            Shoe
        """

        try:
            quantity = int(quantity)

        except ValueError:
            print("Quantity must be an integer or float")

        else:
            self.__quantity = int(quantity)


        return self

    def get_quantity(self) -> int:

        """
        Gets the quantity of the shoe

        Returns:
            int: The quantity of the shoe
        """

        return self.__quantity

    def __str__(self) -> str:

        """
        Prints out a string that represents the class
        Returns:
            str: A string that represents the class when the print function is invoked
        """

        return f"""
            Country: {self.get_country()}
            Code: {self.get_code()}
            Product: {self.get_product()}
            Cost: R{self.get_cost():.2f}
            Quantity: {self.get_quantity()}
        """



#==========Functions outside the class==============
def clear_screen() -> bool:
    """
        FROM Google Gemini - https://www.google.com/search?q=python+clear+console&sca_esv=51d9174c6c91f7ac&sxsrf=APpeQns_wdOoGFNqlrHhlG6fenDRAzuoLw%3A1792453510846&source=chrome.ob&fbs=ABfTbFVyMZGZf1hfvX9uKjN_-G8cxpBkeIeqYwoCbfNVc4vKE7plZzta63Pe5DpJ3XFR9XzxI1gxDxLun-GtPKavu3kEzJNGNBebw1A_XeIxzHPdHc5gGlqeYRrsKc2k_QKKK6kt-AjhNNP6r-v8YZTEDEFOHvz2lLpCCJUsUbach_pOXsAYdFRjnayctnF5WfiXo-KcdTL6sQuPlkZ9Qwpf2Q9WDTqyBw&vsint=&aep=1&ntc=1&cs=1&sa=X&ved=2ahUKEwjK7qjWoceXAxXiRvEDHbveKPUQ2J8OegQIGhAD&biw=1920&bih=911&dpr=1&mstk=AUtExfC7WI-SIykIakRgBoHXHapW917ERie9-1leNiyNiFbpo7cj_AhEcSVS_hs4WBHeBMB2m8NRZQA9FnYb4C0iT7dZGT3AfPABowpeJcWageYeWlKfHW0Mru1vcRPG32YIIEb-thFmdZHsSprTKZavogMzNOxdylIrrYkqyNa4zFTEDGptV2e2vVxyhKxl3VTOkR0zUcE_hkA0-dl0t7kYWpyCtgV3Pb5yfe7R0z7ILiuPFZkWyypOjBGJ75_wPuDoON7VByLPUiQEbtIDcWMOLAF3npObvaWpSjFRydwNuMFlQ9WCBT5O0OAzeDdixPWxjKvnTQUdWIS9_Q&csuir=1&mtid=OazWav6fLIuSxc8P3suioQQ&udm=50
        Date 20/10/2026
        Clears standard terminals completely, and clears IDE consoles cleanly.
    """

    # 1. Try checking if we are running inside a true terminal
    # sys.stdout.isatty() returns False inside most IDE standard run windows
    if sys.stdout.isatty():
        # Universal terminal clear (ANSI + System fallback)
        sys.stdout.write("\033[H\033[J")
        sys.stdout.flush()
        if sys.platform == "win32":
            subprocess.run(['cls'])
        else:
            subprocess.run(['clear'])
    else:
        # 2. IDE Fallback: Print enough newlines to cleanly push old text up
        # shutil.get_terminal_size() automatically detects window height
        try:
            lines = shutil.get_terminal_size((80, 24)).lines
            print("\n" * lines, end="")
        except Exception:
            # Absolute fallback if window dimensions can't be read
            print("\n" * 100, end="")

    return True


def read_shoes_data() -> bool:

    """
        Read the shoes data from a file
    Args:

    Returns:
        bool: Whether or not the file was successfully read
    """

    success = True

    if len(file.get_file_contents()) > 0:
        i = 0
        for line in file.get_file_contents():
            import_country, import_code, import_product, import_cost, import_quantity = line

            try:
                # Cast variables to their correct types
                import_cost = float(import_cost)
                import_quantity = int(import_quantity)
            except ValueError:
                # Any errors handle here
                print(f"Failed to load shoe on line {i+1}")
                success = False
                break


            if success:

                if capture_shoe(
                        country=import_country,
                        code=import_code,
                        product=import_product,
                        cost=import_cost,
                        quantity=import_quantity
                ):
                            continue # returns true if the capture was successful
                else:
                    #If the capture was unsuccessful, print a message and stop the loop
                    #Break on first failure
                    print(f"Failed to load shoe on line {i+1}")
                    success = False
                    break

            i = i + 1
    else:
        print("Shoes content not loaded into memory yet")
        success = False

    return success # return the response


def capture_shoe(country, code , product , cost , quantity, add_to_file = False) -> bool:

    """
    Instantiates a new shoe object and appends it to the shoe list
    Args:
        country (str): The country where the shoe is from
        code (str): The shoe code:
        product (str): The product name of the shoe
        cost (float|int): The cost of the shoe
        quantity (int): The quantity of the shoe
        add_to_file (bool): Whether to add the shoe to the file

    Returns:
        bool: Whether the data capture was a success or not
    """

    try:
        # check that the show list exists and is a list
        if isinstance(shoe_list, list):

            # instantiate a new show object and pass in the values
            # The values can be passed in raw as they will be formatted in the object
            new_shoe = Shoe(country=country, code=code, product=product, cost=cost, quantity=quantity)
            shoe_list.append(new_shoe) # append the new shoe to the shoe list

            # Add the show to the file if the flag is true
            if add_to_file:
                data = [new_shoe.get_country(), new_shoe.get_code(), new_shoe.get_product(), new_shoe.get_cost(), new_shoe.get_quantity()]
                file.add_row(data)

            # check to make sure that the new shoe was appended to the list successfully
            if shoe_list[len(shoe_list) -1 ] == new_shoe:
                print("Shoe added successfully to the list")
                return True

            else:
                return False
        else:
            # Exception raised if the shoe list is not a list
            raise TypeError("Shoe list must be a list")

    except (TypeError, ValueError) as error:
        # print the error and return false
        print(error)
        return False


def view_all() -> bool:

    """
    Lists all the Shoes that have been imported into the application via the shoe list
    Returns:
        bool: Whether the operation was a success or not
    """

    # Loop through each show and output
    for i, shoe in enumerate(shoe_list):
        print(f"{i}: {shoe}")
        print() # new empty line

    return True

def re_stock(new_quantity = 0) -> bool:

    """
    Find the Shoe with the lowest quantity and increase its quantity by the value pass in
    Args:
        new_quantity (int):  The amount to add to the existing quantity

    Returns:
        bool: Whether the operation was a success or not
    """

    #Check the length of the shoe list to make sure we have items inside it, if not, proceed no further
    if len(shoe_list) > 0:
        lowest_quantity_index = 0
        lowest_quantity = shoe_list[0].get_quantity()

        # Loop through the sho list and find the lowest quantity, note the quantity and index of the record
        for i in range(1, len(shoe_list), 1):
            if shoe_list[i].get_quantity() < lowest_quantity:
                lowest_quantity_index = i
                lowest_quantity = shoe_list[i].get_quantity()
            else:
                continue

        # Check that we have a lowest value and that it is a type of Shoe
        if shoe_list[lowest_quantity_index] and type(shoe_list[lowest_quantity_index]) is Shoe:

            # Add the existing quantity to the new quantity
            final_quantity = shoe_list[lowest_quantity_index].get_quantity() + new_quantity

            before_update = shoe_list[lowest_quantity_index]
            # Set the new quantity
            shoe_list[lowest_quantity_index].set_quantity(final_quantity)
            after_update = shoe_list[lowest_quantity_index]

            # Set up the data
            file_update_data = [
                shoe_list[lowest_quantity_index].get_country(),
                shoe_list[lowest_quantity_index].get_code(),
                shoe_list[lowest_quantity_index].get_product(),
                shoe_list[lowest_quantity_index].get_cost(),
                shoe_list[lowest_quantity_index].get_quantity()
            ]

            # Update the file
            file_updated = file.update_row(lowest_quantity_index, file_update_data)

            # Check that the quantity is updated in both the object and the file
            if (shoe_list[lowest_quantity_index].get_quantity() == final_quantity) and file_updated:

                print(f"""BEFORE UPDATE
                       {before_update}
                   """)
                print()
                print(f"""AFTER UPDATE
                              {after_update}
                          """)
                return True

            else:
                print("Failed to update the quantity") # Failed to update
                return False

        else:
            return False

    else:
        return False



def search_shoe(search_shoe_code) -> Shoe|bool:

    """
    Search for a shoe by its shoe code
    Args:
        search_shoe_code (str): The show code to search for

    Returns:
        bool|str: Boolean on failure, string on success
    """

    # Loop through the search list to find the shoe code
    for i, shoe in enumerate(shoe_list):
        # Check for a match
        if shoe.get_code() == search_shoe_code.upper():
            return shoe # return a match
        else:
            continue # No Match but still in the loop, continue to the iteration

    return False # No matches, return false


def value_per_item() -> bool:

    """
    Iterates over the shoe list and gets the total value for each shoe in the list
    Returns:
        bool: Whether the operation was successful or not
    """

    print("Total for each item") # Print a title
    print() # empty line

    # Iterate over the list
    for i, shoe in enumerate(shoe_list):
        total = shoe.get_cost() * shoe.get_quantity() # Get the total by multiplying the cost by the quantity
        print(f"{shoe.get_product()}: R{total:.2f}") # Output the values

    return True


def highest_qty() -> Shoe:

    """

    Returns:
        Shoe: The highest quantity shoe
    """

    # Instantiate a blank shoe object to compare against
    highest_qty_shoe = Shoe("", "", "", 0.0, 0)

    # search through the list and look for the shoe with the highest quantity
    for i, shoe in enumerate(shoe_list):
        if shoe.get_quantity() > highest_qty_shoe.get_quantity():
            highest_qty_shoe = shoe # if the current shoe's quantity is higher than what we already have then replace it

    # return the highest quantity shoe
    return highest_qty_shoe

# START OF THE MAIN APPLICATION

print("****WELCOME****")
print("Shoe Application")

shoe_list = [] # empty shoe list
inventory_text_file = "inventory.txt" # text file name and path
file = File(inventory_text_file, File.READ_TEXT)


# Ask if the user wants to pre-load the inventory.txt file into the application before starting
while True:
    seed_shoe_list = input("Do you want to pre-fill the shoe list? (y) or (n):").strip().lower()

    # load the shoes in
    if seed_shoe_list == "y" or seed_shoe_list == "yes":
        shoes_loaded = read_shoes_data()
        clear_screen()

        # check if shoes are loaded
        if shoes_loaded:
            print(f"The stock from the inventory file ({inventory_text_file}) has already been loaded")
            break

        else:
            # Load failed
            print(f"The stock from the inventory file ({inventory_text_file}) has not been loaded")
            break
    elif seed_shoe_list == "n" or seed_shoe_list == "no":
        print(f"The stock from the inventory file ({inventory_text_file}) has not been loaded")
        break

    else:
        print("Invalid input")
        continue

#==========Main Menu=============

while True:
        option = input(f"""
Enter an option for the menu below:
    (1) Load/Reload the inventory file
    (2) View all shoes
    (3) Capture a new shoe
    (4) Search for a shoe by shoe code
    (5) Restock the shoe with the lowest quantity
    (6) Get the Shoe with the highest quantity
    (7) Get the value for each item
    (q) Exit the program
        
: """).strip().lower()
        if option == "q": # quit the application
            quit()
        else:
            try:
                option = int(option)

            except ValueError:
                print("Invalid option")
                continue

            if option == 1: # load/reload data

                # Get the input from the user
                while True:
                    new_list = input("Do you want to start a new list (n) or append to the existing list (a)? (c) to cancel: ").strip().lower()
                    print(new_list)

                    if new_list == "c": # cancel option in case they selected this by mistake
                        break

                    # check for valid option
                    if "n" != new_list != "a":
                        print("Invalid option")
                        continue

                    else:

                        #if a new list is needed - clear the list and start afresh
                        if new_list == "n":
                            shoe_list = []

                        break

                # execute the function and check for success response - output accordingly
                if read_shoes_data():
                    clear_screen()
                    print("The data from the inventory file has been loaded/re-loaded")
                    continue

                else:
                    clear_screen()
                    print("The data from the inventory file failed to reload")
                    continue

            elif option == 2: # view all
                clear_screen()
                view_all() # display all shoes
                continue

            elif option == 3: # Capture new shoe
                append_to_file = True
                # Capture all the data to enter a new shoe object into the shoe list and update the file
                #Cancels here as well in case of user error

                continue_loop = True

                while True:
                    new_country = input("Enter the full name of the country (or c to cancel): ").strip().title()

                    if new_country == "":
                        continue
                    elif new_country == "c":
                        continue_loop = False

                    break

                if continue_loop:
                    while True:
                        new_code = input("Enter the SKU code of the product (or c to cancel): ").strip().upper()

                        if new_code == "":
                            continue
                        elif new_code == "c":
                            continue_loop = False

                        break

                if continue_loop:
                    while True:
                        new_product = input("Enter the product name (or c to cancel): ").strip().title()

                        if new_product == "":
                            continue

                        elif new_product == "c":
                            continue_loop = False

                        break


                if continue_loop:
                    while True:
                        new_cost = input("Enter the cost of the product (or c to cancel): ").strip()

                        if new_cost == "":
                            continue
                        elif new_cost == "c":
                            continue_loop = False
                            break
                        else:

                            try:
                                new_cost = float(new_cost)

                            except ValueError:
                                print("Invalid input for cost")
                                continue

                            else:
                                break

                if continue_loop:
                    while True:
                        new_quantity = input("Enter the quantity of the product (or c to cancel): ").strip()

                        if new_quantity == "":
                            continue
                        elif new_quantity == "c":
                            continue_loop = False
                            break

                        else:

                            try:
                                new_quantity = float(new_quantity)

                            except ValueError:
                                print("Invalid input for quantity")
                                continue

                            else:
                                break

                if continue_loop:

                    # capture the data and output feedback whether it was successful or not
                    if capture_shoe(
                            country=new_country,
                            code=new_code,
                            product=new_product,
                            cost=new_cost,
                            quantity=new_quantity,
                            add_to_file=append_to_file
                    ):
                        clear_screen()
                        print("The data has been captured")

                    else:
                        clear_screen()
                        print("The data has not been captured")


            elif option == 4: # Search for a shoe

                # Get the shoe code from the user, search for the shoe and display the shoe to the user
                while True:
                    shoe_code = input("Enter a shoe code, or (c) to cancel: ").strip().upper()
                    if shoe_code == "":
                        continue
                    else:
                        break

                if shoe_code == "c":
                    clear_screen()
                    continue

                output = search_shoe(shoe_code)

                if output:
                    clear_screen()
                    print(output)
                    continue

                else:
                    clear_screen()
                    print("No Shoe Found")
                    continue

            elif option == 5: #restock the lowest quantity shoe

                # Get the quantity from the user as to how much they want to top the shoe up by and then top it up - changes saved to object and file
                while True:

                    try:
                        input_quantity = input("Enter a quantity to restock by (c to cancel): ").strip()

                        if input_quantity == "":
                            print("Quantity must be a whole number")
                            continue
                        elif input_quantity == "c":
                            break
                        else:
                            clear_screen()
                            if re_stock(int(input_quantity)):
                                print("Lowest quantity has been updated")
                            else:
                                print("Quantity update failed")

                            break
                    except ValueError:
                        clear_screen()
                        print("Quantity must be a whole number")
                        continue

            elif option == 6: # get the shoe with the highest quantity
                clear_screen()
                print("Shoe with the highest quantity:")
                print('*' * 10)
                print(highest_qty())
                continue

            elif option == 7: # Get the value for each item
                clear_screen()
                value_per_item()
