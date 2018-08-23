yearType = input().lower()
p = int(input()) 
h = int(input()) 

hs = (48 - h) * 3/4
ps = p * 2/3

result = h + hs + ps

leap = 0
if yearType == "leap":
    leap = result * 15 / 100
    result += leap

print(int(result))