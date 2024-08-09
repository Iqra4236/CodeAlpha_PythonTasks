import random

class HangmanGame:
    def __init__(self, words, max_incorrect_guesses=6):
        
        """
        Initialize the Hangman game with a list of words and maximum incorrect guesses.
        """

        self.words = words
        self.max_incorrect_guesses = max_incorrect_guesses
        self.hangman_stages = [
           
            """
               ------
               |    |
               |
               |
               |
               |
            --------
            """,
            """
               ------
               |    |
               |    O
               |
               |
               |
            --------
            """,
            """
               ------
               |    |
               |    O
               |    |
               |
               |
            --------
            """,
            """
               ------
               |    |
               |    O
               |   /|
               |
               |
            --------
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |
               |
            --------
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |   /
               |
            --------
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |   / \\
               |
            --------
            """
        ]

        self.reset_game()
    
    def reset_game(self):
        
        """
        Reset the game to start a new round.
        """

        self.word = random.choice(self.words)  # Randomly choose a word from the list
        self.guessed_letters = set()           # Set of letters guessed by the player
        self.incorrect_guesses = 0             # Number of incorrect guesses
    
    def get_masked_word(self):
        
        """
        Return the current state of the word being guessed, with unguessed letters as underscores.
        """

        return ''.join([c if c in self.guessed_letters else '_' for c in self.word])
    
    def is_word_guessed(self):
        
        """
        Check if the whole word has been guessed.
        """

        return all(c in self.guessed_letters for c in self.word)
    
    def guess_letter(self, letter):
        
        """
        Process a guessed letter.
        """

        if letter in self.word:
            self.guessed_letters.add(letter)
            if self.is_word_guessed():
                return True, f"Congratulations! You guessed the word: {self.word}"
            return False, "Correct guess!"
        else:
            self.incorrect_guesses += 1
            if self.incorrect_guesses >= self.max_incorrect_guesses:
                return True, f"Sorry! You've been hanged. The word was: {self.word}"
            return False, f"Incorrect! You have {self.max_incorrect_guesses - self.incorrect_guesses} guesses left."
    
    def play(self):
        
        """
        Main game loop.
        """
        
        print("Welcome to Hangman!")
        while self.incorrect_guesses < self.max_incorrect_guesses:
            print(self.hangman_stages[self.incorrect_guesses])
            print("Word: " + self.get_masked_word())
            guess = input("Guess a letter: ").lower()
            
            # Validate the input
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please guess a single letter.")
                continue
            
            # Process the guessed letter
            game_over, message = self.guess_letter(guess)
            print(message)
            
            if game_over:
                print(self.hangman_stages[self.incorrect_guesses])
                break

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'yes':
            self.reset_game()
            self.play()
        else:
            print("Thanks for playing Hangman!")

if __name__ == "__main__":
    words = ["programming", "java", "hangman", "challenge", "game"]
    game = HangmanGame(words)
    game.play()