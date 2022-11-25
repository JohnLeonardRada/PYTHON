import random

def guess_checker():
    secret_word = ["poop", "weather", "example", "notebook", "deez", "nutz"]
    guess = ""
    guess_count = 0
    guess_limit = len(secret_word)

    out_of_guesses = False
    random_word = random.choice(secret_word)

    while guess.lower() != random_word and not(out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter guess: ")
            guess_count += 1
        else:
            out_of_guesses = True
    print(f"Wrong! You have {guess_limit - 1} guesses left.")
    if out_of_guesses:
        print(f"You're out of guesses, You Lose! The word is {random_word}")
    else:
        print(f"Congratulations! You Won! The word is {random_word}")

def main():
    print("Welcome to Hangman Game!")
    guess_checker()
    return 

if __name__ == '__main__':
    main()