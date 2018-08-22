num = int(input())
result = ""

def numPrefixTwo(number):
    output = ""

    if number == 2:
        output = "twenty"

    elif number == 3:
        output = "thirty"

    elif number == 4:
        output = "forty"

    elif number == 5:
        output = "fifty"

    elif number == 6:
        output = "sixty"

    elif number == 7:
        output = "seventy"

    elif number == 8:
        output = "eighty"

    elif number == 9:
        output = "ninety"

    return output

def numToText(number):
    output = ""
    if number == 0:
        output = "zero"

    elif number == 1:
        output = "one"

    elif number == 2:
        output = "two"

    elif number == 3:
        output = "three"

    elif number == 4:
        output = "four"

    elif number == 5:
        output = "five"

    elif number == 6:
        output = "six"

    elif number == 7:
        output = "seven"

    elif number == 8:
        output = "eight"

    elif number == 9:
        output = "nine"

    elif number == 10:
        output = "ten"

    elif number == 11:
        output = "eleven"

    elif number == 12:
        output = "twelve"

    elif number == 13:
        output = "thirteen"

    elif number == 14:
        output = "fourteen"

    elif number == 15:
        output = "fifteen"

    elif number == 100:
        output = "one hundred"

    return output

if num >= 0 and num <= 15 or num == 100:
    result = str(numToText(num))
elif num > 15 and num <= 19:
    result = numToText(num % 10) + "teen"
elif num >= 20 and num < 100:
    result = str(numPrefixTwo(num // 10))
    if num % 10 != 0:
        result += " " + str(numToText(num % 10))
else:
    result = "invalid number"

print(result)