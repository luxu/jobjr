import discord
from discord.ext import commands, ipc
from decouple import config

TOKEN = config('DISCORD_TOKEN')


def ex_1():
    class MyClient(discord.Client):
        async def on_ready(self):
            print('Logged on as', self.user)

        async def on_message(self, message):
            # don't respond to ourselves
            if message.author == self.user:
                return

            if message.content == 'ping':
                await message.channel.send('pong')

    intents = discord.Intents.default()
    intents.message_content = True
    client = MyClient(intents=intents)
    client.run('token')


def ex_2():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='>', intents=intents)

    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')

    bot.run('token')

def connection_discord(client):
    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    client.run(TOKEN)

class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ipc = ipc.Server(self, secret_key="this_is_secret")  # used tonnect ipc server to other servers

    async def on_ready(self):
        """Called upon the READY event"""
        print("Bot is ready.")

    async def on_ipc_ready(self):
        """Called upon the IPC Server being ready"""
        print("Ipc server is ready.")

    async def on_ipc_error(self, endpoint, error):
        """Called upon an error being raised within an IPC route"""
        print(endpoint, "raised", error)

if __name__ == '__main__':
    # ex_1()
    # intents = jobjs.Intents.default()
    # intents.typing = False
    # intents.presences = False
    # client = jobjs.Client(intents=intents)
    # connection_discord(client)
    my_bot = MyBot(command_prefix="$", intents=discord.Intents.default())  # prefix to ping the bot
    @my_bot.command()
    async def hello(ctx):
        await ctx.send("Hello there!")  # response from the bot when you send $hello
    my_bot.ipc.start()
    my_bot.run(TOKEN)

