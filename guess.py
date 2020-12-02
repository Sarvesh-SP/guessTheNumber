#Got Bored, So Created this game using Random Module

import random

snum = random.randint(1,51)

def guess():
  for x in range(8):
    guess = int(float(input("Enter your guess..")))
    if guess < snum:
      print("Your guess is too low.")
    elif guess > snum:
      print("Your guess is too high")
    else:
      break
  
  if guess == snum:
    print("Noice!, you're guessed my number in {} guesses!".format(x))
  else:
    print("Nope. It was {}".format(snum))


#Fuction Call.
guess()


