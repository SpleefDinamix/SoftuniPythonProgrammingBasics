n = int(input())

def sum_input():
    _sum = 0
    for i in range(n):
        _sum += int(input())
    return _sum

left_sum = sum_input()
right_sum = sum_input()

if left_sum == right_sum:
    print("Yes, sum =", left_sum)
else:
    print("No, diff =", abs(left_sum - right_sum))