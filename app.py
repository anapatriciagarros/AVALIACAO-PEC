# ============================================================
# SISTEMA DE CONTROLE DE ESTOQUE COM CRUD
# Integração dos paradigmas Imperativo e Funcional
# ============================================================
#
# Para o usuário final, este é apenas um sistema único.
# Internamente, o código foi separado em:
#
# PARTE 01 - Paradigma Funcional:
# - Funções puras
# - Imutabilidade
# - Funções de ordem superior
# - Evita efeitos colaterais
#
# PARTE 02 - Paradigma Imperativo:
# - Variável mutável de estado
# - Estruturas de controle
# - Entrada e saída de dados
# - Manipulação sequencial do fluxo do programa
#
# ============================================================


# ============================================================
# PARTE 01 - PARADIGMA FUNCIONAL
# ============================================================
# Aqui ficam as regras do sistema.
# As funções recebem dados e retornam novos dados.
# Elas não usam input(), print() nem alteram diretamente o estoque.
# ============================================================

def criar_produto(codigo, nome, quantidade, preco):
    """
    Função pura:
    Recebe os dados do produto e retorna um novo dicionário.
    Não altera nenhuma variável externa.
    """
    return {
        "codigo": codigo,
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }


def adicionar_produto(estoque, produto):
    """
    Função pura com imutabilidade:
    Não usa append().
    Retorna uma nova lista contendo o produto adicionado.
    """
    return estoque + [produto]


def buscar_produto(estoque, codigo):
    """
    Função pura:
    Usa filter para buscar produtos pelo código.
    Retorna uma lista com os produtos encontrados.
    """
    return list(
        filter(
            lambda produto: produto["codigo"] == codigo,
            estoque
        )
    )


def atualizar_produto(estoque, codigo, novo_nome, nova_quantidade, novo_preco):
    """
    Função pura:
    Usa map para percorrer o estoque e gerar uma nova lista.
    Se encontrar o produto pelo código, retorna uma nova versão dele.
    Caso contrário, mantém o produto original.
    """

    def atualizar(produto):
        if produto["codigo"] == codigo:
            return {
                "codigo": produto["codigo"],
                "nome": novo_nome,
                "quantidade": nova_quantidade,
                "preco": novo_preco
            }
        return produto

    return list(map(atualizar, estoque))


def remover_produto(estoque, codigo):
    """
    Função pura:
    Usa filter para gerar uma nova lista sem o produto removido.
    Não altera o estoque original.
    """
    return list(
        filter(
            lambda produto: produto["codigo"] != codigo,
            estoque
        )
    )


def formatar_produto(produto):
    """
    Função pura:
    Recebe um produto e retorna uma string formatada.
    """
    return (
        f"Código: {produto['codigo']} | "
        f"Nome: {produto['nome']} | "
        f"Quantidade: {produto['quantidade']} | "
        f"Preço: R$ {produto['preco']:.2f}"
    )


def listar_produtos_formatados(estoque):
    """
    Função pura:
    Usa map para transformar a lista de produtos em uma lista de textos.
    """
    if len(estoque) == 0:
        return ["Estoque vazio."]

    return list(map(formatar_produto, estoque))


def calcular_valor_total_estoque(estoque):
    """
    Função pura:
    Calcula o valor total do estoque sem alterar os dados.
    Usa map e sum.
    """
    valores = map(
        lambda produto: produto["quantidade"] * produto["preco"],
        estoque
    )

    return sum(valores)


def aplicar_operacao(estoque, operacao):
    """
    Função de ordem superior:
    Recebe uma função como parâmetro e aplica essa função ao estoque.
    """
    return operacao(estoque)


# ============================================================
# PARTE 02 - PARADIGMA IMPERATIVO
# ============================================================
# Aqui fica a interação com o usuário.
# Esta parte usa:
# - while
# - if, elif, else
# - input()
# - print()
# - variável mutável estoque
# - fluxo sequencial de execução
# ============================================================

def exibir_menu():
    print("\n========== SISTEMA DE CONTROLE DE ESTOQUE ==========")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar produto")
    print("4 - Remover produto")
    print("5 - Buscar produto")
    print("6 - Ver valor total do estoque")
    print("7 - Sair")


def ler_quantidade():
    while True:
        try:
            quantidade = int(input("Digite a quantidade: "))

            if quantidade < 0:
                print("A quantidade não pode ser negativa.")
            else:
                return quantidade

        except ValueError:
            print("Digite uma quantidade válida.")


def ler_preco():
    while True:
        try:
            preco = float(input("Digite o preço: "))

            if preco < 0:
                print("O preço não pode ser negativo.")
            else:
                return preco

        except ValueError:
            print("Digite um preço válido.")


def sistema_estoque():
    """
    Função principal do sistema.

    O cliente vê apenas um CRUD comum.
    Porém, internamente, o sistema combina:

    - Paradigma imperativo:
      controla o menu, o fluxo e a variável estoque.

    - Paradigma funcional:
      executa as operações de cadastro, listagem,
      atualização, remoção e busca por meio de funções puras.
    """

    estoque = []  # Estado mutável controlado pela parte imperativa

    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- CADASTRAR PRODUTO ---")

            codigo = input("Digite o código do produto: ")

            produto_existente = buscar_produto(estoque, codigo)

            if len(produto_existente) > 0:
                print("Já existe um produto com esse código.")
            else:
                nome = input("Digite o nome do produto: ")
                quantidade = ler_quantidade()
                preco = ler_preco()

                produto = criar_produto(codigo, nome, quantidade, preco)

                # A função funcional retorna uma nova lista.
                # A parte imperativa atualiza a variável estoque.
                estoque = adicionar_produto(estoque, produto)

                print("Produto cadastrado com sucesso!")

        elif opcao == "2":
            print("\n--- LISTA DE PRODUTOS ---")

            produtos_formatados = listar_produtos_formatados(estoque)

            for linha in produtos_formatados:
                print(linha)

        elif opcao == "3":
            print("\n--- ATUALIZAR PRODUTO ---")

            codigo = input("Digite o código do produto que deseja atualizar: ")

            produto_existente = buscar_produto(estoque, codigo)

            if len(produto_existente) == 0:
                print("Produto não encontrado.")
            else:
                novo_nome = input("Digite o novo nome: ")
                nova_quantidade = ler_quantidade()
                novo_preco = ler_preco()

                estoque = atualizar_produto(
                    estoque,
                    codigo,
                    novo_nome,
                    nova_quantidade,
                    novo_preco
                )

                print("Produto atualizado com sucesso!")

        elif opcao == "4":
            print("\n--- REMOVER PRODUTO ---")

            codigo = input("Digite o código do produto que deseja remover: ")

            produto_existente = buscar_produto(estoque, codigo)

            if len(produto_existente) == 0:
                print("Produto não encontrado.")
            else:
                estoque = remover_produto(estoque, codigo)
                print("Produto removido com sucesso!")

        elif opcao == "5":
            print("\n--- BUSCAR PRODUTO ---")

            codigo = input("Digite o código do produto que deseja buscar: ")

            resultado = buscar_produto(estoque, codigo)

            if len(resultado) == 0:
                print("Produto não encontrado.")
            else:
                produtos_formatados = listar_produtos_formatados(resultado)

                for linha in produtos_formatados:
                    print(linha)

        elif opcao == "6":
            print("\n--- VALOR TOTAL DO ESTOQUE ---")

            valor_total = calcular_valor_total_estoque(estoque)

            print(f"Valor total em estoque: R$ {valor_total:.2f}")

        elif opcao == "7":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")


# ============================================================
# EXECUÇÃO DO PROGRAMA
# ============================================================

sistema_estoque()
