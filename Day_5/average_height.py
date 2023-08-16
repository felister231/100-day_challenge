student_height = input("Input the student heights: ").split()

for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])

print(student_height)  # Print the list of student heights

for each_height in student_height:
    print(each_height)  # Print each individual student height

total_height = 0

for height in student_height:
    total_height += height  # Add each height to the total

print("Total height:", total_height)
average = total_height / n
print(average)