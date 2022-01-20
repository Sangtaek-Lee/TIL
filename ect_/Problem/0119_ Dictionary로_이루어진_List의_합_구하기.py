def dict_list_sum(*kwargs):
    sum = 0
    for i in kwargs:
        for j in i:
            sum += j['age']
    return sum       
    
print(dict_list_sum([{'name': 'kim', 'age': 12},{'name': 'lee', 'age': 4}]))