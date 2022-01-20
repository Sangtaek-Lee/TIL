# # # def add(*args):
# # #     print(type(args))
# # #     print(args)
# # # add(1, 2 ,3 ,4)

# # # x = 3+4j
# # # # print(type(x) == type(complex()))
# # # # print(x.real)
# # # # print(-0.0)



# # # # x = -3.75
# # # # print(x*x)
# # # # print((x*x)**0.5)
# # # def my_abs(x):
# # #     if type(x) == type(complex()):
# # #         return (x.real**2 + x.imag**2)**0.5

# # #     elif x > 0:
# # #         return x
# # #     elif x == -0.0:
# # #         return -x
# # #     else:
# # #         return -1*x

# # # # def my_abs(x):
# # # #     if type(x) == type(complex()):
# # # #         return (x.real**2 + x.imag**2)**0.5
# # # #     else:
# # # #         return (x**2)**0.5
# # # # x = -0.0
# # # # print(-1*x)

# # # # print(my_abs(3+4j))
# # # print(my_abs(-0.0))
# # # # print(my_abs(-5))
# # # # print(abs(3+4j), abs(-0.0), abs(-5))











# # # help(all)



# # def my_all(elements):
# #     for i in elements:
# #         if i == 0:
# #             return False
# #         else:
# #             return True


# # print(my_all([]))
# # print(my_all([1, 2, 5, '6']))
# # print(my_all([[], 2, 5, '6']))
# # # print(all([1]), all([1, 2, 5, '6']), all([[], 2, 5, '6']))

# # def my_all(elements):
# #     result = 1
# #     for element in elements:
# #         print(element)
# #         result *= bool(element)
# #         print(result)
# #     if result == 1:
# #         return True
# #     else:
# #         return False

# # print(my_all([]))
# print(not False)

# def my_any(elements):
#     x = 1   
#     for element in elements:
#         y = not bool(element)
#         x = x * y
#     if x == 0:
#         return True
#     else:
#         return False


# print(my_any([1, 2, 5, '6']))
# print(my_any([[], 2, 5, '6']))
# print(my_any([0]))
# print(any([1, 2, 5, '6']), any([[], 2, 5, '6']), any[(0)])

number = 1234
i = str(number)
print(i[0])