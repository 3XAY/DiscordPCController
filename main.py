import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import pyautogui

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
ID = os.getenv("DISCORD_ID")
sendScreen = os.getenv("SEND_SCREENSHOT")

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
		pyautogui.write(type)
		await ctx.send(f"`{type}` was typed")
		if(sendScreen == "True"):
			await screen(ctx)

@bot.command()
async def mouse(ctx):
	coords = ctx.message.content
	coords = coords.removeprefix(".mouse ")
	coordsSplit = coords.split()
	x = coordsSplit[0]
	y = coordsSplit[1]
	if(coords == ".mouse"):
		await ctx.send("No movements provided, mouse movements not sent")
	else:
		pyautogui.moveRel(int(x), -int(y))
		await ctx.send("Mouse has been moved")
		if(sendScreen == "True"):
			await screen(ctx)

@bot.command()
async def screen(ctx):
	pyautogui.screenshot('PCCONTROLLERSCREENSHOTTEMPFILE.png')
	await ctx.send("", file=discord.File("PCCONTROLLERSCREENSHOTTEMPFILE.png"))
	os.remove("PCCONTROLLERSCREENSHOTTEMPFILE.png")


bot.run(token, log_handler=handler, log_level=logging.DEBUG)