import discord
import asyncio
import youtube_dl
from discord.ext import commands

youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

ffmpeg_options = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Audio(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="disconnect", 
                        aliases=["dc", "disc"],
                        help="Scollegati dal canale vocale",
                        brief="Scollegati")
    async def disconnectCleanup(self, ctx: commands.Context):
        if not ctx.voice_client == None:
            vc: discord.VoiceProtocol = ctx.voice_client
            await vc.disconnect()

    @commands.command(help="Comunica con la tua voce soave una canzone",
                        brief="Riproduce Darude Sandstorm")
    async def play(self, ctx: commands.Context, *, url=None):
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" if url == None else url
        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)

        await ctx.send(f'Riproduco: Darude Sand.... {player.title}')

    @commands.command(help="Cambia il volume del bot",
                        brie="Cambia i volume")
    async def volume(self, ctx, volume: int):
        """Changes the player's volume"""

        if ctx.voice_client is None:
            return await ctx.send("Non sono connesso a nessun canale vocale pirla")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"Volume: {volume}%")

    @play.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("Non sei connesso a nessun canale vocale coglione!")
                raise commands.CommandError("L'autore non è connesso da nessuna parte")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()

def setup(bot):
    bot.add_cog(Audio(bot))