
import random
import hangman_words as hw
import hangman_art as ah
import os

chosen_word = random.choice(hw.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
already_guessed = []



print (ah.logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear = lambda: os.system('clear')
    clear()
    
    already_guessed.append(guess)
    length_ag = len(already_guessed)
    sum = 0
    for position in range(length_ag):
        guessed = already_guessed[position]
        if guessed ==guess:
            sum += 1
            if sum >= 2:
                print (f"{guess} already guessed")
    
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    
    if guess not in chosen_word:
        print (f"{guess} is not right.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You won.")

    print(ah.stages[lives])