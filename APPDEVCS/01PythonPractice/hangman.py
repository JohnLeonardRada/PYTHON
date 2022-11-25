import random

words = ["poop", "weather", "example", "notebook", "deez", "nutz"]
guess = words[random.randint(0, len(words)-1)].upper()
display = []

for x in guess:
    display.append("_")

print("Welcome to Hangman Game!")
print("Word:", end=" ")

indexes = []
tries = 6
userWon = False
userLost = False
guessedLetters = []

def start(word, indexes, display, tries, userWon, userLost, guessedLetters):
    chance = False  
    wrong_guess = False
    wordfound = ""  

    if userLost == False:
        if len(indexes) > 0:  
            for val in indexes:
                display[val] = word[val]
        if len(guessedLetters) > 0:
            print("You have ", tries, " chances left")
            print("")
        for dash in display:
            print(dash, end=" ")
        print("")
        user_guessed = input("Guess: ").upper()
        if len(user_guessed) == 1:  
            word_found = False
            for i in range(len(word)):  
                if(word[i] == user_guessed):  
                    if i in indexes:  
                        print(f"{word[i]} Letter have already been used.")
                        chance = True
                        word_found = True
                        break
                    else:
                        indexes.append(i)
                        print("Nice guess it was ", word[i])
                        word_found = True
        elif len(user_guessed) > 1:  
            if(word == user_guessed):
                print("Congratulations! You won! The word was", word)
                userWon = True
            else:
                wrong_guess = True
        if user_guessed in guessedLetters:  
            print("You already tried ", user_guessed)
            chance = True
        elif wrong_guess == True or word_found == False:  
            guessedLetters.append(user_guessed)
            print("Wrong! Try Again!")
            tries -= 1
            if tries == 0:
                userLost = True
            else:  
                chance = True
        if chance == True:
            start(word, indexes, display, tries,
                  userWon, userLost, guessedLetters)
            chance = False  
        elif len(indexes) > 0 and userWon == False and userLost == False and chance == False:
            if len(indexes) == len(word):  
                print("Congratulations! You won! The word was ", word)
            else:
                start(word, indexes, display, chance,
                      userWon, userLost, guessedLetters)
        elif userLost == True:  
            print("You have ", tries, " chances left")
            print("You lost. Better luck next time! The word was ", word)

def main():
    start(guess, indexes, display, tries, userWon, userLost, guessedLetters)
    return 

if __name__ == '__main__':
    main()