menu ="""

[d] Depositar
[s] Sacar
[e] Extrato
[q] Quit

"""

saldo = 0
limite = 500
extrato = []
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        while True:
            valor = input("Insira o valor do depósito:\n")

            if ',' in valor:
                valor = float(valor.replace(',','.'))
                if valor <= 0.0:
                    print("Não foi possivel realizar a operação, por favor insira um valor maior que 0\n")
                else:
                    saldo += valor
                    print(f"Operação realizada com sucesso, deposito de R$ {valor:.2f}. Seu novo saldo é de R$ {saldo:.2f}\n")
                    extrato.append(valor)
                    break
            else:
                valor = int(valor)
                if valor <= 0:
                    print("Não foi possivel realizar a operação, por favor insira um valor maior que 0\n")
                else:
                    saldo += valor
                    print(f"Operação realizada com sucesso, deposito de R$ {valor:.2f}. Seu novo saldo é de R$ {saldo:.2f}\n")
                    extrato.append(valor)
                    break
    
    elif opcao == 'e':
        if len(extrato) == 0:
            print('Não foram realizadas movimentações\n')

        for s in extrato:
            if s > 0:
                print(f"Depósito Realizado: {s:.2f}\n")
            elif s < 0:
                print(f"Saque Realizado: {s:.2f}\n")
        
        print(f"Seu saldo atual é de R$ {saldo:.2f}\n")

    elif opcao == 's':       
        if numero_de_saques < 3:
            while True:
                valor = input("Insira o valor para saque:\n")
            
                if ',' in valor:
                    valor = float(valor.replace(',','.'))
                    if valor < 0.0:
                        print("Não foi possivel realizar a operação, por favor insira um valor maior que 0\n")
                    elif valor > 500.0:
                        print(f"Não foi possivel realizar a operação, valor acima do limite da conta: R$ {limite:.2f}\n")
                    elif valor > saldo:
                        print(f"Não foi possivel realizar a operação, saldo insuficiente | saldo da conta: R$ {saldo:.2f}\n")
                    else:
                        saldo -= valor
                        print(f"Operação realizada com sucesso, saque de R$ {valor:.2f}. Seu novo saldo é de R$ {saldo:.2f}\n")
                        numero_de_saques += 1 
                        extrato.append(valor*-1)
                        break
                else:
                    valor = int(valor)
                    if valor < 0.0:
                        print("Não foi possivel realizar a operação, por favor insira um valor maior que 0\n")
                    elif valor > 500.0:
                        print(f"Não foi possivel realizar a operação, valor acima do limite da conta: R$ {limite:.2f}\n")
                    elif valor > saldo:
                        print(f"Não foi possivel realizar a operação, saldo insuficiente | saldo da conta: R$ {saldo:.2f}\n")
                    else:
                        saldo -= valor
                        print(f"Operação realizada com sucesso, saque de R$ {valor:.2f}. Seu novo saldo é de R$ {saldo:.2f}\n")
                        numero_de_saques += 1 
                        extrato.append(valor*-1)
                        break
        else:
            print(f'Não foi possivel realizar a operação. Limite de {LIMITE_SAQUES} saques atingidos')


    elif opcao == 'q':
        break

    else:
        print("Opção inválida. Selecione alguma das opções disponíveis\n")
                    


        