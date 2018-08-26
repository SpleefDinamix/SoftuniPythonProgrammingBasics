n = int(input())
_max = -1000000

for i in range(n):
    cur_num = int(input())
    if cur_num > _max:
        _max = cur_num
        
print(_max)