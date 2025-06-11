from chatterbot import ChatBot

# This code is used in python 3.6 due to the requirements of chatterbot package
# Initialize
clinic_bot = ChatBot(
    'clinic_Bot',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation'
    ],
    trainer='chatterbot.trainers.ListTrainer'
)

print("Hi! Welcome to the clinic. How may I help you?")

while True:
    user_input = input("You: ")
    clinic_bot_response = clinic_bot.get_response(user_input)
    print(f"Clinic_Bot: {clinic_bot_response}")
