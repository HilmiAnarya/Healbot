import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Started")

@client.command()
async def halo(ctx):
    await ctx.send("Halo juga")

@client.command()
async def bye(ctx):
    await ctx.send("dadah")

@client.command()
async def sakit(ctx):
    await ctx.send("minum obat")

@client.command()
async def lapar(ctx):
    await ctx.send("makan dulu!")

client.run("MTE0OTkxNjY0OTgwNjM3Njk3Mg.GXYeG8._PBVgJcpoLX-KR5xRtCcaffy5p4U6DKTjVtvRY")