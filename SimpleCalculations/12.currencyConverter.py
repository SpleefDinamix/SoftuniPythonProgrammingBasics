cur_input = float(input())
cur_type = input()
cur_to_convert = input()
result = 0.0

if cur_type == "BGN":
    if cur_to_convert == "EUR":
        result = cur_input / 1.95583
        
    elif cur_to_convert == "GBP":
        result = cur_input / 2.53405

    elif cur_to_convert ==  "USD":
        result = cur_input / 1.79549
            
elif cur_type == "EUR":
    if cur_to_convert == "BGN":
        result = cur_input * 1.95583

    elif cur_to_convert == "GBP":
        result = cur_input * 1.95583 / 2.53405

    elif cur_to_convert == "USD":
        result = cur_input * 1.95583 / 1.79549

elif cur_type == "GBP":
    if cur_to_convert == "BGN":
        result = cur_input * 2.53405

    elif cur_to_convert == "EUR":
        result = cur_input * 2.53405 / 1.95583

    elif cur_to_convert == "USD":
        result = cur_input * 2.53405 / 1.79549

elif cur_type == "USD":
    if cur_to_convert == "BGN":
        result = cur_input * 1.79549

    elif cur_to_convert == "EUR":
        result = cur_input * 1.79549 / 1.95583

    elif cur_to_convert == "GBP":
        result = cur_input * 1.79549 / 2.53405

print("{0:.2f}".format(result), cur_to_convert)