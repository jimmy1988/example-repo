name_to_find = "John" #This is the name to find
incorrect_names = [] #initialize the incorrect name list
input_name = "" #initialize input_name
message = "Please give a name to find: " #The starting message

#Loop around until the correct name is given
while input_name.lower() != name_to_find.lower():
    input_name = input(message).lower() #ask the user for name and then convert it to lowercase

    #if the input name is not equal to the name to find, append the name to the incorrect names list
    if input_name != name_to_find.lower():
        incorrect_names.append(input_name)
        message = "Incorrect, Please give another name to find: " #change the message
    else:
        print("Correct, name found") #correct response
        break #break out of the loop

print(incorrect_names) #output the incorrect names