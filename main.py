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
            'https://cdn.discordapp.com/attachments/946549502590976040/947015921107628054/video-output-9D64EA54-2F73-42A9-9A23-738F2ACA1FB5.mov',
            'https://media.discordapp.net/attachments/945616095820279818/949501258732040202/video-output-1048F815-A992-4B05-B1A2-5CAB0851CDC1.mov',
            'https://cdn.discordapp.com/attachments/946549502590976040/947016570666909776/video-output-15DFA988-4E24-494F-8938-8E17816923EE.mov',]
        await message.channel.send(random.choice(variable))



client.run('OTYwMzc3NTIzNTgwMDU1NjU0.YkpjRA.8V5yj8galAyOdaBkOwLBnPX7u-4')
