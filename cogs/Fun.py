import discord
from discord.ext import commands
import random, string
from asyncio import sleep

troll={'server_id': 0, 'user_id': 0, 'mode': 0, 'emoji': None} # 1 - trolldelete, 2 - trollreaction, 3 - trollrepeat

class Fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	@commands.command()
	async def trolldelete(self, ctx, *, user:discord.Member):
		await ctx.message.delete()
		global troll
		troll['server_id']=ctx.guild.id
		troll['user_id']=user.id
		troll['mode']=1
	@commands.command(asliases=['trollreactions'])
	async def trollreaction(self, ctx, user:discord.User, emoji='🤡'):
		await ctx.message.delete()
		global troll
		troll['server_id']=-1
		troll['user_id']=user.id
		troll['emoji']=emoji
		troll['mode']=2
	@commands.command()
	async def trollrepeat(self, ctx, user:discord.User):
		await ctx.message.delete()
		global troll
		troll['server_id']=-1
		troll['user_id']=user.id
		troll['mode']=3
	@commands.command()
	async def untroll(self, ctx):
		await ctx.message.delete()
		global troll
		troll['user_id']=0
	@commands.Cog.listener()
	async def on_message(self, message):
		try:
			if troll['mode'] in [2, 3]:
				if message.author.id==troll['user_id']:
					if troll['mode']==2: await message.add_reaction(troll['emoji'])
					if troll['mode']==3: await message.reply(message.content)
			else:
				if message.author.id==troll['user_id'] and message.guild.id==troll['server_id']: await message.delete()
		except:return
	@commands.command(aliases=['react', 'reactions', 'реакция', 'реакции', 'reactionall'])
	async def reaction(self, ctx, amount: int=15, emoji='🤡'):
		await ctx.message.delete()
		messages=await ctx.channel.history(limit=amount).flatten()
		reactioned=0
		for message in messages:
			await message.add_reaction(emoji)
			reactioned+=1
		await ctx.send(f"**__Selfbot by LALOL__\n\n:white_check_mark: Успешно поставил {reactioned} реакций!**")
	@commands.command(aliases=['lags', 'лаг', 'лаги', 'ascii'])
	async def lag(self, ctx, cat='ascii', amount: int=50):
		await ctx.message.delete()
		if cat=='ascii':
			for i in range(amount):
				text=''
				for i in range(2000):
					text=text+chr(random.randrange(13000))
				await ctx.send(content=text)
		elif cat=='chains':
			text=":chains:"*250
			for i in range(amount):
				await ctx.send(text)
		else:
			await ctx.send(content="**__Selfbot by LALOL__\n\nДоступные варианты: `chains` и `ascii`**")
			return
		await ctx.send(f"**__Selfbot by LALOL__\n\n:white_check_mark: Успешно отправил {amount} лагающих сообщений!**")
def setup(bot):
	bot.add_cog(Fun(bot))
