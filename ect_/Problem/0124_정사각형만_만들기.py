def only_square_area(*args): # 각 리스트 중복 값을 곱한 값 출력
    x = []                  # list를 더해 값을 카운트하여 2인 경우 곱하여 리스트에 출력? 
    area_list = []
    for arg in args:
        x += arg
    for i in args[0]:
        if x.count(i) == 2:
            area_list.append(i*i)
    return area_list

only_square_area([32, 55, 63], [13, 32, 40, 55])
print(only_square_area([32, 55, 63], [13, 32, 40, 55]))