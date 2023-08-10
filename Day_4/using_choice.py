import random
test_seed = int(input("Enter a seed number:"))
random.seed(test_seed)
name_everybody = input("Give me everybody's name separated by a comma: ")
names = name_everybody.split(", ")
#name_index = random.randint(0, len(names) -1)
person_to_pay = random.choice(names)
print(f"{person_to_pay} is going to pay for lunch")
