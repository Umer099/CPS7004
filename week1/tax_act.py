from rule_based_system_with_rule_engine  import RuleEngine
tax_rule = RuleEngine()
tax_rule.add_rule(lambda x: x < 12570, "personal Allowance")
tax_rule. add_rule(lambda x:12570 <= x < 50270, "Basic rate")
tax_rule. add_rule(lambda x: 50270 <= x < 125140, "higher rate")
tax_rule. add_rule(lambda x: 50270 <= x < 125140, "Additional rate")
print ("""
WELCOME TO THE TAX RULE ENGINE
""")
input = int(input("ENTER THE VALUE"))
result = tax_rule.apply_rules(input)

print(f"Your tax return is {result}.")