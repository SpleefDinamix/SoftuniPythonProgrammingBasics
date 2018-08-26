vowels = {
    'a':1, 'e':2, 'i':3, 'o':4, 'u':5
}

word = input()
result = 0

for char in word:
    if char in vowels:
        result += vowels[char]

print(result)
