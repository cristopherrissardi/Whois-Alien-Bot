


import discord
from discord.ext import commands
import requests
import os, io

from utils.buttons import NameResultView

API_KEY = os.getenv("API_KEY")


class CepCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cep(self, ctx, *, cep=None):

        MAPS_API = os.getenv("GOOGLE_MAPS_API_KEY")

        if not cep:
            embed = discord.Embed(title="")
            embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO CEP', icon_url='')
            embed.add_field(name="Base de dados: **CEP AwesomeAPI e Datasus**", value="", inline=False)
            embed.add_field(name="Informações de retorno:", value="INFORMAÇÕES SOBRE O CEP E RESIDÊNTES DO CEP.", inline=False)
            embed.add_field(name="Status das APIs:", value="🟢 APIS ONLINE", inline=False)   
            embed.add_field(name="Use o comando: `./cep` e o {CEP} que deseja.", value='*Exemplo*: `./cep 70150904`', inline=False)
            embed.add_field(name="Observação:", value='*Não utilize pontos, hifens e caracteres especiais*', inline=False)
            await ctx.reply(embed=embed)
            return

        # Consulta do CEP básico

        cep_formatado = cep.strip()
        cep_data = requests.get(f"https://cep.awesomeapi.com.br/json/{cep_formatado}").json()

        if 'erro' in cep_data:
            embed = discord.Embed(title='')
            embed.set_author(name='CEP NÃO ENCONTRADO', icon_url='')
            await ctx.reply(embed=embed)
            return

        latitude = cep_data.get('lat')
        longitude = cep_data.get('lng')
        maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
        mapa_url = f"https://maps.googleapis.com/maps/api/staticmap?center={latitude},{longitude}&zoom=15&size=600x300&markers=color:red%7C{latitude},{longitude}&key={MAPS_API}"

        # Embed com as informações do CEP
        embed = discord.Embed(title='')
        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE CEPㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
        embed.add_field(name="• CEP", value=cep_data.get('cep', 'Sem Informação'), inline=False)
        embed.add_field(name="• NOME DA RUA", value=cep_data.get('address', 'Sem Informação'), inline=False)
        embed.add_field(name="• BAIRRO", value=cep_data.get('district', 'Sem Informação'), inline=False)
        embed.add_field(name="• CIDADE", value=cep_data.get('city', 'Sem Informação'), inline=False)
        embed.add_field(name="• ESTADO", value=cep_data.get('state', 'Sem Informação'), inline=False)
        embed.add_field(name="• IBGE", value=cep_data.get('city_ibge', 'Sem Informação'), inline=False)
        embed.add_field(name="• DDD", value=cep_data.get('ddd', 'Sem Informação'), inline=False)
        embed.add_field(name="• LOCALIZAÇÃO", value=f"[{latitude},{longitude}]({maps_link})", inline=False)
        embed.set_image(url=mapa_url)  # Adiciona a imagem do mapa
        embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved', icon_url='')

        await ctx.reply(embed=embed)

        # Consulta dos moradores no Datasus
        cep_pessoas_formatado = cep.strip().replace(' ', '%20')
        data_url = f"http://127.0.0.1:44340/alienlabs/api/database/datasus/search?cep={cep_pessoas_formatado}"
        headers = {"apikey": API_KEY}

        response = requests.get(data_url, headers=headers)

        if response.status_code == 200:
            data_json = response.json()

            if isinstance(data_json, list) and len(data_json) > 1:
                total_pessoas = len(data_json)
                file_contents = (
                    f"ㅤㅤㅤㅤㅤㅤㅤPESSOAS RESIDÊNTES NO CEP [{cep}]ㅤㅤㅤㅤㅤㅤㅤ\n"
                    f"TOTAL DE PESSOAS ENCONTRADAS: [{total_pessoas}]\n\n"
                )

                for index, result in enumerate(data_json, 1):
                    file_contents += (
                        f"RESULTADO {index}:\n\n"
                        f"• NOME: {result['nome'].upper()}\n"
                        f"• CPF: {result['cpf']}\n"
                        f"• DATA DE NASCIMENTO: {result['nascimento']}\n"
                        f"• LOGRADOURO: {result['logradouro']}\n"
                        f"• NUMERO: {result['numero']}\n"
                        f"• CEP: {result['cep']}\n"
                        f"• MUNICIPIO: {result['municipio']}\n\n"
                    )

                file_contents += "\nWhois Alien © All Rights Reserved\n"
                file = io.StringIO(file_contents)
                file.seek(0)
                await ctx.reply(file=discord.File(file, filename=f"moradores_{cep}.txt"))

            elif isinstance(data_json, dict) or (isinstance(data_json, list) and len(data_json) == 1):
                result = data_json[0] if isinstance(data_json, list) else data_json
                embed_pessoa = discord.Embed(title="INFORMAÇÕES DOS MORADORES", color=0x00ff00)
                embed_pessoa.add_field(name="• NOME", value=result['nome'].upper(), inline=False)
                embed_pessoa.add_field(name="• CPF", value=result['cpf'], inline=False)
                embed_pessoa.add_field(name="• DATA DE NASCIMENTO", value=result['nascimento'], inline=False)
                embed_pessoa.add_field(name="• LOGRADOURO", value=result['logradouro'], inline=False)
                embed_pessoa.add_field(name="• NUMERO", value=result['numero'], inline=False)
                embed_pessoa.add_field(name="• MUNICIPIO", value=result['municipio'], inline=False)
                await ctx.reply(embed=embed_pessoa)

        else:
            embed = discord.Embed(title=f"CEP NÃO ENCONTRADO! {response.status_code}")
            await ctx.reply(embed=embed)




async def setup(bot):
    await bot.add_cog(CepCommand(bot))

