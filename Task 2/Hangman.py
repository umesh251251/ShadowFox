import random


word_list = [
    ("apple", "A common fruit, often keeps doctor away."),
    ("tiger", "A large wild cat with stripes."),
    ("plane", "Flies in the sky, transports people."),
    ("chair", "You sit on it."),
    ("brain", "Controls your thoughts and body."),
    ("river", "A natural flowing watercourse."),
    ("music", "What you listen to with headphones."),
    ("train", "Runs on tracks, transports many."),
    ("clock", "Tells you the time."),
    ("beach", "Sandy shore beside the sea."),
    ("bread", "Used to make sandwiches."),
    ("knife", "Used for cutting."),
    ("house", "Place where you live."),
    ("snake", "A slithering reptile."),
    ("cloud", "White and fluffy in the sky."),
]

images = ["""
 ____
|/   |
|   (_)
|   /|\\
|    |
|   | |
|       dead
|_____   
""","""
 ____
|/   |
|   (_)
|   \\|/
|    |
|   / \\
|
|_____
""", """
 ____
|/   |
|   (_)
|   \\|/
|    |
|   / 
|
|_____
""","""
 ____
|/   |
|   (_)
|   \\|/
|    |
|    
|
|_____
""","""
 ____
|/   |
|   (_)
|   \\|
|    |
|    
|
|_____
""","""
 ____
|/   |
|   (_)
|    |
|    |    
|    
|
|_____
""","""
 ____
|/   |
|   (_)
|    
|    
|    
|
|_____
""",""" 
____
|/   |
|   
|    
|    
|    
|
|_____
"""][::-1]

maxlives = len(images) - 1

def play_hangman():
    word, hint = random.choice(word_list)
    lives = maxlives
    blanks = ['_' for _ in word]
    guessed_letters = set()
    gameover = False

    print("\nWELCOME TO HANGMAN")
    print(f"\nHint: {hint}")
    print(f"The word has {len(word)} letters.\n")

    while not gameover:
        print(images[maxlives - lives])
        print("Word:", " ".join(blanks))
        print("Guessed letters:", ", ".join(sorted(guessed_letters)))
        print(f"Lives remaining: {lives}\n")

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Enter a single letter.\n")
            continue
        if guess in guessed_letters:
            print("Letter already guessed.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    blanks[i] = guess
            print("Correct!\n")
        else:
            lives -= 1
            print("Wrong guess!\n")

        if '_' not in blanks:
            gameover = True
            print("\nYOU WIN! The word was:", word)
        elif lives == 0:
            gameover = True
            print(images[maxlives])
            print("\nGAME OVER! The word was:", word)

while True:
    play_hangman()
    again = input("\nPlay again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing Hangman!")
        break