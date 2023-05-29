## Hangman Game in Python.

import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo



chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


print(logo)
print(f"\n\n\t\t\t\t\t\t\t\t\t\tRemaining Life : {lives}")

# print(f'The solution is {chosen_word}.')

#Create blank list to store each letter.
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        print(f"\t\t\t\t\t\t\t\t\t\tRemaining life : {lives}")
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"\n The Word was : {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("Yay! You won the game, Winner Winner Chicken Dinner.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])