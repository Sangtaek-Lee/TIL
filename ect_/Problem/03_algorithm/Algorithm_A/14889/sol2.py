import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]


def dfs(s):

    if s == N:
        rlt = abs(start_stat - link_stat)
        return rlt

    start_member.append(s)