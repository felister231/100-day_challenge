# A program to calculate the body mass index of  a person 
# And comment on their BMI
height= float(input("Enter your height in metres: "))
weight= float(input("Enter your weight in kilograms: "))
BMI=round(weight/(height ** 2))

if BMI < 18.5:
    print(f"Your BMI is {BMI} and you are underweight\n")
elif BMI < 25:
    print(f"Your BMI is {BMI} and you are normal weight\n")
elif BMI<30:
    print(f"Your BMI is {BMI} and you are slightly overweight\n")
elif BMI < 35:
    print(f"Your BMI is {BMI} and you are slightly obese\n")
else:
    print(f"Your BMI is {BMI} and you are clinically obese")