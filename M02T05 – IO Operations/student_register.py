#Get the number of students
number_of_students = int(input("How many students are you registering? : "))

#open the file in append mode - if the file does not exist, create anyway
file = open("reg_form.txt", "a")

#ask the user for each student id and append it to the end of the file
for i in range(number_of_students):
    student_id = int(input("Enter a student id : "))
    file.write(str(student_id) + "\n") #write the student id to the end of the file with a new line
    file.write("-" * 10) #add the dotted line
    file.write("\n") #add another new line

print("Students registered successfully")

#close the file
file.close()