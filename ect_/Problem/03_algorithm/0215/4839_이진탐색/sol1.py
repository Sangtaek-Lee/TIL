import sys
sys.stdin = open("input.txt")

def binary_search(page, key):
    start = 1
    end = page
    cnt = 0
    while start <= end:
        mid = (start + end) // 2
        if mid == key:
            return cnt
        elif mid > key:
            end = mid
        else:
            start = mid
        cnt += 1

T = int(input())

for tc in range(1, T + 1):
    page, a, b = map(int, input().split())
    page_a = binary_search(page, a)
    page_b = binary_search(page, b)
    rlt = 0

    if page_a < page_b:
        rlt = "A"
    elif page_a > page_b:
        rlt = "B"

    print(f"#{tc} {rlt}")