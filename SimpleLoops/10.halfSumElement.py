n = int(input())
nums = []

for x in range(n):
    nums.append(int(input()))

max_num = max(nums)
rest_sum = sum(nums) - max_num

if max_num == rest_sum:
    print("Yes")
    print("Sum =", rest_sum)
else:
    print("No")
    print("Diff =", abs(max_num - rest_sum))
