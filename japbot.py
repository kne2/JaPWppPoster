from discord.ext import commands
import config
import json
import time


bot = commands.Bot(">>>")

def mencionaWpp(c):
    return not c.lower().find("wpp") == -1 or not c.lower().find("whatsapp") == -1

def mencionaGrupo(c):
    for grupo in grupos['grupos']:
        if not c.find(grupo["id"]) == -1:
            return grupo
    return False

def guardarGrupos(grupos):
    with open("grupos.json", "w") as f:
        json.dump(json.dumps(grupos), f)

def cargarGrupos():
    with open("grupos.json", "r") as f:
        grupos = json.load(f)
    return grupos

grupos = cargarGrupos()

@bot.event
async def on_ready():
    print("-----------------------------------")
    print("Logged in: " + bot.user.name+"#"+bot.user.discriminator)
    print("")
    print("Made by KNE2")
    print("-----------------------------------")


@bot.event
async def on_message(message):
    c=""
    async for m in message.channel.history(limit=1):
        c = m.content
    time.sleep(0.5)
    if (config.JAPSERVER or message.guild.id == 829880060243738644) and not message.author.id == bot.user.id and c:
        grupo = mencionaGrupo(c)
        if grupo and mencionaWpp(c):
            await message.channel.send(grupo["link"]+" "+ message.author.mention)
            print(grupo["id"]+" "+ message.author.name +"#"+message.author.discriminator)



bot.run(config.BOTTOKEN, bot=False)


