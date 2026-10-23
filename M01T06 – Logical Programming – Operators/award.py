#Get the swimming time
swimming_time = int(input("Please enter the swimming time (minutes): "))

#Get the cycling time
cycling_time = int(input("Please enter the cycling time (minutes): "))

#Get the running time
running_time = int(input("Please enter the running time (minutes): "))

#Find the sum of all the times
total_completion_time = sum([swimming_time, cycling_time, running_time])

#Produce the awards based on the total time completed
award = ""
if 0 <= total_completion_time <= 100:
    award = "Provincial colours" #Completed between 0 and 100 minutes
elif 101 <= total_completion_time <= 105:
    award = "Provincial half colours" #Completed between 101 and 105 minutes
elif 106 <= total_completion_time <= 110:
    award = "Provincial scroll" #Completed between 106 and 110 minutes
else:
    award = "No award" #Completed over 111 minutes

#Output the award achieved
print(f"Award: {award}")