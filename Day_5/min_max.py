values = input("Give me all the numbers to check for max: ").split()

highest_score = 0
for value in values:
    if int(value) > highest_score:
     highest_score = int(value)
print(value)

# Find maximum value
#max_value = values[0]
#for value in values:
    #is_max = True
    #for other_value in values:
        #if other_value > value:
            #is_max = False
            #break
    #if is_max:
        #max_value = value
#print(f"The maximum number in the string is {value}")


#numbers = input ("Enter numbers here").split()
#find_max = int(max(numbers))
#print(f"The max number is: {find_max}")