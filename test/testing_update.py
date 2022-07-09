import sys
sys.path.append("C:\\Users\\luann\\Documents\\Python\\crud")
from database.crud import update

u = update('Aluno', 'Nome', 'Maria', '2022.1030')

if u:
    print("dado atualizado")
else:
    print('verifique a tabela e as colunas')