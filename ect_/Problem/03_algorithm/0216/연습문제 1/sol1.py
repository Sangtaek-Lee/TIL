import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    word = input()              # input을 string으로 받아와

    word_rev = word[::-1]       # 슬라이싱으로 역배열 해준다.

    print(f'#{tc}', word_rev)

