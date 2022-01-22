number = int(input())
i = 0
total = 0
if number <= 10000:
    while i <= number:
        total += i
        i += 1
    print(total)
else:
    print('입력 값이 1000을 초과합니다.')