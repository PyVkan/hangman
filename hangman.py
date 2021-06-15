import random

print("H A N G M A N")
secret_word = random.choice(["python", "java", "kotlin", "javascript"])
hint = secret_word[0:3] + "-" * (len(secret_word) - 3)

temp = list('-' * len(secret_word))
temp_letters = list()


def guess(letter):
    statement = 0
    if len(letter) != 1:
        statement = 1
    elif not letter.islower():
        statement = 2
    elif letter in temp_letters:
        statement = 3
    else:
        temp_letters.append(letter)
        for index in range(len(secret_word)):
            if secret_word[index] == letter:
                temp[index] = letter
                statement = None

    return statement


def play():
    lives = 8
    while lives > 0:
        if '-' not in temp:
            break
        print()
        print("".join(temp))
        print("Input a letter: >")
        result = guess(input())
        if result == 0:
            lives -= 1
            print("That letter doesn't appear in the word")
        elif result == 1:
            print("You should input a single letter")
        elif result == 2:
            print("Please enter a lowercase English letter")
        elif result == 3:
            print("You've already guessed this letter")

    if '-' in temp:
        print('You lost!')
    else:
        print()
        print("".join(temp))
        print('You guessed the word!\nYou survived!')


print('Type "play" to play the game, "exit" to quit:')
choice = input()
if choice == 'play':
    play()
