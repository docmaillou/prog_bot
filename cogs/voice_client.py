from discord.ext import commands

class Voice_client(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
    self._last_member = None
  
  async def cog_check(self, ctx):
        return True;

  #Join une channel
  @commands.command(pass_context=True)
  async def join(self,ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = ctx.voice_client
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
  #Leave
  @commands.command(pass_context=True)
  async def leave(self,ctx):
    server = ctx.message.guild.voice_client
    await server.disconnect()