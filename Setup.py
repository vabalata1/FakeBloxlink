import discord
import json

intents = discord.Intents.all()
intents.members = True
bot = discord.Client(intents=intents)

token = input("your bot token here : ")
link = input("your link here : ")

@bot.event
async def on_ready():
    guild = bot.guilds[0]

    id = guild.id

    data = {}
    data['token'] = token
    data['link'] = link
    data['id'] = id

    with open('config.json', 'w') as f:
        json.dump(data, f)

    print(f'Token, link and Guild ID {id} saved to config.json')

bot.run(token)