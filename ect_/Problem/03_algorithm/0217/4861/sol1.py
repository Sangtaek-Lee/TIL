import sys

sys.stdin = open('input.txt')

T = int(input())

# 각
def circular_word(colums, word):
    mid = colums // 2
    word_right = word[:mid]
    word_left = word[colums:mid-1:-1]
    if word_right == word_left:
        return word

for tc in range(1, T + 1):
    row, col = map(int, input().split())
    words_list = [input() for _ in range(row)]      # 행을 문자열로 리스트에 추가
    # 열을 문자열로 바꾸어 리스트에 추가
    for i in range(col):
        temp_str = ''                               # 일시적인 빈 문자열을 만들어
        for j in range(row):
            temp_str = temp_str + words_list[j][i]  # 0,0 ~ 9,0 알파벳 추가
        words_list = words_list + [temp_str]        # 문자열 리스트에 추가



    for i in range(row+col):
        temp_rlt = circular_word(col, words_list[i])
        if temp_rlt != None:
            rlt = temp_rlt
            break


    print(f'#{tc}', rlt)

