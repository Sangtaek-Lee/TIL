'''문자열을 전달 받아 해당 문자열의 정중앙 문자를 반환하는 get_middle_char 함수를
작성하시오. 단, 문자열의 길이가 짝수일 경우에는 정중앙 문자 2개를 반환한다.
'''
words = input()
n = len(words)
def get_middle_char(x):
    if n % 2 == 1:
        return x[n//2]
    else:
        i = int((n/2)-1)
        return x[i:i+2]
print(get_middle_char(words))
