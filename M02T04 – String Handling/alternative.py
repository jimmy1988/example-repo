#Ask the user for a string
alternative_string = input("Please enter a string: ")

#initialize the final string
final_string = ""

#loop around each character in the string
for i in range(len(alternative_string)):

    #starting a the first character make the starting character and each alternative character uppercase
    if i % 2 == 0:
        final_string += alternative_string[i].upper()

    else:
        final_string += alternative_string[i].lower() #convert to lowercase in case theres already an uppercase character at this position

#print the final result
print(final_string)

#split the original string into a list
new_alternative_string = alternative_string.split()

#start a new output
new_final_string = ""

#loop around the list
for i in range(len(new_alternative_string)):

    #convert each alternative word to lowercase, starting at the first word
    if i % 2 == 0:
        new_final_string += new_alternative_string[i].lower()
    else:
        new_final_string += new_alternative_string[i].upper() #else convert to uppercase

    new_final_string += " " # add a space on the end to retain the spacing

print(new_final_string.strip()) #output the result, stripping off whitespace