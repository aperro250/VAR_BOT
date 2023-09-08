import discord
import os
import sys
import asyncio
import time 
import json

from discord.ext import commands
from discord.utils import get

TOKEN = ''

BADWORDS = ["лох", "дурак"]
LINKS = ["https", "http", "://", "com", "ru", "net", "org", "shop"]

if not os.path.exists('users.json'):
  with open('users.json', 'w') as file:
    file.write('{}')
    file.close()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents = intents)

@bot.event
async def on_ready():
  print(f"Бот зашел на сервер. Данные бота:")
  print()
  print(f"Имя Бота: {bot.user.name}")
  print(f"ID Бота: {bot.user.id}")
  print(f"Токен бота: {TOKEN}")
  print()

  for guild in bot.guilds:
    for member in guild.members:
      with open('users.json', 'r') as file:
        data = json.load(file)
        file.close()

      with open('users.json', 'w') as file:
        data[str(member.id)] = {
          "WARNS": 0,
          "CAPS": 0
        }

        json.dump(data, file,indent=4)
        file.close()


@bot.command()
async def hello(ctx): #!hello
  await ctx.send("И снова всем привет, подписчикам и не подписчикам, с вами снова я, Варвар Бот", file = discord.File("varvar.PNG"))

bot.run(TOKEN)