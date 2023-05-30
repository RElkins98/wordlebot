#!/usr/bin/env python3
import discord
from datetime import datetime
import re
import asyncio
import wordleServer
import wordleCast
from discord.ext import commands, tasks, MemberConverter

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="?", intents=intents)
converter = MemberConverter()

@client.event
async def on_message(message):
  

@bot.event()
async def on_ready():
  time_check.start()

@bot.event()
async def on_disconnect():
  time_check.stop()

@bot.command()
async def stats(ctx, member):
  if member == "":
    user = ctx.author
  else:
    try:
      user = await converter.convert(ctx, member)
    except MemberNotFound:
      ctx.send("That user is not in my database yet! They should ?register and play some wordle ;)")
      return
  if(user):
    user = 

@tasks.loop(seconds=10)
async def time_check():
  now = datetime.strftime(datetime.now(), '%H:%M')
  print(now)

server = wordleServer()
bot.run(os.getenv("TOKEN"))
