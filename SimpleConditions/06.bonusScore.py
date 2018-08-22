num = int(input())
bonus_points = 0

if num <= 100:
    bonus_points += 5
elif num > 100 and num <= 1000:
    bonus_points += num * 0.2
else:
    bonus_points += num * 0.1

if num % 2 == 0:
    bonus_points += 1
elif num % 5 == 0:
    bonus_points += 2

print(bonus_points)
print(num + bonus_points)