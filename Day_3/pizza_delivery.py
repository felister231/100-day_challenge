# This program is for making pizza orders.
# It prompts the user to enter the size of the pizza
# and asks if they want extra toppings, updating the bill accordingly.

print("Welcome to Python Pizza deliveries")
size = input("What size do you want? S, M, L\n")
bill = 0

if size == "S":
    bill = 15
    print("Your bill is $15")
    add_pepperoni = input("Do you want pepperoni? Y or N\n")
    if add_pepperoni == "Y":
        bill += 2
        print(f"Your bill is {bill}")
    else:
        print(f"Bill is {bill}")

elif size == "M":
    bill = 20
    print("Your bill is $20")
    add_pepperoni = input("Do you want pepperoni? Y or N\n")
    if add_pepperoni == "Y":
        bill += 3
        print(f"Your bill is {bill}")
    else:
        print(f"Bill is {bill}")

else:
    bill = 25
    print("Your bill is $25")
    add_pepperoni = input("Do you want pepperoni? Y or N\n")
    if add_pepperoni == "Y":
        bill += 3
        print(f"Your bill is {bill}")
    else:
        print(f"Bill is {bill}")

add_cheese = input("Do you want extra cheese? Y or N\n")        
if add_cheese == "Y":
    bill += 1
    print(f"Your Total bill is {bill}")
else:
    print(f"Your total bill is $ {bill}")
