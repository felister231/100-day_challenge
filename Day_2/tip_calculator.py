# this program calculates the amount of tip one wishes to give #
# After getting the tip one calculates the amount one should pay and 
#then calculates how much each individual should pay.#

print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill?\n"))
percent = int(input("What percentage would you like to give? 10, 12 or 15\n"))
friends= int(input("How many people to split the bill\n"))
bill_and_tip = float(((percent/100) * total_bill) + total_bill)
per_person = bill_and_tip/friends
print(f"Each person should pay ${per_person: .2f}")
