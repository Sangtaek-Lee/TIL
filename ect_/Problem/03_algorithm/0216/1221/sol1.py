import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    case_num = input()
    num_list = list(input().split())
    ref_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    # print(num_list)
    # 문자를 정수로
    for i in range(len(num_list)):
        for j in range(len(ref_list)):
            if num_list[i] == ref_list[j]:
                num_list[i] = j
    # print(num_list)
    # 버블소트 정렬
    for i in range(len(num_list)-1):
        for j in range(len(num_list)-i-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    # 숫자를 문자로
    for i in range(len(num_list)):
        for j in range(len(ref_list)):
            if num_list[i] == j:
                num_list[i] = ref_list[j]

    print(f'#{tc}')
    for i in range(len(num_list)):
        print(num_list[i], end=' ')
    print()

