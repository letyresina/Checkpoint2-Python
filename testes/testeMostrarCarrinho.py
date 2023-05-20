carrinho = []

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

        else:
            item = {
                'vinho': vinho,
                'precoTotal': precosVinho[vinho] * quantidade,
                'quantidade': quantidade
            }

            carrinho.append(item)
            print("Adicionado ao carrinho com sucesso!")
            # colocar um time de aguardo!

    else:
        print("Produto não encontrado! Por favor, tente novamente!")
        # colocar um time de aguardo!



def mostrarCarrinho():

    if carrinho == []:
        print("Seu carrinho está vazio...")

    else:
        print("Seu Carrinho")
        print("{:<10} {:<10} {:<10} {:<10}".format("Produto", "Preço", "Quantidade", "Total"))
        print("----------------------------------------")

        for item in carrinho:
            vinho = item['vinho']
            precoTotal = item['precoTotal']
            quantidade = item['quantidade']

            # Caso o carrinho possua mais de 3 garrafas
            if (len(carrinho) == 3): 
                total = precoTotal * quantidade - (0.1 * precoTotal)
            elif (len(carrinho) == 4): # desconto de 20% = 0.2
                print("Fazer depois")
            elif (len(carrinho) >= 5): # desconto de 30% => 0.3
                print("Fazer depois")

