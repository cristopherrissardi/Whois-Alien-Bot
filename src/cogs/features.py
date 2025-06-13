import discord
from discord.ext import commands
import os
import time
import requests


class FeaturesCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member):  # Adicionado 'self' e corrigido a ordem dos parâmetros
        user_id = member.id
        joined_at = member.joined_at
        created_at = member.created_at
        avatar_url = member.avatar.url
        permissions = member.roles
        
        embed = discord.Embed(title=f'Informações de {member}')
        embed.add_field(name="Nome de usuário", value=f"`{member}`", inline=True)
        embed.add_field(name="ID de usuário", value=f"`{user_id}`", inline=True)
        embed.add_field(name="Entrou no Discord em", value=created_at.strftime("%d/%m/%Y %H:%M:%S"), inline=False)
        embed.add_field(name="Entrou no servidor em", value=joined_at.strftime("%d/%m/%Y %H:%M:%S"), inline=False)
        embed.set_image(url=avatar_url)

        await ctx.reply(embed=embed)


    @commands.command()
    async def avatar(self, ctx, member: discord.Member):  # Adicionado 'self' e corrigido a ordem dos parâmetros
        avatar_url = member.avatar.url

        embed = discord.Embed(title=f"Avatar de {member.display_name}")
        embed.set_image(url=avatar_url)
        embed.set_footer(text=f"Solicitado por @{ctx.author.display_name}", icon_url="")
        await ctx.reply(embed=embed)


    @commands.command()
    async def ping(self, ctx, ping_host=None):  # Corrigido: adicionado 'self'
        bot_latency = round(self.bot.latency * 1000)  # Usando self.bot
        start_time = time.time()

        if ping_host is None:
            await ctx.send("Calculando o ping...")
            time.sleep(0.5)
            server_ping = round((time.time() - start_time) * 1000)

            embed = discord.Embed(title='')
            embed.add_field(name='• Ping do usuário', value=f"{round(self.bot.latency * 500)} ms", inline=False)
            embed.add_field(name='• Ping do Bot', value=f"{bot_latency} ms", inline=False)
            embed.add_field(name='• Ping do Discord', value=f"{server_ping} ms", inline=False)
            embed.set_author(name='ㅤㅤㅤCONSULTA DE PINGㅤㅤㅤㅤ', icon_url='')
            embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved', icon_url='')

            await ctx.reply(embed=embed)

        else:
            view_dns_key = os.getenv("VIEWDNS_TOKEN")
            url = f"https://api.viewdns.info/ping/?host={ping_host}&apikey={view_dns_key}&output=json"

            try:
                response = requests.get(url)

                if response.status_code == 200:
                    data = response.json()

                    replies = data.get('response', {}).get('replys', [])
                    
                    embed = discord.Embed(title=f"", description="")
                    
                    if not replies:
                        embed.set_author(name="NENHUMA RESPOSTA DE PING FOI ENCONTRADA.", icon_url='')
                        await ctx.reply(embed=embed)
                        return

                    for ping_info in replies:
                        rtt_info = ping_info.get('rtt', 'Desconhecido')
                        embed.add_field(name="Tempo de resposta", value=f"{rtt_info}", inline=False)

                    embed.set_author(name=f'ㅤㅤㅤPING EFETUADO COM SUCESSOㅤㅤㅤㅤ', icon_url='')
                    embed.add_field(name="Host:", value=f"{ping_host}", inline=False)

                    embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved', icon_url='')

                    await ctx.reply(embed=embed)

            except Exception as e:
                embed = discord.Embed(title="")
                embed.add_field(name="", value=f"Ocorreu um erro ao consultar o servidor: {str(e)}", inline=False)
                embed.set_author(name='Erro na Resposta da API', icon_url='')

                await ctx.reply(embed=embed)



async def setup(bot):
    await bot.add_cog(FeaturesCommands(bot))
