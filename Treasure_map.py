
# Create three blank lists with the empty box emoji.

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

# Now create another list that contains all three rows

map = [row1, row2, row3]
print(f"{row1} \n{row2} \n{row3}")

# input the place where you want to find the treasure.
position = input("Where do you want to put your treasure: ")

# Horizontal and vertical position
horizontal = int(position[0])
vertical = int(position[1])

# As the string is converted to integer value, then the row counting starts from 0 to n-1
selected_row = map[vertical - 1]
selected_row[horizontal -1]= "X"        #Replace the treasure position with "X"

'''(OR) => map[vertical-1][horizontal-1] = "X" '''

# Final output of the above code.
print(f"{row1} \n{row2} \n{row3}")