class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, response):
        self.rules.append({"condition": condition, "response": response})

    def apply_rules(self, text):
        for rule in self.rules:
            if rule["condition"].lower() in text.lower():
                return f"Bot: {rule['response']}"
        return "Bot: I don't understand."
