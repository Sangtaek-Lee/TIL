def lonely(numbers):
    i = 0
    while i < len(numbers)-1:
        if numbers[i] == numbers[i+1]:
            numbers.pop(i+1)
        else:
            i += 1
    return numbers    

lonely([1, 1, 3, 3, 0, 1, 1])
lonely([4, 4, 4, 3, 3])
print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))
