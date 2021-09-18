import discord
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound

class NonChiestoH(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    #@commands.Cog.listener("on_message")
    @commands.command()
    async def nonchiesto(self, ctx):
        await ctx.send(embed=self.bot.nonChiestoHEmbeds)
    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send("PONG", reference=ctx.message)

def setup(bot):
    bot.add_cog(NonChiestoH(bot))