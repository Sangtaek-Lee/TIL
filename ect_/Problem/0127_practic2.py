import random

class ClassHelper:
    
    def __init__(self, name_list):
        self.list = name_list

    def pick(self, n):
        return random.sample(self.list, n)
    
    def match_pair(self):
        if len(self.list) <= 3:        
            return self.list
        random.shuffle(self.list)      
        match_list = []
        for i in range((len(self.list) +1) // 2 ):
            match_list.append(self.list[i*2:(i+1)*2])
        if len(match_list[-1]) == 1:
            match_list[-2].extend(match_list.pop())
        return match_list


ch = ClassHelper(['김싸피', '이싸피', '조싸피', '박싸피', '정싸피'])
print(ch.pick(1))
print(ch.pick(2))
print(ch.pick(3))
print(ch.pick(4))

print(ch.match_pair()) #=> [['조싸피', '이싸피'], ['김싸피', '정싸피', '박싸피']]



# list_5 = ['a', 'b', 'c', 'd', 'e']

# for i in range(5):
#     x = random.sample(list(range(len(list_5))),len(list_5))
#     print(x)
#     match_list_idx = []
#     match_list = []
#     for j in x:
#         match_list_idx.append(list_5[j])
# # while True:
# if len(list_5) != 3:
#     match_list.append(match_list_idx[i:2])


#     # if len(list_5) == 3:
#     #     break
# print (match_list_idx)
# print (match_list)
# print(list(range(len(list_5))))