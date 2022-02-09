import sys
sys.stdin = open('input_2.txt')

N = 4
for i in range(1, N+1):
    globals()[f'temp_list_{i}'] = input()


print(temp_list_1)
print(temp_list_2)
print(temp_list_3)
print(temp_list_4)