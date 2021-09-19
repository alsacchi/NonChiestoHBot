import discord
from enums.embeds import EmbedsList
from discord.ext import commands

from cogs.Permission import Permission
from cogs.NonChiestoH import NonChiestoH
from cogs.Admin import Admin
from cogs.Audio import Audio

cogs = [
    NonChiestoH,
    Admin,
    Permission,
    Audio
]
class NonChiestoHBot(commands.Bot):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_command_error(self, ctx: commands.Context, error):
        if isinstance(error, (commands.errors.CheckFailure, commands.errors.CommandNotFound, commands.errors.CommandError)):
            await ctx.send(embed=EmbedsList.NONCHIESTO.value, reference=ctx.message)
            pass
        else:
            raise error
    def load(self):
        for cog in cogs:
            client.load_extension(f"cogs.{cog.__name__}")

    async def reload(self):
        for cog in cogs:
            client.reload_extension(f"cogs.{cog.__name__}")
    
if __name__ == "__main__":
    client = NonChiestoHBot(command_prefix="!", case_insensitive=True)
    client.load()
    with open("token.txt") as token: # Non hai il token? Non vai da nessuna parte
        client.run(token.readline())
        token.close()


    



    