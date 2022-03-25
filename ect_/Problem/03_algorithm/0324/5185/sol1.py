import sys
sys.stdin = open('input.txt')

T = int(input())

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

for tc in range(1, T + 1):
    N, hex = input().split()
    decimal = hextodec(hex)
    binary = dectobin(decimal)
    print(f'#{tc} {binary}')