<<<<<<< HEAD
import os
import discord
from discord.ext import commands

# Cargar las variables de entorno desde el archivo .env
from dotenv import load_dotenv
load_dotenv()

# Obtener el token del bot desde las variables de entorno
TOKEN = os.getenv("BOT_TOKEN")

# Crear un bot de Discord
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.guild_messages = True
#intents.direct_messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Conectado como {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    palabras_llorar = ["Llorar", "llorar", "Llorón", "llorón", "Lloron", "lloron", "lloras", "Lloras", "llorando", "Llorando"]

    if message.content.strip() in palabras_llorar:
        await message.add_reaction('😭')

# Iniciar el bot con el token
bot.run(TOKEN)
=======
import os
import discord
from discord.ext import commands

# Cargar las variables de entorno desde el archivo .env
from dotenv import load_dotenv
load_dotenv()

# Obtener el token del bot desde las variables de entorno
TOKEN = os.getenv("BOT_TOKEN")

# Crear un bot de Discord
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.guild_messages = True
#intents.direct_messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Conectado como {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    palabras_llorar = ["Llorar", "llorar", "Llorón", "llorón", "Lloron", "lloron", "lloras", "Lloras", "llorando", "Llorando"]

    if message.content.strip() in palabras_llorar:
        await message.add_reaction('😭')

# Iniciar el bot con el token
bot.run(TOKEN)
>>>>>>> e069e32efe8d9941807719c3a3f87c6c17548fe2
