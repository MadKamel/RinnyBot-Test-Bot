# ( ͡° ͜ʖ ͡°)


print('''
.________________________________________________________.
|                                                        |
|	RinnyBot - a discord bot written by MadKamel.          |
|                                                        |
|insert epic/cool stuff here                             |
|                                                        |
|________________________________________________________|

RinnyBot is starting...''')
embedsoff = False


import discord
token = open('.token').read()
print('Token read, initializing the bot.')
#print('Token is (' + token + ')')

# Init Discord Bot Client, with full intents.
intents = discord.Intents.all()
client = discord.Client(intents=intents)

print('Bot initialized, loading code.')

@client.event
async def on_ready():
    global LogChan # Logging channel

    LogChan = loadchan(796421683769638953) #Kamel Realm logging channel
    #LogChan = loadchan() # Rinnyverse logging channel

    print('RinnyBot is active.')



@client.event
async def on_message(msg):
    print('\nINCOMING:===============\n@ ' + msg.author.name + '\n# ' + msg.channel.name + '\n= ' + msg.content + '\n========================\n')
    #if msg.content[0] == '>':
    try:
        if msg.content.split(' ')[0] == '>kick':
          # This line means to kick a user by given ID.
          # example: >kick 433433822248304641
          loadguild(msg.channel.guild.id).kick(loadmember(int(msg.content.split(' ')[1])))
    except:
        pass



@client.event
async def on_message_edit(before, after):
    if embedsoff:
        global LogChan

        await LogChan.send('\n**Message Edited** by** ' + after.author.name + ':\n**Channel: #' + after.channel.name + '\nBefore: ```' + before.content + '```\nAfter: ```' + after.content + '```\n')
    else:
        beforemsg = before.content
        aftermsg = after.content
        
        #Thanks to stackoverflow for this code here
        embedMsg = discord.Embed(title="Message edited in #" + before.channel.name + ".", description=before.author.mention, color=0x00ff00)
        embedMsg.set_thumbnail(url=before.author.avatar_url)
        embedMsg.add_field(name="Before", value=beforemsg, inline=False)
        embedMsg.add_field(name="After", value=aftermsg, inline=False)
        await LogChan.send(embed=embedMsg)

@client.event
async def on_message_delete(msg):
    if embedsoff:
        global LogChan

        await LogChan.send('\n**Message Deleted** Author:** ' + msg.author.name + ':\n**Channel: #' + msg.channel.name + '\nBefore: ```' + msg.content + '```\n')
    else:
        beforemsg = msg.content
        
        #Thanks to stackoverflow for this code here
        embedMsg = discord.Embed(title="Message deleted in #" + msg.channel.name + ".", description=msg.author.mention, color=0x0000ff)
        embedMsg.set_thumbnail(url=msg.author.avatar_url)
        embedMsg.add_field(name="Message", value=beforemsg, inline=False)
        await LogChan.send(embed=embedMsg)

def loadchan(id): # Loads a channel
    global client
    print('Channel #' + str(client.get_channel(id)) + ' loaded.')
    return client.get_channel(id)

def loadrole(guild, id): # Loads a role from a specific guild
    print('Role <' + str(guild.get_role(id)) + '> loaded.')
    return guild.get_role(id)

def loadguild(id): # Loads a guild (server)
    global client
    print('Guild ' + str(client.get_guild(id)) + ' loaded.')
    return client.get_guild(id)

def loadmember(guild, id): # Loads a member from an id
    print('User @' + str(guild.get_member(id)) + ' loaded.')
    return guild.get_member(id)

async def setstatus(activity):
    global client
    print('Setting status to: ' + activity)
    await client.change_presence(status=discord.Status.online, activity=discord.Game(activity))



print('Running RinnyBot...')

client.run(token)
