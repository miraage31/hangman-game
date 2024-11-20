import random, hangman_art, hangman_words

lives = 6

chosen_word = random.choice(hangman_words.word_list)

# print(f"Psst, the solution is {chosen_word}")
print("Welcome to")
print(f"{hangman_art.logo}")
print(f"{hangman_art.stages[lives]}")

display = []

for _ in chosen_word:
    display.append("_")
print(display)

end_of_game = False
while not end_of_game:
    valid_input = False
    safe = False
    while valid_input == False:

        guess = input("Input a letter: ").lower()        
        if guess in display: 
            print(f"You've already guessed {guess}")

        print(f"{hangman_art.stages[lives]}")
        if len(guess) == 1:
            valid_input = True
        else:
            print("Please input only one letter.")

    for position in range(len(chosen_word)):
        if guess == chosen_word[position]:
            display[position] = guess
            safe = True
    if safe == False:
        lives -= 1
        print("Wrong letter. You lose a life.")
        print(f"{hangman_art.stages[lives]}")
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")
    elif lives == 0:
        end_of_game = True
        print("You lose")
        print(f"The answer is {chosen_word}!")