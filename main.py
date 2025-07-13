import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import time
import keyboard

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
ID = os.getenv("DISCORD_ID")

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
	print(f"{bot.user.name} is ready")
	user = await bot.fetch_user(ID)
	await user.send(f"{bot.user.name} is ready")

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
	await bot.process_commands(message)

@bot.command()
async def repeat(ctx):
	await ctx.send(ctx.message.content)

@bot.command()
async def type(ctx):
	type = ctx.message.content
	type = type.removeprefix(".type ")
	if(type == ".type"):
		await ctx.send("No input text provided, keypresses not sent")
	else:
		keyboard.write(type)
		await ctx.send(f"`{type}` was typed")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)