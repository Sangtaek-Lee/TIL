# 퀵 정렬
import sys
sys.stdin = open('input.txt')

T = int(input())

def partition(arr, start, end):
    print(f'partition start')
    print(f'arr {arr}')
    pivot = arr[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left < right and pivot < arr[left]:
            print(f'left: {left} -> {left+1}')
            left += 1
        while left < right and pivot > arr[right]:
            right -= 1
            print(f'right: {right} -> {right+1}')

        print(f'{left} {right}')
        if left <= right:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[start], arr[right] = arr[right], arr[start]

    print(f'partition end')
    print(f'arr {arr}')
    return right

def quick_sort(arr, start, end):
    if start < end: # start >= end
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot-1)
        quick_sort(arr, pivot, end)
    return arr

for tc in range(1, T + 1):
    numbers = list(map(int, input().split()))
    N = len(numbers)
    rlt = quick_sort(numbers, 0, N-1)

    print(f'#{tc} {rlt}')