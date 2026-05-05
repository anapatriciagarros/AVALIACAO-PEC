# ============================================================
# SISTEMA DE CONTROLE DE ESTOQUE COM CRUD
# Integração dos paradigmas Imperativo e Funcional
# ============================================================
#
# O sistema é único para o usuário final.
# A separação entre paradigmas acontece apenas na organização interna do código.
#
# Parte funcional:
# - concentra as regras de manipulação do estoque;
# - utiliza funções puras;
# - evita alteração direta da lista original;
# - usa imutabilidade, map, filter e função de ordem superior.
#
# Parte imperativa:
# - controla o menu e o fluxo de execução;
# - utiliza variáveis mutáveis;
# - usa estruturas condicionais e de repetição;
# - realiza entrada e saída de dados com input() e print().
#
# ============================================================


# ============================================================
# PARTE 01 - PARADIGMA FUNCIONAL
# ============================================================
# Nesta parte, as funções recebem dados, processam esses dados
# e retornam novos valores.
#
# As funções principais não usam input() nem print().
# Isso reduz efeitos colaterais e facilita a reutilização do código.
# ============================================================

def criar_produto(codigo, nome, quantidade, preco):
    # Função pura: cria e retorna um novo produto.
    return {
        "codigo": codigo,
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }


def adicionar_produto(estoque, produto):
    # Imutabilidade: retorna uma nova lista, sem usar append().
    return estoque + [produto]


def buscar_produto(estoque, codigo):
    # Uso de filter para localizar produtos pelo código.
    return list(
        filter(
            lambda produto: produto["codigo"] == codigo,
            estoque
        )
    )


def atualizar_produto(estoque, codigo, novo_nome, nova_quantidade, novo_preco):
    # Uso de map para gerar uma nova lista com o produto atualizado.

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
    # Uso de filter para gerar uma nova lista sem o produto removido.
    return list(
        filter(
            lambda produto: produto["codigo"] != codigo,
            estoque
        )
    )


def formatar_produto(produto):
    # Função pura: transforma os dados de um produto em texto.
    return (
        f"Código: {produto['codigo']} | "
        f"Nome: {produto['nome']} | "
        f"Quantidade: {produto['quantidade']} | "
        f"Preço: R$ {produto['preco']:.2f}"
    )


def listar_produtos_formatados(estoque):
    # Uso de map para formatar todos os produtos da lista.
    if len(estoque) == 0:
        return ["Estoque vazio."]

    return list(map(formatar_produto, estoque))


def calcular_valor_total_estoque(estoque):
    # Uso de map e sum para calcular o valor total do estoque.
    valores = map(
        lambda produto: produto["quantidade"] * produto["preco"],
        estoque
    )

    return sum(valores)


def aplicar_operacao(estoque, operacao):
    # Função de ordem superior: recebe outra função como parâmetro.
    return operacao(estoque)


# ============================================================
# PARTE 02 - PARADIGMA IMPERATIVO
# ============================================================
# Nesta parte, o programa controla a execução passo a passo.
#
# Aqui aparecem:
# - variável mutável;
# - while;
# - if, elif e else;
# - input();
# - print();
# - alteração do estado do estoque ao longo da execução.
# ============================================================

def exibir_menu():
    # Exibe as opções disponíveis para o usuário.
    print("\n========== SISTEMA DE CONTROLE DE ESTOQUE ==========")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar produto")
    print("4 - Remover produto")
    print("5 - Buscar produto")
    print("6 - Ver valor total do estoque")
    print("7 - Sair")


def ler_quantidade():
    # Estrutura imperativa para validar a entrada da quantidade.
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
    # Estrutura imperativa para validar a entrada do preço.
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
    # Variável mutável que representa o estado atual do estoque.
    estoque = []

    # Laço principal do sistema.
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
                # A variável estoque recebe esse novo estado.
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

                # Atualização feita por função pura.
                # O estoque anterior não é alterado diretamente.
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
                # Remoção feita por função pura.
                # Uma nova lista é atribuída à variável estoque.
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
