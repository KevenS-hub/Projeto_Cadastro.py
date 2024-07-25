import sqlite3 as lite

con = lite.connect('dados.db')

dados = ['vaso','sala de estar', 'vaso que comprei na Shein', 'Marca X', '25/07/2024', '100', 'xxxxx', 'c:imagens']

# inserir dados
with con:
    cur = con.cursor()
    query = "INSERT INTO inventorio(nome, local, descricao, marca, data_da_compra, valor_da_compra, serie, imagem) VALUES(?,?,?,?,?,?,?,?)"
    cur.execute(query,dados)


ver_dados = []

# visualizar dados
with con:
    cur = con.cursor()
    query = "SELECT * FROM inventorio"
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        ver_dados.append(row)

print(ver_dados)
