def check_win(secret_word, old_letters_guessed):
    """Checks if the user has guessed the secret word.
        :param secret_word: secret word
        :param old_letters_guessed: letters have been guessed before
        :type secret_word: str
        :type old_letters_guessed: list
        :return: True of the secret word is guessed, otherwise False
        :rtype: True/FalseC
        """
    result = show_hidden_word(secret_word, old_letters_guessed)
    if '_' in result:
        return False
    return True


def check_valid_input(letter_guessed, old_letters_guessed):
    """checks if the letter has not been guessed before and is an alphabet and isn't more than one character.
            :param letter_guessed: letter has been guessed
            :param old_letters_guessed: old letters have been guessed
            :type letter_guessed: str
            :type old_letters_guessed: list
            :return: True if the letter is valid, otherwise False
            :rtype: True/False
            """
    if (len(letter_guessed) != 1 or (not letter_guessed.isalpha()) or letter_guessed in old_letters_guessed):
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """adds the guessed letter to the list of old letters have been guessed if it's valid,
     otherwise print X and the old letters guessed.
                :param letter_guessed: letter has been guessed
                :param old_letters_guessed: old letters have been guessed
                :type letter_guessed: str
                :type old_letters_guessed: list
                :return: True if the letter is valid after adding to the letters list, otherwise prints the list of the
                old letters
                :rtype: True/str
                """
    if (check_valid_input(letter_guessed, old_letters_guessed)):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X\nSelected an already existing character:\n")
        print(' -> '.join(sorted(old_letters_guessed)))

def choose_word(file_path, index):
    """counts the number of different words in the given file.
                :param file_path: given file path
                :param index: index for the returned word of the given file
                :type file_path: str
                :type index: int
                :return: the number of different names in the given file
                 and the word which is located at the given index
                :rtype: tuple
                """
    f1 = open(file_path, 'r')
    str = []
    counter = 0
    read = f1.read().split(' ')

    for i in read:
        if i not in str:
            str.append(i)
            counter += 1
    f1.close()
    return (counter, read[index % len(read) - 1])

def show_hidden_word(secret_word, old_letters_guessed):
    """returns the secret word composed of small letters and bottom lines.
                :param secret_word: the secret word
                :param old_letters_guessed: old letter have been guessed
                :type secret_word: str
                :type old_letters_guessed: list
                :return: str which shows the secret word by small letters and bottom lines
                :rtype: str
                """
    str = ''
    for i in secret_word:
        if (i in old_letters_guessed):
            str += i + ' '
        else:
            str += '_ '
    return str

def print_hangman(num_of_tries):
    """prints a picture of the hangman after each wrong guess in a more advanced situation.
                :param num_of_tries: the number of the wrong answer/try
                :type num_of_tries: int
                :return: a picture composed of a small signs denoting to an appropriate situation of the hangman
                :rtype: str
                """
    str1 = 'x-------x'
    str2 = str1 + '\n|' * 5
    str3 = str1 + """
|       |
|       0
|        
|
|"""
    str4 = str1 + """
|       |
|       0
|
|
|"""
    str5 = str1 + """
|       |
|       0
|      /|\\
|       
|"""
    str6 = str1 + """
|       |
|       0
|      /|\\
|      / 
|"""
    str7 = str1 + """
|       |
|       0
|      /|\\
|      / \\ 
|"""

    HANGMAN_PHOTOS = {1: str1, 2: str2, 3: str3, 4: str4, 5: str5, 6: str6, 7: str7}
    print(HANGMAN_PHOTOS[num_of_tries + 1])

import os.path
from os import path

def main():
    print(""" _    _
| |  | |
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |
                    |___/
6
""")
    f = input('Enter a file path that contains a string/list of strings: ')
    while not path.exists(f):
        print('file does\'nt exist! Try again')
        f = input('Enter file path: ')

    index = int(input('Enter index (>=1) to reach a string in a specific position: '))
    while index < 1:
        print('Index is illegal! Try again')
        index = int(input('Enter index: '))

    secret_word = choose_word(f,index)[1]
    print('\nLet\'s start!\n')
    print_hangman(0)
    old_letters_guessed = []
    print(show_hidden_word(secret_word, old_letters_guessed) + '\n')
    MAX_TRIES = 0

    while MAX_TRIES != 6 and not check_win(secret_word, old_letters_guessed):
        letter = input('Guess a letter: ')

        # the letter is valid and not in secret word
        if ((letter not in secret_word) and (letter not in old_letters_guessed)):
            MAX_TRIES += 1
            print(':(')
            print_hangman(MAX_TRIES)
            old_letters_guessed.append(letter)
            print('\n' + show_hidden_word(secret_word, old_letters_guessed))

        elif try_update_letter_guessed(letter, old_letters_guessed):
            print(show_hidden_word(secret_word, old_letters_guessed))

    if(MAX_TRIES == 6):
        print('YOU LOST')
    else:
        print('YOU WON')


if __name__ == '__main__':
    main()
