# **Discord Bot**
As the name suggests, this is a Discord bot, definetly not on the level of some of the more prominant Discord bots, however for a small server with a few members this bot might be a nice addition!
# Author
Hello, my name is Lucius. This is one of my first larger projects of which is plan to add a few more features, however this was never meant for actual use in a large discord server. Perhaps in the future I will tweak it for such functions but currently its just for learning coding. 
I also have a youtube channel if you want to go and subscribe, I will have a video explaining the bot as a whole.
-  https://www.youtube.com/channel/UCm9ThRewmidHy0fyzIX_VKg (channel link)
- video not finished (video link)

# Features

This Discord bot uses Openai's API to allow you to use AI in your messages, such as asking it a question and having it respond in one app. 

- AI prompt feature, give the bot a prompt and it will respond using the !prompt command
 
- Your historical questions will be saved until the bot is restarted or you clear your history with the !clear command

- A session feature to start sessions for any need you need, such as studying or just as a timer.
- Your session will also end after X amount of minutes which allows you to remind yourself

# Lessons Learned
From making this ive learned much more about the Discord API aswell as the OpenAI API, the Discord API might prove to be useful in the future while the basic knowledge on how to use Open AI's API will almost definetly aid me in future projects of mine. This being one of my first major projects it gives me a great feeling of accomplishment when I see it work as intended.
# Acknowledgements
- Thanks to Arun for helping me figure out the Open AI API as well as guiding me through the process of making the history save

# Needed Modules
To install all needed modules, run 'pip install -r requirments.txt' in the terminal

These are all the modules that are all modules that are imported

- from discord.ext import commands, tasks
- import discord
- from dataclasses import dataclass
- import datetime
- from openai import OpenAI
- import images
- from dotenv import load_dotenv
- import os
