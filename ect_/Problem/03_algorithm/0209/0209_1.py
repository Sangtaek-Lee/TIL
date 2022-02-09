import sys
sys.stdin = open('input_1.txt')

N = 6                                   # 테스트 케이스 개수를 모른다면? 어떻게 받아올까?
for i in range(1, N+1):
    globals()[f'temp_{i}'] = input()    # 변수의 이름을 i를 기준으로 동적으로 변화 시키고 싶어서 globals() 메서드를 사용하였다.

print(temp_1)
print(temp_2)
print(temp_3)
print(temp_4)
print(temp_5)
print(temp_6)