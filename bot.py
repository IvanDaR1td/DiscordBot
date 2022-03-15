import token
import discord
import time
from discord.ext import commands
import datetime
import os
from time import sleep

now = datetime.datetime.now()
print("Gestartet")
print(str(now))
datei = open('bot-log.txt','a')
datei.write("\r\n" + str(now) + "     Bot gestartet")
datei.close()

TOKEN = 'OTUzMDkxMDY2MTA0NTQxMTk0.Yi_hOQ.-DK-pTU1GfndIMYTTJfzKYIuBwc'

client = commands.Bot(command_prefix='-')

description = '''PepegaBot in Python'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def hello(ctx):
    """Says POG,Nice to meet you"""
    await ctx.send("POG,Nice to meet you")


@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    left=int(left)
    right=int(right)
    if ValueError:
        await bot.say("u bum give me 2 numbers like dis 'num1 num2'")
    await bot.say(left + right)

@bot.command()
async def status():
    """Show system info"""
    bashCommand = "free | grep Mem | awk '{printf(\"...\\nFree memory: %.1f%%\\n\", $4/$2*100.0 ) }' && vcgencmd measure_temp | sed 's/temp=/Temperature:\ /g' && df -h | grep root | awk '{printf(\"Free disk space: %s\\n\", $4 ) }'"
    output = subprocess.check_output(['bash','-c', bashCommand])
    await bot.say(output.decode("utf8"))

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
   embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0xff1493)
   embed.add_field(name="Name", value=user.name, inline=True)
   embed.add_field(name="ID", value=user.id, inline=True)
   embed.add_field(name="Status", value=user.status, inline=True)
   embed.add_field(name="Highest role", value=user.top_role)
   embed.add_field(name="Joined", value=user.joined_at)
   embed.set_thumbnail(url=user.avatar_url)
   await bot.say(embed=embed)

@bot.command()
async def iplookup(ip):
    """Look up an ip address"""
    bashCommand = "curl ipinfo.io/{}?token=5b9793245de1f8".format(ip)
    output = subprocess.check_output(['bash','-c', bashCommand])
    await bot.say("```{}```".format(output.decode("utf8")))

@bot.listen()
async def on_message(message):
    if message.content == "Show you":
        await bot.send_message(message.channel, "https://i.guim.co.uk/img/media/327e46c3ab049358fad80575146be9e0e65686e7/0_0_1023_742/master/1023.jpg?w=1920&q=55&auto=format&usm=12&fit=max&s=ecc0b8c0c657bcc0fd231c0e35f89a39")
try:
    bot.run(TOKEN)
except KeyboardInterrupt:
    pass

