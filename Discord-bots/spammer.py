from discord.ext import comamnds
import discord.py

TOKEN = "" # maybe using .env will be better

intents = discord.Intents.default()
intents.message_content = True

bot = comamnds.Bot(command_prefix="!", intents=intents)

@bot.event
async def onready():
    print("succesfully logged in the bot"

@bot.command
async def spam():
    for _ in range(100): # it can be TRUE to spamm infinitely
        await.channel.send(f"Hello, i am a spammer")

bot.run(TOKEN)
