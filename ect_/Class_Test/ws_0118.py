#1
# number = int(input('정수 입력'))
# for i in range(1,number+1):
#     if number % i == 0:
#         print(i, end =' ')
#2
# numbers = [
#        85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
#        51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
#        52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
#     ]
# center=len(numbers)//2
# for j in range(len(numbers)):
#     idx_min = j
#     for i in range(j + 1,len(numbers)):
#         if numbers[idx_min] > numbers[i]:
#             numbers[idx_min], numbers[i] = numbers[i], numbers[idx_min]
# print(numbers[center])
#3
# number = int(input('자연수 입력'))
# for i in range(1,number+1):
#     for j in range(1,i+1):
#         print(j, end = ' ')
#     print('')