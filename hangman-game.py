import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# The random module is imported and ascii hangman art is created

from hangman_words import word_list
# The word list is imported from the hang_man module / file

end_of_game = False
chosen_word = random.choice(word_list)
lives = 6
blanks = []

# The end_of_game variable is initialized to False
# A random word is selected from the word_list using random.choice() and saved in the chosen_word variable
# The lives variable is set to 6, representing the initial number of lives
# An empty list called blanks is created to store the blanks

for letter in chosen_word:
  blanks.append("_")
  
# Fills the blanks list with underscores "_" for each letter in the chosen_word using a for loop.

print(f"{' '.join(blanks)}")
# Prints blanks to console as joined strings : _ _ instead of individual strings in a list : "_" "_"

while not end_of_game:
  guess = input("Guess a letter: ").lower()
  if guess in chosen_word:
    for i in range(len(chosen_word)):
      letter = chosen_word[i]
      if letter == guess:
        blanks[i] = guess
  else:
    lives -= 1
    print(f"Lives left : {lives}")
    if lives == 0:
      end_of_game = True
      print("You lose.")
  print(f"{' '.join(blanks)}")

'''
The game loop starts with a while loop that continues until end_of_game becomes True (line 83)
Inside the loop, the player is asked to guess a letter using input(), and the guess is converted to lowercase (line 84)
The code checks if the guessed letter is in the chosen_word. If it is, the blanks list is updated with the guessed letter using a for loop (lines 85-89)

If the guessed letter is not in the chosen_word, the lives variable is decremented by 1, and the remaining number of lives is printed (lines 90-92)
If the lives variable reaches 0, end_of_game is set to True, and the losing message is printed (lines 93-95)
The updated state of the blanks is printed using print(f"{' '.join(blanks)}") (line 96)
'''

  if "_" not in blanks:
    end_of_game = True
    print("You Win.")

# Checks if all the letters have been guessed correctly by checking if there are no more underscores "_" in the blanks list.
# If all letters are guessed, end_of_game is set to True, and the winning message is printed.
  
  print(stages[lives])
# Finally, the corresponding hangman stage based on the remaining lives is printed
