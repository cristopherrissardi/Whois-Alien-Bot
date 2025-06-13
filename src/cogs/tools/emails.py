

import discord
from discord.ext import commands
import requests
import os, io

from utils.buttons import NameResultView

API_KEY = os.getenv("API_KEY")


class EmailCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def email(self, ctx, *, email=None):

        if not email:

            embed = discord.Embed(title="")
            embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE E-MAIL', icon_url='')
            embed.add_field(name="Base de dados: **Alien DB**", value="", inline=False)
            embed.add_field(name="Informações de retorno:", value="NOME, CPF E E-MAIL.", inline=False)
            embed.add_field(name="Status da API:", value="🟢 API ONLINE", inline=False)   
            embed.add_field(name="Use o comando: `./email` e o {EMAIL} que deseja.", value='*Exemplo: `./email` fulanodetal@gmail.com*', inline=False)
            await ctx.reply(embed=embed)
            return

        email_formatado = email.strip().replace(' ', '%20')
        data = f"http://127.0.0.1:44340/alienlabs/api/database/email/search?e-mail={email_formatado}"

        headers = {"apikey": API_KEY}

        response = requests.get(data, headers=headers)

        try:
            if response.status_code == 200:
                data_json = response.json()

                if isinstance(data_json, list) and len(data_json) > 1:
                    file_contents = ""
                    for index, result in enumerate(data_json, 1):
                        file_contents += f"RESULTADO {index}:\n\n• NOME: {result['nome'].upper()}\n• CPF: {result['cpf']}\n• E-MAIL: {result['e-mail']}\n\n"

                    file_contents += "Whois Alien © All Rights Reserved\n"

                    file = io.StringIO(file_contents)
                    file.seek(0)

                    await ctx.send(file=discord.File(file, filename="resultados.txt"))
                elif isinstance(data_json, dict) or (isinstance(data_json, list) and len(data_json) == 1):
                    result = data_json[0] if isinstance(data_json, list) else data_json

                    embed = discord.Embed(title='')
                    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤCONSULTA DE DADOS POR EMAILㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

                    embed.add_field(name='• NOME', value=result.get('nome') or 'SEM INFORMAÇÃO'.upper(), inline=False)
                    embed.add_field(name='• CPF', value=result.get('cpf') or 'SEM INFORMAÇÃO', inline=False)
                    embed.add_field(name='• E-MAIL', value=result.get('e-mail') or 'SEM INFORMAÇÃO', inline=False)

                    embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                    await ctx.reply(embed=embed)
            else:
                embed = discord.Embed(title="")
                embed.set_author(name=f'ㅤㅤㅤE-MAIL NÃO ENCONTRADO!ㅤㅤㅤ', icon_url='')
                await ctx.reply(embed=embed)

        except Exception as e:       
            embed.set_author(name=f'Erro na consulta {response.status_code}', icon_url='')
            await ctx.reply(embed=embed)



async def setup(bot):
    await bot.add_cog(EmailCommands(bot))


