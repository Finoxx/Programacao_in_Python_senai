import sqlite3

conn  = sqlite3.connect('meu_banco.db')
cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS dados(
                
#                 nome TEXT,
#                 email TEXT,
#                 idade TEXT,
#                endereco TEXT,
#                trabalho TEXT,
#                graduacao TEXT
               
#                )''')
# conn.commit()



# nome  =  input('nome: ')
# idade  =  input('idade: ')
# email = input('e-mail:')
# endereco = input('endereco: ')
# trabalho = input('trabalho: ')
# graduacao = input('graduacao: ')

# cursor.execute('INSERT INTO dados VALUES(?,?,?,?,?,?)', (nome, idade,email,endereco,trabalho,graduacao))
# conn.commit()


cursor.execute('SELECT 0 FROM dados')
dados  =  cursor.fetchall()
print(dados[0][0])



conn.close()