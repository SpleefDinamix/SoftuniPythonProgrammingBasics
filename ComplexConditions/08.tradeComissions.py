town = input().lower()
sales = float(input())
comission = 0
error = False

if town == "sofia":
    if sales >= 0 and sales <= 500:
        comission = sales * 5 / 100
    elif sales > 500 and sales <= 1000:
        comission = sales * 7 / 100
    elif sales > 1000 and sales <= 10000:
        comission = sales * 8 / 100
    elif sales > 10000:
        comission = sales * 12 / 100
    else:
        error = True
        print("error")

elif town == "varna":
    if sales >= 0 and sales <= 500:
        comission = sales * 4.5 / 100
    elif sales > 500 and sales <= 1000:
        comission = sales * 7.5 / 100
    elif sales > 1000 and sales <= 10000:
        comission = sales * 10 / 100
    elif sales > 10000:
        comission = sales * 13 / 100
    else:
        error = True
        print("error")

elif town == "plovdiv":
    if sales >= 0 and sales <= 500:
        comission = sales * 5.5 / 100
    elif sales > 500 and sales <= 1000:
        comission = sales * 8 / 100
    elif sales > 1000 and sales <= 10000:
        comission = sales * 12 / 100
    elif sales > 10000:
        comission = sales * 14.5 / 100
    else:
        error = True
        print("error")
else:
    error = True
    print("error")
if not error:
    print("{0:.2f}".format(comission))