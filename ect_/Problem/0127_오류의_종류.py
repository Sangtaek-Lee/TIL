# 1/0           # ZeroDivisionError : 0으로 나눌때 발생
# print(a)      # NameError         : namespace 상에 이름이 없을 경우
# 1 + '1'       # TypeError         : 타입 불일치, ...
# list = []
# list[1]       # IndexError        : 인덱스가 존재하지 않거나 범위를 벗어난 경우
# dirc = {'A' : 1}
# dirc['B']     # KeyError          : 해당 키가 존재하지 않는 경우
# import good   # ModuleNotFoundError : 존재하지 않는 모듈을 import 하는 경우
# from faker import Fake # ImportError : Module은 있으나 존재하지 않는 클래스/함수를 가져오는 경우
# int('1.5')    # ValueError        : 타입은 올바르나 값이 적절하지 않은 경우