from math import pi
shape = input()

if shape == "square":
    a = float(input())
    print(a ** 2)
elif shape == "triangle":
    a = float(input())
    h = float(input())
    print(a * h / 2)
elif shape == "rectangle":
    a = float(input())
    b = float(input())
    print(a * b)
elif shape == "circle":
    r = float(input())
    print((r ** 2) * pi)
else:
    print("Incorect shape")