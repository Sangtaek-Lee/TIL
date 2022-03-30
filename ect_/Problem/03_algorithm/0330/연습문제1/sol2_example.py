import sys

sys.stdin = open('input.txt')


def quick_sort(arr, low, high):
    if high <= low:
        return

    mid = partition(arr, low, high)
    quick_sort(arr, low, mid - 1)
    quick_sort(arr, mid, high)

def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low + 1, high - 1
    return low


T = int(input())

for tc in range(1, T + 1):
    numbers = list(map(int, input().split()))
    N = len(numbers)
    quick_sort(numbers, 0, len(numbers) - 1)  # 정렬 할 배열, 시작 ~ 끝 idx
    print(f'#{tc} {numbers}')