import sys
sys.stdin = open('input.txt')

T = int(input())

def check(card_list):           # run, triplet 검사
    global rlt
    cnt_list = [0] * 10         # 카드 개수 cnt
    for card in card_list:
        cnt_list[card] += 1

    if 3 in cnt_list:           # run 검사
        rlt = 1
        return

    for i in range(8):          # triplet 검사 
        if cnt_list[i] != 0 and cnt_list[i]*cnt_list[i+1]*cnt_list[i+2] != 0:   # 처음 cnt 값이 0이 아니고 뒤에도 0이 아니어아 하니까
            rlt = 1
            return

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    player1 = []
    player2 = []
    rlt = 0
    for i in range(0, len(arr), 2):         # 2씩 증가시켜 카드 2장씩 받아온다
        player1.append(arr[i])
        player2.append(arr[i+1])
        if i >= 4:                          # 카드가 3장 이상씩 되면 검사 한다.
            check(player1)                  # player1 먼저 검사
            if rlt != 0:                    # rlt 에 값 들어오면 둘 중 하나 검출
                rlt = 1
                break
            check(player2)                  # player2 검사
            if rlt != 0:
                rlt = 2
                break

    print(f'#{tc} {rlt}')