n = int(input())
_min = 1000000

for i in range(n):
    cur_num = int(input())
    if cur_num < _min:
        _min = cur_num
        
print(_min)
