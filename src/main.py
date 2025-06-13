from discord.ext import commands, tasks
from dotenv import load_dotenv 
import discord   
import os 
import nest_asyncio

load_dotenv()
nest_asyncio.apply()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix='./', intents=intents)

EXTENSIONS = [
    'cogs.admin',
    'cogs.features',
    'cogs.views',
    'cogs.generators.data_generators',
    'cogs.generators.hash_generators',
    'cogs.tools.cep',
    'cogs.tools.cnpj',
    'cogs.tools.cpf',
    'cogs.tools.emails',
    'cogs.tools.name',
    'cogs.tools.network',
    'cogs.tools.others',
    'cogs.tools.parents',
    'cogs.tools.phones',
    'cogs.tools.photos',
    'cogs.tools.pwned',
    'cogs.tools.vehicle',
    'utils.buttons',
    'cogs.events'
]

@client.event
async def on_ready():
    activity = discord.Game(name='Created By Alien', type=3)
    await client.change_presence(status=discord.Status.dnd, activity=activity)

    for ext in EXTENSIONS:
        try:
            await client.load_extension(ext)
        except Exception as e:
            print(f"Erro ao carregar {ext}: {e}")

    print(f"\n✅ Bot Conectado com sucesso!")

bot_token = os.getenv("BOT_TOKEN")
client.run(bot_token)
