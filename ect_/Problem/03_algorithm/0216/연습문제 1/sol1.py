import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    word = input()

    word_rev = word[::-1]

    print(f'#{tc}', word_rev)

