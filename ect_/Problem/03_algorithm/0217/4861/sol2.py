import sys

sys.stdin = open('input.txt')

T = int(input())

# 회문 구하기
def circular_word(row, colums, word):
    for i in range(row - colums +1 ):
        mid = colums // 2                           # 슬라이싱으로 회문을 반으로 잘라
        word_right = word[i:mid+i]
        if colums % 2 != 0:                         # 회문길이가 짝수일때랑 홀수일때를 나누어 회문을 구한다.
            word_left = word[colums+i-1:mid+i:-1]   # 오른쪽 반은 역배열 시킨다.
        else:
            word_left = word[colums+i-1:mid+i-1:-1]
        if word_right == word_left:                 # 같으면 리턴한다.
            return word[i:]

for tc in range(1, T + 1):
    row, col = map(int, input().split())
    words_list = [input() for _ in range(row)]      # 행을 리스트에 추가
    # 열을 문자로 바꾸어 리스트에 추가
    for i in range(col):
        temp_str = ''                               # 일시적인 빈 문자열을 만들어
        for j in range(row):
            temp_str = temp_str + words_list[j][i]  # 0,0 ~ 9,0 알파벳 추가
        words_list = words_list + [temp_str]        # 문자열 리스트에 추가

    # 출력
    for i in range(row+col):
        temp_rlt = circular_word(row, col, words_list[i])
        if temp_rlt != None:
            rlt = temp_rlt
            break
        rlt = 0


    print(f'#{tc}', rlt)

