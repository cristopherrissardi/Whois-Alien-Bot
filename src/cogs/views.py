import discord
from discord.ext import commands


class ViewCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command() 
    async def termos(self, ctx):

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

        await ctx.reply(embed=embed)

    @commands.command() 
    async def regras(self, ctx):

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

        await ctx.reply(embed=embed)


    @commands.command()
    async def ajuda(self, ctx):

        embed = discord.Embed(title='ㅤㅤㅤㅤㅤㅤㅤㅤㅤWhois Alienㅤㅤㅤㅤㅤㅤㅤㅤ')
        embed.add_field(name="ㅤ", value='Olá, estou aqui para te ajudar! Aqui está algum dos comandos que o `Whois Alien` possui. Ficou com alguma dúvida em relação aos comandos abaixo? Digite `/[NOME DO COMANDO]`. Exemplo: `./admin`\n\nOBS: Grande parte das consultas de dados como: nome, cpf, cpf2, telefone, mãe, pai e email estão sendo hospedados em meu computador pessoal, no entanto, os comandos só irão funcionar quando o ALIEN estiver online. Parte da madrugada não irá funcionar as consultas, infelizmente! Desde já peço mil desculpas pelo transtorno e tudo será resolvido, ou melhor, normalizado. \n\n', inline=False)
        embed.add_field(name="🔐 Moderação", value='Use o comando `./admin` para ver os comandos administrativos. Comando de moderação existentes: `./kick`, `./ban`, `./unban`, `./unmute`, `./role`, `./mute`, `./clear` `\n\n (OS COMANDOS ADMINISTRATIVOS SÓ FUNCIONARÃO PARA PESSOAS COM CARGOS AUTORIZADOS)`', inline=False)
        embed.add_field(name="🛠️ Ferramentas Avançadas", value='Use o comando `./ferramentas` para obter mais informações. Ferramentas disponíveis: `./portscan`, `./traceroute`, `./whois`', inline=False)
        embed.add_field(name="🧭 Consulta de Dados", value='Use o comando `./consultas` para obter mais informações sobre a aba de consulta de dados. Consultas disponíveis: `./nome`, `./cpf`, `./cpf0`, `./telefone`, `./fixo`, `./cep_pessoas`, `./email`, `./mae`, `./pai`, `./cnpj`, `./placa [NÃO ESTÁ FUNCIONANDO NO MOMENTO]`, `./ip`, `./bin`, `./cep`, `./covid`, `./banco`, `./site`, `./operadora`, `./emailinfo` e possivelmente outros entrem nessa lista futuramente. ', inline=False)
        embed.add_field(name="⚙️ Geradores", value='Use o comando `./gerador` para obter mais informações. Ferramentas disponíveis: `./gerarpessoa`, `./gerarcartao`, `./geraremail`, `./gerarcpf`, `./gerarusr`, `./gerarsenha`, `./gerarveiculo`, `./gerartel`, `./gerarimei`', inline=False)
        embed.add_field(name="🎵 Músicas", value='Use o comando `./musica` para vizualizar os comandos. Comandos acessíveis a classe: `./play`, `./stop`, `./pause`, `./resume`, `./back`, `./skip`, `./disconnect` `\n\n (OS MENUS DE MÚSICAS AINDA NÃO FORAM IMPLEMENTADOS)`', inline=False)
        embed.add_field(name="🪐 Informações", value='Use o comando `./info` para ver os comandos disponíveis. Comandos existentes: `./ajuda`, `./ping`, `./serverinfo`, `./userinfo`', inline=False)
        embed.add_field(name="OBS:", value='`O BOT AINDA ESTÁ EM DESENVOLVIMENTO!, POR ESSE MOTIVO ALGUNS COMANDOS AINDA NÃO FORAM CORRIGIDOS OU IMPLEMENTADOS.`', inline=False)
        embed.set_image(url="https://i.imgur.com/GAw2sJ4.jpg")
        embed.set_footer(text='Whois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

        await ctx.author.send(embed=embed)


    @commands.command()
    async def admin(self, ctx):

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

        await ctx.reply(embed=embed); 


    @commands.command()
    async def consultas(self, ctx):

        embed = discord.Embed(title='',)

        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE DADOSㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

        embed.add_field(name="*Consulta de dados*", value="", inline=False)
        embed.add_field(name="🕵🏻‍♂️ Consulta por Nome", value="Use o comando `./nome` {NOME COMPLETO} para realizar a consulta de dados através do nome completo do indivíduo.", inline=False)
        embed.add_field(name="👽 Consulta por CPF básico", value="Use o comando `./cpf0` {CPF DA PESSOA} para a consultar os dados básicos.", inline=False)
        embed.add_field(name="🔍 Consulta por CPF completo", value="Use o comando `./cpf` {CPF DA PESSOA} para a consultar os dados completa.", inline=False)
        embed.add_field(name="📳 Consulta por Telefone", value="Use o comando `./telefone` {TELEFONE} para realizar a consulta dos dados do proprietário da linha telefonica.", inline=False)
        embed.add_field(name="💎 Consulta por Telefone fixo", value="Use o comando `./fixo` {TELEFONE} para realizar a consulta dos dados do proprietário da linha telefonica fixa (RESIDÊNCIAL).", inline=False)
        embed.add_field(name="📮 Consulta por E-mail", value="Use o comando `./email` {EMAIL} para realizar a consulta dos dados do proprietário do email (SE DISPONÍVEL).", inline=False)
        embed.add_field(name="📑 Consulta por CEP para pessoas", value="Use o comando `./cep_pessoas` {CEP DA RUA} para realizar a consulta de todos os indivíduos que moram na respectiva rua.", inline=False)
        embed.add_field(name="👩‍👦 Consulta de filhos pelo Nome da mãe", value="Use o comando `./mae` {NOME DA MÃE} para realizar a consulta dos dados dos filhos pelo nome da mãe.", inline=False)
        embed.add_field(name="👨‍👦 Consulta de filhos pelo Nome do pai", value="Use o comando `./pai` {NOME DO PAI} para realizar a consulta dos dados dos filhos pelo nome do pai.", inline=False)
        embed.add_field(name="🚘 Consulta de Placa", value="Use o comando `./placa` {PLACA DO VEÍCULO} para realizar a consulta de veículo.", inline=False)
        embed.add_field(name="🏨 Consulta por CNPJ", value="Use o comando `./cnpj` {CNPJ} para consultar de CNPJ completa.", inline=False)

        embed.add_field(name="Consulta de dados/ferramentas", value="", inline=False)
        embed.add_field(name="📌 Consulta de IP", value="Use o comando `./ip` {IP} para realizar a consulta do IP.", inline=False)
        embed.add_field(name="💳 Consulta de BIN", value="Use o comando `./bin` {NÚMERO DA BIN} para realizar a consulta.", inline=False)
        embed.add_field(name="📫 Consulta por CEP", value="Use o comando `./cep` {CEP DA RUA} para realizar a consulta.", inline=False)
        embed.add_field(name="🦠 Consulta de Covid19", value="Use o comando `./covid` {SIGLA DO ESTADO} para realizar a consulta.", inline=False)
        embed.add_field(name="🏦 Consulta de Banco", value="Use o comando `./banco` {CÓDIGO DO BANCO} para realizar a consulta.", inline=False)
        embed.add_field(name="💾 Consulta de Site", value="Use o comando `./site` {URL DO SITE} para realizar a consulta.", inline=False)
        embed.add_field(name="📴 Consulta de Operadora", value="Use o comando `./operadora` {NÚMERO DE CELULAR} para realizar a consulta.", inline=False)    
        embed.add_field(name="🤖 Consulta de Info-email", value="Use o comando `./emailinfo` {EMAIL} para realizar a consulta.", inline=False)
        embed.add_field(name="💰 Consulta de cotação de moedas", value="Use o comando `./cotacao` {PAR DE MOEDA} para realizar a consulta.", inline=False)
        embed.add_field(name="🏙️ Consulta de cidades por DDD", value="Use o comando `./ddd` {DDD} para realizar a consulta do DDD por cidades.", inline=False)
        embed.add_field(name="🌐 Consulta Whois básica", value="Use o comando `./whois` {NOME DO DOMÍNIO} para realizar a consulta de Whois.", inline=False)

        embed.set_image(url='https://i.gifer.com/Cewn.gif')
        embed.set_footer(text='Whois Alien © All Rights Reserved', icon_url='')

        await ctx.reply(embed=embed)


    @commands.command()
    async def gerador(self, ctx):

        embed = discord.Embed(title='')

        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤGERADORESㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
        embed.add_field(name="👥 Gerador de Pessoas", value="Use o comando `./gerar_pessoa` para gerar uma pessoa fictícia.",inline=False)
        embed.add_field(name="💳 Gerador de Cartão", value="Use o comando `./gerar_cartao` para gerar um cartão Debito/Crédito fictício.", inline=False)
        embed.add_field(name="🔆 Gerador de CPF", value="Use o comando `./gerar_cpf` para gerar e validar um CPF fictício.", inline=False)
        embed.add_field(name="🎮 Gerador de Username", value="Use o comando `./gerar_usr` para gerar um username.", inline=False)
        embed.add_field(name="🔐 Gerador de senhas", value="Use o comando `./gerar_senha` para gerar uma senha.", inline=False)
        embed.add_field(name="📞 Gerador de número de telefone", value="Use o comando `./gerar_tel` para gerar um telefone fictício.", inline=False)
        embed.add_field(name="🪪 Gerador de RG", value="Use o comando `./gerar_rg` para gerar um RG.", inline=False)
        embed.add_field(name="📱 Gerador de User Agent", value="Use o comando `./gerar_agent` para gerar um User Agent de um navegador.", inline=False)
        embed.add_field(name="📫 Gerador de E-mail", value="Use o comando `./gerar_email` para gerar um e-mail.", inline=False)
        embed.add_field(name="📲 Gerador de Passaporte", value="Use o comando `./gerar_passaporte` para gerar um passaporte fictício.", inline=False)
        embed.add_field(name="📜 Gerador de Texto", value="Use o comando `./gerar_texto` para gerar um Texto convencional.", inline=False)
        embed.add_field(name="💾 Gerador de IP", value="Use o comando `./gerar_ip` para gerar um IP.", inline=False)
        embed.add_field(name="💻 Gerador de MAC Address", value="Use o comando `./gerar_mac para gerar um endereço MAC", inline=False)
        embed.add_field(name="🌐 Gerador de URL", value="Use o comando `./gerarg` para gerar um RG.", inline=False)
        embed.add_field(name="📍 Gerador de Coordenadas", value="Use o comando `./gerar_coordenadas` para gerar um Coordenada Geogŕaficas aleatória.", inline=False)
        embed.add_field(name="📆 Gerador de Data", value="Use o comando `./gerar_data` para gerar uma Data Aleatória.", inline=False)
        embed.add_field(name="🏬 Gerador de CNPJ", value="Use o comando `./gerar_cnpj` para gerar um CNPJ.", inline=False)
        embed.add_field(name="🔮 Gerador de Cor", value="Use o comando `./gerar_cor` para gerar uma cor Aleatória.", inline=False)
        embed.add_field(name="🚗 Gerador de Placa", value="Use o comando `./gerar_placa` para gerar uma Placa.", inline=False)
    
        embed.set_footer(text='Whois Alien © All Rights Reserved', icon_url='')

        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(ViewCommands(bot))

