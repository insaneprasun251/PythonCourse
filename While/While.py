# for i in range(10):
#     print("i is now {}".format(i))
#
# # While needs a variable declaration before the loop or it won't work
# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1

#
# available_exist = ["east", "north east", "south"]
#
# chosen_exit = ""
# while chosen_exit not in available_exist:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit == "quit":
#         print("Game Over")
#         break
# else:
#     print("aren't you glad you got out of there!")
import random

highest = 1000
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}".format(highest))
guess = 0  # needs to be initialized for while loop and needs to be outside of the loop

while guess is not answer:
    guess = int(input())
    if guess == 0:
        break
    if guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    else:
        print("Well done, you guessed it")

