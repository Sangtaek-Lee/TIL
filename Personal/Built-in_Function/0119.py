words = input()
n = len(words)
def get_middle_char(x):
    if n % 2 == 1:
        return x[n//2]
    else:
        i = int((n/2)-1)
        return x[i:i+2]

print(get_middle_char(words))
        