import random

def play(n):
    number = random.randint(1, n)
    chance = 5
    guess = 0

    while guess != number:
        guess = int(input("Guess the Number : "))

        if guess < number:
            print("Your number too small")
            chance -= 1

        elif guess > number:
            print("Your number too big")
            chance -= 1

        elif guess == number:
            print("You Win")

        if chance == 0 :
            print("You lose")
            break

play(10)
