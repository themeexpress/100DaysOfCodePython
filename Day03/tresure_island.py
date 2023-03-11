print("Welcome to tresure Island")
choose_direction = input("You are at the cross road. Where do you want to go? Type 'left' or 'right' \n").lower()
if choose_direction == "right":
  choose_river = input("There is a river. if you want to swim type 'swim' if you want to wait for boot then type 'wait' \n")
  if choose_river == "swim":
    print("There are crocodile in river. You die")
  else:
    choose_door = input("There are 3 doors, yellow, red, blue, type which door you want to enter.\n").lower()
    if choose_door == 'blue':
      print("You won the tresure")
    else:
      print("Others doors are in danger, you die")
else:
  print('There is big hole in road. you die. Game over')


