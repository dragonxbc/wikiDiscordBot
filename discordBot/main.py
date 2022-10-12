import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents, application_id='1029161693625991175')#change the id based on the application id of your bot in the portal

@bot.event
async def on_ready():
  print('Logged in.')

async def load():
  for file in os.listdir('./cogs'):
    if file.endswith('.py'):
      await bot.load_extension(f'cogs.{file[:-3]}')

async def main():
  await load()
  await bot.start("")#insert bot token. will most likely use config file for this one later down the line
    
asyncio.run(main())

# to do: 
# turn commands into slash command variation (DONE)
# display a link after searching (DONE)
# maybe search output to being an embed - reason: can take up to 6000 characters collectively instead of just 2k in a normal discord message (DONE)
# replace the !help command to display parameter inputs, easier for user
# use cogs, clean up code (DONE)
# work on potential edge cases that pop up
# maybes:
# weather searching functionality?
# datetime / timezone checker
# 
