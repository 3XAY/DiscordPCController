# Discord PC Controller
If you've ever needed to do something small on your computer while you're away, this is an easy solution for you.
It's a lot lighter than a remote access solution and doesn't require anything to be installed on the client side.
Just install the bot and you're good to go. You can even add this bot to a server with **PEOPLE YOU TRUST** and watch the chaos ensue, just like when streamers let chat control their computer.

## Installation instructions:
(This [video](https://youtu.be/-H4yoyXlrEQ?si=jpTu1eZHZhg_42M7) is also available)
1. Download [InstallBot.exe](https://github.com/3XAY/DiscordPCController/releases/latest/download/InstallBot.exe)
2. Run the installer and follow all of the instructions
3. Enjoy the bot! (Run the Discord PC Controller.exe file if you need to run it again)


## Dependencies:
- `discord.py` (Connects to Discord, the actual bot part)
- `python-dotenv` (Allows the app to read info such as tokens)
- `pyautogui` (Used to control most of the computer)
- `pyscreeze` (Enables screenshots, dependency of `pyautogui`)
- `Pillow` (Enables screenshots, dependency of `pyscreeze`)

## Available Commands:
- `.type` <insert string here> (Types the input message on the server)
- `.mouse` <horizontal movement> <vertical movement> (Moves the mouse on the server, horizontal and vertical values separated by 1 space)
- `.left` (Left click on the mouse)
- `.right` (Right click on the mouse)
- `.screen` (Returns a screenshot of the server display)
- `.cmd` <insert command here> (Runs the command in Windows PowerShell, only the bot owner has access)
- `.url` <insert url here> (Opens the URL in the default browser)
- `.win` (Presses the Windows key)
- `.enter` (Presses enter)
- `.shutdown` (Shuts the entire computer down, only the bot owner has access)
- `.k` (Instantly shuts the bot down while keeping the computer on)


# CAUTION: USE AT YOUR OWN RISK, WHOEVER HAS ACCESS TO THIS BOT HAS ACCESS TO YOUR COMPUTER, I AM NOT RESPONSIBLE FOR ANY DAMAGES CAUSED BY THIS BOT
