import os

import discord
import django
from httpx import get

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(".")))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jobjr.settings")

django.setup()

from django.conf import settings

bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")


@bot.command()  # This is the decorator we use to create a prefixed command.
async def ping(ctx):  # This is the function we will use to create the command.
    await ctx.send("Pong!")  # This is the response the bot will send.


@bot.command()
async def jobs_local(ctx):
    BASE_URL = settings.SERVER
    endpoint = 'v1/listar/'
    url = "".join((BASE_URL, endpoint))
    resultado = get(url).json()['data']
    line = "-"*60
    for item in resultado:
        job = " - ".join(
            (item['titulo'], item['url'])
        )
        await ctx.send(job)

    await ctx.send(f'{line}Lista Finalizada com sucesso!{line}')


if __name__ == '__main__':
    token = 'MTA3NDEwMjc2NDI3MzE1NjIwMA.GA8_Ry.6jkwf5W6rh8pYPFBZQ6s3ov29YjxNXp8OenPmw'
    guild_id = 1074341893787365496
    app_client_id = ''
    app_client_secret = ''
    redirect_uri = ''
    bot.run(token)
