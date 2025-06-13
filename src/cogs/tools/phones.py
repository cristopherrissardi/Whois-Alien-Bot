
import discord
from discord.ext import commands
import requests
import os, io

from utils.buttons import NameResultView

API_KEY = os.getenv("API_KEY")


class TelefonesCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def telefone(self, ctx, *, telefone=None):

        if not telefone:
            embed = discord.Embed(title="")
            embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE TELEFONE', icon_url='')
            embed.add_field(name="Base de dados: **Operadoras**", value="", inline=False)
            embed.add_field(name="Informações de retorno:", value="NOME DOS TITULARES, CPF, ENDEREÇOS E OUTROS.", inline=False)
            embed.add_field(name="Status da API:", value="🟢 API ONLINE", inline=False)   
            embed.add_field(name="Use o comando: `./telefone` e o {TELEFONE} que deseja.", value='Exemplo: `./telefone` 11987654321', inline=False)
            await ctx.reply(embed=embed)
            return

        telefone_formatado = telefone.strip().replace(' ', '%20')
        data = f"http://127.0.0.1:44340/alienlabs/api/database/phone/search?telefone={telefone_formatado}"

        headers = {"apikey": API_KEY}

        response = requests.get(data, headers=headers)

        try:
            if response.status_code == 200:
                data_json = response.json()

                if isinstance(data_json, list) and len(data_json) > 1:
                    file_contents = ""
                    for index, result in enumerate(data_json, 1):
                        file_contents += f"RESULTADO {index}:\n\n• TELEFONE: {result['telefone']}\n• NOME: {result['nome'].upper()}\n• CPF/CNPJ: {result['cpf']}\n• LOGRADOURO: {result['rua']}\n• NÚMERO: {result['numero']}\n• COMPLEMENTO: {result['complemento']}\n• BAIRRO: {result['bairro']}\n• CIDADE: {result['cidade']}\n• ESTADO: {result['uf']}\n• CEP: {result['cep']}\n • OPERADORA: {result['operadora']}\n\n"

                    file_contents += "Whois Alien © All Rights Reserved\n"

                    file = io.StringIO(file_contents)
                    file.seek(0)

                    await ctx.send(file=discord.File(file, filename="resultados.txt"))
                elif isinstance(data_json, dict) or (isinstance(data_json, list) and len(data_json) == 1):
                    result = data_json[0] if isinstance(data_json, list) else data_json

                    embed = discord.Embed(title='')
                    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤCONSULTA DE TELEFONEㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

                    embed.add_field(name='• TELEFONE', value=result.get('telefone') or 'SEM INFORMAÇÃO', inline=False)
                    embed.add_field(name='• NOME', value=result.get('nome').upper() or 'SEM INFORMAÇÃO', inline=False)
                    embed.add_field(name='• CPF/CNPJ', value=result.get('cpf') or 'SEM INFORMAÇÃO', inline=False)
                    embed.add_field(name='• LOGRADOURO', value=result.get('rua') or 'SEM INFORMAÇÃO', inline=False)
                    embed.add_field(name='• NÚMERO', value=result.get('numero') or 'SEM INFORMAÇÃO', inline=False)
                    embed.add_field(name='• COMPLEMENTO', value=result.get('complemento') or 'SEM INFORMAÇÃO', inline=False)
                    embed.add_field(name='• BAIRRO', value=result.get('bairro') or 'SEM INFORMAÇÃO', inline=False)
                    embed.add_field(name='• CIDADE', value=result.get('cidade') or 'SEM INFORMAÇÃO', inline=False)
                    embed.add_field(name='• ESTADO', value=result.get('uf') or 'SEM INFORMAÇÃO', inline=False)
                    embed.add_field(name='• CEP', value=result.get('cep') or 'SEM INFORMAÇÃO', inline=False)
                    embed.add_field(name='• OPERADORA', value=result.get('operadora') or 'SEM INFORMAÇÃO', inline=False)
                    embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                    await ctx.reply(embed=embed)
            else:
                embed = discord.Embed(title=f"TELEFONE NÃO ENCONTRADO! {response.status_code}")
                await ctx.reply(embed=embed)

        except Exception as e:       
            embed.set_author(name=f'Erro na consulta {response.status_code}', icon_url='')
            await ctx.reply(embed=embed)



async def setup(bot):
    await bot.add_cog(TelefonesCommand(bot))
