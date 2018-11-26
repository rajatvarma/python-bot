import random
import discord

from discord.ext.commands import Bot

BOT_PREFIX = "^"
TOKEN = 'NDkwNDQyNDg3ODQ0ODMxMjQ5.Dn5YHw.MW82PBMnAxm3QnhCON3-Q4WB_jA'

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(BOT_PREFIX + 'hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith(BOT_PREFIX + 'eightball'):
        responses = ["Yes", "No", "Don't count on it...", "Chances are high...", "50/50, I'd say"]
        msg = (random.choice(responses) + ', ' + '{0.author.mention}!').format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith(BOT_PREFIX + 'ileftfortnite'):
        msg = 'Wow {0.author.mention}! You increased your chances of getting laid by 1%!'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith(BOT_PREFIX + 'rank'):
        msg = 'Sorry, but ranking other than MEE6 is still under development!'
        await client.send_message(message.channel, msg)

    if message.content.startswith(BOT_PREFIX + 'help'):
        msg = '''
        The commands available are:
            `%shello` : Greets the user
            `%sileftfortnite` : Well, try it
            `%srank` : Please don't try it now
            `%seightball` : Answers a simple Yes/No question
        '''.format(BOT_PREFIX)
        await client.send_message(message.channel, msg)

    if message.content.startswith(BOT_PREFIX + 'mute'):
        muted = message.raw_mentions
        await client.add_roles(muted, discord.utils.get(message.server.roles, name='Muted'))

    if message.content.startswith(BOT_PREFIX + 'unmute'):
        unmuted = message.raw_mentions
        await client.remove_roles(unmted, discord.utils.get(message.server.roles, name='Muted'))

    if message.content.startswith(BOT_PREFIX + 'autism'):
        cont = message.content.split(" ")
        x = ""
        print(cont[1:])
        i = 0
        for char in cont[1:]:
            if i & 2 == 0:
                x += char
            else:
                x += char.upper()
            i += 1
        await client.send_message(message.channel, x)

    if message.content.upper() == "ALEXA, PLAY DESPACITO" or message.content.upper() == "ALEXA PLAY DESPACITO":
        await client.send_message(message.channel, 'https://www.youtube.com/watch?v=kJQP7kiw5Fk')
        await client.send_message(message.channel, 'Want me to sing?')
        if 'yes' in message.content.upper():
            await client.send_message(message.channel, '''Despacito Quiero respirar tu cuello despacito Deja que te diga cosas al oído Para que te acuerdes si no estás conmigo Despacito Quiero desnudarte a besos despacito Firmo en las paredes de tu laberinto''', tts=True)
        else:
        await client.send_message(message.channel, 'Suit yourself')            


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command(name='9gag', description='Sends a pic with the specified tag')
async def ninegag(call):
    pass


client.run(TOKEN)
