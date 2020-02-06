from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pickle

bot = ChatBot('ChatBot')
trainer= ListTrainer(bot)

#Loading pickle commments
f = open('./InstagramComments_.p', 'rb')
comments = pickle.load(f)
f.close()

#Training Bot with existing comments
for convo in comments[:60000]:
    trainer.train(convo)

#Testing bot
while True:
    request = input("You: ")
    response = bot.get_response(request)
    print('Bot:', response)