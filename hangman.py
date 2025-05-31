import random

def load_words():
    try:
        with open("words.txt", "r") as f:
            words = f.read().splitlines()
    except FileNotFoundError:
        words = ['banana','rocket','giraffe','mountain','keyboard','internet','puzzle','adventure','galaxy','mystery']
    return words

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
              ===
        """,
        
           -----
           |   |
           O   |
          /|\  |
          /    |
              ===
        """,
        """
           -----
           |   |
           O   |
          /|\  |
               |
              ===
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
              ===
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
              ===
        """,
        """
           -----
           |   |
           O   |
               |
               |
              ===
        """,
        """
           -----
           |   |
               |
               |
               |
              ===
        """
    ]
    return stages[tries]

def play_game():
    words = load_words()
    word = random.choice(words).lower()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6

    print("Welcome to Hangman!")
    print(display_hangman(tries))

    while tries > 0 and word_letters:
        print(f"\nWord: {' '.join([letter if letter in guessed_letters else '_' for letter in word])}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            word_letters.remove(guess)
            print("Good guess!")
        else:
            tries -= 1
            print("Incorrect guess.")
            print(display_hangman(tries))

    if not word_letters:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game Over! The word was: {word}")

def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()
