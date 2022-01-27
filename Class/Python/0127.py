# class Person:
#     cnt = 0

#     def __init__(self, name):
#         self.name = name

# aiden = Person('aiden')
# aiden.cnt = 3           #인스턴스 변수
# print(aiden.cnt)
# print(Person.cnt)


#################################
#데코레이터

# from datetime import datetime as dt 


# def time_display_decorator(origin_func):
#     def decorated():
#         print(dt.now())
#         origin_func()
#         print('----')
#     return decorated

# class 데코레이터
# class TimeDisplay:
#     def __init__(self, origin_func):
#         self.origin_func = origin_func
    
#     def __call__(self):
#         print(dt.now())
#         self.origin_func()
#         print('----')
        
# @TimeDisplay
# def test_a():
#     print('test_a')




# @time_display_decorator
# def test_a():
#     print('test_a')

# @time_display_decorator
# def test_b():
#     print('test_b')

# test_a() # time_display_decorator(test_a)() =>내부적인 함수 콜
        
# test_b()
#--------------------------

#class method 클래스 변수 제어
# class Person:
#     cnt = 0

#     def __init__(self, name):
#         self.name = name

#     @classmethod
#     def plus(cls):
#         cls.cnt += 1

# print(Person.cnt)
# Person.plus()
# print(Person.cnt)


#static method 설명
# class Person:
#     cnt = 0

#     def __init__(self, name):
#         self.name = name

#     @classmethod
#     def plus(cls):
#         cls.cnt += 1

#     @staticmethod     #class와 instance 변수와 상관 없는 method
#     def run():
#         print('뛰어!')

# Person.run()

##############################################
#Public, Protected, Private

# class Person:
#     def __init__(self, age):
#         self.__age = age
    
#     def get_age(self):
#         return self.__age
    
#     def set_age(self):
#         self.__age += 1 # mangling 한다 엄망징창으로 만든다

#     def get_name(stl):
#         pass

# tony = Person(27)
# # print(tony.__age)         # 직접 접근 시 오류 발생
# print(tony.get_age())
# tony.set_age()
# print(tony.get_age())

# print(tony._Person__age()) #private은 magling하여 저장되는 데 magling된 메서드를 이름을 알게되면 호출 할 수 있다.
#하지만 이렇게라도 쓰지 않는다.
