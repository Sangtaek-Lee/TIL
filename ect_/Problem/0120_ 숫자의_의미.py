'''정수로 이루어진 list를 전달 받아, 각 정수에 대응되는 아스키 문자를 이어붙인
문자열을 반환하는 get_secret_word 함수를 작성하시오. 단, list는 65이상 90이하
그리고 97이상 122이하의 정수로만 구성되어 있다.'''

# for i in range(65,123):
#     print(chr(i))           # chr => ascii 코드 변환



# def get_secret_word(args):
#     words = []
#     for arg in args:
#         word = chr(arg)
#         # print(word)
#         words.append(word)
#     return words
# print(get_secret_word([83, 115, 65, 102, 89]))

# a = []
# for i in list([1, 2, 3 ,4, 5]):
#     a.append(i)
#     print(i)
# print(a)


# get_secret_word([83, 115, 65, 102, 89])

def get_secret_word(args):
    words = ''
    for arg in args:
        word = chr(arg)
        words += word
    return words
print(get_secret_word([83, 115, 65, 102, 89]))