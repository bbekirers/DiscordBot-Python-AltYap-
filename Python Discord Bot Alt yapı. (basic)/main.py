import nextcord # Nextcord Modulunu importluyoruz. 
from nextcord.ext import commands
from config import TOKEN, PREFIX # config.py'den " TOKEN " ve " PREFIX " maine çekiyoruz.

intents = nextcord.Intents.default() # İntents'leri Ekliyoruz. Yani Bot İzinlerini.
intents.message_content = True
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents) # config.py'den çektiğimiz PREFIXI kullanıdırtıyoruz.
bot.remove_command('help')  # Kendisine ait olan "help" komutunu kaldırır.

@bot.event
async def on_ready():
    print(f'{bot.user.name} Aktif!') # Bot başladığı zaman terminal'de yazar.



bot.run(TOKEN) # Botun başlaması için config.py den çektiğimiz token ile başlatıyoruz.
