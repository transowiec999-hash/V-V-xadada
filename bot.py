import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import os
TOKEN = os.getenv("MTUwNzY5ODg2MDYzNjc3MDM3NA.GaGGv1.bRYFMO3Vihik_ut3PKq4UBf-95ykJNaP_Ect5s")
intents = discord.Intents.default()
intents.message_content = True
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)
    async def setup_hook(self):
        await self.tree.sync()
        print(f"Zalogowano jako {self.user} | Komendy zsynchronizowane")
    async def on_ready(self):
        print(f"Bot gotowy | Ping: {round(self.latency * 1000)}ms")
bot = Bot()
@bot.tree.command(name="say", description="Bot wysyła wiadomość anonimowo")
@app_commands.describe(tresc="Treść wiadomości do wysłania")
async def say(interaction: discord.Interaction, tresc: str):
    await interaction.response.send_message("Wysyłam...", ephemeral=True)
    await interaction.channel.send(tresc)
@bot.tree.command(name="raid", description="Raid channel z @everyone i @here")
@app_commands.describe(tresc="Treść wiadomości raid")
async def raid(interaction: discord.Interaction, tresc: str = ""):
    author = interaction.user
    msg = f"@everyone @here **RAID OD {author}**\n{tresc}" if tresc else f"@everyone @here **RAID OD {author}**"
    await interaction.response.send_message("Raid wysłany ✅", ephemeral=True)
    await interaction.channel.send(msg)
bot.run(TOKEN)
