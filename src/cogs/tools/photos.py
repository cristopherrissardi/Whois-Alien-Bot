

import discord
from discord.ext import commands
import requests
import os
import base64
from io import BytesIO

from utils.buttons import NameResultView

API_KEY = os.getenv("API_KEY")


class FotoSearch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def foto(self, ctx, *, foto=None):
        if not foto:
            embed = discord.Embed(title="")
            embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE FOTO', icon_url='')
            embed.add_field(name="Base de dados: **Detran**", value="", inline=False)
            embed.add_field(name="Informações de retorno:", value="FOTO DO ROSTO, CPF, NOME, NOME DA MÃE, DATA DE NASCIMENTO ETC.", inline=False)
            embed.add_field(name="Status da API:", value="🟢 API ONLINE", inline=False)   
            embed.add_field(name="Use o comando: `./foto` e o {CPF} que deseja.", value='*Exemplo: `./foto` 123.456.789-12*', inline=False)
            await ctx.reply(embed=embed)
            return

        cpf_formatado = foto.strip()
        data = f"http://127.0.0.1:44340/alienlabs/api/database/fotos/rj/search?CPF={cpf_formatado}"

        headers = {"apikey": API_KEY}
        response = requests.get(data, headers=headers)

        try:
            if response.status_code == 200:
                data = response.json()

                if len(data) > 0:
                    cpf_info = data[0]
                    foto_base64 = cpf_info.get("dados", {}).get("fotos")

                    embed = discord.Embed(title='')
                    embed.set_author(name='ㅤㅤㅤCONSULTA DE FOTO RJㅤㅤㅤ', icon_url='')
                    embed.add_field(name="• NOME", value=cpf_info.get('NOME_COMPLETO') or 'SEM INFORMAÇÃO'.upper(), inline=False)
                    embed.add_field(name='• CPF', value=cpf_info.get('CPF') or 'SEM INFORMAÇÃO', inline=False)
                    embed.add_field(name='• NASCIMENTO', value=cpf_info.get('DT_NASCIMENTO') or 'SEM INFORMAÇÃO', inline=False)

                    file = None
                    if foto_base64:
                        # Decodifica a imagem
                        image_bytes = base64.b64decode(foto_base64)
                        image_file = BytesIO(image_bytes)
                        image_file.seek(0)

                        file = discord.File(image_file, filename="foto.png")
                        embed.set_image(url="attachment://foto.png")

                    embed.add_field(name='', value='', inline=False)
                    embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
                    await ctx.send(embed=embed, file=file if file else None)
            else:
                embed = discord.Embed(title="")
                embed.set_author(name=f'ㅤㅤㅤPESSOA NÃO ENCONTRADA!ㅤㅤㅤ', icon_url='')
                await ctx.reply(embed=embed)

        except Exception as e:
            embed.set_author(name=f'Erro na consulta {response.status_code}', icon_url='')
            await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(FotoSearch(bot))


