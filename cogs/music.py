from discord.ext import commands
import youtube_dl
import discord

class Music(commands.Cog):

  def __init__(self,bot):
    self.bot = bot
    self._last_member = None
  
  async def cog_check(self, ctx):
        return True;

  FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

  @commands.command(name='play')
  async def play(self,ctx, url):
    if url:
      channel = ctx.message.author.voice.channel
      if not channel:
          await ctx.send("You are not connected to a voice channel")
          return
      voice = ctx.guild.voice_client
      if voice and voice.is_connected():
          await voice.move_to(channel)
      else:
          voice = await channel.connect()
      ydl_opts = {'format': 'bestaudio'}
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
      voice = ctx.guild.voice_client
      voice.play(discord.FFmpegPCMAudio(URL))
    else:
      ctx.send("Lien invalide")

  @commands.command(name='stop')
  async def stop(self,ctx):
    voice = ctx.guild.voice_client
    voice.stop()
    
  #VIBINNNNNNNNNNNNN

  @commands.command()
  async def vibe(self,ctx):
    await ctx.send('<a:python3:808851026739986483><a:python3:808851026739986483><a:python3:808851026739986483><a:python3:808851026739986483><a:python3:808851026739986483><a:python3:808851026739986483><a:python3:808851026739986483><a:python3:808851026739986483><a:python3:808851026739986483><a:python3:808851026739986483><a:python3:808851026739986483><a:python3:808851026739986483><a:python3:808851026739986483><a:python3:808851026739986483>')
    await self.play(ctx,'https://www.youtube.com/watch?v=NUYvbT6vTPs&ab_channel=BilalG%C3%B6regen')
  