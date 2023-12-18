import random

def words():
    word_list = [
    "apple",
    "tiger",
    "bicycle",
    "ocean",
    "pizza",
    "elephant",
    "sunshine",
    "guitar",
    "book",
    "rainbow",
    "candle",
    "butterfly",
    "moon",
    "soccer",
    "castle",
    "flower",
    "robot",
    "jellyfish",
    "puzzle",
    "chocolate",
    "dog",
    "cat",
    "house",
    "tree",
    "car",
    "train",
    "fish",
    "star",
    "banana",
    "mountain",
    "key",
    "cloud",
    "shoe",
    "chair",
    "smile",
    "clock",
    "hat",
    "bird",
    "dragon",
    "lighthouse",
    "moonlight",
    "firefly",
]
    return random.choice(word_list)

def display_word(guessed_letters, secret_words):
    display = ""
    for secret_word in secret_words:
        if secret_word in guessed_letters:
            display += secret_word
            display += ' '
        else:
            display += '_ '
    return display

print("Welcome to Word Guessing Game")

secret_words = words()
guessed_letters = []
attempt = 5

while attempt > 0:
    print(f"Word: {display_word(guessed_letters, secret_words)}")

    guess = input("Guess The Letter: ").lower()

    if guess.isalpha() and len(guess) == 1:
        if guess in secret_words:
            print("Great You Choose Correct Letter")
            guessed_letters.append(guess)

        elif guess in guessed_letters:
            print("You Already Choosed This Letter")
            print(guessed_letters)

        else:
            print("You Guessed Incorrect")
            attempt -= 1

    else:
        print("Please enter a valid single letter")

    if set(guessed_letters) == set(secret_words):
        print("Congratulations ! You Guessed it Correct")
        break

    print(f"Attempt Left {attempt}\n")


    if attempt == 5:
        print('    +------+')
        print('    |      |')
        print('    |      |')
        print('           |')
        print('           |')
        print('           |')
        print('           |')
        print('==============\n')


    elif attempt == 4:
        print('    +------+')
        print('    |      |')
        print('    |      |')
        print('    O      |')
        print('           |')
        print('           |')
        print('           |')
        print('==============\n')


    elif attempt == 3:
        print('    +------+')
        print('    |      |')
        print('    |      |')
        print('    O      |')
        print('   / \\     |')
        print('           |')
        print('           |')
        print('==============\n')


    elif attempt == 2:
        print('    +------+')
        print('    |      |')
        print('    |      |')
        print('    O      |')
        print('   /|\\     |')
        print('           |')
        print('           |')
        print('==============\n')


    elif attempt == 1:
        print('    +------+')
        print('    |      |')
        print('    |      |')
        print('    O      |')
        print('   /|\\     |')
        print('   /       |')
        print('           |')
        print('==============\n')




    elif attempt == 0:
        
        print('    +------+')
        print('    |      |')
        print('    |      |')
        print('    O      |')
        print('   /|\\     |')
        print('   / \\     |')
        print('           |')
        print('==============')
        print("\n")
        print("No Attempt Left, You Lost the Game")
        print(f"The Word was {secret_words}")