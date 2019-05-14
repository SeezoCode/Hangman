import re
with open('added_words_log', "r") as f:
    logs = f.read()

def words():
    word_list = []
    with open("10k most used words.txt", "r") as words:
        for line in words:
            word_list.append(line.replace("\n",""))
        return word_list
