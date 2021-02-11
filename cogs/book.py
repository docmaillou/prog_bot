from discord.ext import commands
from replit import db

class Book(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
    self._last_member = None
  
  async def cog_check(self, ctx):
        return True;
  #Save de la prog
  #Enregistré une note
  @commands.command()
  async def save(self,ctx,laDb,*,prog_msg):
    if laDb not in db.keys():
      db[laDb] = []
    
    zeDb = db[laDb]
    zeDb.append(prog_msg + " // " + str(ctx.message.author))
    db[laDb] = zeDb
    await ctx.send("Message enregistré : ["+laDb+"] " + prog_msg)

  #Liste de tous les notes dans la db choisi
  @commands.command()
  async def book(self,ctx,laDb):
    if laDb in db.keys():
      if db[laDb]:
        str1 = '\n'.join(db[laDb])
        await ctx.send(str1)
      else:
        await ctx.send("Aucun enregristrement dans : " + laDb)
  #Supprimer tout
  @commands.command()
  async def deleteAll(self,ctx,laDb):
    if laDb in db.keys():
      db[laDb] = []
      await ctx.send("[" + laDb + "] à été supprimé avec tous ses enregistrements.")

  @commands.command()
  async def delNote(self,ctx,laDb,*,recherche):
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
    
  @commands.command()
  async def delBook(self,ctx,laDb,*,recherche):
    if db[laDb] and recherche:
      del db[laDb]
      await ctx.send("Le livret contenants : " + recherche + " ont été supprimé.")
    else:
      await ctx.send("Erreur. Élément invalide.")


  @commands.command()
  async def find(self,ctx,laDb,*,recherche):
    recherche = recherche.lower()
    if db[laDb] and recherche:
      filter_object = filter(lambda a: recherche in a.lower(), db[laDb])
      await ctx.send('\n'.join(list(filter_object)))
    else:
      await ctx.send("La catégorie recherché est innexistante.")

      