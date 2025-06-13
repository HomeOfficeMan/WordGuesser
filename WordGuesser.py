import random

GAME_TITLE = "Cooles Spiel"
word_Bank = []
letters_Guessed = []
letters_Wrong = []
game_Over = False
word_Found = False

#game preparation
with open("words.txt") as word_List:
    for word in word_List:
        word_Bank.append(word.strip())
print("Welcome to:", GAME_TITLE) 

def begin_game():
    global word_To_Guess
    global word_Found
    word_Found = False

    letters_Guessed.clear()
    letters_Wrong.clear()
    word_To_Guess = random.choice(word_Bank)
    
    print("The word to guess has", len(word_To_Guess), "letters.")
    print("You can guess letters or the whole word.")
    print("You have 6 wrong guesses before you lose.")
    print("Let's start!")
    print ("The word to guess is:", "_" * len(word_To_Guess))

def process_guess(guess):
    if len(guess) == 1:  
        if guess in letters_Guessed or guess in letters_Wrong:
            print("You already guessed that letter.")
        elif guess in word_To_Guess:
            print('Good' if guess in word_To_Guess else 'Wrong', 'guess:', guess)
            letters_Guessed.append(guess)
        else:
            letters_Wrong.append(guess)
            print("Wrong guess!")
        
        current_state = ''.join([letter if letter in letters_Guessed else '_' for letter in word_To_Guess])
        print("Current word:", current_state)

    elif len(guess) == len(word_To_Guess):  
        if guess == word_To_Guess:
            global word_Found
            word_Found = True
            letters_Guessed.extend(set(word_To_Guess))
        else:
            print("Wrong guess! The word was not", guess)
            letters_Wrong.append(guess)
    else:
        print("Invalid input. Please enter a single letter or the whole word.")

def end_game():  
    print("Game Over!")

    if set(word_To_Guess).issubset(set(letters_Guessed)):
        print("Congratulations! You've guessed the word:", word_To_Guess)
    else:
        print("Sorry, you've used all your guesses. The word was:", word_To_Guess)
       
    restart = input("Want to try again? \"y\" to continue. \"n\" to quit.")
    if(restart.lower() == "y"):            
        begin_game()
    else:
        print("Thanks for playing!")
        global game_Over 
        game_Over = True

## Main game loop
begin_game()
while not game_Over:
    guess = input("Please enter a letter or the whole word: ").strip().lower()
    process_guess(guess)    
    if(len(letters_Wrong) >= 6 or word_Found):
        end_game()
    
    
    