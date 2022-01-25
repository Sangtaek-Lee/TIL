def duplicated_letters(word):
    alphabet_list = ' '.join(word).split(' ')
    dupl_list = []
    for alphabet in set(alphabet_list):
        if alphabet_list.count(alphabet) >= 2:
            dupl_list.append(alphabet)
    return dupl_list

print(duplicated_letters('apple'))
print(duplicated_letters('banana'))