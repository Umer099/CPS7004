def multiple_condition_rule_system(input_value):
    if input_value < 5:
        return "Very Low"
    elif 5 <= input_value < 10:
        return "Low"
    elif 10 <= input_value < 20:
        return "Medium"
    else:
        return "High"

result = multiple_condition_rule_system(15)
print(result)