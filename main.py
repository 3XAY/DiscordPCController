#Discord specific imports
from discord import Intents, File
from discord.ext import commands
from logging import FileHandler, DEBUG 

#Environment variables
from dotenv import load_dotenv
from os import getenv, remove #Also helps with screenshots

#Computer control
from pyautogui import write, moveRel, screenshot, press, click, rightClick
from subprocess import run
from webbrowser import open_new
from time import sleep

#Allows the bot to be killed
from sys import exit

#Load in all environment variables
load_dotenv()
token = getenv("DISCORD_TOKEN")
ID = getenv("DISCORD_ID")
sendScreen = getenv("SEND_SCREENSHOT")

#Error logging, only for development
handler = FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intents = Intents.default()
intents.message_content = True
intents.members = True

#Create the bot object, set command prefix to "." and set permissions (intents)
bot = commands.Bot(command_prefix=".", intents=intents)

#DM the bot owner when the bot is online, allows the user to use it privately
@bot.event
async def on_ready():
	print(f"{bot.user.name} is ready")
	user = await bot.fetch_user(ID)
	await user.send(f"{bot.user.name} is ready")

#Checks every message to see if it is a command, if so, it gets handled accordingly
#Ignores its own output
@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
	await bot.process_commands(message)

#Takes an input after the command to type something on the host computer
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

#Takes a pair of integer inputs (x,y) to move the mouse by (negative = left/down, positive = up/right)
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

#Screenshot command takes a screenshot via PyAutoGUI and saves it in the working directory, sends it to Discord, then deletes the saved screenshot
@bot.command()
async def screen(ctx):
	screenshot('PCCONTROLLERSCREENSHOTTEMPFILE.png')
	await ctx.send("", file=File("PCCONTROLLERSCREENSHOTTEMPFILE.png"))
	remove("PCCONTROLLERSCREENSHOTTEMPFILE.png")

#Presses the left mouse button
@bot.command()
async def left(ctx):
	click()
	await ctx.send("Left click pressed")
	if(sendScreen == "True"):
		await screen(ctx)

#Presses the right mouse button
@bot.command()
async def right(ctx):
	rightClick()
	await ctx.send("Right click pressed")
	if(sendScreen == "True"):
		await screen(ctx)

#Allows the owner of the bot to run commands via PowerShell, access is denied to all others due to massive security risks
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

#Allows the client to input a URL which is opened in the default browser (assuming the https:// part is included, otherwise opens in Edge)
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

#Press the Windows key
@bot.command()
async def win(ctx):
	press("win")
	await ctx.send("Windows key pressed")
	if(sendScreen == "True"):
		await screen(ctx)

#Press the enter key
@bot.command()
async def enter(ctx):
	press("enter")
	await ctx.send("Enter key pressed")
	if(sendScreen == "True"):
		await screen(ctx)

#Allows the owner of the bot to shut the computer (and also the bot) down, denied to all others
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

#Allows anyone to quickly kill the bot in case of an emergency
@bot.command()
async def k(ctx):
	exit(0)


bot.run(token, log_handler=handler, log_level=DEBUG)