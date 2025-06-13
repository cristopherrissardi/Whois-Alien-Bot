import discord
from discord.ui import View, Button
import io


    
class DeleteButton(discord.ui.Button):
    def __init__(self, user, user_message):
        super().__init__(label="🗑️ Apagar", style=discord.ButtonStyle.red)
        self.user = user
        self.user_message = user_message

    async def callback(self, interaction: discord.Interaction):
        if interaction.user != self.user:
            await interaction.response.send_message("❌ Você não pode apagar essa mensagem!", ephemeral=True)
            return

        await interaction.message.delete()
        await self.user_message.delete()













#----------------------------------------




















class NameResultView(discord.ui.View):
    def __init__(self, user, user_message, all_results):
        super().__init__(timeout=300)
        self.user = user
        self.user_message = user_message
        self.all_results = all_results  # Lista completa

    @discord.ui.button(label="📥 Enviar no privado", style=discord.ButtonStyle.green)
    async def send_dm(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user != self.user:
            await interaction.response.send_message("❌ Só o dono da consulta pode receber por DM.", ephemeral=True)
            return

        file_contents = ""

        for index, result in enumerate(self.all_results, 1):
            file_contents += (
                f"• NOME: {result.get('nome', 'SEM INFO')}\n"
                f"• CPF: {result.get('cpf', 'SEM INFO')}\n"
                f"• SEXO: {result.get('sexo', 'SEM INFO')}\n"
                f"• NASCIMENTO: {result.get('dataNascimento', 'SEM INFO')}\n"
                f"• MÃE: {result.get('nomeMae', 'SEM INFO')}\n"
                f"• IDADE: {result.get('idade', 'SEM INFO')}\n\n"
            )

        file_contents += "Whois Alien © All Rights Reserved"

        file = discord.File(io.StringIO(file_contents), filename="consulta_nome.txt")

        try:
            await self.user.send("📁 Resultado da sua consulta em anexo:", file=file)
            await interaction.response.send_message("✅ Arquivo enviado no seu privado!", ephemeral=True)
        except discord.Forbidden:
            await interaction.response.send_message("❌ Não consegui te mandar DM!", ephemeral=True)
















class PaisResultView(discord.ui.View):
    def __init__(self, user, user_message, all_results):
        super().__init__(timeout=300)
        self.user = user
        self.user_message = user_message
        self.all_results = all_results  # Lista completa

    @discord.ui.button(label="📥 Enviar no privado", style=discord.ButtonStyle.green)
    async def send_dm(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user != self.user:
            await interaction.response.send_message("❌ Só o dono da consulta pode receber por DM.", ephemeral=True)
            return

        file_contents = ""

        for index, result in enumerate(self.all_results, 1):
            file_contents += (
                f"RESULTADO {index}:\n"
                f"• NOME: {result.get('nomeCompleto', 'SEM INFO')}\n"
                f"• CPF: {result.get('cpf', 'SEM INFO')}\n"
                f"• DATA DE NASCIMENTO: {result.get('dataNascimento', 'SEM INFO')}\n"
                f"• NOME DA MÃE: {result.get('nomeMae', 'SEM INFO')}\n\n"
            )

        file_contents += "Whois Alien © All Rights Reserved"

        file = discord.File(io.StringIO(file_contents), filename="consulta_nome.txt")

        try:
            await self.user.send("📁 Resultado da sua consulta em anexo:", file=file)
            await interaction.response.send_message("✅ Arquivo enviado no seu privado!", ephemeral=True)
        except discord.Forbidden:
            await interaction.response.send_message("❌ Não consegui te mandar DM!", ephemeral=True)






async def setup(bot):
    pass  
