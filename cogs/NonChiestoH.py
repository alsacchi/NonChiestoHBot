import discord
from discord import message
from enums.embeds import EmbedsList
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound

class NonChiestoH(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    #@commands.Cog.listener("on_message")
    @commands.command(help="Comunica che non avete chiesto",
                        brief="Non avete chiesto")
    async def nonchiesto(self, ctx: commands.Context, *, member: discord.Member=None):
        mentioned_user = member or ctx.author
        await ctx.send(content=mentioned_user.mention, embed=EmbedsList.NONCHIESTO.value, reference=ctx.message)
    
    @commands.command(help="Comunica che avete chiesto e siete interessati alla conversazione",
                        brief="Avete chiesto")
    async def chiesto(self, ctx: commands.Context, *, member: discord.Member=None):
        mentioned_user = member or ctx.author
        await ctx.send(content=mentioned_user.mention, embed=EmbedsList.CHIESTO.value, reference=ctx.message)
    
    @commands.command(help="PING",
                        brief="PING")
    async def ping(self, ctx: commands.Context):
        await ctx.send("PONG", reference=ctx.message)

def setup(bot):
    bot.add_cog(NonChiestoH(bot))