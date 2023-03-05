# Roller coaster ticker
print('Welcome to the roller coaster!')
bill = 0
height = int(input('What is your height in CM'))

if height >= 120:
    age = int(input('Enter your age'))
    if age < 12:
        bill += 5
        print(f"Child tickets bill is {bill}$")
    elif age <= 18:
        bill += 7
        print(f"Youth tickets bill is {bill}$")
    else:
        bill += 12
        print(f"Adult tickets bill is {bill}$")

    want_photo = input('Do you want photo? Type Y for Yes and N for No')
    if want_photo == 'Y' or 'y':
        bill += 5
        print(f"Your ticket price with Photo is {bill}$")
    else:
        bill += 0
        print(f"Your ticket price with Photo is {bill}$")

else:
    print("Sorry. Your have to more taller to ride")

