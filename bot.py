import random
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
import psycopg2


BOT_PREFIX = "/"

TOKEN = 'NDkwNDQyNDg3ODQ0ODMxMjQ5.XdUjBQ.W3tF180dhyrwTQKdbwI7aPUAh5U'

client = Bot(command_prefix=BOT_PREFIX)
muted = []

conn = psycopg2.connect(dbname="node", user="postgres", password="123456")
cur = conn.cursor()

def retrieve_ranks(person):
    if person == "":
        cur.execute("SELECT name, awards_won FROM members ORDER BY awards_won DESC")
        a = cur.fetchall()    
    else:
        cur.execute("SELECT name, awards_won FROM members WHERE name='%s' ORDER BY awards_won DESC" % person)
        a = cur.fetchall()
    return a

def bump(person):
    score = retrieve_ranks(person)[0][1] + 1
    cur.execute("UPDATE members SET awards_won = %d WHERE name='%s'" % (score, person))
    conn.commit()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command
async def initranks(ctx):
    server_name = ctx.guild
    cur.execute("CREATE TABLE %s (name, points)" % server_name)
    for member in ctx.guild.members:
        cur.execute("INSERT INTO %s (name, points) values (%s, 0)" % (server_name, member.name))
        conn.commit()
        print("ok")
    ctx.message.channel.send("Initialized ranking system")

@client.event
async def on_message(message):
    if message.content.startswith(BOT_PREFIX + 'hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.content.startswith(BOT_PREFIX + 'eightball'):
        responses = ["Yes", "No", "Don't count on it...", "Chances are high...", "50/50, I'd say"]
        msg = (random.choice(responses) + ', ' + '{0.author.mention}!').format(message)
        await message.channel.send(msg)

    if message.content.startswith(BOT_PREFIX + 'ileftfortnite'):
        msg = 'Wow {0.author.mention}! You increased your chances of getting laid by 1%!'.format(message)
        await message.channel.send(msg)
    if message.content.startswith(BOT_PREFIX + 'bump'):
        person = message.mentions[0].nick
        bump(person)
        god = retrieve_ranks("")
        for guild in client.guilds:
            for member in guild.members:
                for role in member.roles:
                    if role.name == "God":
                        await member.remove_roles(get(member.guild.roles, name="God"))
                if member.nick == god[0][0]:
                    god_member = member
                    role = get(god_member.guild.roles, name="God")
                    await god_member.add_roles(role)
        await message.channel.send(person + " has been bumped")
    if message.content.startswith(BOT_PREFIX + 'rank'):
        god = retrieve_ranks("")
        msg = ""
        for guild in client.guilds:
            godman = god[0][0]
            for member in guild.members:
                for i in god:
                    if i[0] == member.nick:
                        msg+=  member.name + " : " + str(i[1]) + "\n"
        await message.channel.send(msg)

    if message.content.startswith(BOT_PREFIX + 'help'):
        msg = ('''
        The commands available are:
            `%shello` : Greets the user
            `%sileftfortnite` : Well, try it
            `%sbump @person`: Increases a person's rank
            `%srank` : Everyone's ranks
            `%seightball` : Answers a simple Yes/No question
        ''' % (BOT_PREFIX, BOT_PREFIX, BOT_PREFIX, BOT_PREFIX, BOT_PREFIX))
        await message.channel.send(msg)

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
        await message.channel.send('https://www.youtube.com/watch?v=kJQP7kiw5Fk')
        await message.channel.send('Want me to sing?')
        if 'YES' in message.content.upper():
            await message.channel.send('''Despacito Quiero respirar tu cuello despacito Deja que te diga cosas al oído Para que te acuerdes si no estás conmigo Despacito Quiero desnudarte a besos despacito Firmo en las paredes de tu laberinto''', tts=True)

client.run(TOKEN)   