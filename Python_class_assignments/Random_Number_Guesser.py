import random

start = input("Enter the start of the range: ")

while True:
    try:        
        int(start)
        break
    except ValueError:
        print("Please enter a valid number.")
        start = input("Enter the start of the range: ")

end = input("Enter the end of the range: ")

while True:
    try:        
        int(end)
        if end > start:
            break
        else:
            print("Please enter a valid number.")
            end = input("Enter the end of the range: ")
    except ValueError:
        print("Please enter a valid number.")
        end = input("Enter the end of the range: ")

random_num = random.randint(int(start), int(end))

guess = None
attempts = 0

while (guess != random_num):
    guess = input("Guess a number: ")
    while True:
        try:        
            int(guess)
            break
        except ValueError:
            print("Please enter a valid number.")
            guess = input("Guess a number: ")
    attempts += 1
    guess = int(guess)

if guess == random_num and attempts == 1:
    print(f"You guessed the number in {attempts} attempt")
if guess == random_num and attempts > 1:
    print(f"You guessed the number in {attempts} attempts")