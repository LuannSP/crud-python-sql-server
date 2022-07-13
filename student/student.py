from database.crud import delete, read, insert, returnExists, update
import datetime

_attempt: int = 0 

def convertDate(date: str) -> str:
    date = datetime.datetime.strptime(date, "%d/%m/%Y")
    date = str(f"{date.year}/{date.month}/{date.day}")
    return date


def readStudent() -> None:
    command = read("Matricula, Nome, DataNascimento", "Aluno")
    if command is None:
        print("\nSeu banco de dados está vazio.")
        return
    print(f"\n| Exibindo {command.__len__()} alunos(as) |\n")
    for count, i in enumerate(command, 1):
        print(f"{count}: | Matricula: {i[0]} | Nome: {i[1]} | Data de nascimento: {i[2]} |")


def addStudent() -> None:
    try:
        name = str(input("Digite o nome do novo aluno(a): "))
        date = input("Digite a data de nascimento do novo aluno(a): ")
        date = convertDate(date)
        if name == "":
            raise ValueError
    except ValueError:
        global _attempt
        if _attempt == 2:
            print("\nTente novamente, retornando opções.")
            return
        print("\nTente novamente, exemplo:\n * Nome: Nome do aluno\n * Data de nascimento: 00/00/0000\n")
        _attempt += 1
        addStudent()
    else:
        command = insert("Aluno", "Nome, DataNascimento", f"'{name}','{date}'")
        if command:
            print(f"\nO aluno(a): '{name}' foi adicionado.")


def removeStudent() -> None:
    registration = str(input("Digite a matricula do aluno: "))
    if not returnExists("Matricula", "Aluno", "Matricula", f"{registration}"):
        print(f"\nO aluno(a) com a matricula '{registration}' não existe.")
        return
    command = delete("Aluno", "Matricula", f"{registration}")
    if command:
        print(f"\nO aluno(a) com a matricula '{registration}' foi removido(a).")


def updateStudent() -> None:
    registration = str(input("Digite a matricula do aluno: "))
    if not returnExists("Matricula", "Aluno", "Matricula", f"{registration}"):
        print(f"\nO aluno(a) com a matricula '{registration}' não existe.")
        return
    print("\n1 - Alterar o nome do aluno(a)\n2 - Alterar a data de nascimento\n")
    try:
        option = int(input("Digite: "))
        if not 0 < option < 3:
            raise ValueError
    except ValueError:
        print("\nTente novamente, somente 1 ou 2.")
        return
    if option == 1:
        try:
            newName = str(input("Digite o novo nome: "))
            if newName == "":
                raise ValueError
        except ValueError:
            print(f"\nTente novamente, exemplo:\nNome: Nome do aluno")
            return
        command = update("Aluno", "Nome", f"{newName}", "Matricula", f"{registration}")
        if command:
            print(f"\nO aluno(a) com a matricula '{registration}', teve o nome alterado para '{newName}'")
    else:
        try:
            newDate = input("Digite a nova data de nascimento: ")
            newDate = convertDate(newDate)
        except ValueError:
            print("\nTente novamente, exemplo:\nData de nascimento: 00/00/0000")
            return
        command = update("Aluno", "DataNascimento",f"{newDate}", "Matricula", f"{registration}")
        if command:
            print(f"\nO aluno(a) com a matricula '{registration}', teve a sua data de nascimento alterada para '{newDate}'")

