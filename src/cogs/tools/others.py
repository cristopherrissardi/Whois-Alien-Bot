

import discord
from discord.ext import commands
import requests
import os

from utils.buttons import NameResultView

API_KEY = os.getenv("API_KEY")


class OtherToolsCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def cotacao(ctx, cotacao=None):

        if not cotacao:
            
            embed = discord.Embed(title='')

            embed.set_author(name='ㅤㅤㅤㅤ   👽 COMANDO COTAÇÃOㅤㅤㅤ', icon_url='')
            embed.add_field(name="Fonte da consulta: **AwesomeAPI**", value="", inline=False)
            embed.add_field(name="Informações de retorno:", value="Informações sobre a cotação entre as moedas.", inline=False)
            embed.add_field(name="Status da API:", value="🟢 API ONLINE", inline=False)   
            embed.add_field(name="Use o comando: `./cotacao` e o {PAR DE MOEDA} que deseja", value='*Exemplo*: `./cotacao BRL-USD`', inline=False)
            embed.add_field(name="Observação:", value='*O par precisa ser separado com hifen*', inline=False)   
            return await ctx.reply(embed=embed)

        data = requests.get(f"https://economia.awesomeapi.com.br/last/{cotacao}").json()
        coin_name = cotacao.replace("-", "")

        if coin_name in data:
            
            embed = discord.Embed(title='')

            embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCOTAÇÃO DE MOEDASㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

            embed.add_field(name="• MOEDA A COMPARAR", value=data[coin_name]["code"], inline=False)
            embed.add_field(name="• MOEDA A SER COMPARADA", value=data[coin_name]["codein"], inline=False)
            embed.add_field(name="• NOME DAS PARIEDADES", value=data[coin_name]["name"], inline=False)
            embed.add_field(name="• MÁXIMA DO DIA", value=data[coin_name]["high"], inline=False)
            embed.add_field(name="• MÍNIMA DO DIA", value=data[coin_name]["low"], inline=False)
            embed.add_field(name="• VARIAÇÃO", value=data[coin_name]["varBid"], inline=False)
            embed.add_field(name="• PORCENTAGEM DE VARIAÇÃO", value=data[coin_name]["pctChange"], inline=False)
            embed.add_field(name="• COMPRA", value=data[coin_name]["bid"], inline=False)
            embed.add_field(name="• VENDA", value=data[coin_name]["ask"], inline=False)
            embed.add_field(name="• ATUALIZAÇÃO", value=data[coin_name]["create_date"], inline=False)
            embed.add_field(name="Observação", value=f"Pode haver alguma pequena diferença na cotação das moedas!!! Grande parte dos sites que fornecem essa informação informa margem de erros, então vale sempre conferir a informação mais precisa possível no TradingView, O site está disponível abaixo:\nhttps://br.tradingview.com/", inline=False)

            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
        else:
            embed = discord.Embed(title='')
            embed.set_author(name='ㅤㅤCOTAÇÃO DE MOEDAS INVÁLIDAㅤㅤㅤ', icon_url='')

        embed.set_author(name='ㅤㅤCOTAÇÃO DE MOEDAS INVÁLIDAㅤㅤㅤ', icon_url='')

        await ctx.reply(embed=embed)

    @commands.command() 
    async def ddd(self, ctx, ddd=None):

        if not ddd:
            
            embed = discord.Embed(title='') 
            embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO PROCURA DDDㅤㅤㅤ', icon_url='')
            embed.add_field(name="Fonte da consulta: **BrasilAPI**", value="", inline=False)
            embed.add_field(name="Informações de retorno:", value="Informações 100% Atualizadas dos Sites.", inline=False)
            embed.add_field(name="Status da API:", value="🟢 API ONLINE", inline=False)   
            embed.add_field(name="Use o comando: `./ddd` e o {DDD} que deseja", value='*Exemplo*: `./ddd 11`', inline=False)
            await ctx.reply(embed=embed)
            return

        data = requests.get(f"https://brasilapi.com.br/api/ddd/v1/{ddd}").json() 

        try:
            if 'type' in data and data['type'] == 'ddd_error':
                embed = discord.Embed(title='')
                embed.set_author(name='ㅤㅤDDD INVÁLIDO, CIDADE NÃO ENCONTRADAㅤㅤ', icon_url='')
                await ctx.reply(embed=embed)
                return

            else: 
                embed = discord.Embed(title='')

                embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE CIDADES POR DDDㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='') #----->> TÍTULO DO CÓDIGO

                embed.add_field(name="Estado", value=data.get('state', 'Sem Informação'), inline=False)
                embed.add_field(name="Cidades", value=','.join([f"`{city}`" for city in data.get("cities")]), inline=False)

                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                await ctx.reply(embed=embed)

        except Exception:
            pass   


    @commands.command()
    async def bin(self, ctx, bin=None):

        if not bin:

            embed = discord.Embed(title='')
            embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO BINㅤㅤㅤ', icon_url='')
            embed.add_field(name="Fonte da consulta: **BinList**", value="", inline=False)
            embed.add_field(name="Informações de retorno:", value="Sobre a BIN do cartão.", inline=False)
            embed.add_field(name="Status da API:", value="🟢 API ONLINE", inline=False)   
            embed.add_field(name="Use o comando: `./bin` e o {BIN} que deseja checar", value='*Exemplo*: `./bin 522840`', inline=False)
            return await ctx.reply(embed=embed)

        try:
            data = f"https://lookup.binlist.net/{bin}"

            response = requests.get(data)

            if response.status_code == 200:
                data = response.json()

                embed = discord.Embed(title='')

                embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE BINㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

                embed.add_field(name="• BIN", value=data.get(f"{bin}"), inline=False)
                embed.add_field(name="• MODELO", value=data.get("type", "Desconhecido"), inline=False)
                embed.add_field(name="• BANDEIRA", value=data.get("scheme", "Desconhecido"), inline=False)
                embed.add_field(name="• NÍVEL", value=data.get("brand", "Desconhecido"), inline=False)
                embed.add_field(name="• PAÍS", value=data.get("country", {}).get("name", "Desconhecido"), inline=False)
                embed.add_field(name="• SIGLA DO PAÍS", value=data.get("country", {}).get("alpha2", "Desconhecido"), inline=False)
                embed.add_field(name="• BANCO", value=data.get("bank", {}).get("name", "Desconhecido"), inline=False)
                embed.add_field(name="• SITE DO BANCO", value=data.get("bank", {}).get("url", "Desconhecido"), inline=False)
                embed.add_field(name="• TELEFONE", value=data.get("bank", {}).get("phone", "Desconhecido"), inline=False)
                embed.add_field(name="• CIDADE", value=data.get("bank", {}).get("city", "Desconhecido"), inline=False)

                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                await ctx.reply(embed=embed)
            else:
                embed = discord.Embed(title='') 
                embed.set_author(name='ㅤㅤㅤBIN NÃO ENCONTRADAㅤㅤㅤ', icon_url='')
                await ctx.reply(embed=embed)

        except Exception as e: 
            embed = discord.Embed(title='') 
            embed.set_author(name=f'Erro na consulta {response.status_code}', icon_url='')
            await ctx.reply(embed=embed)




    @commands.command()
    async def banco(self, ctx, banco=None):

        if not banco:

            embed = discord.Embed(title='')
            embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO BANCOㅤㅤㅤ', icon_url='')
            embed.add_field(name="Fonte da consulta: **Brasil API**", value="", inline=False)
            embed.add_field(name="Informações de retorno:", value="Informações referente ao banco ou IFNC.", inline=False)
            embed.add_field(name="Status da API:", value="🟢 API ONLINE", inline=False)   
            embed.add_field(name="Use o comando: `./banco` e o {CÓDIGO DO BANCO}", value='*Exemplo*: `./banco 237`', inline=False)
            embed.add_field(name="Observação:", value='*Utilize apenas o código bancário correspondente!*', inline=False)
            return await ctx.reply(embed=embed)

        try:
            data = requests.get(f"https://brasilapi.com.br/api/banks/v1/{banco}").json()

            embed = discord.Embed(title='')

            embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE BANCOㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

            embed.add_field(name="• ISPB", value=data['ispb'], inline=False)
            embed.add_field(name="• NOME DO BANCO", value=data['name'], inline=False)
            embed.add_field(name="• CÓDIGO DO BANCO", value=data['code'], inline=False)
            embed.add_field(name="• INFORMAÇÕES ADICIONAIS", value=data['fullName'], inline=False)

            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
            await ctx.reply(embed=embed)

        except Exception:
            embed = discord.Embed(title='')
            embed.set_author(name='ㅤㅤCÓDIGO BANCÁRIO NÃO ENCONTRADOㅤㅤ', icon_url='')
            return await ctx.reply(embed=embed)



    @commands.command()
    async def covid(self, ctx, covid=None):

        if not covid:

            embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO COVIDㅤㅤㅤ', icon_url='')
            embed.add_field(name="Fonte da consulta: **Covid Brazil**", value="", inline=False)
            embed.add_field(name="Informações de retorno:", value="Informações de casos de covid no brasil por estado.", inline=False)
            embed.add_field(name="Status da API:", value="🟢 API ONLINE", inline=False)   
            embed.add_field(name="Use o comando: `./covid` e o {ESTADO} que deseja.", value='*Exemplo*: `./covid SP`', inline=False)
            embed.add_field(name="Observação:", value='*Utilize apenas a sigla do estado correspondente!*', inline=False)
            embed.add_field(name="Estados Brasileiros com suas respectivas siglas:", value='Acre - `AC`\nAlagoas - `AL`\nAmazonas - `AM`\nBahia - `BA`\nCeará - `CE`\nDistrito Federal - `DF`\nEspírito Santo - `ES`\nGoiás - `GO`\nMaranhão - `MA`\nMato Grosso - `MT`\nMato Grosso do Sul - `MS`\nMinas Gerais - `MG`\nPará - `PA`\nParaíba - `PB`\nParaná - `PR`\nPernambuco - `PE`\nPiauí - `PI`\nRio de Janeiro - `RJ`\nRio Grande do Norte - `RN`\nRio Grande do Sul - `RS`\nRondônia - `RO`\nRoraima	- `RR`\nSanta Catarina - `SC`\nSão Paulo - `SP`\nSergipe - `SE`\nTocantins - `TO`\n', inline=False)
            await ctx.reply(embed=embed)
            return

        data = requests.get(f"https://covid19-brazil-api.vercel.app/api/report/v1/brazil/uf/{covid}").json()

        try:
            embed = discord.Embed(title='')

            embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE COVID19ㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

            embed.add_field(name="• ESTADO", value=data.get('state', 'Sem informação'), inline=False)
            embed.add_field(name="• CASOS", value=data.get('cases', 'Sem informação'), inline=False)
            embed.add_field(name="• MORTES", value=data.get('deaths', 'Sem informação'), inline=False)
            embed.add_field(name="• SUSPEITOS", value=data.get ('suspects', 'Sem informação'), inline=False)
            embed.add_field(name="• DESCARTADOS", value=data.get('refuses', 'Sem informação'), inline=False)
            embed.add_field(name="• ÚLTIMA ATUALIZAÇÃO", value=data.get('datetime', 'Sem informação'), inline=False)
            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

            await ctx.reply(embed=embed)
            
            return
        except Exception:
            embed = discord.Embed(title='')
            embed.set_author(name='ㅤㅤSEM INFORMAÇÕESㅤㅤ', icon_url='')
            return await ctx.reply(embed=embed)



async def setup(bot):
    await bot.add_cog(OtherToolsCommand(bot))


