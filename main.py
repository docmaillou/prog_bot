import discord
import os
from discord.ext import commands
from replit import db
from cogs import *
import random

bot = commands.Bot(command_prefix = '=')


@bot.event
async def on_ready():
  bot.add_cog(music(bot))

@bot.event
async def on_message(msg):
  #Ajoute un emoji sur le =save
  if "=save" in msg.content:
    await msg.add_reaction("<:python3:763608795669725256>")
  await bot.process_commands(msg)

#In Progress
@bot.command()
async def delNote(ctx,laDb,*,recherche):
  recherche = recherche.lower()
  if db[laDb] and recherche:
    filter_object = filter(lambda a: recherche in a.lower(), db[laDb])
    for i in list(filter_object):
      #Bug ici
      index = db[laDb].index(list(filter_object)[i])
    del db[laDb[index]]
    await ctx.send("Les éléments contenants : " + recherche + " ont été supprimé.")
  else:
    await ctx.send("Erreur. Élément invalide.")
    
    
#FONCTIONNE
  
@bot.command()
async def delBook(ctx,laDb,*,recherche):
  if db[laDb] and recherche:
    del db[laDb]
    await ctx.send("Le livret contenants : " + recherche + " ont été supprimé.")
  else:
    await ctx.send("Erreur. Élément invalide.")


@bot.command()
async def find(ctx,laDb,*,recherche):
  recherche = recherche.lower()
  if db[laDb] and recherche:
    filter_object = filter(lambda a: recherche in a.lower(), db[laDb])
    await ctx.send('\n'.join(list(filter_object)))
  else:
    await ctx.send("La catégorie recherché est innexistante.")

@bot.command()
async def vote(ctx,*,question):
  message = await ctx.send("NOUVEAU VOTE : `"+question+"`")
  await message.add_reaction('<:python3:751184060784836628>')
  await message.add_reaction('<:python3:750803505534468166>')


#Save de la prog
#Enregistré une note
@bot.command()
async def save(ctx,laDb,*,prog_msg):
  if laDb not in db.keys():
    db[laDb] = []
  
  zeDb = db[laDb]
  zeDb.append(prog_msg + " // " + str(ctx.message.author))
  db[laDb] = zeDb
  await ctx.send("Message enregistré : ["+laDb+"] " + prog_msg)

#Liste de tous les notes dans la db choisi
@bot.command()
async def book(ctx,laDb):
  if laDb in db.keys():
    if db[laDb]:
      str1 = '\n'.join(db[laDb])
      await ctx.send(str1)
    else:
      await ctx.send("Aucun enregristrement dans : " + laDb)
#Supprimer tout
@bot.command()
async def deleteAll(ctx,laDb):
  if laDb in db.keys():
    db[laDb] = []
    await ctx.send("[" + laDb + "] à été supprimé avec tous ses enregistrements.")

#Embed
@bot.command()
async def presentation(ctx):
  embed = discord.Embed(
    title = 'Prog Bot',
    description = 'Le bot du futur!',
    colour = discord.Colour.red()
  )
  embed.set_footer(text='Thicc dogo')
  embed.set_image(url='https://i.kym-cdn.com/photos/images/newsfeed/001/582/322/94d.png')
  embed.set_thumbnail(url='https://i.kym-cdn.com/photos/images/newsfeed/001/582/316/83b.jpg')
  embed.set_author(name='Prog Bot',
  icon_url='https://i.kym-cdn.com/photos/images/newsfeed/001/582/322/94d.png')
  embed.add_field(name='Les commandes', value='=cmd',inline=False)

  await ctx.send(embed=embed)

#Help
@bot.command(pass_context=True)
async def cmd(ctx):
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
  embed.add_field(name='`=find`', value='Recherche dans la catégorie entrée, la phrase ou le mot entré', inline=False)
  embed.add_field(name='`=delBook`', value='Supprimer la catégorie entrée et ses messages', inline=False)
  embed.add_field(name='`=play`', value='Joue la musique désiré avec un lien youtube', inline=False)
  embed.add_field(name='`=stop`', value='Arrête la musique qui joue présentement', inline=False)
  embed.add_field(name='`=vote`', value='Crée une question que les gens pourront voter', inline=False)
  await author.send(embed=embed)

#Join une channel
@bot.command(pass_context=True)
async def join(ctx):
  channel = ctx.message.author.voice.channel
  if not channel:
      await ctx.send("You are not connected to a voice channel")
      return
  voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
  if voice and voice.is_connected():
      await voice.move_to(channel)
  else:
      voice = await channel.connect()


#RANDOM
@bot.command() 
async def rand(ctx,a:int,b:int):
  await ctx.send(random.randint(a, b))

#MATHS
@bot.command() 
async def add(ctx,a:int,b:int): 
  await ctx.send(a+b)

@bot.command() 
async def sub(ctx,a:int,b:int): 
  await ctx.send(a-b)

@bot.command() 
async def multiply(ctx,a:int,b:int): 
  await ctx.send(a*b)

@bot.command() 
async def divide(ctx,a:int,b:int): 
  await ctx.send(a/b)

#Leave
@bot.command(pass_context=True)
async def leave(ctx):
  server = ctx.message.guild.voice_client
  await server.disconnect()

#Logout
@bot.command()
async def logout():
  await bot.logout()

bot.run(os.getenv('TOKEN'),reconnect = True, bot = True)