n = int(input())
odd_sum = 0
even_sum = 0

for x in range(n):
    if x % 2 == 0:
        odd_sum += int(input())
    else:
        even_sum += int(input())

print(odd_sum)
print(even_sum)

if odd_sum == even_sum:
    print("Yes")
    print("Sum =", odd_sum)
else:
    print("No")
    print("diff =", abs(odd_sum - even_sum))
