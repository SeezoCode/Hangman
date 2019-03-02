from All_words import *
import collections


def len_word():
    x = 1
    while x == 1:
        try:
            word_len = int(input("How long is your word? \n"))
            x += 1
        except(ValueError):
            pass
    return word_len


def ask(a, mn, word_e_ask):    # Is there...
    x = 1
    while x == 1:
        try:
            word_e_ask = str(input(a).lower())
            try:
                mn = int(word_e_ask)
                break
            finally:
                x += 1
                break
        except ValueError:
            pass
    return word_e_ask, mn


def wh_place(num2,pos):
    if num2 > 0 and pos == 0:
        # pos = int(input("On which place? \n"))
        x = 1
        while x == 1:
            try:
                pos = int(input("On which place? \n"))
                x += 1
            except ValueError:
                pass
    else:
        pos = 0
    return pos - 1

def sort(word_list_new, word_len, pos, asking_letter, num2, word_list, word_list_b, used, lose_rules):
    for i in word_list:
        if len(i) == word_len and i[pos] == asking_letter and num2 != 0:  # --With letter
            word_list_b.append(i)
            word_list_new += i
            numx = 1
        elif len(i) == word_len and i.count(asking_letter) == 0 and num2 == 0:  # --No letter
            word_list_b.append(i)
            word_list_new += i
            numx = 0
        else:
            continue
    for u in used:
        # replaces used characters with ""
        word_list_new = word_list_new.replace(u, "")
    try:
        if numx == 0:
            lose_rules += 1
    except(UnboundLocalError): pass
    return word_list_new, word_len, pos, asking_letter, num2, word_list, word_list_b, used, lose_rules
