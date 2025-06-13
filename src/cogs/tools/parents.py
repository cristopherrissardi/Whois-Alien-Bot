import discord
from discord.ext import commands
import requests
import os, io

from utils.buttons import PaisResultView, DeleteButton

API_KEY = os.getenv("API_KEY")


class ParentesCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mae(self, ctx, *, mae=None):

        if not mae:
            embed = discord.Embed(title="")
            embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE NOME', icon_url='')
            embed.add_field(name="Base de dados: **Serasa Experian**", value="", inline=False)
            embed.add_field(name="Informações de retorno:", value="CPF, NOME DOS FILHOS, DATA DE NASCIMENTO, E MÃE.", inline=False)
            embed.add_field(name="Status da API:", value="🟢 API ONLINE", inline=False)   
            embed.add_field(name="Use o comando: `./mae` e o nome da {MÃE} que deseja.", value='*Exemplo: `./mae` Fulana Santos*', inline=False)
            await ctx.reply(embed=embed)
            return

        mae_formatado = mae.strip().replace(' ', '%20')
        data = f"http://127.0.0.1:5000/aliencompanny/security/database/data/full/search?mae={mae_formatado}"

        headers = {"apikey": API_KEY}

        response = requests.get(data, headers=headers)

        embed = discord.Embed(title="Erro na consulta", color=discord.Color.red())  # Define a cor de erro logo aqui
        try:
            if response.status_code == 200:
                data_json = response.json()

                # Verifica se existem resultados
                if isinstance(data_json, list) and len(data_json) > 1:
                    # Caso haja vários resultados
                    file_contents = ""
                    for index, result in enumerate(data_json, 1):
                        file_contents += f"RESULTADO {index}:\n\n• NOME: {result.get('nomeCompleto', 'SEM INFORMAÇÃO')}\n• CPF: {result.get('cpf', 'SEM INFORMAÇÃO')}\n• DATA DE NASCIMENTO: {result.get('dataNascimento', 'SEM INFORMAÇÃO')}\n• NOME DA MÃE: {result.get('nomeMae', 'SEM INFORMAÇÃO')}\n\n"

                    file_contents += "Whois Alien © All Rights Reserved\n"

                    file = io.StringIO(file_contents)
                    file.seek(0)

                    view = PaisResultView(ctx.author, ctx.message, data_json)
                    view.add_item(DeleteButton(ctx.author, ctx.message))  # Adicionando o botão de deletar à view
                    
                    # Envia a resposta com o arquivo e a view
                    await ctx.send(file=discord.File(file, filename="resultados.txt"), view=view)

                elif isinstance(data_json, dict) or (isinstance(data_json, list) and len(data_json) == 1):
                    # Caso haja apenas um único resultado
                    result = data_json[0] if isinstance(data_json, list) else data_json

                    embed = discord.Embed(title='')
                    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤCONSULTA DE NOME DA MÃEㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

                    embed.add_field(name='• NOME', value=result.get('nomeCompleto', 'SEM INFORMAÇÃO').upper(), inline=False)
                    embed.add_field(name='• CPF', value=result.get('cpf', 'SEM INFORMAÇÃO'), inline=False)
                    embed.add_field(name='• DATA DE NASCIMENTO', value=result.get('dataNascimento', 'SEM INFORMAÇÃO'), inline=False)
                    embed.add_field(name='• NOME DA MÃE', value=result.get('nomeMae', 'SEM INFORMAÇÃO'), inline=False)
                    embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                    # Criando a view com o botão de deletar
                    view = PaisResultView(ctx.author, ctx.message, data_json)
                    view.add_item(DeleteButton(ctx.author, ctx.message))  # Adicionando o botão de deletar à view

                    # Enviando a resposta com a view
                    await ctx.reply(embed=embed, view=view)

                else:
                    embed.set_author(name=f'ㅤㅤㅤMÃE NÃO ENCONTRADA!ㅤㅤㅤ', icon_url='')
                    await ctx.reply(embed=embed)

            else:
                embed.set_author(name=f'ㅤㅤㅤMÃE NÃO ENCONTRADA!ㅤㅤㅤ', icon_url='')
                await ctx.reply(embed=embed)

        except Exception as e:       
            embed.set_author(name=f'Erro na consulta {response.status_code}', icon_url='')
            await ctx.reply(embed=embed)






    @commands.command()
    async def pai(self, ctx, *, pai=None):

        if not pai:

            embed = discord.Embed(title="")
            embed.set_author(name='ㅤㅤㅤㅤ👽 CONSULTA PELO NOME DO PAI', icon_url='')
            embed.add_field(name="Base de dados: **Datasus**", value="", inline=False)
            embed.add_field(name="Informações de retorno:", value="CPF, NOME DOS FILHOS, DATA DE NASCIMENTO, E PAI.", inline=False)
            embed.add_field(name="Status da API:", value="🟢 API ONLINE", inline=False)   
            embed.add_field(name="Use o comando: `./pai` e o nome do {PAI} que deseja.", value='*Exemplo: `./pai` Fulano De Jesus Matos*', inline=False)
            await ctx.reply(embed=embed)
            return

        pai_formatado = pai.strip().replace(' ', '%20')

        data = f"http://127.0.0.1:44340/alienlabs/api/database/datasus/search?pai={pai_formatado}"
        headers = {"apikey": API_KEY}

        response = requests.get(data, headers=headers)

        try:
            if response.status_code == 200:
                data_json = response.json()

                if isinstance(data_json, list) and len(data_json) > 1:
                    file_contents = ""
                    for index, result in enumerate(data_json, 1):
                        file_contents += f"RESULTADO {index}:\n\n• NOME: {result['nome'].upper()}\n• CPF: {result['cpf']}\n• DATA DE NASCIMENTO: {result['nascimento']}\n• NOME DO PAI: {result['pai']}\n\n"

                    file_contents += "Whois Alien © All Rights Reserved\n"

                    file = io.StringIO(file_contents)
                    file.seek(0)

                    await ctx.send(file=discord.File(file, filename="resultados.txt"))
                elif isinstance(data_json, dict) or (isinstance(data_json, list) and len(data_json) == 1):
                    result = data_json[0] if isinstance(data_json, list) else data_json

                    embed = discord.Embed(title='')
                    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤCONSULTA DE NOME DO PAIㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

                    embed.add_field(name='• NOME', value=result.get('nome').upper() or 'SEM INFORMAÇÃO', inline=False)
                    embed.add_field(name='• CPF', value=result.get('cpf') or 'SEM INFORMAÇÃO', inline=False)
                    embed.add_field(name='• DATA DE NASCIMENTO', value=result.get('nascimento') or 'SEM INFORMAÇÃO', inline=False)
                    embed.add_field(name='• NOME DO PAI', value=result.get('pai') or 'SEM INFORMAÇÃO', inline=False)
                    embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                    await ctx.reply(embed=embed)
            else:
                embed = discord.Embed(title="")
                embed.set_author(name=f'ㅤㅤㅤNOME DO PAI NÃO ENCONTRADO!ㅤㅤㅤ', icon_url='')
                await ctx.reply(embed=embed)

        except Exception as e:       
            embed.set_author(name=f'Erro na consulta {response.status_code}', icon_url='')
            await ctx.reply(embed=embed)



async def setup(bot):
    await bot.add_cog(ParentesCommand(bot))