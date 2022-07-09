from database.crud import *
import datetime

while True:
    print("""
1 - Exibir todos os alunos(as)
2 - Adicionar um aluno(a)
3 - Remover um aluno(a)
4 - Atualizar dados de um aluno(a)
""")

    try:
        option = int(input("Digite: "))
        if option > 4:
            raise ValueError
    except ValueError:
        print("\nTente novamente, somente valores de 1 a 4.")
        continue

    if option == 1:
        list = read("Matricula, Nome, DataNascimento", "Aluno")
        if list is None:
            print("\nSeu banco de dados está vazio.")
            continue
        print(f"\n| Exibindo {list.__len__()} alunos(as) |\n")
        for count, i in enumerate(list, 1):
            print(f"{count}: | Matricula: {i[0]} | Nome: {i[1]} | DataNascimento: {i[2]} |")

    if option == 2:
        try:
            name = str(input("Digite o nome do novo aluno(a): "))
            date = input("Digite a data de nascimento do novo aluno(a): ")
            date = datetime.datetime.strptime(date, "%d/%m/%Y")
            date = str(f"{date.year}/{date.month}/{date.day}")
            if type(name) != type(str):
                raise ValueError
            command = insert("Aluno", "Nome, DataNascimento", "'{}','{}'".format(name, date))            
            if command:
                print(f"O aluno(a): {name} foi adicionado.")
        except ValueError:
            print("\nTente novamente, exemplo:\nNome: Nome do aluno\nData de nascimento: 00/00/0000")
            continue