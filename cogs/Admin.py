from discord.ext import commands
from cogs.Permission import Permission

class Admin(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        Permission().init()

    @commands.command()
    @commands.check(Permission().isBotOwner)
    async def reload(self, ctx: commands.Context):
        await self.bot.reload()
        await ctx.send("Reload completato!", reference=ctx.message)

    @commands.command()
    @commands.check(Permission().whitelistEmpty)
    async def amOwner(self, ctx: commands.Context):
        Permission.whitelist[ctx.guild.id] = ctx.author.id
        Permission().save()
        await ctx.send(f"Ciao {ctx.author.display_name} sei l'owner del bot!", reference=ctx.message)

def setup(bot):
    bot.add_cog(Admin(bot))