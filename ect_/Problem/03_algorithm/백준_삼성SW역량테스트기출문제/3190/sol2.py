import sys
sys.stdin = open('input.txt')
# input = sys.stdin.readline
from pprint import pprint

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dummy():
    pass


# N*N 행열에 사과가 놓여져 있다
N = int(input())                # 보드의 크기 2 <= N <= 100
K = int(input())                # 사과의 개수 0 <= K <= 100
board = [[0]*N for _ in range(N)]
for i in range(K):
    temp = list(map(int, input().split()))
    board[temp[0]][temp[1]] = 1
pprint(board)
L = int(input())                # 뱀의 방향 변환 정보 1 <= L <= 100
snake_directions = [list(map(str, input().split())) for _ in range(L)]     # 뱀의 방향 정보

dummy()
