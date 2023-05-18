''' 
    Leticia Resina - RM 98069
'''

import time # Essa importação vai ser utilizada no decorrer do programa para facilitar a visualização do usuário!

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
        print("Por favor, informe somente o número da opção!")
        print("Aguarde 1 segundo que irá reiniciar automaticamente!")
        time.sleep(1) # Para dar tempo do usuário ler o que ele fez de errado antes de reiniciar novamente
    except TypeError:
        print("Opção inválida! Por favor, escolha uma opção válida!")
        print("Aguarde 1 segundo que irá reiniciar automaticamente!")
        time.sleep(1) # Para dar tempo do usuário ler o que ele fez de errado antes de reiniciar novamente


# Mensagem de boas vindas
print("Seja bem vindo(a) à loja virtual da Vinheria Agnello!")
print("No que podemos te ajudar hoje?")

while True:
    opcao = menuOpcoes()
    if opcao == 1:
        print("Implementações futuras...")
    
    # Encerrando a loja virtual
    elif opcao == 5: 
        print("Obrigada por utilizar nossa loja virtual! A Vinheria Agnello agradece pela sua escolha e confiança!")
        break
    