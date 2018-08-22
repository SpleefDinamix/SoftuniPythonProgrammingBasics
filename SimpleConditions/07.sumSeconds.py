first = int(input())
second = int(input())
third = int(input())

sec_sum = first + second + third
hours = sec_sum / 60
seconds = sec_sum % 60

print("%d:%02d" % (hours, seconds))