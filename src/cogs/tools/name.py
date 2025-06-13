
import discord
from discord.ext import commands
import requests
import os, io

from utils.buttons import NameResultView, DeleteButton


API_KEY = os.getenv("API_KEY")

class NomeSearchCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nome(self, ctx, *, nome=None):
        if not nome: 
            embed = discord.Embed(title="")
            embed.set_author(name='ㅤㅤㅤㅤㅤㅤ👽 COMANDO DE NOME', icon_url='')
            embed.add_field(name="Base de dados: **DataFantany**", value="", inline=False)
            embed.add_field(name="Informações de retorno:", value="NOME, CPF, DATA DE NASCIMENTO, SEXO, NOME DA MÃE e IDADE", inline=False)
            embed.add_field(name="Status da API:", value="🟢 API ONLINE", inline=False)
            embed.add_field(name="Use o comando: `./nome` e o {NOME} que deseja.", value='*Exemplo: `./nome` Fulano dos Santos*', inline=False)
            await ctx.reply(embed=embed)
            return  

        nome_formatado = nome.strip().replace(' ', '%20')
        url = f"http://127.0.0.1:5000/aliencompanny/security/database/data/basic/search?nome={nome_formatado}"
        headers = {"apikey": API_KEY}

        response = requests.get(url, headers=headers)

        try:
            if response.status_code == 200:
                data_json = response.json()

                # Verifica se tem resultados além do índice 0
                if isinstance(data_json, list) and len(data_json) > 1:
                    resultados = data_json[1:]  # Ignora o índice 0

                    if len(resultados) == 1:
                        result = resultados[0]

                        embed = discord.Embed(title='', color=0xffffff)
                        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤCONSULTA DE NOMEㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

                        embed.add_field(name='• NOME', value=result.get('nome', 'SEM INFORMAÇÃO').upper(), inline=False)
                        embed.add_field(name='• CPF', value=result.get('cpf', 'SEM INFORMAÇÃO'), inline=False)
                        embed.add_field(name='• SEXO', value=result.get('sexo', 'SEM INFORMAÇÃO'), inline=False)
                        embed.add_field(name='• DATA DE NASCIMENTO', value=result.get('dataNascimento', 'SEM INFORMAÇÃO'), inline=False)
                        embed.add_field(name='• NOME DA MÃE', value=result.get('nomeMae', 'SEM INFORMAÇÃO'), inline=False)
                        embed.add_field(name='• IDADE', value=str(result.get('idade', 'SEM INFORMAÇÃO')), inline=False)

                        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                        view = NameResultView(ctx.author, ctx.message, resultados)
                        view.add_item(DeleteButton(ctx.author, ctx.message))  # Adicionando o botão de deletar à view

                        await ctx.reply(embed=embed, view=view)

                    else:
                        file_contents = ""
                        for index, result in enumerate(resultados, 1):
                            file_contents += (
                                f"RESULTADO {index}:\n\n"
                                f"• NOME: {result.get('nome', 'SEM INFORMAÇÃO')}\n"
                                f"• CPF: {result.get('cpf', 'SEM INFORMAÇÃO')}\n"
                                f"• SEXO: {result.get('sexo', 'SEM INFORMAÇÃO')}\n"
                                f"• DATA DE NASCIMENTO: {result.get('dataNascimento', 'SEM INFORMAÇÃO')}\n"
                                f"• NOME DA MÃE: {result.get('nomeMae', 'SEM INFORMAÇÃO')}\n"
                                f"• IDADE: {str(result.get('idade', 'SEM INFORMAÇÃO'))}\n\n"
                            )
                        file_contents += "Whois Alien © All Rights Reserved\n"


                        file = io.StringIO(file_contents)
                        file.seek(0)

                        view = NameResultView(ctx.author, ctx.message, resultados)
                        view.add_item(DeleteButton(ctx.author, ctx.message))  # Adicionando o botão de deletar à view
                        await ctx.reply(file=discord.File(file, filename="resultados.txt"), view=view)

                else:
                    embed = discord.Embed(title="")
                    embed.set_author(name=f'ㅤㅤㅤNOME NÃO ENCONTRADO!ㅤㅤㅤ', icon_url='')
                    await ctx.reply(embed=embed)
            else:
                embed = discord.Embed(title="")
                embed.set_author(name=f'ㅤㅤㅤNOME NÃO ENCONTRADO!ㅤㅤㅤ', icon_url='')
                await ctx.reply(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Erro interno")
            embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE NOME', icon_url='')
            embed.add_field(name="Erro ao processar a resposta da API.", value=str(e), inline=False)
            await ctx.reply(embed=embed)



async def setup(bot):
    await bot.add_cog(NomeSearchCommand(bot))

