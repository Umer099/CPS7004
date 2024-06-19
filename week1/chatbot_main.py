

from simple_chatbot import RuleEngine

bot = RuleEngine()
bot. add_rule("hello", "hello")
bot. add_rule("good bye", "good bye")
bot. add_rule("Whats your name", "My name is bot")


while True:
    inputt = input("ENTER YOUR RESPONSE")
    response = bot.apply_rules(inputt)
    print(response)
    if inputt.lower() == "good bye":
        break