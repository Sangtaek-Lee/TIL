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

def permutation(i, N, arr, temp):              # i는 시작 N 은 끝, arr = 조합할 배열, 조합된 리스트
    if len(temp) == 8:
        print(temp)
        even = 0
        odd = 0
        for i in range(0,8,2):
            odd += temp[i]
        for i in range(1,8,2):
            even += temp[i]
        a = odd * 3 + even
        if a % 10 == 0:
            rlt = odd + even
            print(rlt)
            return
        else:
            return 0
    if i >= N:
        return
    else:
        temp.append(arr[i])
        permutation(i+1, N, arr, temp)
        temp.pop()
        permutation(i+1, N, arr, temp)


for tc in range(1, T +1):
    R, C = map(int, input().split())
    arr = [input() for _ in range(R)]       # 문자열을 리스트로 받아
    arr_set = list(set(arr))                # 중복 제거
    # print(arr_set)
    binary_code = []
    hex_code = []
    for i in range(len(arr_set)):           #
        if '1' in arr_set[i]:
            binary_code = arr_set[i]
    # print(binary_code)
    # print(P.keys())
    for i in range(C):
        temp = binary_code[i:i+7]
        if temp in P.keys():
            # print(temp)
            hex_code.append(P[temp])
    # print(hex_code)
    # 이걸로 8개 짜리 조합 만들어 계산 돌려보자
    N = len(hex_code)
    temp = []
    temp_list = []
    rlt = 0
    permutation(0, N, hex_code, temp)
    #모지... 왜 만족하는 코드가 한개가 아니라 여러개 나오지
    # 문제 잘못 읽은듯 한데...
    print(rlt)

    print(f'#{tc}')
