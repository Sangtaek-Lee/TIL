
def get_dict_avg(args):             #전체 과목 평균 점수 구하기
    return sum(args.values())/4     #dict의 value 값만 추출하여 더한여 나눈다.

get_dict_avg({
    'python' : 80,
    'algorithm' : 90,
    'django' : 89,
    'web' : 83,
})