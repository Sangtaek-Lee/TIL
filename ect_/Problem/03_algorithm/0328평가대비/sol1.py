import sys
sys.stdin = open('input.txt')

problem_list = list(map(int, input().split()))
print(set(problem_list))