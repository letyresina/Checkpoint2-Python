''' 
    Leticia Resina - RM 98069
'''

import time # Essa importação vai ser utilizada no decorrer do programa para facilitar a visualização do usuário!

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
         print("Implementação futura")

    # Visualizar carrinho de compras
    elif opcao == 3:
         print("Implementação futura")
    
    # Finalizar compra
    elif opcao == 4:
        if carrinho == []: # Vê se o carrinho está vazio
            print("Por favor, insira produtos no seu carrinho antes de prosseguir!")
        else: 
            print("Implementação futura")

    # Encerrando a loja virtual
    elif opcao == 5: 
        print("Obrigada por utilizar nossa loja virtual! A Vinheria Agnello agradece pela sua escolha e confiança!")
        break
    