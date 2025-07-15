"""
Step 28: Let the installer finish installing, then run the executable
Step 29: Enjoy the bot and simply run the executable each time you want it on

What does the code need?
	Some way to open links - Webbrowser
	A way to accept user inputs - input()
	A way to create and modify files - open() function(s)
	A way to download files - Use PC-Utilities Installer as framework
	Error handling - PC Utilities Installer framework
"""
from webbrowser import open_new
from subprocess import run
from os import path, getcwd

def installStep(message, command, error):
	print(message)
	try:
		run(["powershell", command], shell=False, check=True)
		print("DONE")
	except:
		print(error + "\nEnter any key to exit...")
		blank = input()
		exit(error)

print("Open Discord and head to the settings (Enter to continue)")
input()
print("Scroll down to the advanced section and click on it (Enter to continue)")
input()
print("Turn on developer mode and exit settings (Enter to continue)")
input()
print("Now, create a Discord server with just you in it and name it whatever you want, this is how the bot will be able to DM you (Enter to continue)")
input()
print("Send any random message in that server and then right click on your profile picture next to the message and click 'Copy User ID' (Enter to continue)")
input()
print("Now, paste the ID into here and press enter to submit it")
ID = input()
print("Do you want the bot to send you a screenshot after every command? Default is Yes (simply press enter) so you can see what you are doing, type the letter N to say no")
screen = input().upper()
print("A new tab will be opened on your computer, sign in to your Discord account (Enter to continue)")
input()
open_new("https://discord.com/developers/")
print("After signing in, close the tab and press enter to continue to the next page")
input()
open_new("https://discord.com/developers/applications")
print("Click on 'New Application' in the top left of the screen (Enter to continue)")
input()
print("Name the bot whatever you want and check the checkbox (Enter to continue)")
input()
print("Click on the 'Bot' tab to the left of the screen and click the 'Reset Token' button (Enter to continue)")
input()
print("Paste the token here and press enter to submit. NOTE: DO NOT SHARE THIS TOKEN WITH ANYONE AS IT WILL ALLOW PEOPLE TO CONTROL YOUR BOT")
token = input()
print("Scroll down in the same tab and enable the 'Server Members Intent' and the 'Message Content Intent' options")
print("These allow the Bot to actually send messages and respond to commands (Enter to continue)")
input()
print("If you wish, you can change the bot's icon and name here (Enter to continue)")
input()
print("Go to the 'General Information' tab on the left of the screen and copy the following description:")
print("Control my owner's PC with my commands!")
print("Read more here: https://github.com/3XAY/DiscordPCController/blob/main/README.md")
print("After copying, paste it into the 'Description' section (Enter to continue)")
input()
print("Now go to the 'OAuth2 tab on the left (Enter to continue)")
input()
print("Enable the 'bot' checkbox in the third column under 'OAuth2 URL Generator' (Enter to continue)")
input()
print("Scroll down and find the 'Text Permissions' column under 'Bot Permissions' and enable the following checkboxes")
print("Send messages, manage messages, embed links, attach files, read message history, use slash commands (Enter to continue)")
input()
print("Copy and open the generated URL at the bottom of the page")
print("It should open Discord and allow you to add the bot to the private server you recently made")
print("You can also add the bot to other servers if you want, but this will give those members access to the bot and therefore your computer (Enter to continue)")
input()
print("Go back to the browser and navigate to the 'Installation' tab on the left of the screen (Enter to continue)")
input()
print("Under 'Guild Install' add 'bot' to 'Scopes' (Enter to continue)")
input()
print("Add the following permissions:")
print("Attach files, embed links, manage messages, read message history, send messages, use slash commands (Enter to continue)")
input()
print("Please wait while the installer wraps everything up")

if(path.exists('Discord PC Controller')):
	installStep("", "rm Discord PC Controller -r -force", "ERROR: Please make sure Discord PC Controller isn't installed")

installStep("Downloading app...", "curl https://github.com/3XAY/DiscordPCController/releases/latest/download/Discord.PC.Controller.zip -o Discord-PC-Controller.zip", "ERROR: Unable to download app")
installStep("Unpacking app...", "Expand-Archive -Force Discord-PC-Controller.zip Discord-PC-Controller/", "ERROR: Unable to extract app")
if(screen == "N"):
	screen = '"False"'
else:
	screen = '"True"'
installStep("Creating .env file", f"'DISCORD_TOKEN={token}\nDISCORD_ID={ID}\nSEND_SCREENSHOT={screen}' >> 'Discord-PC-Controller/Discord PC Controller/_internal/.env'", "ERROR: Unable to save .env file")
installStep("Cleaning things up...", 'Remove-Item -Path Discord-PC-Controller.zip -Force', "ERROR: Unable to clean up installation files")

currDir = getcwd()
installStep("", '$shell = New-Object -ComObject WScript.Shell\n$shortcut = $shell.CreateShortcut("Run Discord Bot.lnk")\n$shortcut.TargetPath = "' + currDir + '\Discord-PC-Controller\Discord PC Controller\Discord PC Controller.exe"\n$shortcut.Save()', "ERROR: Unable to create shortcut")
print("Installer completed, press enter to start the bot")
input()
input()
installStep("Starting bot...", 'Invoke-Item "Run Discord Bot.lnk"', "ERROR: Unable to run bot")