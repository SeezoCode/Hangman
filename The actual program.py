# Hangman game by Filip Hostinsky

"""
This program works with a list of x words. You will choose a word, that will be guessed as follows:
1) the program asks the user to enter the len of the word
2) the program asks for e in the word and it's position
3) the program will repeat step 2 with other letters while excluding the words that have not those letters
4) the program will eventually guess the word with a success and loss counter

feature changelog:
    things to include:
        more idiot proof inputs     done
        GUI
        better design


word_list_new           string of word_list without asked
"""

import re
import collections
from typing import Any
from All_words import *
from New_Defs import *
import json
word_list, mystr = words()
check = str(input("Please check if your word is in the library: \n"))
s = ""
with open("added_words_log", "r+") as f:
    if 1 >= word_list.count(check):
        c = f.read()
        c = re.sub("[^\w]", " ", c).split()
        c = set(c)
        for i in c:
            s += i + " "
        with open("added_words_log", "w") as file:
            file.write(s + check + " ")

if 0 != word_list.count(check):
    print("The word is in the library, the length is {}".format(len(check)))
else:
    print("The word has been added to the library, the length is {}".format(len(check)))
    word_list.append(check)


word_list, word_list_b, lose_rules, numx = sorted(word_list), "", 0, 0
word_len = len_word()

# Now the program will ask for E in the word and it's place   ----    E
used, ff, uu, = "", "e", 0
while 1 == 1:
    if uu != 0:
        word_list = word_list_b
    uu += 1
    asking_letter = ff[0]
    a = "Is there {} in the word? [y/n] \n".format(asking_letter)

    pos, mn, x, word_e_ask = 0, 0, 1, ""
    # Asks for {} in the word
    word_e_ask, mn = ask(a, mn, word_e_ask)
    # -----------Ask E
    num2 = 0
    if word_e_ask == "y":
        num2 = 1
    # -----------Ask place;
    if mn == 0:
        pos = wh_place(num2, pos)
    else:
        pos = mn - 1
        num2 = 1

    print("---------- ---------- ---------- ---------- \nLet's continue:  ")
    most_com, position_most_c_letter = "", ""
    used = used + " " + asking_letter
    print("Asked were:", used)

    print("asking letter was:", asking_letter)
    word_list_new, word_list_b = "", []

    #SORTING
    word_list_new, word_len, pos, asking_letter, num2, word_list, word_listb, used, lose_rules = sort(word_list_new,
            word_len, pos, asking_letter, num2,word_list, word_list_b, used, lose_rules)

    print("Possible words:", word_listb)
    if lose_rules < 100:
        if lose_rules < 3:
            print("Score: {}/3".format(lose_rules))
        elif lose_rules:
            print("I have lost")
            lose_rules += 100
    print("\n")
    if len(word_list_b) == 1:
        print(word_listb[0], "- Your word has been discovered!")
        break

    try:
        ff = collections.Counter(word_list_new).most_common(1)[0]
    except(ValueError, IndexError):
        print("Your word has not been discovered.")
        break

    print(ff)
    print("The most common letter is {}".format(ff[0]))

input("Please press ENTER to exit   ")