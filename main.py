from student import student

while True:

    print("\n1 - Exibir todos os alunos(as)\n2 - Adicionar um aluno(a)\n3 - Remover um aluno(a)\n4 - Atualizar dados de um aluno(a)\n")

    try:
        option = int(input("Digite: "))
        if option > 4 or option < 1:
            raise ValueError
    except ValueError:
        print("\nTente novamente, somente valores de 1 a 4.")
    else:
        if option == 1:
            student.readStudent()
        elif option == 2:
            student.addStudent()
        elif option == 3:
            student.removeStudent()
        else:
            student.updateStudent()
