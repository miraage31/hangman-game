import random
import hangman_art, hangman_words

lives = 6

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"


game_over = False
correct_letters = []

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if len(guess) > 1:
        print("Please input 1 character only.")
    else:
        if guess in correct_letters:
            print(f"You have already guessed {guess}, pick another letter")

        display = ""

        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        print("Word to guess: " + display)

        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            if lives == 0:
                game_over = True
                print(f"It was: {chosen_word}! YOU LOSE")

        if "_" not in display:
            game_over = True
            print("****************************YOU WIN****************************")

        print(hangman_art.stages[lives])
