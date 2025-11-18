import random
import os
import time

# Title Screen 
def title_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("===================================")
    print("        HANGMAN CHALLENGE 🎯")
    print("===================================")
    print("Welcome! Choose your difficulty:")
    print("1. Easy Words (8 lives)")
    print("2. Hard Words (5 lives)")
    print("===================================")
    
    choice = input("Enter 1 for Easy or 2 for Hard: ").strip()
    if choice == '1':
        start_game("Easy")
    elif choice == '2':
        start_game("Hard")
    else:
        print("Invalid choice! Try again.")
        time.sleep(1)
        title_screen()

# Word Lists 
EASY_WORDS = ["cat", "dog", "ball", "tree", "moon", "fish"]
HARD_WORDS = ["python", "galaxy", "mountain", "computer", "airplane", "volcano"]

# Start Game 
def start_game(difficulty):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Starting {difficulty} Mode...\n")

    # Variables
    if difficulty == "Easy":
        lives = 8
        word = random.choice(EASY_WORDS)
    else:
        lives = 5
        word = random.choice(HARD_WORDS)
    
    hidden_word = "_" * len(word)
    score = 0

    # Main Game Loop 
    guessed_letters = []

    while lives > 0:
        print(f"\nWord: {' '.join(hidden_word)}")
        print(f"Lives left: {lives}   Score: {score}")
        print("Guessed letters:", " ".join(guessed_letters))
        
        guess = input("Guess a letter: ").lower().strip()

        # Input validation
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter only one letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.append(guess)

        # Check guess
        if guess in word:
            print("✅ Correct!")
            score += 10
            # Reveal letters in the hidden word
            new_hidden = list(hidden_word)
            for i, letter in enumerate(word):
                if letter == guess:
                    new_hidden[i] = guess
            hidden_word = "".join(new_hidden)
        else:
            print("❌ Wrong!")
            lives -= 1
        
        # Check win condition
        if hidden_word == word:
            win_screen(word, score)
            break
    else:
        # If while loop ends naturally (no lives left)
        game_over_screen(word, score)

#  Win Screen
def win_screen(word, score):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🏆 YOU WIN! 🏆")
    print(f"The word was: {word}")
    print(f"Final Score: {score}")
    restart_game()

#  Game Over Screen
def game_over_screen(word, score):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("💀 GAME OVER, do better💀")
    print(f"The word was: {word}")
    print(f"Your Score: {score}")
    restart_game()

#  Restart Option 
def restart_game():
    print("\nWould you like to play again?")
    choice = input("Type Y to play again or N to quit: ").lower().strip()
    if choice == 'y':
        title_screen()
    else:
        print("Thanks for playing Hangman Challenge! 👋")
        time.sleep(1)
        exit()

#  Run the Game
if __name__ == "__main__":
    title_screen()
