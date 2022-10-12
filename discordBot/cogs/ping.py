import discord
from discord import app_commands
from discord.ext import commands

class ping(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot
    
  @commands.Cog.listener()
  async def on_ready(self):
    print('Ping cog loaded.')
  

  @commands.command()
  async def sync(self,ctx) -> None:
    fmt = await ctx.bot.tree.sync(guild=ctx.guild)
    await ctx.send(f'Synced {len(fmt)} commands.')

  @app_commands.command(name="ping", description="returns ping")
  async def ping(self, interaction: discord.Interaction):
    embed = discord.Embed(title=f"Pong! {round(self.bot.latency * 1000)}ms")
    await interaction.response.send_message(embed=embed)

async def setup(bot):
  await bot.add_cog(ping(bot),guilds=[discord.Object(id=905509936061087814)])
