def count_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    cnt = 0
    for i in vowels:
        cnt += word.count(i)        
    return cnt

count_vowels('apple')
count_vowels('banana')
print(count_vowels('apple'))
print(count_vowels('banana'))