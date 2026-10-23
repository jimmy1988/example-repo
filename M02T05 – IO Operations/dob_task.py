#Open the file in read only  mode and read from the file
file = open("DOB.txt", "r")
file_contents = file.read()

#split the file into a list, using the end of line character as the split reference
file_output = file_contents.split("\n")

#Print the title
print("Name")

#loop around each line outputting all of the names
for line in file_output:
    #If we have an empty line, do not output it
    if len(line) > 0:
        line = line.strip().split(" ") #strip off whitespace and split into another list by each word
        print(line[0].strip() + " " + line[1].strip()) #for each word strip off whitespace and output

#print empty line - for readability
print()
#Print the title
print("BirthDate")
#loop around each line outputting all of the birthdates
for line in file_output:

    # If we have an empty line, do not output it
    if len(line) > 0:
        line = line.strip().split(" ") #strip off whitespace and split into another list by each word
        print(line[2].strip() + " " + line[3].strip() + " " + line[4].strip()) #for each word strip off whitespace and output


#close the file
file.close()