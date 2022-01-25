import discord
from discord.ext import tasks
import os
from neuralintents import GenericAssistant
from random import choice 

chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()

status = ['fantasy world', 'with 901 people', 'on 3 servers', 'Rocket League', 'chatbot lounge', 
         'serial lover', 'osu!', 'Last of us', 'Heavy rain', "on han's local server", 'in danger', 'with fire', 
         'with honeybot', 'crisis', 'midnight monster', 'sleep paralysis', 'among us', 'Assasins creed', 
         'in deep waters', 'with han']

client = discord.Client()

@client.event
async def on_ready():
    change_status.start()
    print('Your AI bot is up and running')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("!aibot"):
        response = chatbot.request(message.content[7:])
        await message.channel.send(response)

@tasks.loop(seconds=360)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))

client.run('OTEwNTAyMTk5NzY1OTE3NzI2.YZTxQA.KtjAJ8kNt360JLE-APbbJeDcloc')
