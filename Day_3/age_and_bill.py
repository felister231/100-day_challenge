# A program that determines whether one can ride a rollercoaster
# depending on their height and calculates their bill based on age

print("Welcome to the rollercoaster")
height = int(input("Enter your height in cm\n"))
bill = 0

if height > 120:
    print("You are tall enough to ride")
    age = int(input("Enter your age\n"))
    if age < 12:
        bill = 5
        print("Your bill is $5")
    elif age < 18:
        bill = 7
        print("Your bill is $7")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything is okay. You are going to ride for free with us")
        want_photo_print = str(input("Do you want a photo? Reply Y or N?\n"))
        if want_photo_print == "Y":
            bill += 3
            print(f"Your total bill is $ {bill}")
    elif age > 55:
        print("Sorry we do not want casualties")        
        
    else:
        bill = 12
        print("Your bill is $12")
        
        # Add $3 to the bill if one wants a photo
        want_photo_print = str(input("Do you want a photo? Reply Y or N?\n"))
        if want_photo_print == "Y":
            bill += 3
            print(f"Your total bill is $ {bill}")
else:
    print("You'll have to grow taller for you to ride")
