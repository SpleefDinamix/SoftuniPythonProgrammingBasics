day = int(input())
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

if day > 0 and day <= 7:
    print(days[day - 1])
else:
    print("Error")