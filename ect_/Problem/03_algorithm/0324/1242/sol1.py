import sys
sys.stdin = open('input.txt')

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

dic_htod = {
    '0' : 0,
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    'A' : 10,
    'B' : 11,
    'C' : 12,
    'D' : 13,
    'E' : 14,
    'F' : 15,
}

def hextodec(hex):
    rlt = 0
    for i in range(1, len(hex)+1):
        rlt += dic_htod[hex[-i]] * (16**(i-1))
    return rlt

def dectobin(dec):
    binary = ''
    while dec != 0:
        mod = dec % 2
        dec = dec // 2
        if mod == 0:
            binary = '0' + binary
        else:
            binary = '1' + binary
    if len(binary) % 4 != 0:
        while len(binary) % 4 != 0:
            binary = '0' + binary
    return binary

T = int(input())

for tc in range(1, T + 1):
    R, C = map(int, input().split())
    arr = [input() for _ in range(R)]       # 문자열을 리스트로 받아
    arr_set = list(set(arr))
    print(arr_set)
    for i in range(len(arr_set)):
        for j in range(len(arr_set[i])):
            arr_set[i][j]


    print(f'#{tc}')

# a = '328D1AF6E4C9BB'
# rlt = 0
# for i in range(len(a)):
#     rlt += dic_htod[a[i]] * (16**(len(a)-i-1))
# print(rlt)
# 1    D    B    1    7    6    C    5    8    8    D    2    6    E    C
# 0111 0110 1100 0101 1101 1011 0001 0110 0010 0011 0100 1001 1010 1110 1100
#
# 0111101
#
# 0011 0010 1101 0001 0111 0111

# 1DB176C588D26EC

