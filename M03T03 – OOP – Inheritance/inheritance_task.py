class Course:
    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    head_office = "Cape Town"

    # Method to display contact details
    def contact_details(self):
        print(f"Please contact us by visiting {self.contact_website}")


    def head_office_details(self):
        print(f"Our Head Office is {self.head_office}")

class OOPCourse(Course):

    description = "OOP Fundamentals"
    trainer = "Mr Anon A. Mouse"

    def trainer_details(self):
        print(f"The course is {self.description}, provided by {self.trainer}")

    def show_course_id(self):
        print("Course ID #1234")

# Example usage:
# Create an instance of the Course class
course = Course()

# Call the contact_details method to display contact information
course.contact_details()

course.head_office_details()

course1 = OOPCourse()

course1.contact_details()
course1.trainer_details()
course1.show_course_id()
