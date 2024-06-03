import random

#if start is not mentioned it will by default generate numbers from 0


#this will explicitly generate numbers that will include 
# from -2 to 1. explicitly means it will not include the end range number
n_1 = random.randrange(-2, 2)
print(n_1)

#implicitly include all the number from -2 to 2
n_2 = random.randint(-2, 2)
print(n_2)


limit = input("Type a number: ")

if limit.isdigit():
    limit = int(limit)

    if limit <= 0:
        print("Please type a number greater than 0")
        quit()
else:
    print("Please type a number")

tries =0
random_num = random.randrange(0, limit)

while True:
    tries += 1
    guess = input("Guess a number: ")

    if guess.isdigit():
        guess = int(guess)
    else:
        print("please print a number")
        continue

    if guess == random_num:
        print("YOU GOT IT!")
        break
    elif guess < random_num:
        print("You are down the range")
    elif guess > random_num:
        print("You have exceeded the limit")



print(" you have got it in", tries, "guesses")