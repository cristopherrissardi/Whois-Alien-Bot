import json
import sqlite3

# Caminhos dos arquivos
json_file = 'all_categories.json'       # Coloque o nome do seu arquivo JSON aqui
db_file = 'Games.db'           # Nome do banco SQLite

# Carregar JSON
with open(json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Conectar ao SQLite
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Criar tabela (se não existir)
cursor.execute('''
CREATE TABLE IF NOT EXISTS TB_GAMES (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    magnet_link TEXT,
    upload_date TEXT,
    file_size TEXT,
    repack_link TEXT
)
''')

# Inserir dados
for item in data['downloads']:
    title = item.get('title')
    magnet = item.get('uris', [None])[0]  # Primeiro magnet da lista
    upload_date = item.get('uploadDate')
    file_size = item.get('fileSize')
    repack = item.get('repackLinkSource')

    cursor.execute('''
    INSERT INTO TB_GAMES (title, magnet_link, upload_date, file_size, repack_link)
    VALUES (?, ?, ?, ?, ?)
    ''', (title, magnet, upload_date, file_size, repack))

# Salvar e fechar
conn.commit()
conn.close()

print("Importação concluída com sucesso!")
