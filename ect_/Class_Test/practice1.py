# x = 3+4j

# print(x.real)
# print(x.imag)



#while
# def is_pal_while(word):
#     word_rev = word[::-1]
#     for i in range(len(word)):
#         if word[i] != word_rev[i]:
#             return False
#     return True

# def is_pal_while(word):
#     while len(word) > 1:    
#         if word[0] == word[-1]:
#             word = word[1:-1]
#         else:
#             return False
#     return True    
    


# def is_pal_recursive(word):
#     if len(word) <= 1:
#         return True
#     elif word[0] == word[-1]:
#         return is_pal_recursive(word[1:-1])
#     else:
#         return False

# print(is_pal_recursive('tomato'))
# print(is_pal_recursive('racecar'))
# print(is_pal_recursive('azza'))