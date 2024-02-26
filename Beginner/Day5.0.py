student_height = input("Enter the students height: \t").split(',')
summation = 0
j=0
for i in range(0,len(student_height)):
    student_height[i] = int(student_height[i])
    summation +=student_height[i]
    j+=1
average_height = summation/j
print(round(average_height))
