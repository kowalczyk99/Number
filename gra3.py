# Number guessing game


import random

top_of_range = input("Type a number: ")


if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Pleas type a number larger than 0 next Time Bro 😘👌")
        quit()
else:
    print("pleas type a number larger than next time DuDe")
    quit()

random_number = random.randint(0, top_of_range)
print(random_number,"Tip")

move = 0
while True:
    move += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print('You got it!')
        break
    elif user_guess > random_number:
        print('You were above the number!⬇️')
    else:
        print('You were below the number ⬆️')

print("You got in in", move, "guesses","🏆🏆")


