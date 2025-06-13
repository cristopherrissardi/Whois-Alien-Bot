import discord
from discord.ext import commands
from faker import Faker
import random, string

from utils.formatters import remover_titulos

fake = Faker("pt_BR")


class GeneratorsCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gerar_pessoa(self, ctx):

        try:
            embed = discord.Embed(title='')
            embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤGERADOR DE PESSOAㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

            embed.add_field(name="Nome", value=remover_titulos(fake.name()), inline=True)
            embed.add_field(name="CPF", value=fake.cpf(), inline=True)
            embed.add_field(name="Data de Nascimento", value=fake.date_of_birth(minimum_age=18, maximum_age=85), inline=True)
            embed.add_field(name="Nacionalidade", value="Brasil", inline=True)
            embed.add_field(name="Naturalidade", value=fake.estado_nome(), inline=True)
            embed.add_field(name="Profissão", value=fake.job(), inline=True)
            embed.add_field(name="E-mail", value=fake.free_email(), inline=True)
            embed.add_field(name="Nome da Mãe", value=remover_titulos(fake.name_female()), inline=True)
            embed.add_field(name="Nome do Pai", value=remover_titulos(fake.name_male()), inline=True)
            embed.add_field(name="Nome do Irmão(a)", value=remover_titulos(fake.name()), inline=True)
            embed.add_field(name="Nome da Avó", value=remover_titulos(fake.name_female()), inline=True)
            embed.add_field(name="Nome do Avô", value=remover_titulos(fake.name_male()), inline=True)
            embed.add_field(name="RG", value=fake.random_number(9, fix_len=True), inline=True)
            embed.add_field(name="Telefone", value=fake.cellphone_number(), inline=True)
            embed.add_field(name="Endereço", value=fake.address().replace("\n", ", "), inline=True)
            embed.add_field(name="Placa do Carro", value=fake.license_plate(), inline=True)
            embed.add_field(name="Chassi do Carro", value=fake.vin(), inline=True)
            embed.add_field(name="Cartão de crédito", value=fake.credit_card_number(), inline=True)
            embed.add_field(name="Validade do Cartão", value=fake.credit_card_expire(), inline=True)
            embed.add_field(name="Cod. Segurança Cartão", value=fake.credit_card_security_code(), inline=True)
            embed.add_field(name="Cor preferida", value=fake.safe_color_name(), inline=True)
            embed.add_field(name="CNPJ do Trabalho", value=fake.cnpj(), inline=True)
            embed.add_field(name="Endereço IP", value=fake.ipv4(), inline=True)
            embed.add_field(name="MAC do celular", value=fake.mac_address(), inline=True)

            embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved', icon_url='')
            
            await ctx.reply(embed=embed)

        except Exception as e:
            embed = discord.Embed(title='')
            embed.set_author(name='NÃO FOI POSSÍVEL GERAR UMA PESSOA NO MOMENTO', icon_url='')
            await ctx.reply(embed=embed)
            
    @commands.command()
    async def gerar_usr(self, ctx):

        try:
            embed = discord.Embed(title='')

            embed.set_author(name='USERNAME GERADO COM SUCESSO', icon_url='')
            embed.add_field(name="", value=fake.user_name(), inline=False)

            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
            
            await ctx.reply(embed=embed)

            return
        except Exception:
            pass

            embed = discord.Embed(title='')
            embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM USER NO MOMENTOㅤㅤㅤ', icon_url='')
            await ctx.reply(embed=embed)

    @commands.command()
    async def gerar_email(self, ctx):

        try:
            embed = discord.Embed(title='')
            embed.set_author(name='EMAIL GERADO COM SUCESSO', icon_url='')
            embed.add_field(name="", value=fake.ascii_free_email(), inline=False)
            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
            await ctx.reply(embed=embed)

            return
        except Exception:
        
            embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM E-MAIL NO MOMENTOㅤㅤㅤ', icon_url='')
            return await ctx.reply(embed=embed)


    @commands.command()
    async def gerar_tel(self, ctx):

        try:
            embed = discord.Embed(title='')
            embed.set_author(name='TELEFONE GERADO COM SUCESSO', icon_url='')
            embed.add_field(name="", value=fake.cellphone_number(), inline=False)
            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
            await ctx.reply(embed=embed)

            return
        except Exception:
        
            embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM TELEFONE NO MOMENTOㅤㅤㅤ', icon_url='')
            return await ctx.reply(embed=embed)

    @commands.command()
    async def gerar_cpf(self, ctx):

        try:
            embed = discord.Embed(title='')
            embed.set_author(name='CPF GERADO COM SUCESSO', icon_url='')
            embed.add_field(name="", value=fake.cpf(), inline=False)
            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
            await ctx.reply(embed=embed)

            return
        except Exception:
            pass

            embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM CPF NO MOMENTOㅤㅤㅤ', icon_url='')
            return await ctx.reply(embed=embed)

    @commands.command()
    async def gerar_cartao(self, ctx):

        try:
            embed = discord.Embed(title='')
            embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤGERADOR DE CARTÃOㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
            embed.add_field(name="• Número do Cartão", value=fake.credit_card_number(), inline=False)
            embed.add_field(name="• Data de expiração", value=fake.credit_card_expire(), inline=False)
            embed.add_field(name="• Código de segurança", value=fake.credit_card_security_code(), inline=False)
            embed.add_field(name="• Banco", value=fake.credit_card_provider(), inline=False)
            embed.add_field(name="• Nome do Proprietário", value=fake.name(), inline=False)
            embed.add_field(name="• CPF", value=fake.cpf(), inline=False)
            embed.add_field(name="• Data de Nascimento", value=fake.date_of_birth(minimum_age=18, maximum_age=85), inline=False)
            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
            await ctx.reply(embed=embed)

            return
        except Exception:

            embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM CARTÃOㅤㅤㅤ', icon_url='')
            await ctx.reply(embed=embed)

    @commands.command()
    async def gerar_rg(self, ctx):

        try:
            embed = discord.Embed(title='')
            embed.set_author(name='RG GERADO COM SUCESSO', icon_url='')
            embed.add_field(name="", value=fake.rg(), inline=False)
            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
            await ctx.reply(embed=embed)

            return
        except Exception:
        
            embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM RG NO MOMENTOㅤㅤㅤ', icon_url='')
            return await ctx.reply(embed=embed)


    @commands.command()
    async def gerar_agent(self, ctx):

        try:
            embed = discord.Embed(title='')
            embed.set_author(name='USER AGENT GERADO COM SUCESSO', icon_url='')
            embed.add_field(name="", value=fake.user_agent(), inline=False)
            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
            await ctx.reply(embed=embed)

            return
        except Exception:
        
            embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM USER AGENT NO MOMENTOㅤㅤㅤ', icon_url='')
            return await ctx.reply(embed=embed)


    @commands.command()
    async def gerar_passaporte(self, ctx):

        try:
            embed = discord.Embed(title='')
            embed.set_author(name='PASSAPORTE GERADO COM SUCESSO', icon_url='')
            embed.add_field(name="", value=fake.passport_full(), inline=False)
            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
            await ctx.reply(embed=embed)

            return
        except Exception:
        
            embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM PASSAPORTE NO MOMENTOㅤㅤㅤ', icon_url='')
            return await ctx.reply(embed=embed)


    @commands.command()
    async def gerar_texto(self, ctx):

        try:
            embed = discord.Embed(title='')
            embed.set_author(name='TEXTO GERADO COM SUCESSO', icon_url='')
            embed.add_field(name="", value=fake.text(max_nb_chars=200, ext_word_list=None), inline=False)
            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
            await ctx.reply(embed=embed)

            return
        except Exception:
        
            embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM TEXTO NO MOMENTOㅤㅤㅤ', icon_url='')
            return await ctx.reply(embed=embed)



    @commands.command()
    async def gerar_ip(self, ctx):

        try:
            embed = discord.Embed(title='')
            embed.set_author(name='IP GERADO COM SUCESSO', icon_url='')
            embed.add_field(name="", value=fake.ipv4(), inline=False)
            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
            await ctx.reply(embed=embed)

            return
        except Exception:
        
            embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM IP NO MOMENTOㅤㅤㅤ', icon_url='')
            return await ctx.reply(embed=embed)


    @commands.command()
    async def gerar_mac(self, ctx):

        try:
            embed = discord.Embed(title='')
            embed.set_author(name='MAC GERADO COM SUCESSO', icon_url='')
            embed.add_field(name="", value=fake.mac_address(), inline=False)
            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
            await ctx.reply(embed=embed)

            return
        except Exception:
        
            embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM MAC NO MOMENTOㅤㅤㅤ', icon_url='')
            return await ctx.reply(embed=embed)

    @commands.command()
    async def gerar_url(self, ctx):

        try:
            embed = discord.Embed(title='')
            embed.set_author(name='URL GERADA COM SUCESSO', icon_url='')
            embed.add_field(name="", value=fake.url(), inline=False)
            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
            await ctx.reply(embed=embed)

            return
        except Exception:
        
            embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UMA URL NO MOMENTOㅤㅤㅤ', icon_url='')
            return await ctx.reply(embed=embed)

    @commands.command()
    async def gerar_coordenadas(self, ctx):

        try:
            embed = discord.Embed(title='')
            embed.set_author(name='COORDENADA GERADA COM SUCESSO', icon_url='')
            embed.add_field(name="", value=fake.latitude() + ',' + fake.longitude(), inline=False)
            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
            await ctx.reply(embed=embed)

            return
        except Exception:
        
            embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UMA COORDENADA NO MOMENTOㅤㅤㅤ', icon_url='')
            return await ctx.reply(embed=embed)

    @commands.command()
    async def gerar_data(self, ctx):

        try:
            embed = discord.Embed(title='')
            embed.set_author(name='DATA GERADA COM SUCESSO', icon_url='')
            embed.add_field(name="", value=fake.date(), inline=False)
            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
            await ctx.reply(embed=embed)

            return
        except Exception:
        
            embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UMA DATA NO MOMENTOㅤㅤㅤ', icon_url='')
            return await ctx.reply(embed=embed)

    @commands.command()
    async def gerar_cnpj(self, ctx):

        global embed
        try:
            embed = discord.Embed(title='')
            embed.set_author(name='CNPJ GERADO COM SUCESSO', icon_url='')
            embed.add_field(name="", value=fake.cnpj(), inline=False)
            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
            await ctx.reply(embed=embed)

            return
        except Exception:
        
            embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM CNPJ NO MOMENTOㅤㅤㅤ', icon_url='')
            return await ctx.reply(embed=embed)

    @commands.command()
    async def gerar_cor(self, ctx):

        global embed
        cor = fake.color()

        try:
            cor_hex = int(cor.replace("#", "0x"), 16)  # Converte "#RRGGBB" para 0xRRGGBB

            embed = discord.Embed(title='', colour=discord.Colour(cor_hex), description='')
            embed.set_author(name='COR GERADA COM SUCESSO', icon_url='')
            embed.add_field(name="", value=cor.upper(), inline=False)
            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
            await ctx.reply(embed=embed)

            return
        except Exception:
        
            embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM CNPJ NO MOMENTOㅤㅤㅤ', icon_url='')
            return await ctx.reply(embed=embed)

    @commands.command()
    async def gerar_placa(self, ctx):

        try:
            embed = discord.Embed(title='')
            embed.set_author(name='PLACA GERADA COM SUCESSO', icon_url='')
            embed.add_field(name="", value=fake.license_plate(), inline=False)
            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
            await ctx.reply(embed=embed)

            return
        except Exception:
        
            embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UMA PLACA NO MOMENTOㅤㅤㅤ', icon_url='')
            return await ctx.reply(embed=embed)

    @commands.command()
    async def gerar_endereco(self, ctx):

        try:
            embed = discord.Embed(title='')
            embed.set_author(name='ENDEREÇO GERADA COM SUCESSO', icon_url='')
            embed.add_field(name="", value=fake.address(), inline=False)
            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
            await ctx.reply(embed=embed)

            return
        except Exception:
        
            embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM ENDEREÇO NO MOMENTOㅤㅤㅤ', icon_url='')
            return await ctx.reply(embed=embed)
        

    @commands.command()
    async def gerar_senha(self, ctx, length=36):

        if 10 <= length <= 64:

            password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        
            embed = discord.Embed(title="Senha gerada com Sucesso!")
            embed.add_field(name="", value='Sua senha foi enviada em seu privado!', inline=False)             
            await ctx.reply(embed=embed)
            embed = discord.Embed(title="")

            embed.set_author(name='SENHA GERADA COM SUCESSO', icon_url='')
            embed.add_field(name="", value=password, inline=False)
            embed.add_field(name="Dicas para criar senhas fortes:", value="Matéria do site [Kaspersky](https://www.kaspersky.com.br/resource-center/threats/how-to-create-a-strong-password)", inline=False)
            embed.add_field(name="Recomendação pessoal de gerenciador de senhas:", value="[Bitwarden](https://bitwarden.com/) - Sistema Open Source.", inline=False)
            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
            await ctx.author.send(embed=embed)

        else:
            embed = discord.Embed(title="")
            embed.set_author(name='O comprimento da senha deve estar entre 10 e 64 caracteres.', icon_url='')
            await ctx.reply(embed=embed)
















async def setup(bot):
    await bot.add_cog(GeneratorsCommands(bot))