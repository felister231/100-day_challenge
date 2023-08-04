# program checks if a year is a leap year

# Get input from the user for the year
year = int(input("Type in the year\n"))

# Check if the year is divisible by 4
if (year % 4 == 0):
    # If the year is divisible by 400 and 100, it's a leap year
    if (year % 400 == 0 and year % 100 == 0):
        print("Year is a leap year")
    # If the year is divisible by 4 but not by 100, it's a leap year
    elif (year % 100 != 0):
        print("Year is a leap year")
    # If the year is divisible by 4 and 100, but not by 400, it's not a leap year
    else:
        print("Year is not a leap year")
# If the year is not divisible by 4, it's not a leap year
else:
    print("Year is not a leap year")
