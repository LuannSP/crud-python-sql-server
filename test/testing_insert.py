import sys
sys.path.append("C:\\Users\\luann\\Documents\\Python\\crud")
from database.crud import insert

i = insert("Aluno", "Nome, DataNascimento", "'Luann', '2000/12/31'")

if i:
    print("add com sucesso!")
else:
    print('verifica as colunas e tabelas insert')
    