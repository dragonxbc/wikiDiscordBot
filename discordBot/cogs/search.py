import discord
from discord import app_commands
from discord.ext import commands
import wikipediaapi

class search(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot
    
  @commands.Cog.listener()
  async def on_ready(self):
    print('Search cog loaded.')
  
  @commands.command()
  async def sync2(self,ctx) -> None:
    fmt = await ctx.bot.tree.sync(guild=ctx.guild)
    await ctx.send(f'Synced {len(fmt)} commands.')
  
  @app_commands.command(name="search", description="returns a wikipedia summary & url")
  async def search(self, interaction: discord.Interaction, search: str):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page('Pokémon')
    page_py = wiki_wiki.page(search)
    pageLength = page_py.summary
    if len(pageLength) > 5900:
      embed = discord.Embed(title= "%s"%page_py.title,description="%s"%page_py.summary[0:5900])
    if len(pageLength) < 5900:
      embed = discord.Embed(title= "%s"%page_py.title,description="%s"%page_py.summary)
    embed.add_field(name = "URL: ", value = page_py.fullurl)
    await interaction.response.send_message(embed=embed)



async def setup(bot):
  await bot.add_cog(search(bot),guilds=[discord.Object(id=905509936061087814)])#change the id based on the server you're in
