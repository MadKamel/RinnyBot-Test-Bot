# ( ͡° ͜ʖ ͡°)


print('''
.________________________________________________________.
|                                                        |
|	RinnyBot - a discord bot written by MadKamel.    |
|                                                        |
|insert epic/cool stuff here                             |
|                                                        |
|________________________________________________________|

RinnyBot is starting...''')



import discord
token = open('.token').read()
print('Token read, initializing the bot.')
print('Token is (' + token + ')')

# Init Discord Bot Client, with full intents.
intents = discord.Intents.all()
client = discord.Client(intents=intents)

print('Bot initialized, loading code.')

@client.event
async def on_ready():
    global LogChan # Logging channel

    LogChan = loadchan(783249066834264065) #Rinnydev logging channel
    #LogChan = loadchan(720701116127510589) # Rinnyverse logging channel

    print('RinnyBot is active.')



@client.event
async def on_message(msg):
    if msg.content[0] == '>':
        try:
            if msg.content.split(' ')[0] == '>kick':
                # This line means to kick a user by given ID.
                # example: >kick 433433822248304641
                loadguild(msg.channel.guild.id).kick(loadmember(int(msg.content.split(' ')[1]), msg.channel.guild.id))
                await msg.delete()
        except:
           pass



@client.event
async def on_message_edit(before, after):
    global LogChan

    await LogChan.send('\n**Message Edited** by ' + after.author.mention + ':\n**Channel: #' + after.channel.name + '**\nBefore: ```' + before.content + '```\nAfter: ```' + after.content + '```\n.')


async def on_message_delete(msg):
    global LogChan

    await LogChan.send('\n**Message Deleted** by ' + after.author.mention + ':\n**Channel: #' + after.channel.name + '**\nMessage: ```' + msg.content + '```\n.')


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
