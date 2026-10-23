#Declare the friends names list
friends_names = ["Bob", "Fred", "Marie"]

#print the first friends name
print(friends_names[0])

#print out the last friends name
print(friends_names[-1])

#print out the length of the friends name list
print(len(friends_names))

#Declare the friends ages list
friends_ages = [21, 32, 44]

#loop around both the friends names and friends ages outputting them to the console
for name, age in zip(friends_names, friends_ages):
    print(f"{name} is {age} years old")