hours = int(input())
mins = int(input())

total_mins = hours * 60 + mins + 15
new_hours = total_mins / 60
new_mins = total_mins % 60

print("%02d:%02d" % (new_hours, new_mins))
