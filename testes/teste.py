carrinho = []

precosVinho = {
    'carbenetsauvignon': 100.0,
    'pinotnoir': 120.0,
    'tintomalbec': 80.0,
    'tintomerlot': 90.0,
    'tintosyrah': 100.0,
    'chardonnay': 80.0,
    'sauvignonblanc': 70.0,
    'riesling': 90.0,
    'pinotgrigio': 60.0,
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
            vinhoExistente['precoTotal'] += precosVinho[vinho] * quantidade

        else:
            item = {
                'vinho': vinho,
                'precoTotal': precosVinho[vinho] * quantidade,
                'quantidade': quantidade
            }

            carrinho.append(item)
            print("Adicionado ao carrinho com sucesso!")

    else:
        print("Produto não encontrado! Por favor, tente novamente!")


def calcularDescontoProgressivo(quantidade_total):
    desconto = 0.0
    if quantidade_total >= 5:
        desconto = 0.3  # 30% de desconto para 5 ou mais itens
    elif quantidade_total >= 4:
        desconto = 0.2  # 20% de desconto para 4 itens
    elif quantidade_total >= 3:
        desconto = 0.1  # 10% de desconto para 3 itens
    return desconto


def mostrarCarrinho():
    if carrinho == []:
        print("Seu carrinho está vazio...")
    else:
        print("Seu Carrinho")
        print("{:<20} {:<10} {:<10} {:<10}".format("Produto", "Preço", "Quantidade", "Total"))
        print("-" * 60)

        quantidade_total = 0
        valor_total = 0.0

        for item in carrinho:
            vinho = item['vinho']
            preco_unitario = precosVinho[vinho]
            quantidade = item['quantidade']
            preco_total = item['precoTotal']

            quantidade_total += quantidade
            valor_total += preco_total

            print("{:<20} R${:<10.2f} {:<10} R${:<10.2f}".format(vinho, preco_unitario, quantidade, preco_total))

        print("-" * 60)

        desconto = calcularDescontoProgressivo(quantidade_total)
        valor_desconto = valor_total * desconto
        valor_final = valor_total - valor_desconto

        print("{:<30} {:<10}".format("Quantidade total de itens:", quantidade_total))
        print("{:<30} R${:<10.2f}".format("Valor total:", valor_total))
        print("{:<30} {:<10.0%}".format("Desconto:", desconto))
        print("{:<30} R${:<10.2f}".format("Valor com desconto:", valor_final))


while True:
    adicionarCarrinho()
    mostrarCarrinho()