def all_list_sum(*args):
    sum = 0
    for arg in args:
        for i in arg:
            sum += i
    return sum

print(all_list_sum([1],[2,3],[4,5,6],[7,8,9,10]))