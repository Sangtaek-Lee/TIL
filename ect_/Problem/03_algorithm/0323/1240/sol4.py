import sys
sys.stdin = open('input.txt')

T = int(input())
# 0 ~ 9까지의 수와 대응하는 이진 코드
P = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

for tc in range(1, T +1):
    R, C = map(int, input().split())
    arr = [input() for _ in range(R)]       # 문자열을 리스트로 받아
    arr_set = list(set(arr))                # 중복 제거
    print(arr_set)
    for i in range(len(arr_set)):
        for j in range(len(arr_set[i])):
            if arr_set[i][j] == 1:
                arr = arr[i]
                break
    print(arr)
    print(f'#{tc}')
