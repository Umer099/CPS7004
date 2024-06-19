def rule_1(input_value):
    return input_value < 5


def rule_2(input_value):
    return 5 <= input_value < 10


def rule_3(input_value):
    return 10 <= input_value < 20


def rule_based_system(input_value):
    if rule_1(input_value):
        return "Very Low"
    elif rule_2(input_value):
        return "Low"
    elif rule_3(input_value):
        return "Medium"
    else:
        return "High"


result = rule_based_system(15)
print(result)  # Output: Medium
