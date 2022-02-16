import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    case_num = input()
    num_list = list(input().split())
    ref_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    cnt_list = [0]*10
    for i in range(len(num_list)):
        for j in range(len(ref_list)):
            if num_list[i] == ref_list[j]:
                cnt_list[j] += 1

    print(f'#{tc}')
    for i in range(len(cnt_list)):
        for cnt in range(cnt_list[i]):
            print(ref_list[i], end=' ')
    print()

