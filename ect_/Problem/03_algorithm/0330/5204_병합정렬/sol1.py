import sys
sys.stdin = open('input.txt')

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]
    return merge(merge_sort(left_array), merge_sort(right_array))

def merge(array1, array2):
    global cnt
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    if len(array1) != N:
        if array1[array1_index-1] > array2[array2_index-1]:
            cnt += 1

    return result

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    rlt = merge_sort(arr)
    print(f'#{tc} {rlt[N//2]} {cnt}')