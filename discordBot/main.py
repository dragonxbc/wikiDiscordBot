
import discord
import wikipediaapi
from discord.ext import commands
import datetime


b145tc0jtd55n = datetime.datetime.now()
rx920374bV = datetime.datetime(2025, 3, 10)
count82oopoint092 = rx920374bV - b145tc0jtd55n

wiki_wiki = wikipediaapi.Wikipedia('en')
page_py = wiki_wiki.page('Pokémon')

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all()) #probably change it so it doesn't interfere lol
#replace the !help command

@bot.event
async def on_ready():
    print("Bot Is Online")

@bot.command()
async def countdown(ctx): 
    await ctx.reply(count82oopoint092) #reformat this and work for inputs, see above

@bot.command()
async def ping(ctx):
    await ctx.reply(f"Pong! {round(bot.latency * 1000)}ms")

@bot.command()
async def search(ctx, *, pageName): 
    page_py = wiki_wiki.page(pageName)
    await ctx.reply("Title: %s" % page_py.title)
    str1 = page_py.summary
    if len(str1) > 2000:
        await ctx.send("Summary: %s" % page_py.summary[0:1990])
        await ctx.send("%s"% page_py.summary[1990:3980]) #highly scuffed, i need to find a way to change this
        await ctx.send(page_py.fullurl)
    elif len(str1)  < 2000:
        await ctx.send("Summary: %s" % page_py.summary[0:1990])
        await ctx.send(page_py.fullurl)

class abot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
    



# to do: 
# turn commands into slash command variation
# display a link after searching , maybe change it to being an embed ? dunno :)























bot.run("")
