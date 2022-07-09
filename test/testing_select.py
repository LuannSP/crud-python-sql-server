import sys
sys.path.append("C:\\Users\\luann\\Documents\\Python\\crud")
from database.crud import read

r = read('Nome, DataNascimento, Matricula', 'Aluno')

if r:
    for i in r:
        print(
            f"| Nome: {i[0]} | DataNascimento: {i[1]} | Matricula: {i[2]} |")
elif r is None:
    print('nao ha dados para exibir')
else:
    print('verifique as colunas e tabela select')
