from database.crud import delete, read, insert, returnExists
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
        command = read("Matricula, Nome, DataNascimento", "Aluno")
        if command is None:
            print("\nSeu banco de dados está vazio.")
            continue
        print(f"\n| Exibindo {command.__len__()} alunos(as) |\n")
        for count, i in enumerate(command, 1):
            print(f"{count}: | Matricula: {i[0]} | Nome: {i[1]} | Data de nascimento: {i[2]} |")

    if option == 2:
        try:
            name = str(input("Digite o nome do novo aluno(a): "))
            date = input("Digite a data de nascimento do novo aluno(a): ")
            date = datetime.datetime.strptime(date, "%d/%m/%Y")
            date = str(f"{date.year}/{date.month}/{date.day}")
            command = insert("Aluno", "Nome, DataNascimento", f"'{name}','{date}'")       
            if command:
                print(f"\nO aluno(a): {name} foi adicionado.")
        except ValueError:
            print("\nTente novamente, exemplo:\nNome: Nome do aluno\nData de nascimento: 00/00/0000")
            continue
    
    if option == 3:
        registration = str(input("Digite a matricula do aluno: "))
        if returnExists("matricula", "Aluno", "Matricula", f"{registration}"):            
            command = delete("Aluno", "Matricula", f"{registration}")
            if command:
                print(f"\nO aluno(a) com a matricula {registration} foi removido(a).")
            else:
                print('error')
        else:
            print(f"\nO aluno(a) com a matricula {registration} não existe.")