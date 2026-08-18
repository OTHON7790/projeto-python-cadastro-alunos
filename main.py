alunos = []

while True:
    print("\n=== SISTEMA DE CADASTRO DE ALUNOS ===")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
    print("4 - Excluir aluno")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        idade = input("Digite a idade do aluno: ")
        curso = input("Digite o curso do aluno: ")

        aluno = {
            "nome": nome,
            "idade": idade,
            "curso": curso
        }

        alunos.append(aluno)

        print("Aluno cadastrado com sucesso!")
    elif opcao == "2":
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            print("\n=== LISTA DE ALUNOS ===")

            for aluno in alunos:
                print("Nome:", aluno["nome"])
                print("Idade:", aluno["idade"])
                print("Curso:", aluno["curso"])
                print("--------------------")
                    elif opcao == "3":
        nome_busca = input("Digite o nome do aluno que deseja buscar: ")

        encontrado = False

        for aluno in alunos:
            if aluno["nome"].lower() == nome_busca.lower():
                print("\nAluno encontrado:")
                print("Nome:", aluno["nome"])
                print("Idade:", aluno["idade"])
                print("Curso:", aluno["curso"])

                encontrado = True
                break

        if not encontrado:
            print("Aluno não encontrado.")
    elif opcao == "5":
        print("Programa encerrado.")
        break
