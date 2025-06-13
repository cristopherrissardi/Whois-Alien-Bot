

import discord
from discord.ext import commands
import os, io
from leakcheck import LeakCheckAPI_Public


from utils.buttons import NameResultView


class LeakChecker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pwned(self, ctx, email_pwned=None):

        if not email_pwned:
            
            embed = discord.Embed(title='')

            embed.set_author(name='ㅤㅤㅤㅤ   👽 COMANDO VERIFICAÇÃO DE VAZAMENTOSㅤㅤㅤ', icon_url='')
            embed.add_field(name="Use o comando: `./pwned` e o e-mail ou usuário que deseja verificar.", value='*Exemplo*: `./pwned joao@gmail.com`', inline=False)
            return await ctx.reply(embed=embed)

        try:
            api = LeakCheckAPI_Public()
            data = api.lookup(query=email_pwned)  # Chama a API corretamente

            leaks = data.get("sources", [])
            leak_info = "\n".join(f"- {leak['name']} ({leak['date']})" for leak in leaks) if leaks else "Nenhum vazamento encontrado."

            embed = discord.Embed(title="")
            embed.set_author(name="ㅤㅤㅤㅤ   VERIFICAÇÃO DE VAZAMENTO DE E-MAILSㅤㅤㅤㅤ   ")
            embed.add_field(name="", value="", inline=False)
            embed.add_field(name="", value="", inline=False)
            embed.add_field(name="E-mail", value=email_pwned, inline=True)
            embed.add_field(name="Total de Vazamentos", value=str(data.get("found", 0)), inline=True)
            embed.add_field(name="", value="", inline=False)
            embed.add_field(name="", value="", inline=False)

            embed.add_field(name="Locais de vazamento", value=leak_info, inline=False)
            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')        
            await ctx.reply(embed=embed)

        except ValueError as e:
            if "Not found" in str(e):  # Trata o erro corretamente
                await ctx.send(f"O e-mail `{email_pwned}` não foi encontrado em nenhum vazamento.")
            else:
                await ctx.send(f"Ocorreu um erro ao processar a solicitação: {e}")


async def setup(bot):
    await bot.add_cog(LeakChecker(bot))
