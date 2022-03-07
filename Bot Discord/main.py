import json
import discord

import stringVerify
import work
import help

client = discord.Client()

f = open("keys.env")
content = f.read()
data = json.loads(content)
f.close()

def nemWork(message):
    return work.input(message)

def printHelp(message):
    return help.input(message)


@client.event
async def on_message(message):

    if message.content.startswith("-mth ping"):
        await message.channel.send("pong")

    if message.content.startswith("-mth help"):
        await message.channel.send(printHelp(message.content))

    elif message.content.startswith("-mth "):
        await message.channel.send(nemWork(message.content))


client.run(data["BotKey"])