
def basic_rule_based_system(input):
    if input < 10:
        return "low"
    else:
        return "high"
result = basic_rule_based_system(7)
print(result)