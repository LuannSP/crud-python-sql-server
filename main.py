from database.crud import *

while True:

    print("""
1 - Exibir todos os alunos(as)
2 - Adicionar um aluno(a)
3 - Remover um aluno(a)
4 - Atulizar dados de um aluno(a)
""")
    try:
        option = int(input("Digite: "))
        if option > 4:
            raise ValueError
    except ValueError:
        print("Tente novamente, somente valores de 1 a 4.")
        continue

    if option == 1:
        list = read("Matricula, Nome, DataNascimento", "Aluno")
        if list is None:
            print("\nSeu banco de dados está vazio.")
            continue
        print(f"\n| Exibindo {list.__len__()} alunos(as) |\n")
        for count, i in enumerate(list, 1):
            print(
                f"{count}: | Matricula: {i[0]} | Nome: {i[1]} | DataNascimento: {i[2]} |")
