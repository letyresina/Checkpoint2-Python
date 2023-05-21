import time # Essa importação vai ser utilizada no decorrer do programa para facilitar a visualização do usuário!

# Lista que vai ser utilizada para encontrar os preços do vinho, sem a necessidade do usuário inserir os preços
precosVinho = {
    # Vinhos tintos
    'carbenetsauvignon': 100.0,
    'pinotnoir': 120.0,
    'tintomalbec': 80.0,
    'tintomerlot': 90.0,
    'tintosyrah': 100.0,

    # Vinhos brancos
    'chardonnay': 80.0,
    'sauvignonblanc': 70.0,
    'riesling': 90.0,
    'pinotgrigio': 60.0,

    # Vinhos rosés
    'cabernetfranc': 70.0,
    'syrah': 80.0,
    'grenache': 60
} 

# Lista que armazena os metódos de pagamento para validação
formasPagamento = {
    'pix',
    'boleto',
    'crédito',
    'débito'
}

# Variavel carrinho em forma de lista (vazia)
carrinho = []

# Menu de opções
def menuOpcoes():
    # Lista do menu, organizada para o usuário
    print("Digite 1: Listar vinhos disponíveis para venda;")
    print("Digite 2: Adicionar vinhos no carrinho de compras;")
    print("Digite 3: Visualizar o carrinho de compras;")
    print("Digite 4: Finalizar a compra;")
    print("Digite 5: Finalizar a loja virtual;")
    
    # Validação para saber se o usuário digitou um número inteiro como menu
    try:
        opcao = int(input("Informe a opção desejada: "))
            # Caso o usuário digite um número, entretanto, não foi entre 1 e 5
        if (opcao < 1) or (opcao > 5):
            raise TypeError
        return opcao
    except ValueError:
        print("Por favor, informe somente o números dentro das opções disponíveis!")
        print("Aguarde 1 segundo que irá reiniciar automaticamente!")
        time.sleep(1) # Para dar tempo do usuário ler o que ele fez de errado antes de reiniciar novamente
    except TypeError:
        print("Opção inválida! Por favor, escolha uma opção válida!")
        print("Aguarde 1 segundo que irá reiniciar automaticamente!")
        time.sleep(1) # Para dar tempo do usuário ler o que ele fez de errado antes de reiniciar novamente

# Função para listar vinhos e deixar o código do looping mais clean
def listarVinhos():
    print("-------------------------------------------------------------------")
    print("Vinhos Tintos:")
    print("• Carbenet Sauvignon – R$ 100,00")
    print("• Pinot Noir – R$ 120,00")
    print("• Tinto Malbec – R$ 80,00")
    print("• Tinto Merlot – R$ 90,00")
    print("• Tinto Syrah – R$ 100,00")
    print("-------------------------------------------------------------------")
    print("Vinhos Brancos:")
    print("• Chardonnay – R$ 80,00")
    print("• Sauvignon Blanc – R$ 70,00")
    print("• Riesling – R$ 90,00")
    print("• Pinot Grigio – R$ 60,00")
    print("-------------------------------------------------------------------")
    print("Vinhos Rosés:")
    print("• Cabernet Franc – R$ 70,00")
    print("• Syrah – R$ 80,00")
    print("• Grenache – R$ 60,00")
    print("-------------------------------------------------------------------")
    time.sleep(2) # Para dar tempo do usuário ler antes de aparecer o menu novamente

# Função adicionar carrinho -> tratamento feito dentro da própria função
def adicionarCarrinho():
    vinho = input("Digite o nome do vinho desejado: ").lower().replace(" ", "")
    
    if vinho in precosVinho:
        quantidade = int(input("Informe a quantidade desejada: "))

        vinhoExistente = None
        for item in carrinho:
            if item['vinho'] == vinho:
                vinhoExistente = item
                break

        if vinhoExistente:
            vinhoExistente['quantidade'] += quantidade
            vinhoExistente['precoTotal'] += precosVinho[vinho]
            print("Adicionado ao carrinho com sucesso!")
            time.sleep(1)

        else:
            item = {
                'vinho': vinho,
                'precoTotal': precosVinho[vinho] * quantidade,
                'quantidade': quantidade
            }

            carrinho.append(item)
            print("Adicionado ao carrinho com sucesso!")
            time.sleep(1)

    else:
        print("Produto não encontrado! Por favor, tente novamente!")
        time.sleep(1)

def calcularDescontoProgressivo(quantidadeTotal):
    desconto = 0.0
    if quantidadeTotal >= 5:
        desconto = 0.3  # 30% de desconto para 5 ou mais itens
    elif quantidadeTotal >= 4:
        desconto = 0.2  # 20% de desconto para 4 itens
    elif quantidadeTotal >= 3:
        desconto = 0.1  # 10% de desconto para 3 itens
    return desconto


def mostrarCarrinho():
    if carrinho == []:
        print("Seu carrinho está vazio...")
    else:
        print("Seu Carrinho")
        print("{:<20} {:<10} {:<10} {:<10}".format("Produto", "Preço", "Quantidade", "Total"))
        print("-" * 60)

        quantidadeTotal = 0
        valorTotal = 0.0

        for item in carrinho:
            vinho = item['vinho']
            precoUnitario = precosVinho[vinho]
            quantidade = item['quantidade']
            precoTotal = item['precoTotal']

            quantidadeTotal += quantidade
            valorTotal += precoTotal

            print("{:<20} R${:<10.2f} {:<10} R${:<10.2f}".format(vinho, precoUnitario, quantidade, precoTotal))

        print("-" * 60)

        desconto = calcularDescontoProgressivo(quantidadeTotal)
        valorDesconto = valorTotal * desconto
        valorFinal = valorTotal - valorDesconto

        print("{:<30} {:<10}".format("Quantidade total de itens:", quantidadeTotal))
        print("{:<30} R${:<10.2f}".format("Valor total:", valorTotal))
        print("{:<30} {:<10.0%}".format("Desconto:", desconto))
        print("{:<30} R${:<10.2f}".format("Valor com desconto:", valorFinal))
        time.sleep(1)

# Função para finalizar a compra
def FinalizarCompra():
    print("Para finalizar a compra, precisamos realizar seu cadastro!")
    try:
        nomeCompleto = input("Qual seu nome completo? ")
        email = input("Qual seu e-mail? ")

        try:
            cpf = int(input("Qual seu CPF? Informe somente números: "))
        except ValueError:
            print("Por favor, informe somente números!")
            cpf = int(input("Qual seu CPF? Informe somente números: "))

        dataNasc = input("Qual sua data de nascimento? ")

        print("Agora as informações sobre seu endereço!")
        rua = input("Qual sua rua? ")
        try:
            numero = int(input("Qual o número? "))
        except ValueError:
            print("Por favor, informe somente números!")
            numero = int(input("Qual o número? "))

        complemento = input("Se houver complemento, informe: ")
        try:
            cep = int(input("Informe seu CEP somente com números: "))
        except ValueError:
            print("Por favor, informe somente números!")
            cep = int(input("Informe seu CEP somente com números: "))

        cidade = input("Informe a cidade: ")
        estado = input("Informe o Estado: ")

        print("Por favor, confirme seus dados!")
        print(f"\n Nome: {nomeCompleto} \n Email: {email} \n CPF: {cpf} \n Data de nascimento: {dataNasc} \n")
        print(f"\n Endereço: Rua {rua}, Número {numero}, Complemento: {complemento}, CEP {cep}")
        print(f"Cidade: {cidade}, Estado: {estado}")

        print("\n Digite 1 para sim \n Digite 2 para não")
        try:
            confirmaDados = int(input("Informe a opção aqui: "))

            if confirmaDados == 1:
                mostrarCarrinho()
                time.sleep(1)
                print("Qual o metódo de pagamento?")
                print("\n Pix \n Boleto \n Débito \n Crédito")
                metodoPagamento = input("Informe aqui o metódo de pagamento: ").lower()
                if metodoPagamento in formasPagamento:
                    print(f"\n Metódo selecionado: {metodoPagamento} \n Processando sua compra...")
                    time.sleep(2)
                    print("A Vinheria Agnello agradece a sua compra!")
                    carrinho.clear()
                else:
                    print("Metódo de pagamento inválido! Tente novamente!")

        except ValueError:
            print("Por favor, informe apenas números para a confirmação! Digite somente 1.")
            print("Reinicie novamente para realização do cadastro e finalização da compra.")

    except:
        print("Um erro inesperado aconteceu. Por favor, reinicie seu cadastro! Confirme de enviar os dados conforme solicitado, por favor.")


# Mensagem de boas vindas
print("Seja bem vindo(a) à loja virtual da Vinheria Agnello!")
print("No que podemos te ajudar hoje?")

while True:
    opcao = menuOpcoes()
    
    # Lista vinhos
    if opcao == 1:
        listarVinhos()

    # Adicionar vinhos no carrinho
    elif opcao == 2:
        adicionarCarrinho()

    # Visualizar carrinho de compras
    elif opcao == 3:
        mostrarCarrinho()
    
    # Finalizar compra
    elif opcao == 4:
        if carrinho == []: # Vê se o carrinho está vazio
            print("Por favor, insira produtos no seu carrinho antes de prosseguir!")
            time.sleep(1)
        else: 
            FinalizarCompra()

    # Encerrando a loja virtual
    elif opcao == 5: 
        print("Obrigada por utilizar nossa loja virtual! A Vinheria Agnello agradece pela sua escolha e confiança!")
        break