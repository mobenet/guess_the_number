import random

def guess_the_number(): 
    print("\nWelcome to the Guess the Number Game!")
    lower_limit = int(input(f"Introduce the lower limit to Guess the number:"))
    upper_limit = int(input(f"Introduce the upper limit to Guess the number:"))

    random_number = random.randint(lower_limit,upper_limit)
    guess = 0

    while guess!=random_number:
        guess = int(input(f"Guess a number between {lower_limit} and {upper_limit}: "))
        if guess<random_number:
            print("Try again. That number is too low.")
        if guess>random_number:
            print("Try again. That number is too high.")

    print(f"Congratulations! You have guessed the number {random_number} correctly.")
  
def main():
    guess_the_number()

if __name__ == "__main__":
    main()