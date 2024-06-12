import random

def choose_word():
    words = ["python", "rainbow", "miracle", "happiness", "soulmate"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return display

def hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses:
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Incorrect guesses: {incorrect_guesses}")
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            if set(word) <= guessed_letters:
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            print(f"Incorrect guess. You have {max_incorrect_guesses - incorrect_guesses} guesses left.")
        
        if incorrect_guesses == max_incorrect_guesses:
            print(f"Game over! The word was: {word}")

hangman()