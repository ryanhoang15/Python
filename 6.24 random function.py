import random
i = 0
print("I am thinking of a number between 1 and 10.")
comp = random.randint(1,10)
while i < 5:
    # comp = random.randint(1,10)
    user = int(input("Take a guess : "))
    while user not in range(1,11):
        user = int(input("Wrong value, re-enter:"))
    i = i + 1

    if user > comp:
        print("Your guess is too high.")

    elif user < comp:
        print("Your guess is too low.")

    elif user == comp:
        print("Good job, you got it with", i, "guesses")
        break
else:
    if i >= 5:
        print("You guessed wrong, the number I was thinking of was", comp)
