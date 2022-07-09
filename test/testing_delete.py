import sys
sys.path.append("C:\\Users\\luann\\Documents\\Python\\crud")
from database.crud import delete

d = delete('Aluno', '2022.1010')

if d:
    print("deletado com sucesso!")
else:
    print("verifique a tabela e as colunas")