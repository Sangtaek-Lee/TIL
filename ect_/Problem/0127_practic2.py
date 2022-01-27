import random

# class ClassHelper:
    
#     def __init__(self, name_list):
#         self.list = name_list

#     def pick(self, n):
#         return random.sample(self.list, n)
    
#     def match_pair(self):
#         pass


# ch = ClassHelper(['김싸피', '이싸피', '조싸피', '박싸피', '정싸피'])
# print(ch.pick(1))
# print(ch.pick(2))
# print(ch.pick(3))
# print(ch.pick(4))
# # ch.pick(1) #=> ['이싸피']
# # ch.pick(1) #=> ['김싸피']
# # ch.pick(2) #=> ['김싸피', '박싸피']
# # ch.pick(3) #=> ['김싸피', '조싸피', '정싸피']
# # ch.pick(4) #=> ['박싸피', '이싸피', '김싸피', '정싸피']

# # ch.match_pair() #=> [['조싸피', '이싸피'], ['김싸피', '정싸피', '박싸피']]

# # import random
# # print(random.randint(1,1))

list_5 = ['a', 'b', 'c', 'd', 'e']

for i in range(5):
    x = random.sample(list(range(len(list_5))),len(list_5))
    print(x)
    match_list_idx = []
    match_list = []
    for j in x:
        match_list_idx.append(list_5[j])
    if len(list_5) != 3:
        match_list += match_list_idx.pop()

    # if len(list_5) == 3:
    #     break
print (match_list_idx)
print (match_list)
# print(list(range(len(list_5))))