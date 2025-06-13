import discord
from discord.ext import commands


class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mute(self, ctx, member: discord.Member):  # Corrigido: agora o método é associado corretamente à classe
        if ctx.author.guild_permissions.mute_members:
            mute_role = discord.utils.get(ctx.guild.roles, name='Muted') 
            if mute_role:
                await member.add_roles(mute_role)
                await ctx.send(f'{member.mention} foi mutado por {ctx.author.mention}.')
            else:
                await ctx.send('O cargo de silenciamento (Muted) não foi encontrado. Crie um cargo com esse nome e configure as permissões corretamente.')
        else:
            await ctx.send('Você não tem permissão para mutar membros.')


    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        if ctx.author.guild_permissions.mute_members:
            mute_role = discord.utils.get(ctx.guild.roles, name='Muted')  # Nome do cargo silenciado
            if mute_role:
                await member.remove_roles(mute_role)
                await ctx.send(f'{member.mention} foi desmutado por {ctx.author.mention}.')
            else:
                await ctx.send('O cargo de silenciamento (Muted) não foi encontrado. Crie um cargo com esse nome e configure as permissões corretamente.')
        else:
            await ctx.send('Você não tem permissão para desmutar membros.')


    @commands.command()
    async def kick(ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)

        embed = discord.Embed(title=f'Usuário Expulso: {member.name}', description=f'O usuário {member.mention} foi expulso do servidor por ser babaca!')
        await ctx.reply(embed=embed)


    @commands.command()
    async def ban(ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)

        embed = discord.Embed(title=f'Usuário Banido: {member.name}', description=f'O usuário {member.mention} foi bnido do servidor por ser otário e babaca!')
        await ctx.reply(embed=embed)


    @commands.command()
    async def unban(ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Desbanido {user.mention}')
        return


    @commands.command() 
    async def clear(self, ctx, amount: int):  
        if ctx.author.guild_permissions.manage_messages:
            if amount <= 0 or amount > 100:
                embed = discord.Embed(
                    title='Não foi possível excluir as mensagens!', 
                    description='Por favor, forneça um número entre 1 e 100 para limpar mensagens.'
                )
                await ctx.reply(embed=embed)
            else:
                await ctx.channel.purge(limit=amount + 1)
                embed = discord.Embed(
                    title='Limpeza de Mensagens feita!', 
                    description=f'{amount} mensagens foram excluídas.'
                )
                await ctx.send(embed=embed, delete_after=5)
        else:
            embed = discord.Embed(
                title='', 
                description='Sai dai bostinha, você não tem permissão para limpar as mensagens.'
            )
            await ctx.reply(embed=embed)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):  
            await ctx.send('Você precisa fornecer um número de mensagens para limpar!')
        else:
            await ctx.send(f'Ocorreu um erro: {error}')








async def setup(bot):
    await bot.add_cog(AdminCommands(bot))
