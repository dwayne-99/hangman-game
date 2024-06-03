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

from hangman_words import word_list
end_of_game = False
chosen_word = random.choice(word_list)
lives = 6
blanks = []

for letter in chosen_word:
  blanks.append("_")
print(f"{' '.join(blanks)}")

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

  if "_" not in blanks:
    end_of_game = True
    print("You Win.")

  print(stages[lives])