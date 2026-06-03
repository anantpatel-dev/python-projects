import random
            # play_again = "yes"
while True: # while play_again == "yes":
    secret_number = random.randint(1,100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    print("You have 7 attempts. Good Luck!")
    print("---------------------------------------------")

    while attempts < 7:
        guess = int(input("Enter your guess: "))
        attempts += 1
        remaining = 7 - attempts

        if guess < secret_number:
            print("Higher", remaining, "attempts remaining")
        elif guess > secret_number:
            print("Lower", remaining, "attempts reamaining")
        else:
            print("Correct! You got it in", attempts, "attempts")
            break
    else:
        print("Game over! The number was", secret_number)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "no": # No need for if and break statement if doing with other method 
                            #because it will automatically stops when play_again becomes "no"
        print("Thanks for playing!")
        break # No need for breaks also