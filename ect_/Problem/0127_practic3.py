# def tax(won):
#     if won <= 1200:
#         return won*0.06
#     elif won <= 4600:
#         return 72 + (won - 1200)*0.15
#     elif won <= 8800:
#         return 582 + (won - 4600)*0.24

# print(tax(1200))
# print(tax(4600))
# print(tax(5000))

#####################################
# def fee(minute, distance):
#     retal_fee = (minute/10)*1200
#     insurance_time = minute//30
#     if minute % 30 >= 20:
#         insurance_time = minute//30 + 1
#     insurance_fee = 525*insurance_time
#     distance_fee = distance * 170
#     if distance > 100:
#         distance_fee = 170*100 + (distance - 100)*85
#     return int(retal_fee + insurance_fee + distance_fee)

# print(fee(600, 50))
# print(fee(600, 110))

#############################
# def start_end(words):
#     count = 0
#     for i in words:
#         if len(i) >= 2 and i[0] == i[-1]:
#             count += 1
#     return count

# print(start_end(['level', 'asdwe', 's', 'abceda', 'gsdwrtfg']))
################################

# def collatz(num):
#     cnt = 0

#     while True:
#         cnt += 1

#         if num % 2 ==0:
#             num = num / 2
#         else:
#             num = num*3 + 1
        
#         if num == 1:
#             return cnt
#         elif cnt == 500:
#             return -1


# print(collatz(6))
# print(collatz(16))
# print(collatz(27))
# print(collatz(626331))


#####################################


# def dict_invert(my_dict):
#     dict_temp = {}
    
#     for key, value in my_dict.items():

#         if value in dict_temp.keys():
#             dict_temp[value] += [key]
#         else:
#             dict_temp[value] = [key]
        
#     return dict_temp




# print(dict_invert({1: 10, 2: 20, 3: 30}))
# print(dict_invert({1: 10, 2: 20, 3: 30, 4: 30}))
# print(dict_invert({1: True, 2: True, 3: True}))