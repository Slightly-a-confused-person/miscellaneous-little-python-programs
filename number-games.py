import random

num = random.randint(1, 100)
print("There are 100 numbers. One is chosen. If you get that number, you win. You will have 20 guesses.")

for i in range(20):
    try:
        guess = int(input(f"Pick a number (guess {i+1}/20): "))
    except ValueError:
        print("That's not a number. Try again.")
        continue

    if guess > num:
        print("Too high. Try again.")
    elif guess < num:
        print("Too low. Try again.")
    else:
        print(f"Correct! You won in {i+1} guesses!")
        break
else:
    print(f"You ran out of guesses. The number was {num}.")

print("Good game. *applause*")
