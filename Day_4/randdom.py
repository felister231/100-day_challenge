import random
test_seed = int(input("Enter a seed number:"))
random.seed(test_seed)
name_everybody = input("Give me everybody's name separated by a comma: ")
name = name_everybody.split(", ")
selected_name_index = random.randint(0, len(name) - 1)
selected_name = name[selected_name_index]

print(f"{selected_name} is going to pay today")