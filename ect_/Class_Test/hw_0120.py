#1
# def get_secret_word(x):
#     y = ''
#     for i in x:
#         y += chr(i)
#     return y

# print(get_secret_word([83, 65, 65, 65, 65]))

#2
# def get_secret_number(x):
#     word = 0
#     for i in range(len(x)):
#         word += ord(x[i])
#     return word

# print(get_secret_number('tom'))

#3
def get_strong_word(*arg):
    word_sum_list = []
    for i in arg:       
        word_sum = 0
        for j in range(len(i)):
            word_sum += ord(i[j])
        word_sum_list.append(word_sum)
    
    if word_sum_list[0] > word_sum_list[1]:
        return arg[0]
    else:
        return arg[1]
    




print(get_strong_word('z', 'a'))
print(get_strong_word('tom', 'john'))