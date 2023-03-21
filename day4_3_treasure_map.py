# Treasure Map. 
# Access nested list to store your treasure
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# Type cust the input
horizontal = int(position[0])
vertical = int(position[1])

if(0 > horizontal or horizontal <= 3) and (0 > vertical or vertical <= 3):
  selected_row = map[vertical-1]
  selected_row[horizontal-1] = 'X'
else:
  print('maximum selction range is 33')
  

# Your treasure will be shown here
print(f"{row1}\n{row2}\n{row3}")
