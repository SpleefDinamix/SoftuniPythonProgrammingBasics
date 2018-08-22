current_metric_value = float(input())
metric_type = input()
metric_type_to_convert = input()

def find_metric_value(value):
    if value == "mm":
        return 1000
    elif value == "cm":
        return 100
    elif value == "mi":
        return 0.000621371192
    elif value == "in":
        return 39.3700787
    elif value == "km":
        return 0.001
    elif value == "ft":
        return 3.2808399
    elif value == "yd":
        return 1.0936133
    else:
        return 1

metric_devider = find_metric_value(metric_type)
metric_multiplier = find_metric_value(metric_type_to_convert)

result = current_metric_value * metric_multiplier / metric_devider
print(result, metric_type_to_convert)