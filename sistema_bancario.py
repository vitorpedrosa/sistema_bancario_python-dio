menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 3

while True:
    print(menu)
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        valor = float(input("Digite o valor que deseja depositar: "))
        if valor < 0:
            print("Error: Digite um valor válido")
        else:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Operação realizada com sucesso!") 

    elif opcao == "2":
        valor = float(input("Digite o valor que deseja sacar: "))
        if valor > saldo:
            print("Saldo insuficiente!")
        elif valor > limite:
            print("O limite para saques é de R$ 500! ")
        elif numero_saques == 0:
            print("Limite de saques diarios atingido!")            
        else:
            if(valor > 0):
                saldo -= valor
                numero_saques -= 1
                extrato += f"Saque: R$ {valor:.2f}\n"
                print("Operação Realiada com Sucesso!")
            else:
                print("Error: O Valor digitado é Invalido!") 

    elif opcao == "3":
        print("\n ============== Extrato ===============")
        print(extrato)
        print(f"Saldo R$: {saldo:.2f}")

     

    elif opcao == "4":
        break

    else:
        print("Opção Invalida, favor digitar uma opção válida!")