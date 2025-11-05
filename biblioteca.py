biblioteca = dic()t

while True:
    print("Sistema de Biblioteca Pessoal")
    print("1 - Adicionar livro")
    print("2 - Consultar livro")
    print("3 - Atualizar páginas")
    print("4 - Remover livro")
    print("5 - Listar todos os livros")
    print("6 - Contar livros")
    print("7 - Sair")
    print("-"*30)
    opcao = int(input("Escolha uma opcão: "))
    
    if  opcao == 1:
        try:
            livro = input("Qual o nome do livro? ")
            biblioteca[livro] = int(input(f"Quantas páginas possui o {livro}? "))
            
            print("Livro adicionado com sucesso!")
            print(biblioteca)
            
        except Exception:
            print(f"Erro! Não foi possível adicionar o livro {livro}")
    
    elif opcao == 2:
        for chave in biblioteca.keys():
            try:
                input("Digite o nome do livro")
                print(f"{chave}")
            except Exception:
                print(f"Esse livro {chave} não está adicionado na biblioteca")
