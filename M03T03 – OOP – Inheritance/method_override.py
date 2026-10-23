"""" START OF THE ADULT CLASS """
class Adult:

    # All properties are private because i do not want the to be read and written verbatim
    # I want the getters or setters to set them and get them
    # Prevents data contamination
    _name = "" # Stores the name
    _age  = 0 # Stores the age
    _hair_colour = "" # Stores the hair colour
    _eye_colour = "" # Stores the eye colour

    def __init__(self, name, age, hair_colour, eye_colour) -> None:

        """
        Initializes the class (and any Child Classes)
        Take all the attributes through the initializer and set them using the setters
        Args:
            name (str): The name of the person:
            age (int): The age of the person:
            hair_colour (str): The hair colour of the person:
            eye_colour (str): The eye colour of the person:
        """

        self.set_name(name)
        self.set_age(age)
        self.set_hair_colour(hair_colour)
        self.set_eye_colour(eye_colour)

    def set_name(self, name) -> None:

        """
        Sets the name of the person:
        Args:
            name (str): The name of the person:

        Returns:
            None
        """
        self._name = str(name)

    def get_name(self)  -> str:

        """
        Returns the name of the person:
        Returns:
            str: The name of the person:
        """

        return self._name

    def set_age(self, age)  -> None:

        """
        Sets the age of the person:
        Args:
            age (int): The age of the person:

        Returns:
            None
        """

        self._age = int(age)

    def get_age(self)  -> int:

        """
        Returns the age of the person:
        Returns:
            int: The age of the person:

        """

        return self._age

    def set_hair_colour(self, hair_colour) -> None:

        """
        Sets the hair colour of the person:
        Args:
            hair_colour (str): The hair colour of the person:

        Returns:
            None
        """

        self._hair_colour = str(hair_colour)

    def get_hair_colour(self) -> str:

        """
        Returns the hair colour of the person:

        Returns:
            str: The hair colour of the person:

        """

        return self._hair_colour

    def set_eye_colour(self, eye_colour)  -> None:

        """
        Sets the eye colour of the person:
        Args:
            eye_colour (str): The eye colour of the person:

        Returns:
            None

        """

        self._eye_colour = str(eye_colour)

    def get_eye_colour(self) -> str:

        """
        Returns the eye colour of the person:
        Returns:
            str: The eye colour of the person:

        """

        return self._eye_colour

    def can_drive(self) -> None:

        """
        Prints out that the person is old enough to drive.
        Returns:
            None
        """

        print(f"{self.get_name()}, you are old enough to drive!")

"""" END OF THE ADULT CLASS """

"""" START OF THE CHILD CLASS """

class Child(Adult):

    def can_drive(self) -> None:
        """
                Prints out that the person is not old enough to drive.
                Returns:
                    None
                """

        print(f"{self.get_name()}, you are too young to drive!")

"""" END OF THE ADULT CLASS """

"""" START OF MAIN PROGRAM """

# Get the users name
while True:

    try:
        new_name = input("Enter your name: ").strip()

        break
    except ValueError:
        print("Please enter a valid name")


# Get the users age
while True:

    try:
        new_age = int(input("Enter your age: ").strip())

        if new_age > 0:
            break

    except ValueError:
        print("Please enter a valid age")

# Get the users hair colour
while True:
    try:
        new_hair_colour = input("Enter your hair colour: ").strip()
        break

    except ValueError:
        print("Please enter a valid hair colour")


# Get the users eye colour
while True:

    try:
        new_eye_colour = input("Enter your eye colour: ").strip()
        break

    except ValueError:
        print("Please enter a valid eye colour")

# If the person is 18 or over initialize the Adult class and pass in the inputs
# else initialize the Child class
if new_age >= 18:
    person = Adult(new_name, new_age, new_hair_colour, new_eye_colour)
else:
    person = Child(new_name, new_age, new_hair_colour, new_eye_colour)

# Print out of the person can drive or not
# Place here to save on repetition
person.can_drive()

"""" END OF MAIN PROGRAM """