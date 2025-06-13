import discord
from discord.ext import commands


class MembroNovo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # seu código aqui

        welcome = member.guild.get_channel(913133936610246656) # Canal de boas vindas do servidor House´s Alien
        user_id = member.id

        if welcome:

            embed = discord.Embed(title=f'Olá {member} Seja muito bem vindo ao nosso servidor!', description=f'A partir de agora <@{user_id}>, você terá alguns requisitos a serem cumpridos para que você possa ser um membro em nosso servidor. Segue abaixo os requisitos')

            embed.add_field(name="\n\n", value="\n\n", inline=False)        
            embed.add_field(name="Requisitos Importântes:", value="", inline=False) 
            embed.add_field(name="\n\n", value="\n\n", inline=False)        
            embed.add_field(name="Requisito 1", value=f"Leia atentamente canal de <#{913138175520673812}>. É de extrema importância que você leia atentamente as regras e os termos!", inline=False)
            embed.add_field(name="Requisito 2", value=f"A opinião do <@{589502565243289612}> sempre prevalecerá! se ele dizer não, é não!", inline=False)
            embed.add_field(name="\n\n", value="\n\n", inline=False)        

            embed.add_field(name="Outros requisitos:", value="", inline=False)        
            embed.add_field(name="\n\n", value="\n\n", inline=False)        

            embed.add_field(name="Requisito 3", value="2 (duas) cópias do comprovante de residência", inline=False)
            embed.add_field(name="Requisito 4", value="1 (uma) cópia da escritura do terreno ou do imóvel reconhecida em cartórioㅤㅤ", inline=False)
            embed.add_field(name="Requisito 5", value="1 (uma) copia do RGㅤㅤ", inline=False)
            embed.add_field(name="Requisito 6", value="1 (uma) foto 3x4 recenteㅤㅤ", inline=False)
            embed.add_field(name="Requisito 7", value="Ter CPF com situação regular na Receita Federal", inline=False)
            embed.add_field(name="Requisito 8", value="Ter conta no Serasa com mais de 30 dias de criaçãoㅤㅤ", inline=False)        
            embed.add_field(name="", value="Lembrando, antes de tudo sempre tenha senso de humor e senso de dissernimento! Nada acima é verdadeiro a não ser os 2 primeiros requisitos!", inline=False)        
            embed.set_image(url='https://i.imgur.com/yInAO6g.gif')
            embed.set_footer(text='Whois Alien © All Rights Reserved', icon_url='')
            
            role = member.guild.get_role(913150428907184149) # Cargo de "Membro" para novos usuários
            if role:
                await member.add_roles(role)

            await welcome.send(embed=embed)


async def setup(bot):
    await bot.add_cog(MembroNovo(bot))
