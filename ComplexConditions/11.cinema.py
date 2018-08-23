c_type = input()
rows = int(input())
cols = int(input())
price = 0

if c_type == "Premiere":
    price = 12.00
elif c_type == "Normal":
    price = 7.50
elif c_type == "Discount":
    price = 5.00
else:
    raise ValueError("Not a valid type!")

total_price = price * rows * cols
print("{0:.2f}".format(total_price), "leva")
