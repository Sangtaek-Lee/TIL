import sys
sys.stdin = open('input.txt')

T = int(input())


def quick_sort(arr, left, right):
    if left >= right:
        return

    mid = partition(arr, left, right)
    quick_sort(arr, left, mid - 1)
    quick_sort(arr, mid, right)

def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            print(low, high)
            print(arr)
            low, high = low + 1, high - 1
    return low

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    quick_sort(numbers, 0, N - 1)

    print(f'#{tc} {numbers}')