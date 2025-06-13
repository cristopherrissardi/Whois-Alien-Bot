
import discord
from discord.ext import commands
import requests
import os, io

from utils.buttons import NameResultView

API_KEY = os.getenv("API_KEY")


class PlacaCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def placa(self, ctx, *, placa=None):

        if not placa:

            embed = discord.Embed(title="")
            embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE PLACA', icon_url='')
            embed.add_field(name="Base de dados: **Detran**", value="", inline=False)
            embed.add_field(name="Informações de retorno:", value="INFORMAÇÕES COMPLETAS SOBRE O VEÍCULO E ÀS VEZES O PROPRIETÁRIO.", inline=False)
            embed.add_field(name="Status da API:", value="🟢 API ONLINE", inline=False)   
            embed.add_field(name="Use o comando: `./placa` e a {PLACA} que deseja.", value='Exemplo: `./placa` ABC1234', inline=False)
            await ctx.reply(embed=embed)
            return

        placa_formatada = placa.strip().upper().replace('-', '')
        url = f"http://127.0.0.1:44340/alienlabs/api/database/vehicle/search?placa={placa_formatada}"

        headers = {"apikey": API_KEY}

        response = requests.get(url, headers=headers)
        try:
            if response.status_code == 200:
                data = response.json()

                if len(data) > 0:
                    placa_veiculo = data[0] 
                    modelo_veiculo = placa_veiculo.get('modelo_veiculo', {})

                    embed = discord.Embed(title="")
                    embed.set_author(
                        name=f'ㅤㅤㅤㅤㅤㅤㅤCONSULTA DE PLACA - INFORMAÇÕES GERAISㅤㅤㅤㅤㅤㅤㅤㅤ',icon_url='')
                    embed.set_thumbnail(url=placa_veiculo.get('logo_marca', ''))

                    embed.add_field(name="Placa do veículo", value=placa_veiculo.get('placa', 'Desconhecido'), inline=True)
                    embed.add_field(name="Marca", value=modelo_veiculo.get('marca', 'Desconhecido'), inline=True)
                    embed.add_field(name="Modelo", value=modelo_veiculo.get('modelo', 'Desconhecido'), inline=True)
                    embed.add_field(name="Cor do Veículo", value=placa_veiculo.get('cor_veiculo', 'Desconhecido'), inline=True)
                    embed.add_field(name="Grupo do Modelo", value=modelo_veiculo.get('grupo_modelo_veiculo', 'Desconhecido'), inline=True)
                    embed.add_field(name="Segmento", value=modelo_veiculo.get('segmento', 'Desconhecido'), inline=True)
                    embed.add_field(name="Sub-Segmento", value=modelo_veiculo.get('sub_segmento', 'Desconhecido'), inline=True)
                    embed.add_field(name="Tipo de Veículo", value=placa_veiculo.get('tipo_veiculo', 'Desconhecido'), inline=True)
                    embed.add_field(name="Espécie do Veículo", value=placa_veiculo.get('especie_veiculo', 'Desconhecido'), inline=True)
                    embed.add_field(name="Tipo de Montagem", value=placa_veiculo.get('tipo_montagem', 'Desconhecido'), inline=True)
                    embed.add_field(name="Situação do Chassi", value=placa_veiculo.get('situacao_chassi', 'Desconhecido'), inline=True)
                    embed.add_field(name="Chassi", value=placa_veiculo.get('chassi', 'Desconhecido'), inline=True)
                    embed.add_field(name="Renavam", value=placa_veiculo.get('renavam', 'Desconhecido'), inline=True)
                    embed.add_field(name="Número do motor", value=placa_veiculo.get('motor', 'Desconhecido'), inline=True)
                    embed.add_field(name="Combustível", value=placa_veiculo.get('combustivel', 'Desconhecido'), inline=True)
                    embed.add_field(name="Linha", value=placa_veiculo.get('linha', 'Desconhecido'), inline=True)
                    embed.add_field(name="Situação do veículo", value=placa_veiculo.get('situacao_veiculo', 'Desconhecido'), inline=True)
                    embed.add_field(name="Tipo DOC. Proprietário", value=placa_veiculo.get('tipo_doc_prop', 'Desconhecido'), inline=True)
                    embed.add_field(name="Município", value=placa_veiculo.get('municipio', 'Desconhecido'), inline=True)
                    embed.add_field(name="UF da Placa", value=placa_veiculo.get('uf_placa', 'Desconhecido'), inline=True)
                    embed.add_field(name="Ano de Fabricação", value=placa_veiculo.get('ano_fabricacao', 'Desconhecido'), inline=True)
                    embed.add_field(name="Ano do Modelo", value=placa_veiculo.get('ano_modelo', 'Desconhecido'), inline=True)
                    embed.add_field(name="Nacionalidade", value=placa_veiculo.get('nacionalidade', 'Desconhecido'), inline=True)
                    embed.add_field(name="Data de atualização", value=placa_veiculo.get('data_atualizacao', 'Desconhecido'), inline=True)
                    embed.add_field(name="Última atualização", value=placa_veiculo.get('ultima_atualizacao', 'Desconhecido'), inline=True)

                    embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
                    await ctx.reply(embed=embed)

                    embed = discord.Embed(title="")
                    embed.set_author(
                        name=f'ㅤㅤㅤㅤㅤㅤㅤCONSULTA DE PLACA - INFORMAÇÕES GERAISㅤㅤㅤㅤㅤㅤㅤㅤ',icon_url='')
                    embed.set_thumbnail(url=placa_veiculo.get('placa_png', ''))

                    embed.add_field(name="Cilindradas", value=placa_veiculo.get('cilindradas', 'Desconhecido'), inline=True)
                    embed.add_field(name="Potência", value=placa_veiculo.get('potencia', 'Desconhecido'), inline=True)
                    embed.add_field(name="Carroceria", value=placa_veiculo.get('carroceria', 'Desconhecido'), inline=True)
                    embed.add_field(name="Tipo de Carroceria", value=placa_veiculo.get('tipo_carroceria', 'Desconhecido'), inline=True)
                    embed.add_field(name="Peso Bruto Total", value=placa_veiculo.get('peso_bruto_total', 'Desconhecido'), inline=True)
                    embed.add_field(name="Capacidade de Carga", value=placa_veiculo.get('capacidade_carga', 'Desconhecido'), inline=True)
                    embed.add_field(name="Capacidade Máxima de Tração", value=placa_veiculo.get('cap_maxima_tracao', 'Desconhecido'), inline=True)
                    embed.add_field(name="Eixo traseiro", value=placa_veiculo.get('eixo_traseiro_dif', 'Desconhecido'), inline=True)
                    embed.add_field(name="Terceiro eixo", value=placa_veiculo.get('terceiro_eixo', 'Desconhecido'), inline=True)
                    embed.add_field(name="Quantidade de eixos", value=placa_veiculo.get('eixos', 'Desconhecido'), inline=True)
                    embed.add_field(name="Quantidade de passageiros", value=placa_veiculo.get('quantidade_passageiro', 'Desconhecido'), inline=True)
                    embed.add_field(name="Caixa de cambio", value=placa_veiculo.get('caixa_cambio', 'Desconhecido'), inline=True)

                    embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
                    await ctx.reply(embed=embed)

                    embed = discord.Embed(title="")
                    embed.set_author(
                        name=f'ㅤㅤㅤㅤCONSULTA DE PLACA - INFORMAÇÕES TRIBUTÁRIASㅤㅤㅤㅤㅤㅤㅤㅤ',icon_url='')
                    embed.set_thumbnail(url="https://i.imgur.com/TKLsWNT.png")

                    embed.add_field(name="ID do Veículo", value=placa_veiculo.get('id_veiculo', 'Desconhecido'), inline=True)
                    embed.add_field(name="Tipo de Documento Importadora", value=placa_veiculo.get('tipo_doc_importadora', 'Desconhecido'), inline=True)
                    embed.add_field(name="CNPJ Importadora", value=placa_veiculo.get('ident_importadora', 'Desconhecido'), inline=True)
                    embed.add_field(name="Declaração de Imposto", value=placa_veiculo.get('di', 'Desconhecido'), inline=True)
                    embed.add_field(name="Reg. Declaração de Imposto", value=placa_veiculo.get('registro_di', 'Desconhecido'), inline=True)
                    embed.add_field(name="Unidade da Secr. da RFB", value=placa_veiculo.get('uf_faturado', 'Desconhecido'), inline=True)
                    embed.add_field(name="Limite Restrição Tributária", value=placa_veiculo.get('limite_restricao_trib', 'Desconhecido'), inline=True)
                    embed.add_field(name="Comprado em", value=placa_veiculo.get('faturado', 'Desconhecido'), inline=True)
                    embed.add_field(name="Tipo de Documento Faturado", value=placa_veiculo.get('tipo_doc_faturado', 'Desconhecido'), inline=True)
                    embed.add_field(name="UF de faturamento", value=placa_veiculo.get('uf_faturado', 'Desconhecido'), inline=True)
                    embed.add_field(name="Placa modelo antigo", value=placa_veiculo.get('placa_modelo_antigo', 'Desconhecido'), inline=True)
                    embed.add_field(name="Placa modelo novo", value=placa_veiculo.get('placa_modelo_novo', 'Desconhecido'), inline=True)
                    embed.add_field(name="Restrição 1", value=placa_veiculo.get('restricao_1', 'Desconhecido'), inline=True)
                    embed.add_field(name="Restrição 2", value=placa_veiculo.get('restricao_2', 'Desconhecido'), inline=True)
                    embed.add_field(name="Restrição 3", value=placa_veiculo.get('restricao_3', 'Desconhecido'), inline=True)
                    embed.add_field(name="Restrição 4", value=placa_veiculo.get('restricao_4', 'Desconhecido'), inline=True)
                    embed.add_field(name="Proprietário", value=placa_veiculo.get('proprietario_info', {}).get('proprietario', 'Desconhecido'), inline=True)
                    embed.add_field(name="CPF/CNPJ", value=placa_veiculo.get('proprietario_info', {}).get('cpf', 'Desconhecido'), inline=True)

                    embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
                    await ctx.reply(embed=embed)

                else:
                    embed = discord.Embed(title="")
                    embed.set_author(name='PLACA NÃO ENCONTRADAㅤㅤㅤ', icon_url='')
                    await ctx.reply(embed=embed)
            else:
                embed.set_author(name='ㅤㅤㅤPLACA NÃO ENCONTRADAㅤㅤㅤ', icon_url='')
                await ctx.reply(embed=embed)

        except Exception as e:
            embed.set_author(name=f'Erro na consulta {response.status_code}', icon_url='')
            await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(PlacaCommand(bot))
