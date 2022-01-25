def low_and_up(word):
    alphabet_list = ' '.join(word).split(' ')
    chg_word = ''
    for i in range(len(alphabet_list)):
        if i % 2 == 1:
            alphabet_list[i] = word[i].upper()
        chg_word += alphabet_list[i]
    return chg_word

low_and_up('apple')
low_and_up('banana')
print(low_and_up('apple'))
print(low_and_up('banana'))