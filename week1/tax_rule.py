from rule_based_system_with_rule_engine  import RuleEngine
tax_rule = RuleEngine()
tax_rule.add_rule(lambda x: x < 5, "very low")
tax_rule. add_rule(lambda x: 5 <= x < 10, "low")
tax_rule. add_rule(lambda x: 10 <= x < 20, "medium")

result = tax_rule.apply_rules(15)
print(result)