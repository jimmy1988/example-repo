# --- CLASSES --- #
class Email:
    # Class properties
    _email_address = "" #store the email address
    _subject_line = "" # store the subject line
    _email_content = "" # store the email content
    _has_been_read = False # store whether the email has been read or not

    # Constructor method
    def __init__(self, email_address, subject_line, email_content) -> None:
        """
        Initialize an Email object.
        Args:
            email_address:
            subject_line:
            email_content:

        Returns:
            None
        """
        self.set_email_address(email_address)
        self.set_subject_line(subject_line)
        self.set_email_content(email_content)

    def set_email_address(self, email_address) -> None:
        """
        Set the email address for this message.
        Args:
            email_address (str): Email address to use:

        Returns:
            None
        """
        self._email_address = str(email_address)

    def get_email_address(self) -> str:
        """
        Get the email address for this message.

        Returns:
            str: Email address to use:

        """
        return self._email_address

    def set_subject_line(self, subject_line) -> None:

        """"
        Set the subject line for this message.
        Args:
            subject_line (str): Subject line to use:

        Returns:
            None
            """

        self._subject_line = str(subject_line)

    def get_subject_line(self) -> str:

        """
        Get the subject line for this message.

        Returns:
            str: Subject line to use:

        """

        return self._subject_line

    def set_email_content(self, email_content) -> None:

        """
        Set the email content for this message.

        Args:
            email_content (str): Email content to use:

        Returns:
            None
        """

        self._email_content = str(email_content)

    def get_email_content(self) -> str:

        """
            Get the email content for this message.
        Returns:
            str: Email content to use:
        """

        return self._email_content

    def get_has_been_read(self) -> bool:

        """
        Get the has_been_read flag for this message.
        Returns:
            bool
        """

        return self._has_been_read

    def mark_as_read(self) -> None:

        """

        Returns:
            None
        """

        self._has_been_read = True

    def mark_as_unread(self) -> None:

        """

        Returns:
            None
        """

        self._has_been_read = False


# --- FUNCTIONS --- #

emails = [] # Initialize the emails list

def populate_inbox() -> None:

    """
    Populates the emails list

    Returns:
        None
    """

    email_data = [
        (
            "john.doe@example.com",
            "Welcome to our platform!",
            (
                "Hi John,\n\nWelcome aboard! We are thrilled to have you join our"
                " community. Please let us know if you have any questions."
            ),
        ),
        (
            "sarah.connor@cyberdyne.net",
            "Security Alert: New login from unknown device",
            (
                "Hi Sarah,\n\nWe noticed a login to your account from a new device."
                " If this was you, you can safely ignore this email."
            ),
        ),
        (
            "alex.smith@techcorp.io",
            "Project Update: Q3 Deliverables",
            (
                "Hi team,\n\nHere is the latest status update for our Q3"
                " deliverables. Please review the attached notes before our"
                " meeting tomorrow."
            ),
        ),
    ]

    for email, subject, content in email_data:
        emails.append(Email(email, subject, content))


def list_emails() -> None:

    """
        List all emails read
        Returns:
            None
    """

    if len(emails) == 0:
        print("No emails To Display.")

    else:

        for i, email in enumerate(emails):
            print(f"{i}  {email.get_subject_line()}")


def read_email(index) -> None:

    """
    Read an email and display it as a string
    Args:
        index (int): Index of the email to read:

    Returns:
        None
    """

    email = emails[index]
    email.mark_as_read()

    print(f"From: {email.get_email_address()}")
    print(f"Subject: {email.get_subject_line()}")
    print(f"Content: {email.get_email_content()}")


def view_unread_emails() -> None:

    """
    List all unread emails
    Returns:
        None
    """

    for i, email in enumerate(emails):
        if not email.get_has_been_read():
            print(f"{i}  {email.get_subject_line()}")


# --- PROGRAM START --- #

populate_inbox() # Populate the inbox

#Gets the users input, keeps interactivity going until the user quits
while True:
    #Get the users choice
    user_choice = int(
        input(
            """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. List all emails
    4. Quit application

    Enter selection: """
        )
    )

    if user_choice == 1:
        try:
            #Get the email index
            email_index = int(input(f"Please provide the index of the email (0 to {len(emails) - 1}): "))
            read_email(email_index) #Pass to the read email function and display the email

        except ValueError:
            #If value error exception is thrown, display message and continue loop
            print("Oops - incorrect input, try again.")
            continue

    elif user_choice == 2:
        view_unread_emails() # Display unread emails

    elif user_choice == 3:
        list_emails() # list all emails

    elif user_choice == 4:
        break #break the loop - quits the program

    else:
        print("Oops - incorrect input.") # invalid input option supplied
