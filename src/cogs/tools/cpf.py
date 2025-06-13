
import discord
from discord.ext import commands
import requests
import os, io

from utils.buttons import NameResultView

API_KEY = os.getenv("API_KEY")


class CPFSearchCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cpf(self, ctx, *, cpf=None):
        if not cpf: 
            embed = discord.Embed(title="")
            embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE CPF', icon_url='')
            embed.add_field(name="Base de dados: **DataFantany**", value="", inline=False)
            embed.add_field(name="Informações de retorno:", value="NOME, CPF, DATA DE NASCIMENTO, SEXO, NOME DA MÃE, IDADE, etc...", inline=False)
            embed.add_field(name="Status da API:", value="🟢 API ONLINE", inline=False)
            embed.add_field(name="Use o comando: `./cpf` e o {CPF} que deseja.", value='*Exemplo: `./cpf` 123.456.789-00*', inline=False)
            await ctx.reply(embed=embed)
            return  

        cpf_formatado = cpf.strip()
        url = f"http://127.0.0.1:5000/aliencompanny/security/database/data/full/search?cpf={cpf_formatado}"
        headers = {"apikey": API_KEY}

        response = requests.get(url, headers=headers)

        try:
            if response.status_code == 200:
                data_json = response.json()

                if isinstance(data_json, list) and len(data_json) > 1:
                    resultados = data_json[1:]  # Ignora o índice 0

                    file_contents = ""
                    for index, result in enumerate(resultados, 1):
                        dados = result.get('dadosBasicos', {})

                        file_contents += (
                            f"RESULTADO:\n\n"
                            f"• NOME: {dados.get('nome', 'SEM INFORMAÇÃO')}\n"
                            f"• CPF: {dados.get('cpf', 'SEM INFORMAÇÃO')}\n"
                            f"• SEXO: {dados.get('sexo', 'SEM INFORMAÇÃO')}\n"
                            f"• DATA DE NASCIMENTO: {dados.get('dataNascimento', 'SEM INFORMAÇÃO')}\n"
                            f"• NOME DA MÃE: {dados.get('nomeMae', 'SEM INFORMAÇÃO')}\n"
                            f"• NOME DO PAI: {dados.get('nomePai', 'SEM INFORMAÇÃO')}\n"
                            f"• IDADE: {str(dados.get('idade', 'SEM INFORMAÇÃO'))}\n"
                            f"• ESTADO CIVIL: {dados.get('estadoCivil', 'SEM INFORMAÇÃO')}\n"
                            f"• ESCOLARIDADE: {dados.get('escolaridade', 'SEM INFORMAÇÃO')}\n"
                            f"• NACIONALIDADE: {dados.get('nacionalidade', 'SEM INFORMAÇÃO')}\n"
                            f"• MUNICÍPIO DE NASCIMENTO: {dados.get('municipioNascimento', 'SEM INFORMAÇÃO')}\n"
                            f"• SIGNO: {dados.get('signo', 'SEM INFORMAÇÃO')}\n"
                            f"• SITUAÇÃO CADASTRAL: {dados.get('situacaoCadastral', 'SEM INFORMAÇÃO')}\n"
                            f"• TÍTULO ELEITORAL: {dados.get('tituloEleitoral', 'SEM INFORMAÇÃO')}\n"
                            f"• CNS: {dados.get('cns', 'SEM INFORMAÇÃO')}\n"
                            f"• NIS: {dados.get('nis', 'SEM INFORMAÇÃO')}\n\n"
                        )

                        historico_emails = result.get('historicoEmails', [])

                        if isinstance(historico_emails, dict):
                            historico_emails = [historico_emails]
                        elif isinstance(historico_emails, str):
                            # Se vier como string, ignora ou loga como inválido
                            historico_emails = []

                        if isinstance(historico_emails, list) and historico_emails:
                            file_contents += f"HISTÓRICO DE E-MAILS:\n\n"
                            for i, email in enumerate(historico_emails, 1):
                                if isinstance(email, dict):
                                    file_contents += (
                                        f"    • EMAIL: {email.get('email', 'SEM INFORMAÇÃO')}\n"
                                        f"    • SCORE: {email.get('emailScore', 'SEM INFORMAÇÃO')}\n"
                                        f"    • VALIDAÇÃO: {email.get('statusValidacao', 'SEM INFORMAÇÃO')}\n\n"
                                    )
                                else:
                                    file_contents += f"  [{i}] EMAIL MAL FORMATADO\n"
                        else:
                            file_contents += "HISTÓRICO DE E-MAILS: SEM INFORMAÇÃO OU FORMATO INVÁLIDO\n\n"


                    file_contents += "Whois Alien © All Rights Reserved\n"
                    file = io.StringIO(file_contents)
                    file.seek(0)
                    await ctx.reply(file=discord.File(file, filename="resultados.txt"))

                else:
                    file_contents = "Nenhum resultado encontrado para o CPF informado.\nWhois Alien © All Rights Reserved\n"
                    file = io.StringIO(file_contents)
                    file.seek(0)
                    await ctx.reply(file=discord.File(file, filename="resultados.txt"))

            else:
                file_contents = "Erro ao acessar a API. Tente novamente mais tarde.\nWhois Alien © All Rights Reserved\n"
                file = io.StringIO(file_contents)
                file.seek(0)
                await ctx.reply(file=discord.File(file, filename="resultados.txt"))

        except Exception as e:
            file_contents = f"Erro interno: {str(e)}\nWhois Alien © All Rights Reserved\n"
            file = io.StringIO(file_contents)
            file.seek(0)
            await ctx.reply(file=discord.File(file, filename="resultados.txt"))


    @commands.command()
    async def cpf1(self, ctx, *, cpf1=None):
        if not cpf1:
            embed = discord.Embed(title="")
            embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE CPF 1', icon_url='')
            embed.add_field(name="Base de dados: **DataFantany**", value="", inline=False)
            embed.add_field(name="Informações de retorno:", value="NOME, CPF, DATA DE NASCIMENTO, SEXO, NOME DA MÃE e IDADE", inline=False)
            embed.add_field(name="Status da API:", value="🟢 API ONLINE", inline=False)
            embed.add_field(name="Use o comando: `./cpf1` e o {CPF} que deseja.", value='*Exemplo: `./cpf1` 123.456.789-12*', inline=False)
            await ctx.reply(embed=embed)
            return

        cpf_formatado = cpf1.strip()
        url = f"http://127.0.0.1:5000/aliencompanny/security/database/data/basic/search?cpf={cpf_formatado}"
        headers = {"apikey": API_KEY}

        try:
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                response_json = response.json()
                print(response_json)  # Para inspeção

                if isinstance(response_json, list) and len(response_json) > 1:
                    # Acessando os dados reais (segundo item da lista)
                    cpf_info = response_json[1]

                    embed = discord.Embed(title='')
                    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE CPFㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

                    embed.add_field(name='• NOME', value=cpf_info.get('nome', 'SEM INFORMAÇÃO').upper(), inline=False)
                    embed.add_field(name='• CPF', value=cpf_info.get('cpf', 'SEM INFORMAÇÃO'), inline=False)
                    embed.add_field(name='• SEXO', value=cpf_info.get('sexo', 'SEM INFORMAÇÃO'), inline=False)
                    embed.add_field(name='• DATA DE NASCIMENTO', value=cpf_info.get('dataNascimento', 'SEM INFORMAÇÃO'), inline=False)
                    embed.add_field(name='• NOME DA MÃE', value=cpf_info.get('nomeMae', 'SEM INFORMAÇÃO'), inline=False)
                    embed.add_field(name='• IDADE', value=str(cpf_info.get('idade', 'SEM INFORMAÇÃO')), inline=False)

                    embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
                    await ctx.reply(embed=embed)
                else:
                    embed = discord.Embed(title="")
                    embed.set_author(name=f'ㅤㅤㅤCPF NÃO ENCONTRADO!ㅤㅤㅤ', icon_url='')
                    await ctx.reply(embed=embed)
            else:
                embed = discord.Embed(title="")
                embed.set_author(name=f'ㅤㅤㅤCPF NÃO ENCONTRADO!ㅤㅤㅤ', icon_url='')
                await ctx.reply(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Erro interno")
            embed.set_author(name='🛑 ERRO DE SISTEMA', icon_url='')
            embed.add_field(name="Mensagem de erro:", value=str(e), inline=False)
            await ctx.reply(embed=embed)




















async def setup(bot):
    await bot.add_cog(CPFSearchCommand(bot))

