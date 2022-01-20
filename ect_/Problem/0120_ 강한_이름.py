'''문자열 2개를 전달 받아 두 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 비교하
여 더 큰 합을 가진 문자열을 반환하는 get_strong_word 함수를 작성하시오.'''


def get_strong_word(words_1, words_2):
    words_list = [words_1, words_2]
    total_list = []
    for j in words_list:                
        number_sum = 0
        for i in range(0,len(j)):
            number = ord(j[i])
            number_sum += number
        total_list.append(number_sum)
    if total_list[0] > total_list[1]:
        return words_1
    else:
        return words_2

print(get_strong_word('z', 'a'))
print(get_strong_word('tom', 'john'))





# get_strong_word('z', 'a')
# get_strong_word('tom', 'john')
