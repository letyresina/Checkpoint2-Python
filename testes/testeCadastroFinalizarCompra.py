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
                # coloca um tempo
                print("Qual o metódo de pagamento?")
                print("\n 1 - Pix \n 2 - Boleto \n 3 - Débito \n 4 - Crédito")
                metodoPagamento = input("Informe aqui o metódo de pagamento: ")
                print(f"\n Metódo selecionado: `{metodoPagamento} \n Processando sua compra...")
                # coloca um tempo
                print("A Vinheria Agnello agradece a sua compra!")
                carrinho.clear()

        
        except ValueError:
            print("Por favor, informe apenas números para a confirmação! Digite somente 1.")
            print("Reinicie novamente para realização do cadastro e finalização da compra.")

    except:
        print("Um erro inesperado aconteceu. Por favor, reinicie seu cadastro! Confirme de enviar os dados conforme solicitado, por favor.")



FinalizarCompra()
