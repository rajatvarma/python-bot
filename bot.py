import random
import discord
#from lxml import etree

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
print(god)
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
        banned_stuff = ['Rajat', 'rajat', 'RAJAT']
        if banned_stuff[0] in message.content or banned_stuff[1] in message.content or banned_stuff[2] in message.content:
            await client.send_message(message.channel, 'Shut up, {0.author.mention}'.format(message))   
        else:
            responses = ["Yes", "No", "Don't count on it...", "Chances are high...", "50/50, I'd say"]
            msg = (random.choice(responses) + ', ' + '{0.author.mention}!').format(message)
            await client.send_message(message.channel, msg)
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
    if message.content.startswith(BOT_PREFIX + 'mute'):
        muted = message.raw_mentions
        await client.add_roles(muted, discord.utils.get(message.server.roles, name='Muted'))
    if message.content.startswith(BOT_PREFIX + 'unmute'):
        unmuted = message.raw_mentions
        await client.remove_roles(unmuted, discord.utils.get(message.server.roles, name='Muted'))




@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    for i in range(len(god)):
        for j in range(i, len(god)):
            if god[i][1] < god[j][1]:
                c = god[i]
                god[i] = god[j]
                god[j] = c
    


    client.run(TOKEN)
