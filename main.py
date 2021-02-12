import discord
import os
from discord.ext import commands
from cogs import *
from logging import info, warning, error, critical

bot = commands.Bot(command_prefix = '=')

@bot.event
async def on_command_error(ctx, error):
	info(f"Error: {error}. Issued by {ctx.author}")

	if isinstance(error, commands.MissingRequiredArgument):
		await bot.help_command.send_command_help(ctx, ctx.command)

	if isinstance(error, commands.CommandNotFound):
		await ctx.send(f"Commande introuvable. Fait `{bot.command_prefix[0]}help` pour obtenir de l'aide")

	if isinstance(error, commands.MissingPermissions):
		await ctx.send("Vous n'avez pas l'autorisation d'utiliser cette commande.")

@bot.event
async def on_ready():
  print("Bot activé")
  bot.add_cog(Music(bot))
  bot.add_cog(Book(bot))
  bot.add_cog(Maths(bot))
  bot.add_cog(Random(bot))
  bot.add_cog(Voice_client(bot))
  
@bot.event
async def on_message(msg):
  #Ajoute un emoji sur le =save
  if "=save" in msg.content:
    await msg.add_reaction("<:python3:763608795669725256>")
  await bot.process_commands(msg)

#Logout
@bot.command()
async def logout():
  await bot.logout()

bot.run(os.getenv('TOKEN'),reconnect = True, bot = True)