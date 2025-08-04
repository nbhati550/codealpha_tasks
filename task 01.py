import random

def play_hangman():
    """
    A simple text-based Hangman game.
    The player guesses a word one letter at a time.
    """
    word_list = ["python", "hangman", "computer", "program", "keyboard"]
    chosen_word = random.choice(word_list)
    word_display = ["_" for _ in chosen_word]
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("The word has", len(chosen_word), "letters.")
    print(" ".join(word_display))

    while incorrect_guesses < max_incorrect_guesses and "_" in word_display:
        guess = input("\nGuess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in chosen_word:
            print("Good guess!")
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    word_display[i] = guess
        else:
            print("Incorrect guess!")
            incorrect_guesses += 1
            print(f"You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses remaining.")
        
        print(" ".join(word_display))
    
    # Game conclusion
    if "_" not in word_display:
        print("\nCongratulations! You won! The word was", chosen_word)
    else:
        print("\nGame over! You ran out of guesses. The word was", chosen_word)

if __name__ == "__main__":
    play_hangman()