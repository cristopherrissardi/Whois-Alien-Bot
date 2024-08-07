##=====================================================>>> BIBLIOTECAS IMPORTADAS <<<=======================================================##
from ast import main
from asyncio import tasks
from discord.ext import commands, tasks
from ntpath import join
from optparse import Values
from dataclasses import replace
from dotenv import load_dotenv 
from googletrans import Translator  
from typing import Text
from datetime import datetime
from g4f.client import Client
import discord   
import random
import dataclasses
import json      
import socket
import requests  
import asyncio
import os 
import string
import random
import io
import nest_asyncio

nest_asyncio.apply()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix='./', intents=intents)
client_gpt3 = Client()

load_dotenv()

API_KEY = os.getenv("API_KEY")

@client.event
async def on_ready():
    activity = discord.Game(name='Created By Alien', type=3)
    await client.change_presence(status=discord.Status.dnd, activity=activity)
    print("Conectado")

@client.event
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel):
        return
    await client.process_commands(message)

@client.command()
async def clear(ctx, amount: int):
    if ctx.author.guild_permissions.manage_messages:
        if amount <= 0 or amount > 100:

            embed = discord.Embed(title='Não foi possível excluir as mensagens!', description='Por favor, forneça um número entre 1 e 100 para limpar mensagens.')
            await ctx.send(embed=embed)
        else:
            await ctx.channel.purge(limit=amount + 1)
            embed = discord.Embed(title='Limpeza de Mensagens feita!', description=f'{amount} mensagens foram excluídas.')
            await ctx.send(embed=embed, delete_after=5)
    else:
        embed = discord.Embed(title='',description='Sai dai bostinha, você não tem permissão para limpar as mensagens.',)
        await ctx.send(embed=embed)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

    embed = discord.Embed(title=f'Usuário Expulso: {member.name}', description=f'O usuário {member.mention} foi expulso do servidor por ser babaca!')
    await ctx.send(embed=embed)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

    embed = discord.Embed(title=f'Usuário Banido: {member.name}', description=f'O usuário {member.mention} foi bnido do servidor por ser otário e babaca!')
    await ctx.send(embed=embed)

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.send(f'Desbanido {user.mention}')
      return

@client.command()
async def mute(ctx, member: discord.Member):
    if ctx.author.guild_permissions.mute_members:
        mute_role = discord.utils.get(ctx.guild.roles, name='Muted')  # Nome do cargo de silenciamento
        if mute_role:
            await member.add_roles(mute_role)
            await ctx.send(f'{member.mention} foi mutado por {ctx.author.mention}.')
        else:
            await ctx.send('O cargo de silenciamento (Muted) não foi encontrado. Crie um cargo com esse nome e configure as permissões corretamente.')
    else:
        await ctx.send('Você não tem permissão para mutar membros.')

@client.command() #COMANDO
async def unmute(ctx, member: discord.Member): #COMANDO

    if ctx.author.guild_permissions.mute_members:
        mute_role = discord.utils.get(ctx.guild.roles, name='Muted') #NOME DO CARGO DE SILENCIADO
        if mute_role:
            await member.remove_roles(mute_role)
            await ctx.send(f'{member.mention} foi desmutado por {ctx.author.mention}.')
        else:
            await ctx.send('O cargo de silenciamento (Muted) não foi encontrado. Crie um cargo com esse nome e configure as permissões corretamente.')
    else:
        await ctx.send('Você não tem permissão para desmutar membros.')

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArguments):
        await ctx.send('...')

@client.event
async def on_member_join(member):
    welcome = member.guild.get_channel(913133936610246656)
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
        
        role = member.guild.get_role(913150428907184149)
        if role:
            await member.add_roles(role)

        await welcome.send(embed=embed)

@client.command()
async def projectovnia(ctx):

    embed = discord.Embed(title='')
    
    embed.add_field(name="", value=f"O Project OVNIA é um projeto em colaboração com a Google integrando o motor de inteligência artificial `Gemini-Pro` para oferecer uma boa experiência aos usuários do Bot Whois Alien, criado e interpretado por offalien. Todos os usuários estão autorizados a usarem! esperamos que você tenha uma ótima experiência ao usar a ia. Quaisquer dúvidas ou sugestões, entre em contato com o <@{589502565243289612}>.", inline=False)
    embed.add_field(name="", value="Para usar a ferramenta de inteligência articial, é importante antes saber como de fato funciona uma inteligência artificial! use a opção `./ovnia` e insira o seu parâmetro/busca/dúvida que deseja.", inline=False)
    embed.add_field(name="", value="", inline=False)
    embed.add_field(name="Exemplo:", value="", inline=False)
    embed.add_field(name="", value="`./ovnia` Sabendo que pedro alvares cabral descobriu o brasil no ano de 1500, em que dia foi descoberto a américa e quem encontrou inicialmente?", inline=False)
    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤProject OVNIAㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
    embed.set_footer(text='Whois Alien © All Rights Reserved', icon_url='')
    embed.set_image(url='https://i.imgur.com/jQIkv9s.jpeg')

    await ctx.send(embed=embed)

@client.command()
async def ia(ctx):

    embed = discord.Embed(title='')
    embed.add_field(name="Project OVNIA", value="Para visualizar a opção personalizada do Project OVNIA, digite: `./projectovnia` ou o parâmetro `./ovnia` + o que você deseja perguntar", inline=False)
    embed.add_field(name="", value="Exemplo: `./ovnia` que dia George Washington morreu?", inline=False)    
    embed.add_field(name="", value="", inline=False)    
    embed.add_field(name="OpenAI ChatGPT-4", value="O motor de inteligência usa o ChatGPT-4 como referência, use o parâmetro `./gpt4` e o que você deseja pedir.", inline=False)
    embed.add_field(name="", value="Exemplo: `./gpt4` que dia nasceu pelé?", inline=False)    
    embed.add_field(name="", value="", inline=False)    
    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤInteligências artificais disponíveisㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
    embed.set_footer(text='Whois Alien © All Rights Reserved', icon_url='')

    await ctx.send(embed=embed)

# @client.command()
# async def gpt4(ctx, *, question):
#     response = client_gpt3.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": question}],
#     )
#     answer = response.choices[0].message.content
#     embed = discord.Embed(title="", description=answer)
#     embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤOpenAI GPT-4ㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
#     embed.set_footer(text='Whois Alien © All Rights Reserved', icon_url='')
#     await ctx.send(embed=embed, reference=ctx.message)

# @client.command()
# async def ovnia(ctx, *, question):
#     response = client_gpt3.chat.completions.create(
#         model="gemini",
#         messages=[{"role": "user", "content": question}],
#     )
#     answer = response.choices[0].message.content
#     embed = discord.Embed(title="", description=answer)
#     embed.set_footer(text='Whois Alien © All Rights Reserved', icon_url='')
#     await ctx.send(embed=embed, reference=ctx.message)


@client.command()
async def consultas(ctx):

    embed = discord.Embed(title='',)

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE DADOSㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

    embed.add_field(name="🕵🏻‍♂️ Consulta por Nome", value="Use o comando `./nome` {NOME COMPLETO} para realizar a consulta.", inline=False)
    embed.add_field(name="👽 Consulta por CPF", value="Use o comando `./cpf0` {CPF DA PESSOA} para a consultar os dados.", inline=False)
    embed.add_field(name="🔍 Consulta por CPF completo", value="Use o comando `./cpf` {CPF DA PESSOA} para a consultar os dados completa.", inline=False)
    embed.add_field(name="📳 Consulta por Telefone", value="Use o comando `./telefone` {TELEFONE} para realizar a consulta dos dados do proprietário da linha telefonica.", inline=False)
    embed.add_field(name="💎 Consulta por Telefone fixo", value="Use o comando `./fixo` {TELEFONE} para realizar a consulta dos dados do proprietário da linha telefonica.", inline=False)
    embed.add_field(name="👩‍👦 Consulta por Nome da mãe", value="Use o comando `./mae` {NOME DA MÃE} para realizar a consulta dos dados dos filhos pelo nome da mãe.", inline=False)
    embed.add_field(name="👨‍👦 Consulta por Nome do pai", value="Use o comando `./pai` {NOME DO PAI} para realizar a consulta dos dados dos filhos pelo nome do pai.", inline=False)
    embed.add_field(name="📮 Consulta por E-mail", value="Use o comando `./email` {EMAIL} para realizar a consulta dos dados do proprietário do email.", inline=False)
    embed.add_field(name="🏨 Consulta por CNPJ", value="Use o comando `./cnpj` {CNPJ} para consultar os dados.", inline=False)
    embed.add_field(name="🚘 Consulta de Placa", value="Use o comando `./placa` {PLACA DO VEÍCULO} para realizar a consulta.", inline=False)
    embed.add_field(name="📌 Consulta de IP", value="Use o comando `./ip` {IP} para realizar a consulta do IP.", inline=False)
    embed.add_field(name="💳 Consulta de BIN", value="Use o comando `./bin` {NÚMERO DA BIN} para realizar a consulta.", inline=False)
    embed.add_field(name="📫 Consulta por CEP", value="Use o comando `./cep` {CEP DA RUA} para realizar a consulta.", inline=False)
    embed.add_field(name="📑 Consulta por CEP para pessoas", value="Use o comando `./cep_pessoas` {CEP DA RUA} para realizar a consulta de todos que moram na rua.", inline=False)
    embed.add_field(name="🦠 Consulta de Covid19", value="Use o comando `./covid` {SIGLA DO ESTADO} para realizar a consulta.", inline=False)
    embed.add_field(name="🏦 Consulta de Banco", value="Use o comando `./banco` {CÓDIGO DO BANCO} para realizar a consulta.", inline=False)
    embed.add_field(name="💾 Consulta de Site", value="Use o comando `./site` {URL DO SITE} para realizar a consulta.", inline=False)
    embed.add_field(name="📴 Consulta de Operadora", value="Use o comando `./operadora` {NÚMERO DE CELULAR} para realizar a consulta.", inline=False)    
    embed.add_field(name="🤖 Consulta de Info-email", value="Use o comando `./emailinfo` {EMAIL} para realizar a consulta.", inline=False)    
    embed.set_image(url='https://i.gifer.com/Cewn.gif')
    embed.set_footer(text='Whois Alien © All Rights Reserved', icon_url='')

    await ctx.send(embed=embed)

@client.command()
async def diversos(ctx):

    embed = discord.Embed(title='')
    
    embed.add_field(name="💰 CONSULTA DE COTAÇÃO", value="Use o comando `./cotacao` {PAR DE MOEDA} para realizar a consulta.", inline=False)
    embed.add_field(name="🏙️ CONSULTA DE CIDADE POR DDD", value="Use o comando `./ddd` {DDD} para realizar a consulta do DDD por cidades.", inline=False)
    embed.add_field(name="💼 CONSULTA DE FERIADOS", value="Use o comando `./feriados` {ANO} para realizar a consulta.", inline=False)
    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤDIVERSOSㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
    embed.set_footer(text='Whois Alien © All Rights Reserved', icon_url='')

    await ctx.send(embed=embed)

@client.command()
async def ajuda(ctx):

    embed = discord.Embed(title='ㅤㅤㅤㅤㅤㅤㅤㅤㅤWhois Alienㅤㅤㅤㅤㅤㅤㅤㅤ')
    embed.add_field(name="ㅤ", value='Olá, estou aqui para te ajudar! Aqui está algum dos comandos que o `Whois Alien` possui. Ficou com alguma dúvida em relação aos comandos abaixo? Digite `/[NOME DO COMANDO]`. Exemplo: `./admin`\n\nOBS: Grande parte das consultas de dados como: nome, cpf, cpf2, telefone, mãe, pai e email estão sendo hospedados em meu computador pessoal, no entanto, os comandos só irão funcionar quando o ALIEN estiver online. Parte da madrugada não irá funcionar as consultas, infelizmente! Desde já peço mil desculpas pelo transtorno e tudo será resolvido, ou melhor, normalizado. \n\n', inline=False)
    embed.add_field(name="🔐 Moderação", value='Use o comando `./admin` para ver os comandos administrativos. Comando de moderação existentes: `./kick`, `./ban`, `./unban`, `./unmute`, `./role`, `./mute`, `./clear` `\n\n (OS COMANDOS ADMINISTRATIVOS SÓ FUNCIONARÃO PARA PESSOAS COM CARGOS AUTORIZADOS)`', inline=False)
    embed.add_field(name="🛠️ Ferramentas Avançadas", value='Use o comando `./ferramentas` para obter mais informações. Ferramentas disponíveis: `./portscan`, `./traceroute`, `./whois`', inline=False)
    embed.add_field(name="🧭 Consulta de Dados", value='Use o comando `./consultas` para obter mais informações sobre a aba de consulta de dados. Consultas disponíveis: `./nome`, `./cpf`, `./cpf0`, `./telefone`, `./fixo`, `./cep_pessoas`, `./email`, `./mae`, `./pai`, `./cnpj`, `./placa [NÃO ESTÁ FUNCIONANDO NO MOMENTO]`, `./ip`, `./bin`, `./cep`, `./covid`, `./banco`, `./site`, `./operadora`, `./emailinfo` e possivelmente outros entrem nessa lista futuramente. ', inline=False)
    embed.add_field(name="⚙️ Geradores", value='Use o comando `./gerador` para obter mais informações. Ferramentas disponíveis: `./gerarpessoa`, `./gerarcartao`, `./geraremail`, `./gerarcpf`, `./gerarusr`, `./gerarsenha`, `./gerarveiculo`, `./gerartel`, `./gerarimei`', inline=False)
    embed.add_field(name="🎵 Músicas", value='Use o comando `./musica` para vizualizar os comandos. Comandos acessíveis a classe: `./play`, `./stop`, `./pause`, `./resume`, `./back`, `./skip`, `./disconnect` `\n\n (OS MENUS DE MÚSICAS AINDA NÃO FORAM IMPLEMENTADOS)`', inline=False)
    embed.add_field(name="🪐 Informações", value='Use o comando `./info` para ver os comandos disponíveis. Comandos existentes: `./ajuda`, `./ping`, `./serverinfo`, `./userinfo`', inline=False)
    embed.add_field(name="🎓 Diversos", value='Use o comando `./diversos` para vizualizar os comandos. Comandos disponíveis: `./cotacao`, `./ddd`, `./feriados`', inline=False)    
    embed.add_field(name="🉐 Tradutor", value='Use o comando `./traduzir` para ver todas as opções.\nUse o comando `./traduzir` "Texto" Língua (Exemplo: en, es, pt, ru)', inline=False)
    embed.add_field(name="🌐 Inteligência artifical", value='Use o comando `./ia` para visualizar todas as IAs presentes no BOT.', inline=False)
    embed.add_field(name="OBS:", value='`O BOT AINDA ESTÁ EM VERSÃO BETA, POR ESSE MOTIVO ALGUNS COMANDOS AINDA NÃO FORAM CORRIGIDOS OU IMPLEMENTADOS.`', inline=False)
    embed.set_image(url="https://i.imgur.com/GAw2sJ4.jpg")
    embed.set_footer(text='Whois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

    await ctx.author.send(embed=embed)

@client.command()
async def admin(ctx):

    embed = discord.Embed(title='')

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤWhois Alienㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

    embed.add_field(name="", value="Aqui fica os comandos administrativos, no entanto, somente pessoas com cargos superiores conseguiram usar essa função.", inline=False)
    embed.add_field(name="Os comandos administrativos são:", value="\n`./kick`, `./ban`, `./unban`, `./mute`, `./unmute`, `./role`, `./clear`", inline=False)
    embed.add_field(name="", value="Cada comando tem um objetivo diferente. Abaixo estará uma ***explicação breve*** de como usa-los.", inline=False)
    embed.add_field(name="❌ Comando de Expulsar", value="Use o comando `./kick` e o @ usuário da pessoa. *Exemplo ./kick @ALIEN*", inline=False)
    embed.add_field(name="⛔ Comando de Banir", value="Use o comando `./ban` e o @ usuário de quem deseja banir. *Exemplo ./ban @ALIEN*", inline=False)
    embed.add_field(name="🟢 Comando de Desbanir", value="Use o comando `./unban` precedido do @ usuário de quem deseja desbanir. *Exemplo ./unban @ALIEN*", inline=False)
    embed.add_field(name="🔇 Comando de Mutar", value="Use o comando  `./mute` e em seguida o @ usuário de quem deseja mutar. *Exemplo ./mute @ALIEN*", inline=False)
    embed.add_field(name="🔊 Comando de Desmutar", value="Use o comando `./unmute` e o @ usuário de quem deseja desmutar. *Exemplo ./unmute @ALIEN*", inline=False)
    embed.add_field(name="➕ Comando de Adicionar Cargos", value="Esse comando ainda está em fase de criação.", inline=False)
    embed.add_field(name="✔️ Comando de Limpar mensagens", value="Use o comando `./clear` e em seguida a quantidade de mensagens que deseja limpar. *Exemplo ./clear 10*", inline=False)
    embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

    await ctx.send(embed=embed); 

@client.command()
async def ferramentas(ctx):

    embed = discord.Embed(title="", description="")

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤFERRAMENTAS E OUTROSㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

    embed.add_field(name="🚀 Portscan Avançado", value="Use o comando `./portscan` {DOMINIO} que deseja scanear as portas (Scan feito através do NMAP)", inline=False)
    embed.add_field(name="🛰️ Traceroute Avançado", value="Use o comando `./traceroute` {DOMINIO} que deseja traçar as rotas do servidor.", inline=False)
    embed.add_field(name="🛩️ MAC Adress Lookup", value="Use o comando `./maclookup` {MAC} que deseja buscar nos nossos bancos de dados.", inline=False)

    embed.set_footer(text='Whois Alien © All Rights Reserved', icon_url='')

    await ctx.send(embed=embed)

@client.command()
async def regras(ctx):

    embed = discord.Embed(title='ㅤㅤㅤRegras/Termos e Responsabilidades - Houses Alienㅤㅤㅤ', description='Olá usuários! Gostaria de deixar as boas-vindas a você, membro ou amigo que está presente em nosso servidor! Esta aba é dedicada a deixar as regras e termos que seguimos para que fique o mais transparente possível as coisas que rolam por aqui. Como uma comunidade organizada, temos diretrizes a serem seguidas e termos a serem respeitados, então esperamos que você **dedique o seu tempo para que você possa ler as diretrizes e políticas**!\n\n Tempo de Leitura: **10 minutos**')
    embed.add_field(name="", value="", inline=False)
    embed.add_field(name="Regras do servidor:", value="", inline=False)
    embed.add_field(name="\n", value="\n", inline=False)
    embed.add_field(name="🌁 1. O que acontece aqui, fica aqui", value="Aqui em nosso servidor é igual Las Vegas! **Tudo o que ocorre aqui, fica por aqui!** não saiam espalhando informações/desinformações, senso comum ou outros itens que possam vir ocorrer por aqui!", inline=False)
    embed.add_field(name="🗣️ 2. Xingamentos", value="Nossa comunidade foi criada especialmente com o intuito de poder juntar os amigos e colegas para jogarem... Como todos sabem, em jogos online sempre houve e sempre haverá xingamentos e brigas internas em relação aos membros, então não há nenhuma restrição de xingamentos e outros insultos com o intuito de difamar, menosprezar e/ou insultar quaisquer dos membros. Sempre conseguimos distinguir o que é brincadeira ou não, então a regra é clara, xingamentos e outros insultos que sejam apenas por brincadeiras entre amigos é permitido! O que não será permitido são brigas e desavenças entre membros que não se conhecem! Se você não conhece o outro membro, por gentileza, não insulte-o até possuir um certo nível de intimidade! ", inline=False)
    embed.add_field(name="❌ 3. Preconceito", value="Não será tolerada a discriminação por raça, cor, religião, identidade de gênero, orientação sexual, deficiência ou qualquer outro fator extra-racial aqui dentro do servidor! Se houver difamação e brincadeirinhas toscas que possa prejudicar algum outro membro, será notificado ou expulso e não quero nem saber de justificativa!", inline=False)
    embed.add_field(name="👾 4. Vírus/Malwares", value="Totalmente proibido disseminar Malwares, Trojans, Ransonwares, phishing e qualquer outro tipo de conteúdo que possa trazer malefícios à comunidade.", inline=False)
    embed.add_field(name="⚽ 5. Futebol", value="Liberado debater sobre futebol desde que seja algo ético e sensato. Brincadeiras são liberadas desde que outros membros se sintam confortáveis.", inline=False)
    embed.add_field(name="💼 6. Política", value="Assuntos sobre Política também são liberados, desde que você tenha mínimo conhecimento prévio e conteúdo para debater. Nossa comunidade não possui nenhuma filiação partidária, muito menos posições políticas. A opinião dos membros, é, apenas, opinião dos membros. Assuntos políticos aqui dentro do servidor, podem não estar relacionados à opinião direta dos membros! Se você quiser debater sobre política, debata! porém tenha a total ciência do que está falando e não saia espalhando desinformação, muito menos ignorância.", inline=False)
    embed.add_field(name="⛪ 7. Religião", value="Pode ser debatido desde que não exista ignorância.", inline=False)
    embed.add_field(name="😀 8. Membros", value=f"Nunca confie 100% em ninguém do servidor, muito menos nos membros! Aqui raramente alguém vai te chamar no privado para querer saber algo sobre você ou algo relacionado! Confie apenas nos membros com cargos de <@&{913150421063835659}> ou <@&{913150435651629106}> já que são de confiança do dono do servidor.", inline=False)
    embed.add_field(name="🤖 9. Comandos de Bot", value=f"Os comandos dos bots disponíveis no servidor devem ser usados apenas no canal <#{1179508687556051074}>. Comandos de música devem ser usados apenas no canal <#{913225365072257046}>.", inline=False)
    embed.add_field(name="📯 10. Divulgações", value=f"Caso queira fazer alguma divulgação no servidor, use o canal <#{913225542059315240}>. OBS: Só será aceito divulgações coerentes como redes sociais, campanhas beneficentes, vakinhas e outros! Links para outros servidores, pedir permissão para mim (<@{589502565243289612}>).", inline=False)
    embed.add_field(name="📧 11. Convites", value=f"Para manter algo mais organizado, nenhum usuário tem a permissão de criar link de convites a não ser os membros com privilégios, como o <@&{913150421063835659}> ou <@&{913150435651629106}>. Peço a gentileza de outros membros que usem apenas o convite fixado no canal <#{1065675289163726848}>!", inline=False)
    embed.add_field(name="⚙️ 12. Atualizações", value=f"Sempre que houver atualizações significativas no servidor será notificado em <#{913137314845306900}>, então é de extrema importância que seja lido as mensagens do canal quando houver atualização!", inline=False)
    embed.add_field(name="🎰 13. Jogos de Azar", value=f"É totalmente proibídio a divulgação e/ou disseminação de links, publicidades, campanhas e outros meios que venham existir sobre jogos de azar, apostas esportivas, bets, slots e quaiquer outros serviços relacionados! Nossa comunidade é totalmente contra esse tipo de ato e o criador <@{589502565243289612}> repugna qualquer coisa relacionada a essa área! Se você, você que faz parte desse esquema de pirâmide financeira vir divulgar aqui no meu servidor, você será banido e não vai ter justificativa!", inline=False)
    embed.add_field(name="🧠 14. Conhecimento", value="O conhecimento te liberta! discuta e propague o quanto quiser! Hoje em dia com o aumento de pessoas nas redes sociais e a quantidade de desinformação que é propagada diariamente, é raro achar alguém que fale coisas boas e propague conteúdo de qualidade. Grande parte das pessoas na atualidade fazem vídeos e espalham conteúdos extremamente ruins e/ou sem valor a agregar para a comunidade como um todo. Aqui valorizamos conteúdos bons e conhecimentos! Então fique a vontade para discutir/debater/conversar sobre quaisquer assuntos!", inline=False)
    embed.add_field(name="🗃️ 15. Termos e Políticas", value=f"Será destinado em um comando separado os termos e políticas do servidor em relação ao Bot <@{927981778419998750}> e em relação a outros itens, então a regra número 12 é estar ciente de TODOS OS TERMOS E POLÍTICAS do mesmo em relação ao servidor. LEIAM! Seu orgão genital não vai cair por perder alguns minutos da sua vida lendo ao importante! - Comando para visualizar os termos: `./termos`", inline=False)
    embed.add_field(name="🏷️ 16. Regra importante", value=f"A regra 16 é importantissima! A regra 16 é somente a regra 16! Obrigado!", inline=False)
   
    embed.add_field(name="\n", value="\n", inline=False)
    embed.set_footer(text='Regras elaboradas por offalien\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

    await ctx.send(embed=embed)

@client.command()
async def termos(ctx):

    embed = discord.Embed(title='ㅤㅤㅤRegras/Termos e Responsabilidades - Houses Alienㅤㅤㅤ', description='\n\n Tempo de Leitura: **3 minutos**\n\n')

    embed.add_field(name="\n", value="\n", inline=False)
    embed.add_field(name="Termos de uso e Responsabilidades", value="", inline=False)
    embed.add_field(name="\n", value="\n", inline=False)
    embed.add_field(name="1. Comunidade Inclusivaㅤ", value='O Bot de Discord Whois Alien se esforça para criar um ambiente inclusivo onde todos os usuários são bem-vindos e respeitados. Não toleramos qualquer forma de discriminação com base em raça, cor, religião, identidade de gênero, orientação sexual, deficiência ou qualquer outra característica protegida por lei. \n\n', inline=False)
    embed.add_field(name="2. LGPD - Lei Geral de Proteção de Dados", value='As consultas de dados realizadas pelo Bot de Discord Whois Alien estão em estrita conformidade com a Lei Geral de Proteção de Dados (LGPD). Isso significa que:\n\n             - Os dados coletados são utilizados apenas para os fins específicos para os quais foram autorizados.\n\n             - Os usuários têm o direito de acessar, corrigir ou excluir seus dados pessoais contatando o criador/compilador do mesmo, conforme previsto pela LGPD.', inline=False)
    embed.add_field(name="3. Uso Indevido das Consultas", value='O criador do Bot de Discord Whois Alien não é responsável pelo uso indevido das consultas realizadas pela ferramenta. Os participantes do servidor também são orientados a usar as informações obtidas de maneira ética e legal. Qualquer uso indevido é estritamente proibido e não reflete a intenção ou responsabilidade do criador ou dos participantes do servidor.', inline=False)
    embed.add_field(name="4. Dados Gerados e Coincidências", value='Dados gerados pelo Bot de Discord Whois Alien que possam coincidir com informações reais são puramente coincidência. O bot é projetado para fornecer informações gerais baseadas em dados disponíveis publicamente e não garante a precisão ou exatidão das informações fornecidas.', inline=False)
    embed.add_field(name="5. Uso Consciente e Ético da Ferramenta", value='Os usuários são incentivados a usar o Bot de Discord Whois Alien de maneira consciente e ética. Isso inclui:\n\n             - Não utilizar a ferramenta para atividades ilegais ou ilícitas.\n\n             - Respeitar os direitos de privacidade de terceiros.\n\n             - Não realizar consultas em larga escala que possam sobrecarregar os sistemas ou violar os termos de serviço de terceiros.', inline=False)
    embed.add_field(name="6. Consequências do Uso Indevido", value='Qualquer uso indevido do Bot de Discord Whois Alien resultará em medidas disciplinares, incluindo, mas não limitado a, banimento permanente do servidor e revogação do acesso à ferramenta. A equipe de moderação se reserva o direito de tomar ações apropriadas para manter a integridade e a segurança do ambiente do servidor.', inline=False)
    embed.add_field(name="", value='', inline=False)
    embed.add_field(name="Outros Detalhes e Informações Importantes", value='', inline=False)    
    embed.add_field(name="", value='\n\n- **Atualizações e Mudanças**: O Bot de Discord Whois Alien pode ser atualizado periodicamente para melhorar funcionalidades e segurança. Os usuários serão informados sobre quaisquer mudanças significativas que possam afetar o uso da ferramenta.\n\n             - **Suporte e Contato**: Para dúvidas, suporte ou relatar problemas, os usuários podem entrar em contato com o dono do servidor, conforme as instruções fornecidas.', inline=False)    
    embed.add_field(name="", value='Estes termos e responsabilidades visam garantir um ambiente seguro, ético e responsável para todos os usuários que interagem com o Bot de Discord Whois Alien.', inline=False)
    embed.add_field(name="", value=f'Caso verifique que seus dados estão presentes na ferramenta e você tenha interesse em remove-los, entre em contato diretamente com o <@{589502565243289612}>.', inline=False)
    embed.add_field(name="\n", value="\n", inline=False)    
    embed.set_footer(text='Termos e políticas elaboradas por offalien\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

    await ctx.send(embed=embed)

@client.command()
async def repositorio(ctx):

    await ctx.send("https://github.com/cristopherrissardi/Whois-Alien-Bot")

@client.command()
async def info(ctx):

    embed = discord.Embed(title="", description="")

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤINFORMAÇÕESㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

    embed.add_field(name="🚀 Comando de Ajuda", value="Use o comando `./ajuda` para que seja retornado parte dos comandos existentes no bot.", inline=False)
    embed.add_field(name="🛰️ Veja seu Ping", value="Use o comando `./ping` para ver o seu ping no discord e o ping do servidor em uma escala de 0-1000. `Lembre-se que no quiesito ping em bot pode sempre existir uma margem de erro.`", inline=False)
    embed.add_field(name="🛩️ Informações do servidor", value="Use o comando `./serverinfo` para ver as informações do servidor. [AINDA NÃO IMPLEMENTADO]", inline=False)
    embed.add_field(name="🛩️ Informações do usuário", value="Use o comando `./userinfo` para ver as informações do usuário. [AINDA NÃO IMPLEMENTADO]", inline=False)

    embed.set_footer(text='Whois Alien © All Rights Reserved', icon_url='')

    await ctx.send(embed=embed)

@client.command()
async def ryanboiola(ctx):

    embed = discord.Embed(title='', description='',)

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤMinha Históriaㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

    embed.add_field(name="", value='Ryan era um jovem de 17 anos que morava na cidade de Muqui, um município tranquilo no Espírito Santo, Brasil. Desde cedo, Ryan sabia que era diferente dos outros meninos de sua idade. Enquanto seus amigos se interessavam por garotas, ele sentia uma atração diferente, uma atração por garotos. Essa descoberta o deixou confuso no início. Ele se perguntava se estava certo ser quem era, se sua família e amigos o aceitariam.', inline=False)              
    embed.add_field(name="", value='Mas à medida que o tempo passava, Ryan começou a entender que sua orientação sexual era uma parte natural e bonita de quem ele era.', inline=False)  
    embed.add_field(name="", value='Ryan tinha o apoio de sua família. Seus pais e irmãos o amavam incondicionalmente e o aceitavam completamente. Eles sempre o encorajavam a ser honesto consigo mesmo e com os outros. Com o tempo, ele também encontrou apoio em alguns amigos próximos que o aceitaram sem hesitar.', inline=False)             
    embed.add_field(name="", value='Conforme os anos passaram, Ryan se tornou mais confiante em relação à sua identidade. Ele começou a se envolver em grupos de apoio LGBTQ+ em Muqui, onde conheceu pessoas incríveis que compartilhavam suas experiências e desafios. Essas amizades o ajudaram a crescer e a aceitar completamente quem ele era.', inline=False)             
    embed.add_field(name="", value='Embora Muqui fosse uma cidade pequena, a mentalidade das pessoas estava mudando gradualmente. A aceitação estava crescendo e mais pessoas estavam se tornando conscientes da importância de respeitar as diferenças. Ryan, com sua autenticidade, contribuiu para essa mudança positiva ao educar as pessoas sobre a comunidade LGBTQ+.', inline=False)             
    embed.add_field(name="", value='Ryan tinha um sonho de um mundo onde todos fossem aceitos independentemente de sua orientação sexual. Ele sabia que havia muito trabalho a ser feito, mas estava determinado a fazer a diferença, não apenas em Muqui, mas em todos os lugares onde sua voz pudesse ser ouvida.', inline=False)             
    embed.add_field(name="", value='A história de Ryan era uma história de autodescoberta, aceitação e coragem. Ele aprendeu a abraçar sua verdadeira identidade e a usar sua voz para promover a igualdade e a compreensão em sua cidade natal e além. E à medida que ele continuava sua jornada, Ryan estava ansioso para um futuro onde todos pudessem ser livres para amar e ser quem são, independentemente de sua orientação sexual.', inline=False)                       
    embed.add_field(name="Minhas Tags:", value='`gay`,`boiola`,`bicha`,`homossexual`,`baitola`,`viado`,`bambi`,`invertido`,`afemeninado`', inline=False)             
    embed.add_field(name="Eu sou também:", value='`gay`,`boiola`,`bicha`,`homossexual`,`baitola`,`viado`,`bambi`,`invertido`,`afemeninado`', inline=False)
    embed.add_field(name="Podem me chamar de:", value='`gay`,`boiola`,`bicha`,`homossexual`,`baitola`,`viado`,`bambi`,`invertido`,`afemeninado`', inline=False)
    embed.add_field(name="", value='\n\n', inline=False)
    embed.add_field(name="", value='ESPERO DE CORAÇÃO QUE TENHAM GOSTADO DA MINHA HISTÓRIA ❤️', inline=False)
    embed.set_image(url='https://media.tenor.com/m8-MzOoeUEgAAAAd/lookupanddown-gay.gif')
    embed.set_footer(text='Nossa comunidade é totalmente contra o preconceito ou qualquer outro tipo de discriminação! Diga não ao preconceito 🏳️‍🌈\n\nWhois Alien © All Rights Reserved', icon_url='')
    
    await ctx.send(embed=embed)

@client.command()
async def nome(ctx, *, nome):

    nome_formatado = nome.strip().replace(' ', '%20')
    data = f"http://18.228.166.136:8000/api/v1/database/serasa/search?nome={nome_formatado}"

    headers = {"apikey": API_KEY}

    response = requests.get(data, headers=headers)

    try:
        if response.status_code == 200:
            data_json = response.json()

            if isinstance(data_json, list) and len(data_json) > 1:
                file_contents = ""
                for index, result in enumerate(data_json, 1):
                    file_contents += f"RESULTADO {index}:\n\n• NOME: {result['nome']}\n• CPF: {result['cpf']}\n• SEXO: {result['sexo']}\n• DATA DE NASCIMENTO: {result['data_nascimento']}\n\n"

                file_contents += "\nWhois Alien © All Rights Reserved\n"

                file = io.StringIO(file_contents)
                file.seek(0)

                await ctx.send(file=discord.File(file, filename="resultados.txt"))
            elif isinstance(data_json, dict) or (isinstance(data_json, list) and len(data_json) == 1):
                result = data_json[0] if isinstance(data_json, list) else data_json

                embed = discord.Embed(title='')
                embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE NOMEㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

                embed.add_field(name='• NOME', value=result.get('nome', 'SEM INFORMAÇÃO').upper(), inline=False)
                embed.add_field(name='• CPF', value=result.get('cpf', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• SEXO', value=result.get('sexo', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• DATA DE NASCIMENTO', value=result.get('data_nascimento', 'SEM INFORMAÇÃO'), inline=False)

                embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)
                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="")
            embed.set_author(name=f'ㅤㅤㅤNOME NÃO ENCONTRADO!ㅤㅤㅤ', icon_url='')
            await ctx.send(embed=embed)

    except Exception as e:       
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE NOME', icon_url='')
        embed.add_field(name="Use o comando: `/nome` e o {NOME} que deseja.", value='*Exemplo: `/nome` Fulano Santos*', inline=False)

        await ctx.send(embed=embed)

@client.command()
async def mae(ctx, *, mae):

    mae_formatado = mae.strip().replace(' ', '%20')
    data = f"http://18.228.166.136:8000/api/v1/database/datasus/search?mae={mae_formatado}"

    headers = {"apikey": API_KEY}

    response = requests.get(data, headers=headers)

    try:
        if response.status_code == 200:
            data_json = response.json()

            if isinstance(data_json, list) and len(data_json) > 1:
                file_contents = ""
                for index, result in enumerate(data_json, 1):
                    file_contents += f"RESULTADO {index}:\n\n• NOME: {result['nome']}\n• CPF: {result['cpf']}\n• DATA DE NASCIMENTO: {result['nascimento']}\n• NOME DA MÃE: {result['mae']}\n\n"

                file_contents += "\nWhois Alien © All Rights Reserved\n"

                file = io.StringIO(file_contents)
                file.seek(0)

                await ctx.send(file=discord.File(file, filename="resultados.txt"))
            elif isinstance(data_json, dict) or (isinstance(data_json, list) and len(data_json) == 1):
                result = data_json[0] if isinstance(data_json, list) else data_json

                embed = discord.Embed(title='')
                embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤCONSULTA DE NOME DA MÃEㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

                embed.add_field(name='• NOME', value=result.get('nome', 'SEM INFORMAÇÃO').upper(), inline=False)
                embed.add_field(name='• CPF', value=result.get('cpf', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• DATA DE NASCIMENTO', value=result.get('nascimento', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• NOME DA MÃE', value=result.get('mae', 'SEM INFORMAÇÃO'), inline=False)

                embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)
                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="")
            embed.set_author(name=f'ㅤㅤㅤNOME DA MÃE NÃO ENCONTRADO!ㅤㅤㅤ', icon_url='')
            await ctx.send(embed=embed)

    except Exception as e:       
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE NOME', icon_url='')
        embed.add_field(name="Use o comando: `/mae` e o nome da {MÃE} que deseja.", value='*Exemplo: `/mae` Fulana Santos*', inline=False)

        await ctx.send(embed=embed)

@client.command()
async def pai(ctx, *, pai):

    pai_formatado = pai.strip().replace(' ', '%20')
    data = f"http://18.228.166.136:8000/api/v1/database/datasus/search?pai={pai_formatado}"

    headers = {"apikey": API_KEY}

    response = requests.get(data, headers=headers)

    try:
        if response.status_code == 200:
            data_json = response.json()

            if isinstance(data_json, list) and len(data_json) > 1:
                file_contents = ""
                for index, result in enumerate(data_json, 1):
                    file_contents += f"RESULTADO {index}:\n\n• NOME: {result['nome']}\n• CPF: {result['cpf']}\n• DATA DE NASCIMENTO: {result['nascimento']}\n• NOME DO PAI: {result['pai']}\n\n"

                file_contents += "\nWhois Alien © All Rights Reserved\n"

                file = io.StringIO(file_contents)
                file.seek(0)

                await ctx.send(file=discord.File(file, filename="resultados.txt"))
            elif isinstance(data_json, dict) or (isinstance(data_json, list) and len(data_json) == 1):
                result = data_json[0] if isinstance(data_json, list) else data_json

                embed = discord.Embed(title='')
                embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤCONSULTA DE NOME DO PAIㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

                embed.add_field(name='• NOME', value=result.get('nome', 'SEM INFORMAÇÃO').upper(), inline=False)
                embed.add_field(name='• CPF', value=result.get('cpf', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• DATA DE NASCIMENTO', value=result.get('nascimento', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• NOME DO PAI', value=result.get('pai', 'SEM INFORMAÇÃO'), inline=False)

                embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)
                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="")
            embed.set_author(name=f'ㅤㅤㅤNOME DO PAI NÃO ENCONTRADO!ㅤㅤㅤ', icon_url='')
            await ctx.send(embed=embed)

    except Exception as e:       
        embed.set_author(name='ㅤㅤㅤㅤ👽 CONSULTA PELO NOME DO PAI', icon_url='')
        embed.add_field(name="Use o comando: `/pai` e o nome do {PAI} que deseja.", value='*Exemplo: `/pai` Fulano Santos*', inline=False)

        await ctx.send(embed=embed)

@client.command()
async def email(ctx, *, email):

    email_formatado = email.strip().replace(' ', '%20')
    data = f"http://18.228.166.136:8000/api/v1/datasus_emails/search?email={email_formatado}"

    headers = {"apikey": API_KEY}

    response = requests.get(data, headers=headers)

    try:
        if response.status_code == 200:
            data_json = response.json()

            if isinstance(data_json, list) and len(data_json) > 1:
                file_contents = ""
                for index, result in enumerate(data_json, 1):
                    file_contents += f"RESULTADO {index}:\n\n• NOME: {result['nome']}\n• CPF: {result['cpf']}\n• DATA DE NASCIMENTO: {result['nascimento']}\n• E-MAIL: {result['emails']}\n\n"

                file_contents += "\nWhois Alien © All Rights Reserved\n"

                file = io.StringIO(file_contents)
                file.seek(0)

                await ctx.send(file=discord.File(file, filename="resultados.txt"))
            elif isinstance(data_json, dict) or (isinstance(data_json, list) and len(data_json) == 1):
                result = data_json[0] if isinstance(data_json, list) else data_json

                embed = discord.Embed(title='')
                embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤCONSULTA DE DADOS POR EMAILㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

                embed.add_field(name='• NOME', value=result.get('nome', 'SEM INFORMAÇÃO').upper(), inline=False)
                embed.add_field(name='• CPF', value=result.get('cpf', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• DATA DE NASCIMENTO', value=result.get('nascimento', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• E-MAIL', value=result.get('emails', 'SEM INFORMAÇÃO'), inline=False)

                embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)
                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="")
            embed.set_author(name=f'ㅤㅤㅤE-MAIL NÃO ENCONTRADO!ㅤㅤㅤ', icon_url='')
            await ctx.send(embed=embed)

    except Exception as e:       
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE E-MAIL', icon_url='')
        embed.add_field(name="Use o comando: `/email` e o {EMAIL} que deseja.", value='*Exemplo: `/email` fulanodetal@gmail.com*', inline=False)

        await ctx.send(embed=embed)

@client.command()
async def cpf(ctx, *, cpf):

    cpf_formatado = cpf.strip()
    data = f"http://18.228.166.136:8000/api/v1/database/datasus/search?cpf={cpf_formatado}"

    headers = {"apikey": API_KEY}

    response = requests.get(data, headers=headers)
    try:
        if response.status_code == 200:
            data = response.json()

            if len(data) > 0:
                cpf2_info = data[0]  # Acessa o primeiro item na lista

                embed = discord.Embed(title='')

                embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE CPFㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

                embed.add_field(name='• CPF', value=cpf2_info.get('cpf', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name="• CNS", value=cpf2_info.get('cns', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name="• RG", value=cpf2_info.get('rgNumero', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name="• TÍTULO ELEITORAL", value='SEM INFORMAÇÃO', inline=False)
                embed.add_field(name="• NOME", value=cpf2_info.get('nome', 'SEM INFORMAÇÃO').upper(), inline=False)
                embed.add_field(name="• NASCIMENTO", value=cpf2_info.get('nascimento', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name="• MÃE", value=cpf2_info.get('mae', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name="• PAI", value=cpf2_info.get('pai', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name="• CIDADE DE NASCIMENTO", value=cpf2_info.get('municipioNascimento', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name="• LOGRADOURO", value=cpf2_info.get('logradouro', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name="• NÚMERO", value=cpf2_info.get('numero', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name="• COMPLEMENTO", value='SEM INFORMAÇÃO', inline=False)
                embed.add_field(name="• BAIRRO", value=cpf2_info.get('bairro', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name="• CIDADE", value=cpf2_info.get('municipio', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name="• CEP", value=cpf2_info.get('cep', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name="• E-MAIL", value='SEM INFORMAÇÃO', inline=False)
                embed.add_field(name="• TELEFONE", value=cpf2_info.get('telefone', 'SEM INFORMAÇÃO'), inline=False)

                embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)
                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="")
                embed.set_author(name=f'CPF NÃO ENCONTRADO!', icon_url='')

                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="")
            embed.set_author(name=f'CPF NÃO ENCONTRADO! {response.status_code}', icon_url='')

            await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(title='')
        embed.set_author(name=f'CPF NÃO ENCONTRADO! {response.status_code}', icon_url='')

        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE CPF', icon_url='')
        embed.add_field(name="Use o comando: `/cpfx` e o {CPF} que deseja.", value='*Exemplo: `/cpf` 123.456.789-12*', inline=False)

        await ctx.send(embed=embed)

@client.command()
async def cpf0(ctx, *, cpf0):

    cpf_formatado = cpf0.strip()
    data = f"http://18.228.166.136:8000/api/v1/database/serasa/search?cpf={cpf_formatado}"

    headers = {"apikey": API_KEY}

    response = requests.get(data, headers=headers)

    try:
        if response.status_code == 200:
            data = response.json()

            if len(data) > 0:
                cpf_info = data[0]  # Acessa o primeiro item na lista

                embed = discord.Embed(title='')

                embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE CPFㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

                embed.add_field(name='• CPF', value=cpf_info.get('cpf', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name="• NOME", value=cpf_info.get('nome', 'SEM INFORMAÇÃO').upper(), inline=False)
                embed.add_field(name='• SEXO', value=cpf_info.get('sexo', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• DATA DE NASCIMENTO', value=cpf_info.get('data_nascimento', 'SEM INFORMAÇÃO'), inline=False)

                embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)
                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="")
            embed.set_author(name=f'ㅤㅤㅤCPF NÃO ENCONTRADO!ㅤㅤㅤ', icon_url='')

            await ctx.send(embed=embed)

    except Exception as e:

        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE CPF', icon_url='')
        embed.add_field(name="Use o comando: `/cpf` e o {CPF} que deseja.", value='*Exemplo: `/cpf0` 123.456.789-12*', inline=False)

        await ctx.send(embed=embed)

@client.command()
async def telefone(ctx, *, telefone):

    telefone_formatado = telefone.strip().replace(' ', '%20')
    data = f"http://18.228.166.136:8000/api/v1/database/telefone/search?telefone={telefone_formatado}"

    headers = {"apikey": API_KEY}

    response = requests.get(data, headers=headers)

    try:
        if response.status_code == 200:
            data_json = response.json()

            if isinstance(data_json, list) and len(data_json) > 1:
                file_contents = ""
                for index, result in enumerate(data_json, 1):
                    file_contents += f"RESULTADO {index}:\n\n• TELEFONE: {result['telefone']}\n• NOME: {result['nome']}\n• CPF/CNPJ: {result['cpf']}\n• LOGRADOURO: {result['rua']}\n• NÚMERO: {result['numero']}\n• COMPLEMENTO: {result['complemento']}\n• BAIRRO: {result['bairro']}\n• CIDADE: {result['cidade']}\n• ESTADO: {result['uf']}\n• CEP: {result['cep']}\n\n"

                file_contents += "\nWhois Alien © All Rights Reserved\n"

                file = io.StringIO(file_contents)
                file.seek(0)

                await ctx.send(file=discord.File(file, filename="resultados.txt"))
            elif isinstance(data_json, dict) or (isinstance(data_json, list) and len(data_json) == 1):
                result = data_json[0] if isinstance(data_json, list) else data_json

                embed = discord.Embed(title='')
                embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤCONSULTA DE TELEFONEㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

                embed.add_field(name='• TELEFONE', value=result.get('telefone', 'SEM INFORMAÇÃO').upper(), inline=False)
                embed.add_field(name='• NOME', value=result.get('nome', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• CPF/CNPJ', value=result.get('cpf', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• LOGRADOURO', value=result.get('rua', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• NÚMERO', value=result.get('numero', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• COMPLEMENTO', value=result.get('complemento', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• BAIRRO', value=result.get('bairro', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• CIDADE', value=result.get('cidade', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• ESTADO', value=result.get('uf', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• CEP', value=result.get('cep', 'SEM INFORMAÇÃO'), inline=False)

                embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)
                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="")
            embed = discord.Embed(title=f"TELEFONE NÃO ENCONTRADO! {response.status_code}")
            await ctx.send(embed=embed)

    except Exception as e:       
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE TELEFONE', icon_url='')
        embed.add_field(name="Use o comando:", value='`/telefone` e o {TELEFONE} que deseja.', inline=False)
        embed.add_field(value='Exemplo: `/telefone` 11987654321', inline=False)

        await ctx.send(embed=embed)

@client.command()
async def fixo(ctx, *, fixo):

    fixo_formatado = fixo.strip().replace(' ', '%20')
    data = f"http://18.228.166.136:8000/api/v1/database/telefone/search?fixo={fixo_formatado}"

    headers = {"apikey": API_KEY}

    response = requests.get(data, headers=headers)

    try:
        if response.status_code == 200:
            data_json = response.json()

            if isinstance(data_json, list) and len(data_json) > 1:
                file_contents = ""
                for index, result in enumerate(data_json, 1):
                    file_contents += f"RESULTADO {index}:\n\n• TELEFONE: {result['telefone']}\n• NOME: {result['nome']}\n• CPF/CNPJ: {result['cpf']}\n• LOGRADOURO: {result['rua']}\n• NÚMERO: {result['numero']}\n• COMPLEMENTO: {result['complemento']}\n• BAIRRO: {result['bairro']}\n• CIDADE: {result['cidade']}\n• ESTADO: {result['uf']}\n• CEP: {result['cep']}\n\n"

                file_contents += "\nWhois Alien © All Rights Reserved\n"

                file = io.StringIO(file_contents)
                file.seek(0)

                await ctx.send(file=discord.File(file, filename="resultados.txt"))
            elif isinstance(data_json, dict) or (isinstance(data_json, list) and len(data_json) == 1):
                result = data_json[0] if isinstance(data_json, list) else data_json

                embed = discord.Embed(title='')
                embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤCONSULTA DE TELEFONEㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

                embed.add_field(name='• TELEFONE FIXO', value=result.get('fixo', 'SEM INFORMAÇÃO').upper(), inline=False)
                embed.add_field(name='• NOME', value=result.get('nome', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• CPF/CNPJ', value=result.get('cpf', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• LOGRADOURO', value=result.get('rua', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• NÚMERO', value=result.get('numero', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• COMPLEMENTO', value=result.get('complemento', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• BAIRRO', value=result.get('bairro', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• CIDADE', value=result.get('cidade', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• ESTADO', value=result.get('uf', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• CEP', value=result.get('cep', 'SEM INFORMAÇÃO'), inline=False)

                embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)
                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="")
            embed = discord.Embed(title=f"TELEFONE NÃO ENCONTRADO! {response.status_code}")
            await ctx.send(embed=embed)

    except Exception as e:       
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE TELEFONE', icon_url='')
        embed.add_field(name="Use o comando:", value='`/fixo` e o {TELEFONE} que deseja.', inline=False)
        embed.add_field(value='Exemplo: `/fixo` 1833621583', inline=False)

        await ctx.send(embed=embed)

@client.command()
async def cep_pessoas(ctx, *, cep_pessoas):

    cep_pessoas_formatado = cep_pessoas.strip().replace(' ', '%20')
    data = f"http://18.228.166.136:8000/api/v1/database/datasus/search?cep={cep_pessoas_formatado}"

    headers = {"apikey": API_KEY}

    response = requests.get(data, headers=headers)

    try:
        if response.status_code == 200:
            data_json = response.json()

            if isinstance(data_json, list) and len(data_json) > 1:
                file_contents = ""
                for index, result in enumerate(data_json, 1):
                    file_contents += f"RESULTADO {index}:\n\n• NOME: {result['nome']}\n• CPF: {result['cpf']}\n• DATA DE NASCIMENTO: {result['nascimento']}\n• LOGRADOURO: {result['logradouro']}\n• NUMERO: {result['numero']}\n• CEP: {result['cep']}\n• MUNICIPIO: {result['municipio']}\n\n"

                file_contents += "\nWhois Alien © All Rights Reserved\n"

                file = io.StringIO(file_contents)
                file.seek(0)

                await ctx.send(file=discord.File(file, filename="resultados.txt"))
            elif isinstance(data_json, dict) or (isinstance(data_json, list) and len(data_json) == 1):
                result = data_json[0] if isinstance(data_json, list) else data_json

                embed = discord.Embed(title='')
                embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤCONSULTA DE DADOS POR CEPㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

                embed.add_field(name='• NOME', value=result.get('nome', 'SEM INFORMAÇÃO').upper(), inline=False)
                embed.add_field(name='• CPF', value=result.get('cpf', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• DATA DE NASCIMENTO', value=result.get('nascimento', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• LOGRADOURO', value=result.get('logradouro', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• NÚMERO', value=result.get('numero', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• CEP', value=result.get('cep', 'SEM INFORMAÇÃO'), inline=False)
                embed.add_field(name='• MUNICIPIO', value=result.get('municipio', 'SEM INFORMAÇÃO'), inline=False)

                embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)
                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="")
            embed = discord.Embed(title=f"CEP NÃO ENCONTRADO! {response.status_code}")
            await ctx.send(embed=embed)

    except Exception as e:       
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE CEP', icon_url='')
        embed.add_field(name="Use o comando:", value='`/cep` e o {CEP} que deseja.', inline=False)
        embed.add_field(value='Exemplo: `/telefone` 01153000', inline=False)

        await ctx.send(embed=embed)


@client.command()
async def placa(ctx, placa = None):

    placa_token = os.getenv("PLACA_TOKEN_API")

    data = requests.get(f'https://wdapi2.com.br/consulta/{placa}/{placa_token}').json()  

    embed = discord.Embed(title='')

    validateMarca = data["MARCA"] if data["MARCA"] != "" else "Não encontrado"
    validateAno = data["ano"] if data["ano"] != "" else "Não encontrado"
    validateDataAtt = data["data"] if data["data"] != "" else "Não encontrado"
    validateModelo = data["MODELO"] if data["MODELO"] != "" else "Não encontrado"
    validateAnoModelo = data["anoModelo"] if data["anoModelo"] != "" else "Não encontrado"
    validateCor = data["cor"] if data["cor"] != "" else "Não encontrado"
    validateChassi = data["chassi"] if data["chassi"] != "" else "Não encontrado"

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE PLACAㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

    embed.add_field(name="• MARCA", value=validateMarca, inline=False)
    embed.add_field(name="• ANO", value=validateAno, inline=False)
    embed.add_field(name="• DATA DE ATUALIZAÇÃO ", value=validateDataAtt, inline=False)
    embed.add_field(name="• MODELO", value=validateModelo, inline=False)
    embed.add_field(name="• ANO DO MODELO", value=validateAnoModelo, inline=False)
    embed.add_field(name="• COR", value=validateCor, inline=False)
    embed.add_field(name="• CHASSI", value=validateChassi, inline=False)

    embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)             
    embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

    await ctx.send(embed=embed)

@client.command() 
async def cnpj(ctx, cnpj = None):

    data = requests.get(f"https://hyb.com.br/curl_cnpj.php?action=acessa_curl&cnpj={cnpj}").json()
    
    try:
        embed = discord.Embed(title='')
        
        validateCnpj = data["cnpj"] if data["cnpj"] != "" else "SEM INFORMAÇÃO"
        validateNome = data["nome_fantasia"] if data["nome_fantasia"] != "" else "SEM INFORMAÇÃO"
        validateRazao = data["razao_social"] if data["razao_social"] != "" else "SEM INFORMAÇÃO"
        validateEmail = data["email"] if data["email"] != "" else "SEM INFORMAÇÃO"
        validateUf = data["uf"] if data["uf"] != "" else "SEM INFORMAÇÃO"
        validateComplemento = data["complemento"] if data["complemento"] != "" else "SEM INFORMAÇÃO"
        validateBairro = data["bairro"] if data["bairro"] != "" else "SEM INFORMAÇÃO"
        validateNumero = data["numero"] if data["numero"] != "" else "SEM INFORMAÇÃO"
        validateMunicipio = data["municipio"] if data["municipio"] != "" else "SEM INFORMAÇÃO"
        validateData = data["data_inicio_ativ"] if data["data_inicio_ativ"] != "" else "SEM INFORMAÇÃO"
        validateCnae = data["qualif_resp"] if data["qualif_resp"] != "" else "SEM INFORMAÇÃO"
        validateCnaeCod = data["cnae_fiscal"] if data["cnae_fiscal"] != "" else "SEM INFORMAÇÃO"
        validateMatriz = data["matriz_filial"] if data["matriz_filial"] != "" else "SEM INFORMAÇÃO"
        validateFilial = data["motivo_situacao"] if data["motivo_situacao"] != "" else "SEM INFORMAÇÃO"
        validateDataSituacao = data["data_situacao"] if data["data_situacao"] != "" else "SEM INFORMAÇÃO"
        validateJuridica = data["nm_cidade_exterior"] if data["nm_cidade_exterior"] != "" else "SEM INFORMAÇÃO"
        validateLogradouro = data["logradouro"] if data["logradouro"] != "" else "SEM INFORMAÇÃO"
        validateTipoRua = data["tipo_logradouro"] if data["tipo_logradouro"] != "" else "SEM INFORMAÇÃO"
        validateSocios = ', '.join(data["socios"]) if data["socios"] else "SEM INFORMAÇÃO"
        validateTelefone1 = data["telefone_1"] if data["telefone_1"] != "" else "SEM INFORMAÇÃO"
        validateTelefone2 = data["telefone_2"] if data["telefone_2"] != "" else "SEM INFORMAÇÃO"
        validateQualificacao = data["cod_pais"] if data["cod_pais"] != "" else "SEM INFORMAÇÃO"
        validateCapital = data["capital_social"] if data["capital_social"] != "" else "SEM INFORMAÇÃO"
        validateSimples = data["opc_simples"] if data["opc_simples"] != "" else "SEM INFORMAÇÃO"
        validateSimplesDate = data["data_opc_simples"] if data["data_opc_simples"] != "" else "SEM INFORMAÇÃO"
        validateCep = data["cep"] if data["cep"] != "" else "SEM INFORMAÇÃO"
        
        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE CNPJㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

        embed.add_field(name="• CNPJ", value=validateCnpj, inline=False) #
        embed.add_field(name="• NOME FANTASIA", value=validateNome, inline=False)  #
        embed.add_field(name="• RAZÃO SOCIAL", value=validateRazao, inline=False) #
        embed.add_field(name="• MATRIZ FILIAL", value=validateMatriz, inline=False) #
        embed.add_field(name="• MOTIVO DA ABERTURA", value=validateFilial, inline=False) #
        embed.add_field(name="• ENDEREÇO", value=validateTipoRua + ' ' + validateLogradouro + ',' + ' ' + validateNumero + ' ' + '-' + ' ' + validateBairro, inline=False) #
        embed.add_field(name="• CEP", value=validateCep, inline=False) #        
        embed.add_field(name="• MUNICÍPIO", value=validateMunicipio + ' ' + '-' + ' ' + validateUf, inline=False) #
        embed.add_field(name="• COMPLEMENTO", value=validateComplemento, inline=False) #
        embed.add_field(name="• TELEFONE ", value=validateTelefone1, inline=False) #
        embed.add_field(name="• TELEFONE 2", value=validateTelefone2, inline=False) #
        embed.add_field(name="• DATA DE ABERTURA", value=validateData, inline=False) #
        embed.add_field(name="• E-MAIL", value=validateEmail, inline=False) #
        embed.add_field(name="• SÓCIOS PROPRIETÁRIOS", value=validateSocios, inline=False) #
        embed.add_field(name="• DATA DE ATUALIZAÇÃO", value=validateDataSituacao, inline=False) #
        embed.add_field(name="• QUALIFICAÇÃO DO RESPONSÁVEL", value=validateCnae, inline=False) #
        embed.add_field(name="• CIDADE NO EXTERIOR", value=validateJuridica, inline=False) #
        embed.add_field(name="• CÓDIGO DO PAÍS EXTERIOR", value=validateQualificacao, inline=False) #
        embed.add_field(name="• CAPITAL SOCIAL", value=validateCapital, inline=False) #
        embed.add_field(name="• OPÇÃO PELO SIMPLES", value=validateSimples, inline=False) #
        embed.add_field(name="• DATA OPÇÃO PELO SIMPLES", value=validateSimplesDate, inline=False) #
        embed.add_field(name="• CNAE FISCAL", value=validateCnaeCod, inline=False) #
        embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)             
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

        await ctx.send(embed=embed)
    
        return
    except Exception:
        pass

        embed = discord.Embed(title='')

    if (cnpj == None):
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO CNPJㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/cnpj` e o {CNPJ} que deseja.", value='*Exemplo: `/cnpj` 12345678901234*', inline=False)
        embed.add_field(name="Observação:", value='*Não utilize pontos, hifens e caracteres especiais*', inline=False)        
        return await ctx.send(embed=embed)
    else:
       embed.set_author(name='ㅤㅤㅤㅤCNPJ NÃO ENCONTRADOㅤㅤㅤ', icon_url='')
       return await ctx.send(embed=embed)


@client.command()
async def ip(ctx, ip = None):

    data = requests.get(f"http://ipwhois.app/json/{ip}").json()
    
    try:
        embed = discord.Embed(title='')

        validateAsn = data["asn"] if data["asn"] != "" else "SEM INFORMAÇÃO"
        validateAsn = data["org"] if data["org"] != "" else "SEM INFORMAÇÃO"

        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE IPㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

        embed.add_field(name="• IP", value=data['ip'], inline=False)
        embed.add_field(name="• TIPO", value=data['type'], inline=False)
        embed.add_field(name="• CIDADE", value=data['city'], inline=False)
        embed.add_field(name="• ESTADO", value=data['region'], inline=False)
        embed.add_field(name="• PAÍS", value=data['country'], inline=False)
        embed.add_field(name="• CONTINENTE", value=data["continent"], inline=False)
        embed.add_field(name="• LATITUDE", value=data['latitude'], inline=False)
        embed.add_field(name="• LONGITUDE", value=data['longitude'], inline=False)
        embed.add_field(name="• PROVEDOR", value=data['isp'], inline=False)
        embed.add_field(name="• ORGANIZAÇÃO", value=validateAsn, inline=False)
        embed.add_field(name="• ASN", value=validateAsn, inline=False)
        embed.add_field(name="• EMPRESA RESPONSÁVEL", value=data['org'], inline=False)
        embed.add_field(name="• TIPO DE CONEXÃO", value=data['type'], inline=False)

        embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)             
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

        await ctx.send(embed=embed)

        return
    except Exception:
        pass
         
        embed = discord.Embed(title='')
    
    if (ip == None):
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO IPㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/ip` e o {IP} que deseja.", value='*Exemplo: `/ip` 127.0.0.1*', inline=False)
        return await ctx.send(embed=embed)
    else:
       embed.set_author(name='ㅤㅤㅤIP NÃO ENCONTRADOㅤㅤㅤ', icon_url='')
       return await ctx.send(embed=embed)

@client.command()
async def covid(ctx, covid = None):

    data = requests.get(f"https://covid19-brazil-api.vercel.app/api/report/v1/brazil/uf/{covid}").json()

    try:
        embed = discord.Embed(title='')

        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE COVID19ㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

        embed.add_field(name="• ESTADO", value=data['state'], inline=False)
        embed.add_field(name="• CASOS", value=data['cases'], inline=False)
        embed.add_field(name="• MORTES", value=data['deaths'], inline=False)
        embed.add_field(name="• SUSPEITOS", value=data['suspects'], inline=False)
        embed.add_field(name="• DESCARTADOS", value=data['refuses'], inline=False)
        embed.add_field(name="• DATA DE ATUALIZAÇÃO", value=data['datetime'], inline=False)

        embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

        await ctx.send(embed=embed)
        
        return
    except Exception:
        pass

        embed = discord.Embed(title='')

    if (covid == None):
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO COVIDㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/covid` e o {ESTADO} que deseja.", value='*Exemplo*: `/covid SP`', inline=False)
        embed.add_field(name="Observação:", value='*Utilize apenas a sigla do estado correspondente!*', inline=False)
        embed.add_field(name="Estados Brasileiros com suas respectivas siglas:", value='Acre - `AC`\nAlagoas - `AL`\nAmazonas - `AM`\nBahia - `BA`\nCeará - `CE`\nDistrito Federal - `DF`\nEspírito Santo - `ES`\nGoiás - `GO`\nMaranhão - `MA`\nMato Grosso - `MT`\nMato Grosso do Sul - `MS`\nMinas Gerais - `MG`\nPará - `PA`\nParaíba - `PB`\nParaná - `PR`\nPernambuco - `PE`\nPiauí - `PI`\nRio de Janeiro - `RJ`\nRio Grande do Norte - `RN`\nRio Grande do Sul - `RS`\nRondônia - `RO`\nRoraima	- `RR`\nSanta Catarina - `SC`\nSão Paulo - `SP`\nSergipe - `SE`\nTocantins - `TO`\n', inline=False)
        return await ctx.send(embed=embed)
    else:
       embed.set_author(name='ㅤㅤㅤㅤㅤㅤESTADO INVÁLIDOㅤㅤㅤ', icon_url='')
       return await ctx.send(embed=embed)

@client.command()
async def cep(ctx, cep=None):

    if not cep:

        embed = discord.Embed(title='')
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO CEP', icon_url='')
        embed.add_field(name="Use o comando: `/cep` e o {CEP} que deseja.", value='*Exemplo*: `/cep 70150904`', inline=False)
        embed.add_field(name="Observação:", value='*Não utilize pontos, hifens e caracteres especiais*', inline=False)      
        await ctx.send(embed=embed)

        return

    data = requests.get(f"https://viacep.com.br/ws/{cep}/json/").json()

    if 'erro' in data:
        embed = discord.Embed(title='')
        embed.set_author(name='CEP NÃO ENCONTRADO', icon_url='')
        await ctx.send(embed=embed)
        return

    embed = discord.Embed(title='')

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE CEPㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='') #----->> TÍTULO DO CÓDIGO

    embed.add_field(name="• CEP", value=data['cep'], inline=False)
    embed.add_field(name="• NOME DA RUA", value=data['logradouro'], inline=False)
    embed.add_field(name="• BAIRRO", value=data['bairro'], inline=False)
    embed.add_field(name="• CIDADE", value=data['localidade'], inline=False)
    embed.add_field(name="• ESTADO", value=data['uf'], inline=False)
    embed.add_field(name="• IBGE", value=data['ibge'], inline=False)
    embed.add_field(name="• DDD", value=data['ddd'], inline=False)

    embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)             
    embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

    await ctx.send(embed=embed)

@client.command()
async def maclookup(ctx, maclookup):

    mac_key = os.getenv("MACLOOKUP_KEY")
    url = f"https://mac-address.whoisxmlapi.com/api/v1?apiKey={mac_key}&macAddress={maclookup}&outputFormat=json" #--------->> API

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()


            date_created_iso = data.get("blockDetails", {}).get("dateCreated", "SEM INFORMAÇÃO")
            date_updated_iso = data.get("blockDetails", {}).get("dateUpdated", "SEM INFORMAÇÃO")

            date_created_br = datetime.strptime(date_created_iso, "%Y-%m-%d").strftime("%d/%m/%Y") #----->> VARIAVEL CORRIGIDA DE DATA DE CRIAÇÃO
            date_updated_br = datetime.strptime(date_updated_iso, "%Y-%m-%d").strftime("%d/%m/%Y") #----->> VARIAVEL CORRIGIDA DE DATA DE ATUALIZAÇÃO

            embed = discord.Embed(title="")

            embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤBUSCA DE ENDEREÇO MACㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='') #----->> TÍTULO DO CÓDIGO

            embed.add_field(name="INICIAL DO MAC ADRESS", value=data.get("vendorDetails", {}).get("oui", "SEM INFORMAÇÃO"), inline=False)
            embed.add_field(name="ENDEREÇO PRIVADO", value=data.get("vendorDetails", {}).get("isPrivate", "SEM INFORMAÇÃO"), inline=False)
            embed.add_field(name="FABRICANTE", value=data.get("vendorDetails", {}).get("companyName", "SEM INFORMAÇÃO"), inline=False)
            embed.add_field(name="ENDEREÇO DO FABRICANTE", value=data.get("vendorDetails", {}).get("companyAddress", "SEM INFORMAÇÃO"), inline=False)
            embed.add_field(name="PAÍS", value=data.get("vendorDetails", {}).get("countryCode", "SEM INFORMAÇÃO"), inline=False)
            embed.add_field(name="BLOCO ENCONTRADO", value=data.get("blockDetails", {}).get("blockFound", "SEM INFORMAÇÃO"), inline=False)
            embed.add_field(name="DATA DE CRIAÇÃO", value=date_created_br, inline=False)
            embed.add_field(name="DATA DE ATUALIZAÇÃO", value=date_updated_br, inline=False)
            embed.add_field(name="ENDEREÇO MAC COMPLETO", value=data.get("macAddressDetails", {}).get("searchTerm", "SEM INFORMAÇÃO"), inline=False)
            embed.add_field(name="VALIDO", value=data.get("macAddressDetails", {}).get("isValid", "SEM INFORMAÇÃO"), inline=False)
            embed.add_field(name="MAQUINA VIRTUAL ATIVA", value=data.get("virtualMachine", {}).get("virtualMachine", "SEM INFORMAÇÃO"), inline=False)
            embed.add_field(name="TRANSMISSÃO", value=data.get("macAddressDetails", {}).get("transmissionType", "SEM INFORMAÇÃO"), inline=False)
            embed.add_field(name="ADMINISTRADOR", value=data.get("macAddressDetails", {}).get("administrationType", "SEM INFORMAÇÃO"), inline=False)
            embed.add_field(name="NOTAS WIRESHARK", value=data.get("macAddressDetails", {}).get("wiresharkNotes", "SEM INFORMAÇÃO"), inline=False)

            embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)             
            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
            
            await ctx.send(embed=embed)

        else:

            embed = discord.Embed(title="")
            embed.set_author(name=f'ERRO AO CONSULTAR O ENDEREÇO MAC {maclookup}', icon_url='')

            await ctx.send(embed=embed)
    except Exception as e: #--------->> SE ENCONTRAR BRANCO OU NULO, RETORNA O COMANDO DO BOT DE "TUTORIAL"
        embed = discord.Embed(title="")

        embed.set_author(name="ㅤㅤCOMANDO DE CONSULTA DE ENDEREÇO MACㅤㅤ") 
        embed.add_field(name="Use o comando: `/maclookup` e a endereço {MAC} que deseja.", value='*Exemplo*: `/maclookup 00:00:5E:00:53:AF`', inline=False)
        embed.add_field(name="Observação:", value='*Pode ser utilizado somente letras maiúscilas e minúsculas*', inline=False)  
        await ctx.send(embed=embed)

@client.command()
async def reverseip(ctx, reverseip):

    view_dns_key = os.getenv("VIEW_DNS_API_KEY")

    url = f"https://api.viewdns.info/reverseip/?host={reverseip}&apikey={view_dns_key}&output=json"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            reverse_ip = data.get('response', {}).get('domains', [])

            embed = discord.Embed(title="", description="")

            for reverse in reverse_ip:

                nome_site = reverse.get('name', 'Desconhecida')
                ultimo_resolve = reverse.get('last_resolved', 'Desconhecido')


                embed.add_field(name=f"NOME DO SITE: {nome_site}", value=f"ÚLTIMO RESOLVER: {ultimo_resolve}", inline=False)


                embed.set_author(name='ㅤㅤㅤㅤREVERSE IP LOOKUP EFETUADO COM SUCESSOㅤㅤㅤ', icon_url='')
                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

            await ctx.send(embed=embed)

        else:

            embed = discord.Embed(title="",)
            embed.add_field(name="", value=f"Ocorreu um erro durante consultar o IP Reverso. Status code: {response.status_code}", inline=False)
            embed.set_author(name='Erro na Resposta da API - ReverseIP Lookup', icon_url='')

            await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(title="")
        embed.add_field(name="", value=f"Ocorreu um erro ao consultar o IP Reverso: {str(e)}", inline=False)
        embed.set_author(name='Erro na Resposta da API - ReverseIP Lookup', icon_url='')

        await ctx.send(embed=embed)

@client.command()
async def traceroute(ctx, traceroute):

    view_dns_key = os.getenv("VIEW_DNS_API_KEY")
    url = f"https://api.viewdns.info/traceroute/?domain={traceroute}&apikey={view_dns_key}&output=json"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            route = data.get('response', {}).get('hops', [])

            embed = discord.Embed(title="", description="")

            for route_info in route:

                numero_id = route_info.get('number', 'Desconhecida')
                hostname = route_info.get('hostname', 'Desconhecido')
                ip_addrs = route_info.get('ip', 'Desconhecido')
                rtt_info = route_info.get('rtt', 'Desconhecido')
                
                embed.add_field(name=f"SERVIDOR N°: {numero_id}", value=f"ENDEREÇO IP: {ip_addrs}\nSERVIDOR: {hostname}\nTEMPO DE IDA E VOLTA (ms): {rtt_info}", inline=False)

                embed.set_author(name='ㅤㅤㅤㅤㅤTRACEROUTE EFETUADO COM SUCESSOㅤㅤㅤㅤ', icon_url='')
                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

            await ctx.send(embed=embed)

        else:

            embed = discord.Embed(title="",)
            embed.add_field(name="", value=f"Ocorreu um erro durante traçar a rota do servidor. Status code: {response.status_code}", inline=False)
            embed.set_author(name='Erro na Resposta da API - Traceroute', icon_url='')

            await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(title="")
        embed.add_field(name="", value=f"Ocorreu um erro ao traçar a rota do servidor: {str(e)}", inline=False)
        embed.set_author(name='Erro na Resposta da API - Traceroute', icon_url='')

        await ctx.send(embed=embed)

@client.command()
async def portscan(ctx, portscan):
    
    view_dns_key = os.getenv("VIEW_DNS_API_KEY")
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

            await ctx.send(embed=embed)

        else:

            embed = discord.Embed(title="",)
            embed.add_field(name="", value=f"ERRO: {response.status_code}", inline=False)
            embed.set_author(name='ERRO NA RESPOSTA DA API - PORTSCAN', icon_url='')

            await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(title="")
        embed.add_field(name="", value=f"ERRO: {str(e)}", inline=False)
        embed.set_author(name='ERRO NA RESPOSTA DA API - PORTSCAN', icon_url='')
        await ctx.send(embed=embed)

@client.command()
async def ping(ctx):

    embed = discord.Embed(title='')

    embed.add_field(name='• Ping do usuário', value=f"{round(client.latency * 500)} ms", inline=False)
    embed.add_field(name='• Ping do servidor', value=f"{round(client.latency * 1000)} ms", inline=False)
    embed.set_author(name='ㅤㅤㅤCONSULTA DE PINGㅤㅤㅤㅤ', icon_url='')
    embed.set_image(url='')
    embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

    await ctx.send(embed=embed)

@client.command()
async def banco(ctx, banco=None):

    if banco is None: #--------->> SE ENCONTRAR BRANCO OU NULO, RETORNA O COMANDO DO BOT DE "TUTORIAL"

        embed = discord.Embed(title='')
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO BANCOㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/banco` e o {CÓDIGO DO BANCO}", value='*Exemplo*: `/banco 237`', inline=False)
        embed.add_field(name="Observação:", value='*Utilize apenas o código bancário correspondente!*', inline=False)
        return await ctx.send(embed=embed)

    try: #--------->> SE ENCONTRAR, RETORNA OS DADOS
        data = requests.get(f"https://brasilapi.com.br/api/banks/v1/{banco}").json() #--------->> API

        embed = discord.Embed(title='')

        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE BANCOㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='') #--------->> TÍTULO DO CÓDIGO

        embed.add_field(name="• ISPB", value=data['ispb'], inline=False)
        embed.add_field(name="• NOME DO BANCO", value=data['name'], inline=False)
        embed.add_field(name="• CÓDIGO DO BANCO", value=data['code'], inline=False)
        embed.add_field(name="• INFORMAÇÕES ADICIONAIS", value=data['fullName'], inline=False)
        embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)

        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
        await ctx.send(embed=embed)

    except Exception: #--------->> SE NÃO ENCONTRAR, RETORNA NÃO ENCONTRADO
        embed = discord.Embed(title='')
        embed.set_author(name='ㅤㅤCÓDIGO BANCÁRIO NÃO ENCONTRADOㅤㅤ', icon_url='')
        return await ctx.send(embed=embed)

@client.command()
async def bin(ctx, bin):

    try:
        data = f"https://lookup.binlist.net/{bin}" #--------->> API

        response = requests.get(data)

        if response.status_code == 200:
            data = response.json()

            embed = discord.Embed(title='')

            embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE BINㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='') #--------->> TÍTULO DO CÓDIGO

            embed.add_field(name="• BIN", value=data.get("{bin}"), inline=False)
            embed.add_field(name="• MODELO", value=data.get("type", "Desconhecido"), inline=False)
            embed.add_field(name="• BANDEIRA", value=data.get("scheme", "Desconhecido"), inline=False)
            embed.add_field(name="• NÍVEL", value=data.get("brand", "Desconhecido"), inline=False)
            embed.add_field(name="• PAÍS", value=data.get("country", {}).get("name", "Desconhecido"), inline=False)
            embed.add_field(name="• SIGLA DO PAÍS", value=data.get("country", {}).get("alpha2", "Desconhecido"), inline=False)
            embed.add_field(name="• BANCO", value=data.get("bank", {}).get("name", "Desconhecido"), inline=False)
            embed.add_field(name="• SITE DO BANCO", value=data.get("bank", {}).get("url", "Desconhecido"), inline=False)
            embed.add_field(name="• TELEFONE", value=data.get("bank", {}).get("phone", "Desconhecido"), inline=False)
            embed.add_field(name="• CIDADE", value=data.get("bank", {}).get("city", "Desconhecido"), inline=False)

            embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)                 
            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

            await ctx.send(embed=embed)
 
        else: #--------->> SE NÃO ENCONTRAR, RETORNA NÃO ENCONTRADO
            embed = discord.Embed(title='') 
            embed.set_author(name='ㅤㅤㅤBIN NÃO ENCONTRADAㅤㅤㅤ', icon_url='')
            await ctx.send(embed=embed)

    except Exception as e: #--------->> SE ENCONTRAR BRANCO OU NULO, RETORNA O COMANDO DO BOT DE "TUTORIAL"

        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO BINㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/bin` e a {BIN} que deseja.", value='*Exemplo*: `/bin 522840`', inline=False)
        embed.add_field(name="Observação:", value='*Não utilize pontos, hifens e caracteres especiais*', inline=False)     

        await ctx.send(embed=embed)

@client.command()
async def site(ctx, site = None):

    data = requests.get(f"http://ipwhois.app/json/{site}").json()

    try:
        embed = discord.Embed(title='')

        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE SITEㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='') #----->> TÍTULO DO CÓDIGO

        embed.add_field(name="• IP", value=data['ip'], inline=False)
        embed.add_field(name="• CIDADE", value=data['city'], inline=False)
        embed.add_field(name="• ESTADO", value=data['region'], inline=False)
        embed.add_field(name="• PAÍS", value=data['country'], inline=False)
        embed.add_field(name="• LATITUDE", value=data['latitude'], inline=False)
        embed.add_field(name="• LONGITUDE", value=data['longitude'], inline=False)
        embed.add_field(name="• ORGANIZAÇÃO", value=data['isp'], inline=False)
        embed.add_field(name="• EMPRESA", value=data['org'], inline=False)
        embed.add_field(name="• FUSO HORÁRIO", value=data['timezone'], inline=False)

        embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)             
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(title='')

    if (site == None): #--------->> SE ENCONTRAR BRANCO OU NULO, RETORNA O COMANDO DO BOT DE "TUTORIAL"
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO SITEㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/site` e a {SITE} que deseja.", value='*Exemplo*: `/site google.com`', inline=False)
        return await ctx.send(embed=embed)
    else: #--------->> SE NÃO ENCONTRAR, RETORNA NÃO ENCONTRADO
       embed.set_author(name='ㅤㅤㅤSITE NÃO ENCONTRADOㅤㅤㅤ', icon_url='')
       return await ctx.send(embed=embed)

@client.command() 
async def operadora(ctx, operadora = None):

    operadora_token = os.getenv("OPERADORA_TOKEN")

    data = requests.get(f"http://apilayer.net/api/validate?access_key={operadora_token}&number={operadora}&country_code=&format=1").json()
    
    try:
        embed = discord.Embed(title='')

        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCHECKER DE OPERADORAㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='') #----->> TÍTULO DO CÓDIGO

        embed.add_field(name="• VÁLIDO", value=data['valid'], inline=False)
        embed.add_field(name="• NÚMERO", value=data['number'], inline=False)
        embed.add_field(name="• FORMATO INTERNACIONAL", value=data['international_format'], inline=False)
        embed.add_field(name="• DDI DO PAÍS", value=data['country_prefix'], inline=False)
        embed.add_field(name="• CÓDIGO DO PAÍS", value=data['country_code'], inline=False)
        embed.add_field(name="• NOME DO PAÍS", value=data['country_name'], inline=False)
        embed.add_field(name="• LOCALIZAÇÃO", value=data['location'], inline=False)
        embed.add_field(name="• OPERADORA/PROVEDOR", value=data['carrier'], inline=False)
        embed.add_field(name="• LINHA DE DISPOSITÍVO", value=data['line_type'], inline=False)

        embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)                
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(title='')

    if (operadora == None): #--------->> SE ENCONTRAR BRANCO OU NULO, RETORNA O COMANDO DO BOT DE "TUTORIAL"
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO OPERADORAㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/operadora` e a {NÚMERO}", value='*Exemplo*: `/operadora +5511987654321`', inline=False)
        embed.add_field(name="Observação:", value='*utilize o padrão universal.*', inline=False)        
        return await ctx.send(embed=embed)
    else: #--------->> SE NÃO ENCONTRAR, RETORNA NÃO ENCONTRADO
       embed.set_author(name='ㅤㅤㅤOPERADORA NÃO ENCONTRADAㅤㅤㅤ', icon_url='')
       return await ctx.send(embed=embed)

@client.command()
async def emailinfo(ctx, emailinfo = None):

    email_token = os.getenv("EMAILINFO_TOKEN")
    data = requests.get(f"http://apilayer.net/api/check?access_key={email_token}&email={emailinfo}&smtp=1&format=1").json()
    
    try:
        embed = discord.Embed(title='')

        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCHECKER DE E-MAILㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='') #----->> TÍTULO DO CÓDIGO

        embed.add_field(name="• E-MAIL", value=data['email'], inline=False)
        embed.add_field(name="• USUÁRIO", value=data['user'], inline=False)
        embed.add_field(name="• DOMÍNIO", value=data['domain'], inline=False)
        embed.add_field(name="• FORMATO VALIDO", value=data['format_valid'], inline=False)
        embed.add_field(name="• CORREIO ATIVO", value=data['mx_found'], inline=False)
        embed.add_field(name="• SMTP DISPONÍVEL", value=data['smtp_check'], inline=False)
        embed.add_field(name="• FUNÇÕES ATIVAS", value=data['role'], inline=False)
        embed.add_field(name="• E-MAIL DISPONÍVEL", value=data['disposable'], inline=False)
        embed.add_field(name="• GRATUITO", value=data['free'], inline=False)
        embed.add_field(name="• PONTUAÇÃO", value=data['score'], inline=False)

        embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)             
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(title='')

    if (emailinfo == None): #--------->> SE ENCONTRAR BRANCO OU NULO, RETORNA O COMANDO DO BOT DE "TUTORIAL"
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO EMAILㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/emailinfo` e a {E-MAIL}", value='*Exemplo*: `/emailinfo google@gmail.com`', inline=False)
        return await ctx.send(embed=embed)
    else: #--------->> SE NÃO ENCONTRAR, RETORNA NÃO ENCONTRADO
       embed.set_author(name='E-MAIL NÃO ENCONTRADO', icon_url='')
       return await ctx.send(embed=embed)
   
@client.command()
async def cotacao(ctx, cotacao = None):

    if cotacao is None: #--------->> SE ENCONTRAR BRANCO OU NULO, RETORNA O COMANDO DO BOT DE "TUTORIAL"
        
        embed = discord.Embed(title='')

        embed.set_author(name='ㅤㅤㅤㅤ   👽 COMANDO COTAÇÃOㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/cotacao` e o {PAR DE MOEDA} que deseja", value='*Exemplo*: `/cotacao BRL-USD`', inline=False)
        embed.add_field(name="Observação:", value='*O par precisa ser separado com hifen*', inline=False)   
        return await ctx.send(embed=embed)

    data = requests.get(f"https://economia.awesomeapi.com.br/last/{cotacao}").json()
    coin_name = cotacao.replace("-", "")

    if coin_name in data:
        
        coin_data = data[coin_name]

        embed = discord.Embed(title='')

        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCOTAÇÃO DE MOEDASㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='') #----->> TÍTULO DO CÓDIGO

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

        embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)             
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
    else:
        embed = discord.Embed(title='')
        embed.set_author(name='ㅤㅤCOTAÇÃO DE MOEDAS INVÁLIDAㅤㅤㅤ', icon_url='')

    embed.set_author(name='ㅤㅤCOTAÇÃO DE MOEDAS INVÁLIDAㅤㅤㅤ', icon_url='')

    await ctx.send(embed=embed)

@client.command() 
async def ddd(ctx, ddd = None):

    if ddd is None: #--------->> SE ENCONTRAR BRANCO OU NULO, RETORNA O COMANDO DO BOT DE "TUTORIAL"
        
        embed = discord.Embed(title='') 
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DDDㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/ddd` e o {DDD} que deseja", value='*Exemplo*: `/ddd 11`', inline=False)
        await ctx.send(embed=embed)
        return

    data = requests.get(f"https://brasilapi.com.br/api/ddd/v1/{ddd}").json() 

    if 'type' in data and data['type'] == 'ddd_error':
        embed = discord.Embed(title='')
        embed.set_author(name='ㅤㅤDDD INVÁLIDO, CIDADE NÃO ENCONTRADAㅤㅤ', icon_url='')
        await ctx.send(embed=embed)
        return

    try:
        embed = discord.Embed(title='')

        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE CIDADES POR DDDㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='') #----->> TÍTULO DO CÓDIGO

        embed.add_field(name="Estado", value=data['state'], inline=False)
        embed.add_field(name="• CIDADES", value=','.join([f"`{city}`" for city in data["cities"]]), inline=False)

        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

        await ctx.send(embed=embed)

    except Exception:
        pass   

@client.command()
async def feriados(ctx, feriados):

    feriados_key = os.getenv("FERIADOS_API_KEY")

    url = f"https://api.invertexto.com/v1/holidays/{feriados}?token={feriados_key}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            embed = discord.Embed(title="")
            
            for feriado in data:
                nome = feriado.get("name", "Desconhecido")
                data_feriado = feriado.get("date", "Desconhecida")
                tipo = feriado.get("type", "Desconhecido")
                level = feriado.get("level", "Desconhecido")
                
                data_br = datetime.strptime(data_feriado, "%Y-%m-%d").strftime("%d/%m/%Y")

                embed.set_author(name=f"ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE FERIADOS {feriados}ㅤㅤㅤㅤㅤㅤㅤㅤ", icon_url='') #----->> TÍTULO DO CÓDIGO

                embed.add_field(name=nome, value=f"DATA: {data_feriado}\nTIPO DE FERIADO: {tipo}\nNÍVEL: {level}", inline=False)
                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

            await ctx.send(embed=embed)

        else: #--------->> SE NÃO ENCONTRAR, RETORNA NÃO ENCONTRADO
            embed = discord.Embed(title='')
            embed.set_author(name=f'ㅤㅤㅤERRO AO CONSULTAR FERIADOS DE {feriados}ㅤㅤㅤ', icon_url='')          

            await ctx.send(embed=embed)

    except Exception as e: #--------->> SE ENCONTRAR BRANCO OU NULO, RETORNA O COMANDO DO BOT DE "TUTORIAL"

        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO FERIADOSㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/feriados` e o {ANO}", value='*Exemplo*: `/feriados 2022`', inline=False)
        embed.add_field(name="Observação:", value='*Suportado entre os anos 1900 e 2199*', inline=False)

        await ctx.send(embed=embed)

@client.command()
async def gerador(ctx):

    embed = discord.Embed(title='')

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤGERADORESㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
    embed.add_field(name="👥 GERADOR DE PESSOA", value="Use o comando `./gerarpessoa` para gerar uma pessoa.",inline=False)
    embed.add_field(name="💳 GERADOR DE CARTÃO", value="Use o comando `./gerarcartao` para gerar um cartão Debito/Crédito.", inline=False)
    embed.add_field(name="📁 GERADOR DE E-MAIL", value="Use o comando `./geraremail` para gerar um e-mail aleatório.", inline=False)
    embed.add_field(name="🔆 GERADOR DE CPF", value="Use o comando `./gerarcpf` para gerar e validar um CPF.", inline=False)
    embed.add_field(name="🎮 GERADOR DE USERNAME", value="Use o comando `./gerarusr` para gerar um username.", inline=False)
    embed.add_field(name="🔐 GERADOR DE SENHA", value="Use o comando `./gerarsenha` para gerar uma senha.", inline=False)
    embed.add_field(name="🚙 GERADOR DE VEÍCULO", value="Use o comando `./gerarveiculo` para gerar um veículo.", inline=False)
    embed.add_field(name="📞 GERADOR DE NÚMERO TELEFONE", value="Use o comando `./gerartel` para gerar um telefone.", inline=False)
    embed.add_field(name="📲 GERADOR DE IMEI", value="Use o comando `./gerarimei` para gerar um IMEI.", inline=False)
    embed.set_footer(text='Whois Alien © All Rights Reserved', icon_url='')

    await ctx.send(embed=embed)
    
@client.command()
async def gerarpessoa(ctx):

    gen_api_key = os.getenv("GEN_DATA_API_KEY")

    data = requests.get(f"https://api.invertexto.com/v1/faker?token={gen_api_key}&locale=pt_BR").json()

    try:
        
        embed = discord.Embed(title='')
    
        embed.add_field(name="• NOME", value=data['name'], inline=False)
        embed.add_field(name="• CPF", value=data['cpf'], inline=False)
        embed.add_field(name="• DATA DE NASCIMENTO", value=data['birth_date'], inline=False)
        embed.add_field(name="• EMAIL", value=data['email'], inline=False)
        embed.add_field(name="• NOME DE USUÁRIO", value=data['username'], inline=False)
        embed.add_field(name="• NÚMERO DE TELEFONE", value=data['phone_number'], inline=False)
        embed.add_field(name="• SITE HOSPEDADO", value=data['domain_name'], inline=False)
        embed.add_field(name="• COMPANHIA", value=data['company'], inline=False)
        embed.add_field(name="• IP REVERSO DE HOSPEDAGEM", value=data['ipv4'], inline=False)
        embed.add_field(name="• NAVEGADOR", value=data['user_agent'], inline=False)
        embed.add_field(name="", value=["`Não garantimos que os dados gerados pelo Bot sejam totalmente verídicos... Podem sim haver dados verdadeiros como podem ser meramente fictícios! Use por sua própria conta e risco.`"], inline=False)
        embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)             
        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤGERADOR DE PESSOAㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(title='')

    if (gerarpessoa == None):
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO GERAR PESSOA', icon_url='')
        embed.add_field(name="Use o comando: `./gerarpessoa` e o bot retornara os dados", value='*Exemplo*: `./gerarpessoa`', inline=False)
        embed.add_field(name="Observação:", value='*NÃO GARANTIMOS QUE OS DADOS FORNECIDOS PELO NOSSO BOT SEJAM VERDADEIROS... PODEM SIM HAVER DADOS VERÍDICOS!USE POR SUA PROPRIA CONTA E RISCO*', inline=False)        
        return await ctx.send(embed=embed)
    else:
       embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UMA PESSOA NO MOMENTOㅤㅤㅤ', icon_url='')
       return await ctx.send(embed=embed)

@client.command()
async def gerarusr(ctx):

    gen_api_key = os.getenv("GEN_DATA_API_KEY")

    data = requests.get(f"https://api.invertexto.com/v1/faker?token={gen_api_key}&locale=pt_BR").json()

    try:

        embed = discord.Embed(title='')

        embed.set_author(name='GERADOR DE USERNAME', icon_url='')

        embed.add_field(name="USERNAME GERADO COM SUCESSO", value=data['username'], inline=False)
        embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)             
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(title='')

    if (gerarpessoa == None):
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO GERAR USERNAME', icon_url='')
        embed.add_field(name="Use o comando: `./gerarusr` e o bot retornara o user gerado", value='*Exemplo*: `./gerarusr`', inline=False)
        return await ctx.send(embed=embed)
    else:
       embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM USER NO MOMENTOㅤㅤㅤ', icon_url='')
       return await ctx.send(embed=embed)


@client.command()
async def geraremail(ctx):

    gen_api_key = os.getenv("GEN_DATA_API_KEY")

    data = requests.get(f"https://api.invertexto.com/v1/faker?token={gen_api_key}&locale=pt_BR").json()

    try:

        embed = discord.Embed(title='')

        embed.set_author(name='GERADOR DE EMAIL', icon_url='')

        embed.add_field(name="EMAIL GERADO COM SUCESSO", value=data['email'], inline=False)
        embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)             
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(title='')

    if (gerarpessoa == None):
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO GERAR EMAIL', icon_url='')
        embed.add_field(name="Use o comando: `./geraremail` e o bot retornara o email gerado", value='*Exemplo*: `./geraremail`', inline=False)
        return await ctx.send(embed=embed)
    else:
       embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM EMAIL NO MOMENTOㅤㅤㅤ', icon_url='')
       return await ctx.send(embed=embed)


@client.command()
async def gerartel(ctx):

    gen_api_key = os.getenv("GEN_DATA_API_KEY")

    data = requests.get(f"https://api.invertexto.com/v1/faker?token={gen_api_key}&locale=pt_BR").json()

    try:

        embed = discord.Embed(title='')

        embed.set_author(name='GERADOR DE TELEFONE', icon_url='')

        embed.add_field(name="TELEFONE GERADO COM SUCESSO", value=data['phone_number'], inline=False)
        embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)             
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(title='')

    if (gerarpessoa == None):
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO GERAR TELEFONE', icon_url='')
        embed.add_field(name="Use o comando: `./gerartel` e o bot retornara o telefone gerado", value='*Exemplo*: `./gerartel`', inline=False)
        return await ctx.send(embed=embed)
    else:
       embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM TELEFONE NO MOMENTOㅤㅤㅤ', icon_url='')
       return await ctx.send(embed=embed)

@client.command()
async def gerarcpf(ctx):

    gen_api_key = os.getenv("GEN_DATA_API_KEY")

    data = requests.get(f"https://api.invertexto.com/v1/faker?token={gen_api_key}&locale=pt_BR").json()

    try:

        embed = discord.Embed(title='')

        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤGERADOR DE CPF', icon_url='')

        embed.add_field(name="CPF GERADO COM SUCESSO", value=data['cpf'], inline=False)
        embed.add_field(name="", value='Não garantimos que o CPF gerado pelo Bot sejam totalmente verídicos... Grande parte dos CPFs gerados são sim verdadeiros, porém pode haver a possibilidade de ALGUNS não serem reais. `Não nos responsabilizamos pelos seus atos.`', inline=False)
        embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)             
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(title='')

    if (gerarpessoa == None):
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO GERAR CPF', icon_url='')
        embed.add_field(name="Use o comando: `./gerarcpf` e o bot retornara o CPF gerado", value='*Exemplo*: `./gerarcpf`', inline=False)
        embed.add_field(name="Observação", value='`Não garantimos que o CPF gerado pelo Bot sejam totalmente verídicos... Grande parte dos CPFs gerados são sim verdadeiros, porém pode haver a possibilidade de ALGUNS não serem reais. *Não nos responsabilizamos pelos seus atos.*`', inline=False)
        return await ctx.send(embed=embed)
    else:
       embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM CPF NO MOMENTOㅤㅤㅤ', icon_url='')
       return await ctx.send(embed=embed)

@client.command()
async def gerarcartao(ctx):

    gen_api_key = os.getenv("GEN_DATA_API_KEY")

    data = requests.get(f"https://api.invertexto.com/v1/faker?token={gen_api_key}&locale=pt_BR").json()

    random_numbers = [random.randint(100, 999) for _ in range(1)]
    
    for i, num in enumerate(random_numbers, start=1):

        embed = discord.Embed(title='')

        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤGERADOR DE CARTÃO', icon_url='')

        embed.add_field(name="NÚMERO DO CARTÃO", value=data.get("credit_card", {}).get("number", "DESCONHECIDO"), inline=False) 
        embed.add_field(name="DATA DE EXPIRAÇÃO", value=data.get("credit_card", {}).get("expiration", "DESCONHECIDO"), inline=False)
        embed.add_field(name="BANDEIRA DO CARTÃO", value=data.get("credit_card", {}).get("type", "DESCONHECIDO"), inline=False)
        embed.add_field(name="NOME IMPRESSO NO CARTÃO", value=data.get("credit_card", {}).get("name", "DESCONHECIDO"), inline=False)
        embed.add_field(name="CVV DO CARTÃO", value=num, inline=True)
        embed.add_field(name="", value='`Não garantimos que os cartões gerado pelo Bot seja autêntico ou que seja Débito/Crédito! Não nos responsabilizamos pelos seus atos! Qualquer semelhança é mera coincidência.`', inline=False)
        
        embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)             
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

        await ctx.send(embed=embed)

@client.command()
async def gerarsenha(ctx, length=12):

    if 4 <= length <= 32:

        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        
        embed = discord.Embed(title="")

        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤGERADOR DE SENHAS', icon_url='')
        embed.add_field(name="SENHA GERADA", value=password, inline=False)
        embed.add_field(name="", value="Para garantir a segurança de suas contas online, é altamente recomendável o uso de senhas geradas aleatoriamente e exclusivas para cada serviço que você utiliza. Evite senhas óbvias, como datas de nascimento ou sequências de números comuns, e opte por senhas mais complexas que combinem letras maiúsculas, minúsculas, números e caracteres especiais. Além disso, ative a autenticação de dois fatores sempre que possível, mantenha seus dispositivos e software atualizados e seja cauteloso ao clicar em links suspeitos. A segurança online é fundamental para proteger sua identidade e informações pessoais.", inline=False)

        embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)             
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
        
        await ctx.send(embed=embed)
    else:
        await ctx.send("O comprimento da senha deve estar entre 4 e 32 caracteres.")

@client.command()
async def tradutor(ctx):    

    embed = discord.Embed(title='')
    
    embed.set_author(name='ㅤㅤㅤCOMANDO PARA TRADUÇÃOㅤㅤㅤㅤ', icon_url='')

    embed.add_field(name="Use o comando: `/traduzir sigla da lingua (ou a lingua em inglês) + [TEXTO]`", value='*Exemplo 1*: `/traduzir pt Hello, World!`\n*Exemplo 2*: `/traduzir spanish Hello friend, you are very beautiful!`', inline=False)
    embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

    await ctx.send(embed=embed)

@client.command()
async def traduzir(ctx, target_language, *, text):

    translator = Translator()

    try:

        translation = translator.translate(text, dest=target_language)
        translated_text = translation.text

        embed = discord.Embed(title="")

        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤTRADUÇÃO DE TEXTOㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

        embed.add_field(name="", value="", inline=False)
        embed.add_field(name=f"TEXTO TRADUZIDO PARA ({target_language})", value="", inline=False)
        embed.add_field(name="", value=translated_text, inline=False)
        embed.add_field(name="", value="", inline=False)

        embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)             
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

        await ctx.send(embed=embed)

    except Exception as e:

        embed = discord.Embed(title="")
        embed.set_author(name=f"ERRO AO TRADUZIR TEXTO. {str(e)}", icon_url='')

        await ctx.send(embed=embed)

@client.command()
async def criador(ctx):

    embed = discord.Embed(title='')

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤSOBRE O CRIADOR DO BOTㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

    embed.add_field(name="ㅤ", value='O criador do Bot não é nada mais que uma pessoa entusiasta em segurança da informação e programação. Tem uma idade/nome e localidade desconhecida pelas pessoas que não são próximas. Saúdem o Rei alien. ', inline=False) 

    embed.set_image(url="https://i.imgur.com/GAw2sJ4.jpg")
    embed.set_footer(text='Whois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

    await ctx.send(embed=embed)





bot_token = os.getenv("BOT_TOKEN")
client.run(bot_token)


