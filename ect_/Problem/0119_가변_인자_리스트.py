'''가변 인자 리스트를 사용하여, 갯수가 정해지지 않은 여러 정수들을 전달 받아 해당 정
수들의 평균 값을 반환하는 my_avg 함수를 작성하시오'''


def my_avg(*args):
    sum = 0
    n = 0
    for arg in args:
        sum += arg
        n += 1
    return sum/n

print(my_avg(77, 83, 95, 80, 70))    



