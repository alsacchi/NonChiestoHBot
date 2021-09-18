import json
from discord.ext import commands
from pathlib import Path

FILE_NAME = "permissions.json"
class Permission(commands.Cog):
    whitelist = {}
    def __init__(self, bot: commands.Context=None):
        self.bot = bot

    def init(self):
        if(self.fileExists(FILE_NAME)):
            self.load()
        else:
            self.save()


    def fileExists(self, path):
        fle = Path(path)
        return fle.exists()

    def load(self):
        with open(FILE_NAME) as jsonz:
            Permission.whitelist = json.load(jsonz)
            jsonz.close()

    def save(self): 
        with open(FILE_NAME, "w") as jsonz:
            json.dump(Permission.whitelist, jsonz)
            jsonz.close()

    def isBotOwner(self, ctx: commands.Context):
        if Permission.whitelist[str(ctx.guild.id)] == ctx.author.id:
            return True
        return False

    def whitelistEmpty(self, ctx: commands.Context):
        if str(ctx.guild.id) in Permission.whitelist:
            return False
        return True

def setup(bot):
    bot.add_cog(Permission(bot))