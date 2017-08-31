import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('ph help'):
        await client.send_message(message.channel, 'Hi I\'m phantom. I\'m a work' +
            'in progress right now, please be patient')
    elif message.content.startswith('ph test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('ph sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

client.run('MzUyNzExODk2MzIwNzA0NTIy.DInSpg.WkpcLr5DHa9h2yGGQMZO9iu3pd4')
