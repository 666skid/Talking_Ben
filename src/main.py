import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random


Client = discord.client
client = commands.Bot(command_prefix = '')
Clientdiscord = discord.Client()

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        variable = [
            'ben/yes.mov',
            'ben/no.mov',
            'ben/hohoho.mov']
        await message.reply(file=discord.File(random.choice(variable)))



client.run('OTYwMzc3NTIzNTgwMDU1NjU0.YkpjRA.8V5yj8galAyOdaBkOwLBnPX7u-4')
