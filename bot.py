import random
import discord
from discord.ext.commands import Bot

BOT_PREFIX = "^"
TOKEN = 'NDkwNDQyNDg3ODQ0ODMxMjQ5.Dn5YHw.MW82PBMnAxm3QnhCON3-Q4WB_jA'

client = Bot(command_prefix=BOT_PREFIX)

muted = []


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(BOT_PREFIX + 'hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith(BOT_PREFIX + 'eightball'):
        banned_stuff = ['Rajat', 'rajat', 'RAJAT']
        if banned_stuff[0] in message.content or banned_stuff[1] in message.content or banned_stuff[2] in message.content:
            await client.send_message(message.channel, 'Shut up, {0.author.mention}'.format(message))   
        else:
            responses = ["Yes", "No", "Don't count on it...", "Chances are high...", "50/50, I'd say"]
            msg = (random.choice(responses) + ', ' + '{0.author.mention}!').format(message)
            await client.send_message(message.channel, msg)
    if message.content.startswith(BOT_PREFIX + 'ileftfortnite'):
        msg = 'Wow {0.author.mention}! You increased your chances of getting laid by 1%!'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith(BOT_PREFIX + 'rank'):
        msg = 'Sorry, but ranking other than MEE6 is still under development!'
        await client.send_message(message.channel, msg)
    if message.content.startswith(BOT_PREFIX + 'comms'):
        msg = '''
        The commands available are:
            `!hello` : Greets the user
            `!ileftfortnite` : Well, try it
            `!rank` : Please don't try it now
            `!eightball` : Answers a simple Yes/No question
        '''
        await client.send_message(message.channel, msg)
    if "SMUGFACE" in message.content.upper() or "SMUGASS" in message.content.upper():
        await client.delete_message(message)
        await client.send_message(message.channel, "No u, fucking cunt!")
    if message.content.startswith(BOT_PREFIX + 'mute'):
        muted = message.raw_mentions
        await client.add_roles(muted, discord.utils.get(message.server.roles, name='Muted'))
    if message.content.startswith(BOT_PREFIX + 'unmute'):
        unmuted = message.raw_mentions
        await client.remove_roles(unmted, discord.utils.get(message.server.roles, name='Muted'))
    if message.content.startswith(BOT_PREFIX + 'autism'):
        cont = message.content.split(" ")
        x = ""
        print(cont[1])
        i = 0
        for char in cont[1:]:
            io = random.choice([0,1])
            if io == 1:
                x += char.upper()
            else:
                x += char
        await client.send_message(message.channel, x)
    if message.content.startswith("@SlaVe") or message.content.startswith("@BotMan88#6889"):
        await client.send_message(message.channel, "Yes?")

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
