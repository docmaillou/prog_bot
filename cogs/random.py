from discord.ext import commands
import discord
import asyncio
class Random(commands.Cog):

  def __init__(self,bot):
    self.bot = bot
    self._last_member = None
  
  async def cog_check(self, ctx):
        return True;

  @commands.command()
  async def vote(self,ctx,*,question):
    message = await ctx.send("NOUVEAU VOTE : `"+question+"`")
    await message.add_reaction('<:python3:751184060784836628>')
    await message.add_reaction('<:python3:750803505534468166>')


  #Embed
  @commands.command()
  async def presentation(self,ctx):
    embed = discord.Embed(
      title = 'Prog Bot',
      description = 'Le bot du futur!',
      colour = discord.Colour.red()
    )
    embed.set_footer(text='MASSY PULLL')
    embed.set_image(url='https://media.tenor.com/images/2ef0284a5bdb2a8c5346699814059570/tenor.gif')
    embed.set_thumbnail(url='https://media.tenor.com/images/2ef0284a5bdb2a8c5346699814059570/tenor.gif')
    embed.set_author(name='Charlo',
    icon_url='https://media.tenor.com/images/2ef0284a5bdb2a8c5346699814059570/tenor.gif')
    embed.add_field(name='Les commandes', value='=cmd',inline=False)

    await ctx.send(embed=embed)
   

  #Pour que massy vienne m'aider à prog
  @commands.command()
  async def massypull(self,ctx):
    embed = discord.Embed(
      title = 'Massy',
      description = 'PULL',
      colour = discord.Colour.red()
    )
    embed.set_footer(text='MASSY PULLL')
    embed.set_image(url='https://i.pinimg.com/originals/e4/26/70/e426702edf874b181aced1e2fa5c6cde.gif')
    embed.set_thumbnail(url='https://media.tenor.com/images/2ef0284a5bdb2a8c5346699814059570/tenor.gif')
    embed.set_author(name='Charlo',
    icon_url='https://i.imgur.com/cyzsgKt.gif')
    embed.add_field(name='Jvais te niquer', value='pull pull pull',inline=False)
    await ctx.send(embed=embed)
    await asyncio.sleep(5)
    await ctx.send(embed=embed)
    await asyncio.sleep(10)
    await ctx.send(embed=embed)

    #Help
  @commands.command(pass_context=True)
  async def cmd(self,ctx):
    author = ctx.message.author

    embed = discord.Embed(
      colour = discord.Colour.orange()
    )
    embed = discord.Embed(
      title = 'Les commandes',
      description = 'Les commandes les plus utiles du bot!',
      colour = discord.Colour.blue()
    )
    embed.set_thumbnail(url='https://www.texasobserver.org/wp-content/uploads/2020/09/pepe_poster.jpg')
    embed.set_author(name='CharloGriot Bot',
    icon_url='https://i.kym-cdn.com/photos/images/newsfeed/001/582/322/94d.png')
    embed.set_footer(text='Crédit : Charlo')
    embed.add_field(name='`=vibe`', value='Just do it...', inline=False)
    embed.add_field(name='`=rand`', value='Entre le nombre x et y que vous entré (ex : =rand 1 2)', inline=False)
    embed.add_field(name='`=add`', value='Addition', inline=False)
    embed.add_field(name='`=sub`', value='Soustraction', inline=False)
    embed.add_field(name='`=divide`', value='Division', inline=False)
    embed.add_field(name='`=multiply`', value='Multiplication', inline=False)
    embed.add_field(name='`=join`', value='Le bot rejoignera le channel', inline=False)
    embed.add_field(name='`=leave`', value='Le bot quittera le channel', inline=False)
    embed.add_field(name='`=save`', value='Sauvegarde du texte dans une db au choixEx : =save code "DU CODE".', inline=False)
    embed.add_field(name='`=book`', value='Donne la liste de tous les messages dans une db entrée', inline=False)
    embed.add_field(name='`=find`', value='Recherche dans la catégorie entrée, la phrase ou le mot entré',inline=False)
    embed.add_field(name='`=delBook`', value='Supprimer la catégorie entrée et ses messages', inline=False)
    embed.add_field(name='`=play`', value='Joue la musique désiré avec un lien youtube', inline=False)
    embed.add_field(name='`=stop`', value='Arrête la musique qui joue présentement', inline=False)
    embed.add_field(name='`=vote`', value='Crée une question que les gens pourront voter', inline=False)
    await author.send(embed=embed)