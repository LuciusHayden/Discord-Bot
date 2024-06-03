from discord.ext import commands, tasks
import discord
from dataclasses import dataclass
import datetime
from openai import OpenAI
import images
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
OPENAI_API_KEY = os.getenv("OPENAI_KEY")
ORGANIZATION_KEY = os.getenv("ORGANIZATION_KEY")
PROJECT_ID = os.getenv("PROJECT_ID")
print(ORGANIZATION_KEY,PROJECT_ID,OPENAI_API_KEY)

MAX_SESSION_TIME = 1

client = OpenAI(
    organization=ORGANIZATION_KEY, 
    api_key=OPENAI_API_KEY,
)



@dataclass
class Session:
    is_active: bool = False
    start_time: int = 0

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
session = Session()


@bot.event
async def on_ready():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello!")
    await channel.send(images.selected)

@tasks.loop(minutes=MAX_SESSION_TIME,count=2)
async def reminder():
    if reminder.current_loop == 0:
        return 
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(f"**Take a break!** you have been studying for {MAX_SESSION_TIME} minutes.")

@bot.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, user: discord.Member):
    await ctx.send(f"**{user}** has been muted")
    await ctx.message.channel.set_permissions(user, read_messages=True, send_messages=False)

@bot.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, user: discord.Member):
    await ctx.send(f"**{user}** has been unmuted")
    await ctx.message.channel.set_permissions(user, read_messages=True, send_messages=True)

@bot.command()
async def start(ctx):
    if Session.is_active:
        await ctx.send("A session already exists")
        return
    Session.is_active = True
    Session.start_time = ctx.message.created_at.timestamp()
    readable = ctx.message.created_at.strftime("%H:%M:%S")
    reminder.start()
    await ctx.send(f"Session started at {readable}")

@bot.command()
async def end(ctx):
    if not Session.is_active:
        await ctx.send("No session is active")
        return
    
    Session.is_active = False
    end_time = ctx.message.created_at.timestamp()
    duration = end_time - Session.start_time
    readableDuration = str(datetime.timedelta(seconds=duration))
    reminder.stop()
    await ctx.send(f"Session lasted {readableDuration}")


@bot.command()
@commands.has_permissions(administrator=True)
async def prompt(ctx, *args):
    print(f"{args=}")
    prompt = " ".join(args)
    response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo",)
    print(response)
    print(prompt, type(prompt))
    print(ctx.message)
    
    await ctx.send(response.choices[0].message.content)
    

bot.run(BOT_TOKEN)