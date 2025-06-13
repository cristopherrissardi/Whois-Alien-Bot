

import discord
from discord.ext import commands
import requests
import os, re

from utils.buttons import NameResultView

API_KEY = os.getenv("API_KEY")


class CnpjCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cnpj(self, ctx, cnpj=None):

        if not cnpj:

            embed = discord.Embed(title="")
            embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE CNPJ', icon_url='')
            embed.add_field(name="Base de dados: **Receita Federal**", value="", inline=False)
            embed.add_field(name="Informações de retorno:", value="FOTO DO ROSTO, CPF, NOME, NOME DA MÃE, DATA DE NASCIMENTO ETC.", inline=False)
            embed.add_field(name="Status da API:", value="🟢 API ONLINE", inline=False)   
            embed.add_field(name="Use o comando: `./cnpj` e a {CNPJ} que deseja.", value='Exemplo: `./cnpj` 00000000000191', inline=False)
            await ctx.reply(embed=embed)
            return


        cnpj = re.sub(r"[.\-\/]", "", cnpj)

        url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
        response = requests.get(url)
        data = response.json()

        def verificar_erro_api(data):
            if data.get("status") == "ERROR":
                return data.get("message", "Erro desconhecido.")
            return None

        erro = verificar_erro_api(data)
        if erro:
            embed = discord.Embed(title='')

            embed.set_author(name=f'ㅤㅤㅤCNPJ NÃO ENCONTRADOㅤㅤㅤ', icon_url='')
            return await ctx.reply(embed=embed)

        def formatar_qualificacao(qualificacao):
            return re.sub(r"^\d+-", "", qualificacao).strip()

        def verificar_campo(campo, padrao="Sem informação"):
            return campo if campo else padrao

        def buscar_informacoes_socio(nome, qualificacao):
            try:
                api_url = f"http://127.0.0.1:44340/alienlabs/api/database/serasa/basic/search?nome={nome}"
                headers = {"apikey": API_KEY}
                resposta = requests.get(api_url, headers=headers).json()

                if len(resposta) == 1:
                    socio = resposta[0]
                    return f"➣ **Nome**: {socio['nome'].upper()}\n➣ **CPF**: {socio['cpf']}\n➣ **Qualificação**: {qualificacao}"
                elif len(resposta) > 1:
                    return f"➣ **Nome**: {nome}\n➣ **Qualificação**: {qualificacao}"
                else:
                    return f"➣ **Nome**: {nome}\n➣ **Qualificação**: {qualificacao}"
            except Exception as e:

                return f"➣ **Nome**: {nome}\n➣ **Qualificação**: {qualificacao}"
            
        try:
            atividade_principal = data.get("atividade_principal", [])
            if atividade_principal:
                atividade = f"{verificar_campo(atividade_principal[0]['code'])} - {verificar_campo(atividade_principal[0]['text'])}"

            endereco = f"{verificar_campo(data.get('logradouro'))}, {verificar_campo(data.get('numero'))}, {verificar_campo(data.get('bairro'))}, {verificar_campo(data.get('municipio'))} - {verificar_campo(data.get('uf'))}, - {verificar_campo(data.get('cep'))}"
            contato = f"Email: {verificar_campo(data.get('email'))}\nTelefone: {verificar_campo(data.get('telefone'))}"

            embed = discord.Embed(title='')
            embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE CNPJㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

            embed.add_field(name="• CNPJ", value=verificar_campo(data.get("cnpj")), inline=False)
            embed.add_field(name="• NOME DA EMPRESA", value=verificar_campo(data.get("nome")), inline=False)
            embed.add_field(name="• NOME FANTASIA", value=verificar_campo(data.get("fantasia")), inline=False)
            embed.add_field(name="• DATA DE ABERTURA", value=verificar_campo(data.get("abertura")), inline=False)
            embed.add_field(name="• SITUAÇÃO DA EMPRESA", value=verificar_campo(data.get("situacao")), inline=False)
            embed.add_field(name="• CAPITAL SOCIAL", value=f"R$ {verificar_campo(data.get('capital_social'))}", inline=False)
            embed.add_field(name="• TIPO", value=verificar_campo(data.get("tipo")), inline=False)
            embed.add_field(name="• PORTE", value=verificar_campo(data.get("porte")), inline=False)
            embed.add_field(name="• NATUREZA JURÍDICA", value=verificar_campo(data.get("natureza_juridica")), inline=False)
            embed.add_field(name="• ATIVIDADE PRINCIPAL", value=atividade, inline=False)
            embed.add_field(name="• ENDEREÇO", value=endereco, inline=False)    
            embed.add_field(name="• COMPLEMENTO DO ENDEREÇO", value=verificar_campo(data.get("complemento")), inline=False)
            embed.add_field(name="• CONTATOS DA EMPRESA", value=contato, inline=False)
            embed.add_field(name="• ÚLTIMA ATUALIZAÇÃO", value=verificar_campo(data.get("ultima_atualizacao")), inline=False)
            embed.add_field(name="• STATUS DA EMPRESA", value=verificar_campo(data.get("status")), inline=False)
            embed.add_field(name="• ENTES FEDERAIS", value=verificar_campo(data.get("efr")), inline=False)
            embed.add_field(name="• MOTIVO SITUAÇÃO", value=verificar_campo(data.get("motivo_situacao")), inline=False)
            embed.add_field(name="• SITUAÇÃO ESPECIAL", value=verificar_campo(data.get("situacao_especial")), inline=False)
            embed.add_field(name="• DATA SITUAÇÃO ESPECIAL", value=verificar_campo(data.get("data_situacao_especial")), inline=False)
            embed.add_field(name="• SÓCIOS/ADMINISTRADORES", value="", inline=False)

            qsa = data.get("qsa", [])

            if qsa:

                qsa_limited = qsa[:15]

                if len(qsa) > 15:
                    socios_nomes = "\n".join([f"{verificar_campo(s['nome'])}" for s in qsa_limited])
                    embed.add_field(name="", value=socios_nomes, inline=False)
                    embed.add_field(name="• Aviso", value=f"Exibindo os primeiros 15 de {len(qsa)} sócios.", inline=False)
                else:
                    socios_info = []
                    for socio in qsa_limited:
                        nome_socio = verificar_campo(socio.get('nome'))
                        qualificacao_socio = formatar_qualificacao(verificar_campo(socio.get('qual')))
                        info_socio = buscar_informacoes_socio(nome_socio, qualificacao_socio)
                        if info_socio:
                            socios_info.append(info_socio)

                    if socios_info:
                        socios_texto = "\n\n".join(socios_info)
                        embed.add_field(name="", value=socios_texto, inline=False)
                    else:
                        socios_nomes = "\n".join([f"- **Nome**: {verificar_campo(s['nome'])}\n- **Qualificação**: {verificar_campo(s['qual'])}" for s in qsa_limited])
                        embed.add_field(name="", value=socios_nomes, inline=False)
            else:
                embed.add_field(name="", value="Nenhum sócio proprietário encontrado.", inline=False)


            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

            await ctx.reply(embed=embed)
            return

        except Exception as e:
            embed = discord.Embed(title='')
            embed.set_author(name=f'Erro na consulta {response.status_code}', icon_url='')
            return await ctx.reply(embed=embed)



async def setup(bot):
    await bot.add_cog(CnpjCommand(bot))
