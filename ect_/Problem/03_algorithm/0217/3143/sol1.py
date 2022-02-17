import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):

    A, B = input().split()
    cnt = 0
    i = 0
    while i < len(A):
        temp_str = A[i:i+len(B)]    # A를 B문자열 길이만큼 슬라이싱하여
        if B == temp_str:           # B와 비교하여 같다면
            i += len(B)             # B 길이만큼 인덱스 이동
            cnt += 1                # 타이핑 카운트 1 증가
        else:                       # 아니라면
            i += 1                  # 다음인덱스로
            cnt += 1                # 타이핑 1 증가

    print(f'#{tc}', cnt)

