from discord import Intents, File
from discord.ext import commands
from logging import FileHandler, DEBUG 
from dotenv import load_dotenv
from os import getenv, remove
from pyautogui import write, moveRel, screenshot, press, click, rightClick
from subprocess import run
from webbrowser import open_new
from time import sleep

load_dotenv()
token = getenv("DISCORD_TOKEN")
ID = getenv("DISCORD_ID")
sendScreen = getenv("SEND_SCREENSHOT")

handler = FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intents = Intents.default()
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
async def type(ctx):
	type = ctx.message.content
	type = type.removeprefix(".type ")
	if(type == ".type"):
		await ctx.send("No input text provided, keypresses not sent")
	else:
		write(type)
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
		moveRel(int(x), -int(y))
		await ctx.send("Mouse has been moved")
		if(sendScreen == "True"):
			await screen(ctx)

@bot.command()
async def screen(ctx):
	screenshot('PCCONTROLLERSCREENSHOTTEMPFILE.png')
	await ctx.send("", file=File("PCCONTROLLERSCREENSHOTTEMPFILE.png"))
	remove("PCCONTROLLERSCREENSHOTTEMPFILE.png")

@bot.command()
async def left(ctx):
	click()
	await ctx.send("Left click pressed")
	if(sendScreen == "True"):
		await screen(ctx)

@bot.command()
async def right(ctx):
	rightClick()
	await ctx.send("Right click pressed")
	if(sendScreen == "True"):
		await screen(ctx)

@bot.command()
async def cmd(ctx):
	if(int(ctx.author.id) != int(ID)):
		await ctx.send("Unauthorized")
	else:
		command = ctx.message.content
		command = command.removeprefix(".cmd ")
		if(command == ".cmd"):
			await ctx.send("No command provided, no commands sent")
		else:
			await ctx.send(f"Running the command `{command}`, it may take some time to finish...")
			result = run(["powershell", command], shell=True, capture_output=True, text=True, check=True)
			await ctx.send(result.stdout)
			await ctx.send(result.stderr)
			if(sendScreen == "True"):
				await screen(ctx)

@bot.command()
async def url(ctx):
	website = ctx.message.content
	website = website.removeprefix(".url ")
	if(website == ".url"):
		await ctx.send("No URL provided, nothing was opened")
	else:
		open_new(website)
		await ctx.send(f"Opened `{website}` on the default browser")
		sleep(1.5)
		if(sendScreen == "True"):
			await screen(ctx)

@bot.command()
async def win(ctx):
	press("win")
	await ctx.send("Windows key pressed")
	if(sendScreen == "True"):
		await screen(ctx)

@bot.command()
async def enter(ctx):
	press("enter")
	await ctx.send("Enter key pressed")
	if(sendScreen == "True"):
		await screen(ctx)

@bot.command()
async def shutdown(ctx):
	if(int(ctx.author.id) != int(ID)):
		await ctx.send("Unauthorized")
	else:
		input = ctx.message.content
		input = input.removeprefix(".shutdown ")

		if(input == "CONFIRM SHUTDOWN"):
			await ctx.send("Shutting down...")
			run(["powershell", "shutdown /s /t 0"], shell=True)
		else:
			await ctx.send("Are you sure you want to **SHUTDOWN** your computer?")
			await ctx.send("This will turn the computer AND the bot (me) fully off as well as any running programs.")
			await ctx.send("Type `.shutdown CONFIRM SHUTDOWN` to confirm")


bot.run(token, log_handler=handler, log_level=DEBUG)