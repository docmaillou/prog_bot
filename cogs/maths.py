from discord.ext import commands
import random

class Maths(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
    self._last_member = None
  
  async def cog_check(self, ctx):
        return True;

    #RANDOM
  @commands.command() 
  async def rand(self,ctx,a:int,b:int):
    await ctx.send(random.randint(a, b))

  #MATHS
  @commands.command() 
  async def add(self,ctx,a:int,b:int): 
    await ctx.send(a+b)

  @commands.command() 
  async def sub(self,ctx,a:int,b:int): 
    await ctx.send(a-b)

  @commands.command() 
  async def multiply(self,ctx,a:int,b:int): 
    await ctx.send(a*b)

  @commands.command() 
  async def divide(self,ctx,a:int,b:int): 
    await ctx.send(a/b)
    