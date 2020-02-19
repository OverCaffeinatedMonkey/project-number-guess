import random

def get_guess(min_val, max_val):
    while True:
        try:
            print("Enter your guess, between %d and %d inclusive." % (min_val, max_val))
            guess = int(input())
            if guess <  min_val or guess > max_val:
                print("Guess must be between %d and %d inclusive." % (min_val, max_val))
            else:
                return guess;
        except:
            print("Your guess must be a number.")

def game_loop(num_times):
    
    for i in range(0, num_times):
        print("Game %d" % (i + 1))

        target_number = random.randint(1, 26)
        number_guesses = 0

        guess = -1
        while guess != target_number:
            guess = get_guess(1, 25)
            number_guesses += 1

            if guess > target_number:
                print("Lower")
            elif guess < target_number:
                print("Higher")

        print("Correct, it took you %d guesses." % number_guesses)

    print("guess = %d, target = %d" % (guess, target_number))

    

while True:
    try:
        num_times = int(input("How many times would you like to play? "))
        break;
    except:
        print("Please enter the number of times")
game_loop(num_times)
        



