
import discord
from discord.ext import commands
import hashlib, secrets, random, string
from datetime import datetime
from faker import Faker

class HashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gen_md5(self, ctx, *, text: str = ""):

        md5_hash = hashlib.md5(text.encode()).hexdigest()
        
        embed = discord.Embed(title='')
        embed.set_author(name="ㅤㅤㅤㅤㅤㅤㅤHASH MD5ㅤㅤㅤㅤㅤㅤㅤ   ")
        embed.add_field(name="Input", value=text if text else "[Empty String]", inline=False)
        embed.add_field(name="Hash MD5", value=md5_hash, inline=False)
        embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
        
        await ctx.reply(embed=embed)

    @commands.command()
    async def gen_sha1(self, ctx, *, text: str = ""):

        sha1_hash = hashlib.sha1(text.encode()).hexdigest()
        
        embed = discord.Embed(title='')
        embed.set_author(name="ㅤㅤㅤㅤㅤㅤㅤHASH SHA1ㅤㅤㅤㅤㅤㅤㅤ   ")
        embed.add_field(name="Input", value=text if text else "[Empty String]", inline=False)
        embed.add_field(name="Hash SHA1", value=sha1_hash, inline=False)
        embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
        
        await ctx.reply(embed=embed)

    @commands.command()
    async def gen_sha256(self, ctx, *, text: str = ""):

        sha256_hash = hashlib.sha256(text.encode()).hexdigest()
        
        embed = discord.Embed(title='')
        embed.set_author(name="ㅤㅤㅤㅤㅤㅤㅤHASH SHA256ㅤㅤㅤㅤㅤㅤㅤ   ")
        embed.add_field(name="Input", value=text if text else "[Empty String]", inline=False)
        embed.add_field(name="Hash SHA256", value=sha256_hash, inline=False)
        embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
        
        await ctx.reply(embed=embed)

    @commands.command()
    async def gen_sha512(self, ctx, *, text: str = ""):

        sha512_hash = hashlib.sha512(text.encode()).hexdigest()
        
        embed = discord.Embed(title='')
        embed.set_author(name="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤHASH SHA512ㅤㅤㅤㅤㅤㅤㅤ   ")
        embed.add_field(name="Input", value=text if text else "[Empty String]", inline=False)
        embed.add_field(name="Hash SHA512", value=sha512_hash, inline=False)
        embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
        
        await ctx.reply(embed=embed)

    @commands.command()
    async def gen_blake2b(self, ctx, *, text: str = ""):

        blake2b_hash = hashlib.blake2b(text.encode()).hexdigest()
        
        embed = discord.Embed(title='')
        embed.set_author(name="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤHASH BLAKE2Bㅤㅤㅤㅤㅤㅤㅤ   ")
        embed.add_field(name="Input", value=text if text else "[Empty String]", inline=False)
        embed.add_field(name="Hash BLAKE2B", value=blake2b_hash, inline=False)
        embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
        
        await ctx.reply(embed=embed)

    @commands.command()
    async def gen_blake2s(self, ctx, *, text: str = ""):

        blake2s_hash = hashlib.blake2s(text.encode()).hexdigest()
        
        embed = discord.Embed(title='')
        embed.set_author(name="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤHASH BLAKE2Bㅤㅤㅤㅤㅤㅤㅤ   ")
        embed.add_field(name="Input", value=text if text else "[Empty String]", inline=False)
        embed.add_field(name="Hash BLAKE2S", value=blake2s_hash, inline=False)
        embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
        
        await ctx.reply(embed=embed)

    @commands.command()
    async def gen_sha224(self, ctx, *, text: str = ""):

        sha224_hash = hashlib.sha224(text.encode()).hexdigest()
        
        embed = discord.Embed(title='')
        embed.set_author(name="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤHASH SHA224ㅤㅤㅤㅤㅤㅤㅤ   ")
        embed.add_field(name="Input", value=text if text else "[Empty String]", inline=False)
        embed.add_field(name="Hash SHA224", value=sha224_hash, inline=False)
        embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
        
        await ctx.reply(embed=embed)

    @commands.command()
    async def gen_sha384(self, ctx, *, text: str = ""):

        sha384_hash = hashlib.sha384(text.encode()).hexdigest()
        
        embed = discord.Embed(title='')
        embed.set_author(name="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤHASH SHA384ㅤㅤㅤㅤㅤㅤㅤ   ")
        embed.add_field(name="Input", value=text if text else "[Empty String]", inline=False)
        embed.add_field(name="Hash SHA384", value=sha384_hash, inline=False)
        embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
        
        await ctx.reply(embed=embed)

    @commands.command()
    async def gen_shake128(self, ctx, *, text: str = ""):

        shake128_hash = hashlib.shake_128(text.encode()).hexdigest()
        
        embed = discord.Embed(title='')
        embed.set_author(name="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤHASH SHAKE128ㅤㅤㅤㅤㅤㅤㅤ   ")
        embed.add_field(name="Input", value=text if text else "[Empty String]", inline=False)
        embed.add_field(name="Hash SHAKE128", value=shake128_hash, inline=False)
        embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
        
        await ctx.reply(embed=embed)

    @commands.command()
    async def gen_shake256(self, ctx, *, text: str = ""):

        shake256_hash = hashlib.shake_256(text.encode()).hexdigest()
        
        embed = discord.Embed(title='')
        embed.set_author(name="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤHASH SHAKE256ㅤㅤㅤㅤㅤㅤㅤ   ")
        embed.add_field(name="Input", value=text if text else "[Empty String]", inline=False)
        embed.add_field(name="Hash SHAKE256", value=shake256_hash, inline=False)
        embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
        
        await ctx.reply(embed=embed)

    @commands.command()
    async def gen_scrypt(self, ctx, *, text: str = ""):

        scrypt_hash = hashlib.scrypt(text.encode()).hexdigest()
        
        embed = discord.Embed(title='')
        embed.set_author(name="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤHASH SCRYPTㅤㅤㅤㅤㅤㅤㅤ   ")
        embed.add_field(name="Input", value=text if text else "[Empty String]", inline=False)
        embed.add_field(name="Hash SCRYPT", value=scrypt_hash, inline=False)
        embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
        
        await ctx.reply(embed=embed)



    @commands.command()
    async def genpassword(self, ctx, length=36):

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



    @commands.command()
    async def genkey(self, ctx):
        timestamp = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
        
        embed = discord.Embed(title="Chave gerada com Sucesso!")
        embed.add_field(name="", value='Sua chave foi enviada em seu privado!', inline=False)             
        await ctx.reply(embed=embed)
        
        key = f"{secrets.token_hex(4)}-{secrets.token_hex(2)}-{secrets.token_hex(2)}-{secrets.token_hex(2)}-{secrets.token_hex(6)}"
        
        embed = discord.Embed(title="")
        embed.set_author(name=f'', icon_url='')
        embed.add_field(name="", value=key, inline=False)
        embed.set_footer(text=f'Generated By {ctx.author} in {timestamp}', icon_url='') 

        await ctx.author.send(embed=embed)










async def setup(bot):
    await bot.add_cog(HashCommands(bot))

