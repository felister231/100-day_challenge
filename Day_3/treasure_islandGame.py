# A simple game that takes you step by step to treasure island
print("Welcome to treasure island. Your mission is to find the treasure")
pick_side = input("Pick the way you want to go. 'Left' or 'Right'\n")

if pick_side == "Right":
    print("Game over")
elif pick_side == "Left":
    swim_orWait = input("Do you want to swim or wait? Please type 'Swim' or 'Wait'\n")
    
    if swim_orWait == "Swim":
        print("Game over")
    elif swim_orWait == "Wait":
        choose_door = input("Which door do you want to enter? Type 'Red', 'Blue' or 'Yellow'\n")
        
        if choose_door == "Red" or choose_door == "Blue":
            print("Game over")
        else:
            print("You win")
