from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

# This code is used in python 3.6 due to the requirements of chatterbot package

clinic_bot = ChatBot('clinic_bot')
clinic_bot.set_trainer(ListTrainer)
for file in os.listdir('data'):
        convData = open('data/' + file).readlines()
        clinic_bot.train(convData)

print("Training completed")
    

