product = input().lower()
day = input().lower()
quantity = float(input())
days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

catalog = {
    "banana":2.50,
    "apple":1.20,
    "orange":0.85,
    "grapefruit":1.45,
    "kiwi":2.70,
    "pineapple":5.50,
    "grapes":3.85
}

catalog_weekend = {
    "banana":2.70,
    "apple":1.25,
    "orange":0.90,
    "grapefruit":1.60,
    "kiwi":3.00,
    "pineapple":5.60,
    "grapes":4.20
}

if day not in days or product not in catalog.keys():
    print("error")
elif day == "sunday" or day == "saturday":
    print("{0:.2f}".format(catalog_weekend[product]*quantity))
else:
    print("{0:.2f}".format(catalog[product]*quantity))