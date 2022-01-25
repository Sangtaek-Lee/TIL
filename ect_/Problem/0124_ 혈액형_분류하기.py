def count_blood(args):
    args_set = set(args)
    cnt = 0
    blood_dict = {}
    for blood_type in args_set:
        cnt = args.count(blood_type)
        blood_dict[blood_type] = cnt
    return blood_dict

count_blood([
    'A', 'B', 'A', 'O', 'AB', 'AB',
    'O', 'A', 'B', 'O', 'B', 'AB', 
])

print(count_blood([
    'A', 'B', 'A', 'O', 'AB', 'AB',
    'O', 'A', 'B', 'O', 'B', 'AB', 
]))