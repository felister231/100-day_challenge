row1 = ["😝", "😝", "😝"]
row2 = ["😝", "😝", "😝"]
row3 = ["😝", "😝", "😝"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}\n")

position = input("Where do you want to put the treasure? ")
# Assuming the input format is like "12" for row 1, column 2

vertical = int(position[0]) - 1  # Adjusting for 0-based indexing
horizontal = int(position[1]) - 1  # Adjusting for 0-based indexing

if 0 <= vertical < len(map) and 0 <= horizontal < len(map[0]):
    selected_row = map[vertical]
    selected_row[horizontal] = "X"
    print(f"Treasure placed at {position}!")
    print(f"{row1}\n{row2}\n{row3}\n")
else:
    print("Invalid position. Please choose a valid position within the grid.")



       