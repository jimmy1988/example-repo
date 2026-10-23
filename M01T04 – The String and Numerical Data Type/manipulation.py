#Get a string from the user
str_manip = input("Enter a string: ")

#calculate the length of the string and display it to the user
print(f"The length of the string is:{len(str_manip)}")

#find the last letter
last_letter = str_manip[-1]

#replace the last letter and all letters like it with an @
str_manip_replace = str_manip.replace(last_letter,"@")
"""
    For example,
    bring me the busy bodies bbbb
    would output 
    @ring me the @usy @odies @@@@
"""
print(str_manip_replace)

#Print the lst 3 characters
"""
    For example,
    bring me the busy bodies bbbb
    would output 
    bbb
"""
print(str_manip[-1:-4:-1])

#output the first 3 characters and the last 2 characters
"""
    For example,
    bring me the busy bodies bbbb
    would output 
    bribbb
"""
print(f"{str_manip[:3:1]}{str_manip[-1:-3:-1]}")