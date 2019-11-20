import random
import discord
from discord.ext.commands import Bot
import psycopg2


BOT_PREFIX = "/"

TOKEN = 'NDkwNDQyNDg3ODQ0ODMxMjQ5.Dn5YHw.MW82PBMnAxm3QnhCON3-Q4WB_jA'

client = Bot(command_prefix=BOT_PREFIX)
server_id = 631064048947167242

muted = []

ranks = {}
conn = psycopg2.connect(dbname="node", user="postgres", password="123456")
cur = conn.cursor()
cur.execute("SELECT name, awards_won FROM members ORDER BY awards_won DESC")
god = cur.fetchall()


'''for member in server_members:
        if member.nick == god:
            client.add_roles(member, discord.utils.get(server.Server.roles, name="God"))'''

@client.event
async def on_message(message):
    if message.content.startswith(BOT_PREFIX + 'hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)
        #client.add_roles(, discord.utils.get(message.Server.roles, name="God"))


    if message.content.startswith(BOT_PREFIX + 'eightball'):
        responses = ["Yes", "No", "Don't count on it...", "Chances are high...", "50/50, I'd say"]
        msg = (random.choice(responses) + ', ' + '{0.author.mention}!').format(message)
        await message.channel.send(sage.channel, msg)

    if message.content.startswith(BOT_PREFIX + 'ileftfortnite'):
        msg = 'Wow {0.author.mention}! You increased your chances of getting laid by 1%!'.format(message)
        await message.channel.send(msg)
    if message.content.startswith(BOT_PREFIX + 'rank'):
        msg = ""
        for guild in client.guilds:
            godman = god[0][0]
            for member in guild.members:
                for i in god:
                    if i[0] == member.nick:
                        msg+=  member.name + " " + str(i[1]) + "\n"
                if member.nick in god:
                    await client.add_roles(member, discord.utils.get(message.server.roles, name="God"))

            

        await message.channel.send(msg)
    if message.content.startswith(BOT_PREFIX + 'comms'):
        msg = '''
        The commands available are:
            `hello` : Greets the user
            `ileftfortnite` : Well, try it
            `rank` : Please don't try it now
            `eightball` : Answers a simple Yes/No question
        '''
        await message.channel.send(msg)

    if message.content.startswith(BOT_PREFIX + 'rank'):
        msg = 'Sorry, but ranking other than MEE6 is still under development!'
        await client.send_message(message.channel, msg)

    if message.content.startswith(BOT_PREFIX + 'help'):
        msg = ('''
        The commands available are:
            `%shello` : Greets the user
            `%sileftfortnite` : Well, try it
            `%srank` : Please don't try it now
            `%seightball` : Answers a simple Yes/No question
        ''' %BOT_PREFIX)
        await client.send_message(message.channel, msg)

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
        await message.channel.send(x)

    if message.content.upper() == "ALEXA, PLAY DESPACITO" or message.content.upper() == "ALEXA PLAY DESPACITO":
        await client.send_message(message.channel, 'https://www.youtube.com/watch?v=kJQP7kiw5Fk')
        await client.send_message(message.channel, 'Want me to sing?')
        if 'yes' in message.content.upper():
            await client.send_message(message.channel, '''Despacito Quiero respirar tu cuello despacito Deja que te diga cosas al oído Para que te acuerdes si no estás conmigo Despacito Quiero desnudarte a besos despacito Firmo en las paredes de tu laberinto''', tts=True)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    client.run(TOKEN)
