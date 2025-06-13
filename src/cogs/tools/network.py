
import discord
from discord.ext import commands
import requests
import os, aiohttp 
from datetime import datetime

from utils.buttons import NameResultView
from utils.formatters import convert_info


API_KEY = os.getenv("API_KEY")


class NetworkToolsCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ip(self, ctx, ip=None):

        if not ip:
            embed = discord.Embed(title='')
            embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO IPㅤㅤㅤ', icon_url='')
            embed.add_field(name="Fonte da consulta: **IP Whois**", value="", inline=False)
            embed.add_field(name="Informações de retorno:", value="Informações 100% Atualizadas de IP.", inline=False)
            embed.add_field(name="Status da API:", value="🟢 API ONLINE", inline=False)   
            embed.add_field(name="Use o comando: `./ip` e o {IP} que deseja.", value='*Exemplo: `./ip` 1.1.1.1*', inline=False)
            await ctx.reply(embed=embed)
            return

        data = requests.get(f"https://ipwhois.app/json/{ip}").json()

        MAPS_API = os.getenv("GOOGLE_MAPS_API_KEY")

        latitude = data.get('latitude')
        longitude = data.get('longitude')

        maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
        mapa_url = f"https://maps.googleapis.com/maps/api/staticmap?center={latitude},{longitude}&zoom=15&size=700x250&markers=color:red%7C{latitude},{longitude}&key={MAPS_API}"


        country_code_icon = data.get('country_code').lower()

        try:
            embed = discord.Embed(title='')

            embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE IPㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
            embed.add_field(name="\n\n", value="\n\n", inline=False)
            embed.add_field(name="IP", value=data.get('ip', 'Sem informação'), inline=True)
            embed.add_field(name="TIPO", value=data.get('type', 'Sem informação'), inline=True)
            embed.add_field(name="STATUS", value=data.get('success', 'Sem informação'), inline=True)
            embed.add_field(name="CIDADE", value=data.get('city', 'Sem informação'), inline=True)
            embed.add_field(name="ESTADO", value=data.get('region', 'Sem informação'), inline=True)
            embed.add_field(name="PAÍS", value=data.get('country', 'Sem informação'), inline=True)
            embed.add_field(name="CONTINENTE", value=data.get('continent_code', 'Sem informação'), inline=True)
            embed.add_field(name="CÓD. DO PAIS", value=data.get('country_code', 'Sem informação'), inline=True)
            embed.add_field(name="LOCALIZAÇÃO", value=f"[{latitude},{longitude}]({maps_link})", inline=True)
            embed.add_field(name="PROVEDOR", value=data.get('isp', 'Sem informação'), inline=True)
            embed.add_field(name="ORG", value=data.get('org', 'Sem informação'), inline=True)
            embed.add_field(name="ASN", value=data.get('asn', 'Sem informação'), inline=True)
            embed.add_field(name="", value="", inline=False)
            embed.add_field(name="INFORMAÇÕES EXTRAS", value="", inline=False)
            embed.add_field(name="CÓD. DO CONTINENTE", value=data.get('continent_code', 'Sem informação'), inline=True)
            embed.add_field(name="CAPITAL DO PAÍS", value=data.get('country_capital', 'Sem informação'), inline=True)
            embed.add_field(name="DDI", value=data.get('country_phone', 'Sem informação'), inline=True)
            embed.add_field(name="MOEDA", value=data.get('currency', 'Sem informação'), inline=True)
            embed.add_field(name="VALOR DA MOEDA", value=data.get('currency_rates', 'Sem informação'), inline=True)
            embed.add_field(name="COD. DA MOEDA", value=data.get('currency_code', 'Sem informação'), inline=True)
            embed.add_field(name="FUSO HORÁRIO", value=data.get('timezone', 'Sem informação'), inline=True)
            embed.add_field(name="OFFSET", value=data.get('timezone_name', 'Sem informação'), inline=True)
            embed.add_field(name="GMT", value=data.get('timezone_gmt', 'Sem informação'), inline=True)

            embed.set_thumbnail(url=f"https://flagcdn.com/w640/{country_code_icon}.png")
            embed.set_image(url=mapa_url)

            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

            await ctx.reply(embed=embed)

            return
        except Exception:
            pass





    @commands.command()
    async def site(self, ctx, site=None):

        if not site:
            embed = discord.Embed(title='')
            embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO SITE LOOKUPㅤㅤㅤ', icon_url='')
            embed.add_field(name="Fonte da consulta: **IP Whois**", value="", inline=False)
            embed.add_field(name="Informações de retorno:", value="Informações 100% Atualizadas dos Sites.", inline=False)
            embed.add_field(name="Status da API:", value="🟢 API ONLINE", inline=False)   
            embed.add_field(name="Use o comando: `./site` e o {SITE} que deseja.", value='*Exemplo: `./site` www.google.com*', inline=False)
            await ctx.reply(embed=embed)
            return

        data = requests.get(f"https://ipwhois.app/json/{site}").json()

        MAPS_API = os.getenv("GOOGLE_MAPS_API_KEY")

        latitude = data.get('latitude')
        longitude = data.get('longitude')

        maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
        mapa_url = f"https://maps.googleapis.com/maps/api/staticmap?center={latitude},{longitude}&zoom=15&size=700x250&markers=color:red%7C{latitude},{longitude}&key={MAPS_API}"

        country_code_icon = data.get('country_code').lower()

        try:
            embed = discord.Embed(title='')

            embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE SITEㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
            embed.add_field(name="\n\n", value="\n\n", inline=False)
            embed.add_field(name="IP", value=data.get('ip', 'Sem informação'), inline=True)
            embed.add_field(name="TIPO", value=data.get('type', 'Sem informação'), inline=True)
            embed.add_field(name="STATUS", value=data.get('success', 'Sem informação'), inline=True)
            embed.add_field(name="CIDADE", value=data.get('city', 'Sem informação'), inline=True)
            embed.add_field(name="ESTADO", value=data.get('region', 'Sem informação'), inline=True)
            embed.add_field(name="PAÍS", value=data.get('country', 'Sem informação'), inline=True)
            embed.add_field(name="CONTINENTE", value=data.get('continent_code', 'Sem informação'), inline=True)
            embed.add_field(name="CÓD. DO PAIS", value=data.get('country_code', 'Sem informação'), inline=True)
            embed.add_field(name="LOCALIZAÇÃO", value=f"[{latitude},{longitude}]({maps_link})", inline=True)
            embed.add_field(name="PROVEDOR", value=data.get('isp', 'Sem informação'), inline=True)
            embed.add_field(name="ORG", value=data.get('org', 'Sem informação'), inline=True)
            embed.add_field(name="ASN", value=data.get('asn', 'Sem informação'), inline=True)
            embed.add_field(name="", value="", inline=False)
            embed.add_field(name="INFORMAÇÕES EXTRAS", value="", inline=False)
            embed.add_field(name="CÓD. DO CONTINENTE", value=data.get('continent_code', 'Sem informação'), inline=True)
            embed.add_field(name="CAPITAL DO PAÍS", value=data.get('country_capital', 'Sem informação'), inline=True)
            embed.add_field(name="DDI", value=data.get('country_phone', 'Sem informação'), inline=True)
            embed.add_field(name="MOEDA", value=data.get('currency', 'Sem informação'), inline=True)
            embed.add_field(name="VALOR DA MOEDA", value=data.get('currency_rates', 'Sem informação'), inline=True)
            embed.add_field(name="COD. DA MOEDA", value=data.get('currency_code', 'Sem informação'), inline=True)
            embed.add_field(name="FUSO HORÁRIO", value=data.get('timezone', 'Sem informação'), inline=True)
            embed.add_field(name="OFFSET", value=data.get('timezone_name', 'Sem informação'), inline=True)
            embed.add_field(name="GMT", value=data.get('timezone_gmt', 'Sem informação'), inline=True)

            embed.set_thumbnail(url=f"https://flagcdn.com/w640/{country_code_icon}.png")
            embed.set_image(url=mapa_url)

            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

            await ctx.reply(embed=embed)

            return
        except Exception:
            pass




    @commands.command()
    async def whois(self, ctx, domain: str, whois=None):


        if not whois:
            embed = discord.Embed(title='') 
            embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO WHOISㅤㅤㅤ', icon_url='')
            embed.add_field(name="Fonte da consulta: **IP2 Whois**", value="", inline=False)
            embed.add_field(name="Informações de retorno:", value="ISP, ASN, DOMÍNIO E OUTROS.", inline=False)
            embed.add_field(name="Status da API:", value="🟢 API ONLINE", inline=False)   
            embed.add_field(name="Use o comando: `./whois` e o {SITE} que deseja", value='*Exemplo*: `./whois google.com`', inline=False)
            await ctx.reply(embed=embed)
            return


        api_key_whois = os.getenv("IP2WHOIS_KEY")
        api_url = f"https://api.ip2whois.com/v2?key={api_key_whois}&domain={domain}"
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(api_url) as response:
                    if response.status != 200:
                        embed = discord.Embed(title="")
                        embed.set_author(name=f'ERRO AO OBTER OS DADOS WHOIS PARA! ERRO: {response.status}', icon_url='')
                        await ctx.reply(embed=embed)
                        return
                    
                    data = await response.json()

            def get_value(key, default="Não encontrado"):
                return str(data.get(key, default)) if data.get(key) else default

            def get_nested_value(parent_key, child_key, default="Não encontrado"):
                return str(data.get(parent_key, {}).get(child_key, default)) if data.get(parent_key) else default

            def format_section(section_data):

                formatted = ""
                for key, value in section_data.items():
                    formatted += f"- **{key.capitalize().replace('_', ' ')}:** {value if value else 'Não encontrado'}\n"
                return formatted.strip()

            embed = discord.Embed(title=f"")
            
            embed.set_author(name='ㅤㅤㅤㅤㅤㅤCONSULTA WHOIS REALIZADA COM SUCESSOㅤㅤㅤㅤㅤㅤ', icon_url='')

            embed.add_field(name="Domínio", value=get_value("domain"), inline=False)
            embed.add_field(name="ID do Domínio", value=get_value("domain_id"), inline=False)
            embed.add_field(name="Status", value=get_value("status"), inline=False)
            embed.add_field(name="Criado em", value=get_value("create_date"), inline=False)
            embed.add_field(name="Atualizado em", value=get_value("update_date"), inline=False)
            embed.add_field(name="Expira em", value=get_value("expire_date"), inline=False)
            embed.add_field(name="Idade do Domínio (dias)", value=get_value("domain_age") + " dias", inline=False)
            embed.add_field(name="Servidor WHOIS", value=get_value("whois_server"), inline=False)

            sections = {
                "Informações do Registrador": data.get("registrar", {}),
                "Informações do Registrante": data.get("registrant", {}),
                "Informações do Administrador": data.get("admin", {}),
                "Informações Técnicas": data.get("tech", {}),
                "Informações de Cobrança": data.get("billing", {}),
            }

            for title, section_data in sections.items():
                if section_data:  
                    embed.add_field(name=title, value=format_section(section_data), inline=False)

            nameservers = data.get("nameservers", [])
            if nameservers:
                embed.add_field(
                    name="Servidores de Nome (DNS)",
                    value="\n".join(nameservers) if nameservers else "Não encontrado",
                    inline=False
                )

            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

            await ctx.reply(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="")
            embed.set_author(name=f'ERRO AO CONSULTAR O ENDEREÇO WHOIS', icon_url='')

            await ctx.reply(embed=embed)

    @commands.command()
    async def maclookup(self, ctx, maclookup=None):

        if not maclookup:
            embed = discord.Embed(title='') 
            embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO MACLOOKUPㅤㅤㅤ', icon_url='')
            embed.add_field(name="Fonte da consulta: **WhoisXML**", value="", inline=False)
            embed.add_field(name="Informações de retorno:", value="Fabricante, Data de criação, endereço do fabricante, país etc.", inline=False)
            embed.add_field(name="Status da API:", value="🟢 API ONLINE", inline=False)   
            embed.add_field(name="Use o comando: `./maclookup` e o {MAC} que deseja", value='*Exemplo*: `./maclookup FC:FB:FB:01:FA:21`', inline=False)
            await ctx.reply(embed=embed)
            return

        mac_key = os.getenv("WHOISXML_TOKEN")
        url = f"https://mac-address.whoisxmlapi.com/api/v1?apiKey={mac_key}&macAddress={maclookup}&outputFormat=json"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()

                date_created_iso = data.get("blockDetails", {}).get("dateCreated", "SEM INFORMAÇÃO")
                date_updated_iso = data.get("blockDetails", {}).get("dateUpdated", "SEM INFORMAÇÃO")

                date_created_br = datetime.strptime(date_created_iso, "%Y-%m-%d").strftime("%d/%m/%Y") 
                date_updated_br = datetime.strptime(date_updated_iso, "%Y-%m-%d").strftime("%d/%m/%Y")

                embed = discord.Embed(title="")

                embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤBUSCA DE ENDEREÇO MACㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='') 

                embed.add_field(name="• INICIAL DO MAC ADRESS", value=data.get("vendorDetails", {}).get("oui", "SEM INFORMAÇÃO"), inline=False)
                embed.add_field(name="• ENDEREÇO PRIVADO", value=data.get("vendorDetails", {}).get("isPrivate", "SEM INFORMAÇÃO"), inline=False)
                embed.add_field(name="• FABRICANTE", value=data.get("vendorDetails", {}).get("companyName", "SEM INFORMAÇÃO"), inline=False)
                embed.add_field(name="• ENDEREÇO DO FABRICANTE", value=data.get("vendorDetails", {}).get("companyAddress", "SEM INFORMAÇÃO"), inline=False)
                embed.add_field(name="• PAÍS", value=data.get("vendorDetails", {}).get("countryCode", "SEM INFORMAÇÃO"), inline=False)
                embed.add_field(name="• BLOCO ENCONTRADO", value=data.get("blockDetails", {}).get("blockFound", "SEM INFORMAÇÃO"), inline=False)
                embed.add_field(name="• DATA DE CRIAÇÃO", value=date_created_br, inline=False)
                embed.add_field(name="• DATA DE ATUALIZAÇÃO", value=date_updated_br, inline=False)
                embed.add_field(name="• ENDEREÇO MAC COMPLETO", value=data.get("macAddressDetails", {}).get("searchTerm", "SEM INFORMAÇÃO"), inline=False)
                embed.add_field(name="• VALIDO", value=data.get("macAddressDetails", {}).get("isValid", "SEM INFORMAÇÃO"), inline=False)
                embed.add_field(name="• MAQUINA VIRTUAL ATIVA", value=data.get("virtualMachine", {}).get("virtualMachine", "SEM INFORMAÇÃO"), inline=False)
                embed.add_field(name="• TRANSMISSÃO", value=data.get("macAddressDetails", {}).get("transmissionType", "SEM INFORMAÇÃO"), inline=False)
                embed.add_field(name="• ADMINISTRADOR", value=data.get("macAddressDetails", {}).get("administrationType", "SEM INFORMAÇÃO"), inline=False)
                embed.add_field(name="• NOTAS WIRESHARK", value=data.get("macAddressDetails", {}).get("wiresharkNotes", "SEM INFORMAÇÃO"), inline=False)

                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
                
                await ctx.reply(embed=embed)

            else:
                embed = discord.Embed(title="")
                embed.set_author(name=f'ERRO AO CONSULTAR O ENDEREÇO MAC {maclookup}', icon_url='')

                await ctx.reply(embed=embed)

        except Exception as e: 
            
            embed = discord.Embed(title="")

            embed.set_author(name="ㅤㅤCOMANDO DE CONSULTA DE ENDEREÇO MACㅤㅤ") 
            embed.add_field(name="Use o comando: `./maclookup` e a endereço {MAC} que deseja.", value='*Exemplo*: `./maclookup 00:00:5E:00:53:AF`', inline=False)
            embed.add_field(name="Observação:", value='*Pode ser utilizado somente letras maiúscilas e minúsculas*', inline=False)  
            await ctx.reply(embed=embed)

    # @commands.command()
    # async def reverseip(self, ctx, reverseip):

    #     view_dns_key = os.getenv("VIEWDNS_TOKEN")

    #     url = f"https://api.viewdns.info/reverseip/?host={reverseip}&apikey={view_dns_key}&output=json"

    #     try:
    #         response = requests.get(url)

    #         if response.status_code == 200:
    #             data = response.json()
    #             reverse_ip = data.get('response', {}).get('domains', [])

    #             embed = discord.Embed(title="", description="")

    #             for reverse in reverse_ip:

    #                 nome_site = reverse.get('name', 'Desconhecida')
    #                 ultimo_resolve = reverse.get('last_resolved', 'Desconhecido')


    #                 embed.add_field(name=f"NOME DO SITE: {nome_site}", value=f"ÚLTIMO RESOLVER: {ultimo_resolve}", inline=False)

    #                 embed.set_author(name='ㅤㅤㅤㅤREVERSE IP LOOKUP EFETUADO COM SUCESSOㅤㅤㅤ', icon_url='')
    #                 embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

    #             await ctx.reply(embed=embed)

    #         else:

    #             embed = discord.Embed(title="",)
    #             embed.add_field(name="", value=f"Ocorreu um erro durante consultar o IP Reverso. Status code: {response.status_code}", inline=False)
    #             embed.set_author(name='Erro na Resposta da API - ReverseIP Lookup', icon_url='')

    #             await ctx.reply(embed=embed)

    #     except Exception as e:
    #         embed = discord.Embed(title="")
    #         embed.add_field(name="", value=f"Ocorreu um erro ao consultar o IP Reverso: {str(e)}", inline=False)
    #         embed.set_author(name='Erro na Resposta da API - ReverseIP Lookup', icon_url='')

    #         await ctx.reply(embed=embed)

    # @commands.command()
    # async def traceroute(self, ctx, traceroute):

    #     view_dns_key = os.getenv("VIEWDNS_TOKEN")
    #     url = f"https://api.viewdns.info/traceroute/?domain={traceroute}&apikey={view_dns_key}&output=json"

    #     try:
    #         response = requests.get(url)

    #         if response.status_code == 200:
    #             data = response.json()
    #             route = data.get('response', {}).get('hops', [])

    #             embed = discord.Embed(title="", description="")

    #             for route_info in route:

    #                 numero_id = route_info.get('number', 'Desconhecida')
    #                 hostname = route_info.get('hostname', 'Desconhecido')
    #                 ip_addrs = route_info.get('ip', 'Desconhecido')
    #                 rtt_info = route_info.get('rtt', 'Desconhecido')
                    
    #                 embed.add_field(name=f"SERVIDOR N°: {numero_id}", value=f"ENDEREÇO IP: {ip_addrs}\nSERVIDOR: {hostname}\nTEMPO DE IDA E VOLTA (ms): {rtt_info}", inline=False)

    #                 embed.set_author(name='ㅤㅤㅤㅤㅤTRACEROUTE EFETUADO COM SUCESSOㅤㅤㅤㅤ', icon_url='')
    #                 embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

    #             await ctx.reply(embed=embed)

    #         else:

    #             embed = discord.Embed(title="",)
    #             embed.add_field(name="", value=f"Ocorreu um erro durante traçar a rota do servidor. Status code: {response.status_code}", inline=False)
    #             embed.set_author(name='Erro na Resposta da API - Traceroute', icon_url='')

    #             await ctx.reply(embed=embed)

    #     except Exception as e:
    #         embed = discord.Embed(title="")
    #         embed.add_field(name="", value=f"Ocorreu um erro ao traçar a rota do servidor: {str(e)}", inline=False)
    #         embed.set_author(name='Erro na Resposta da API - Traceroute', icon_url='')

    #         await ctx.reply(embed=embed)

    @commands.command()
    async def portscan(self, ctx, portscan=None):
        
        if not portscan:

            embed = discord.Embed(title='') 
            embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO PORTSCANㅤㅤㅤ', icon_url='')
            embed.add_field(name="Fonte da consulta: **NMAP**", value="", inline=False)
            embed.add_field(name="Informações de retorno:", value="Portas abertas e serviços", inline=False)
            embed.add_field(name="Status da API:", value="🟢 API ONLINE", inline=False)   
            embed.add_field(name="Use o comando: `./portscan` e o {IP} que deseja", value='*Exemplo*: `./portscan 1.1.1.1`', inline=False)
            await ctx.reply(embed=embed)
            return


        view_dns_key = os.getenv("VIEWDNS_TOKEN")
        url = f"https://api.viewdns.info/portscan/?host={portscan}&apikey={view_dns_key}&output=json"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                portas = data.get('response', {}).get('port', [])

                embed = discord.Embed(title="", description="Nosso scan de portas são totalmente baseados nos bancos de dados do Nmap.")
                
                for porta_info in portas:

                    numero_porta = porta_info.get('number', 'Desconhecida')
                    servico = porta_info.get('service', 'Desconhecido')
                    status = porta_info.get('status', 'Desconhecido')
                    
                    embed.add_field(name=f"Porta {numero_porta}", value=f"Serviço: {servico}\nStatus: {status}", inline=True)
                    embed.set_author(name='ㅤㅤㅤㅤㅤㅤSCAN DE PORTAS EFETUADO COM SUCESSOㅤㅤㅤㅤ', icon_url='')
                    embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                await ctx.reply(embed=embed)

            else:

                embed = discord.Embed(title="",)
                embed.add_field(name="", value=f"ERRO: {response.status_code}", inline=False)
                embed.set_author(name='ERRO NA RESPOSTA DA API - PORTSCAN', icon_url='')

                await ctx.reply(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="")
            embed.add_field(name="", value=f"ERRO: {str(e)}", inline=False)
            embed.set_author(name='ERRO NA RESPOSTA DA API - PORTSCAN', icon_url='')
            await ctx.reply(embed=embed)


    @commands.command()
    async def emailinfo(self, ctx, emailinfo=None):

        if not emailinfo:
            embed = discord.Embed(title='') 
            embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO EMAIL-INFOㅤㅤㅤ', icon_url='')
            embed.add_field(name="Fonte da consulta: **APILayer**", value="", inline=False)
            embed.add_field(name="Informações de retorno:", value="Informações, domínios, validade e outros.", inline=False)
            embed.add_field(name="Status da API:", value="🟢 API ONLINE", inline=False)   
            embed.add_field(name="Use o comando: `./emailinfo` e o {E-MAIL} que deseja", value='*Exemplo*: `./emailinfo joao@gmail.com`', inline=False)

            await ctx.reply(embed=embed)
            return

        email_token = os.getenv("APILAYER_TOKEN")
        data = requests.get(
            f"https://api.apilayer.com/email_verification/check?email={emailinfo}&apikey={email_token}"
        ).json()
        
        try:
            embed = discord.Embed(title='')
            embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCHECKER DE E-MAILㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')  
            embed.add_field(name="• E-MAIL", value=data['email'], inline=False)
            embed.add_field(name="• USUÁRIO", value=data['user'], inline=False)
            embed.add_field(name="• DOMÍNIO", value=data['domain'], inline=False)
            embed.add_field(name="• FORMATO VÁLIDO", value=convert_info(data['format_valid']), inline=False)
            embed.add_field(name="• CORREIO VÁLIDO", value=convert_info(data['mx_found']), inline=False)
            embed.add_field(name="• SMTP DISPONÍVEL", value=convert_info(data['smtp_check']), inline=False)
            embed.add_field(name="• FUNÇÕES ATIVAS", value=convert_info(data['role']), inline=False)
            embed.add_field(name="• E-MAIL DISPONÍVEL", value=convert_info(data['disposable']), inline=False)
            embed.add_field(name="• E-MAIL GRATUITO", value=convert_info(data['free']), inline=False)
            embed.add_field(name="• PONTUAÇÃO DE E-MAIL", value=data['score'], inline=False)

            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

            await ctx.reply(embed=embed)

            return
        except Exception:
            embed = discord.Embed(title='')
            embed.set_author(name='E-MAIL NÃO ENCONTRADO', icon_url='')
            return


async def setup(bot):
    await bot.add_cog(NetworkToolsCommand(bot))
