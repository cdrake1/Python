import discord


msg = ""

def run_discord_bot():
    #token and connecting through dbot file
    TOKEN = 'put token here'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        #lets us know bot connected to discord
        print(f'{client.user} has connected to discord!')

    @client.event
    async def on_message(message):
        # bot response
        global msg
        if message.author == client.user:
            return

        if message.content.startswith('hello'):
            msg = await message.channel.send('Hello!')
        elif message.content.startswith('yo'):
            msg = await message.channel.send('yo')
        elif message.content.startswith('hey'):
            msg = await message.channel.send('yo')
        elif message.content.startswith('whats up'):
            msg = await message.channel.send('not much')
        else:
            msg = await message.channel.send('yare yare daze')
        
        # logging
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        print(f"{username} said: '{user_message}' ({channel})")
        
    # authorize bot
    client.run(TOKEN)