import discord
from discord.ext import commands

from cogs.Permission import Permission
from cogs.NonChiestoH import NonChiestoH
from cogs.Admin import Admin


cogs = [
    NonChiestoH,
    Admin,
    Permission
]
class NonChiestoHBot(commands.Bot):
    nonChiestoHEmbeds = discord.Embed()
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        self.nonChiestoHEmbeds.set_image(url="https://cdn.discordapp.com/attachments/255063370804232192/887793381219139594/photo_2021-09-15_18-07-06.jpg")
        self.nonChiestoHEmbeds.add_field(name="🍌ChiestoH?🍌", value="NooooH!")

    async def on_command_error(self, ctx: commands.Context, error):
        if isinstance(error, (commands.errors.CheckFailure, commands.errors.CommandNotFound)):
            await ctx.send(embed=self.nonChiestoHEmbeds, reference=ctx.message)
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
    client.run('***REMOVED***')


    



    