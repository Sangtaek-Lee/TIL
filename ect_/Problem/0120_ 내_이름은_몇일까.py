'''문자열을 전달 받아 해당 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 반환하는
get_secret_number 함수를 작성하시오. 단, 문자열은 A~Z, a~z로만 구성되어 있다.
'''

def get_secret_number(words):
    total = 0
    for i in range(0,len(words)):
        word = words[i]
        total += ord(word)          # ord => ascii를 숫자로
    return total

print(get_secret_number('tom'))

