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

    elif opcao == "5":
        print("Programa encerrado.")
        break
