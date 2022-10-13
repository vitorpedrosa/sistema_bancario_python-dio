menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastrar Usuário
[5] Cadastrar Conta
[6] Sair
"""
LIMITE_SAQUES = 3
AGENCIA = "0001"
saldo = 0
limite = 500
extrato = ""
usuarios = []
contas = []
numero_saques = 0


def sacar (*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if (valor > saldo):
        print("Saldo insuficiente!")
    elif (valor > limite):
        print("O limite para saques é de R$ 500! ")
    elif numero_saques >= limite_saques:
        print("Limite de saques diarios atingido!")            
    elif (valor > 0):
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Operação Realiada com Sucesso!")
            print(numero_saques, limite_saques)
    else:
        print("Error: O Valor digitado é Invalido!")
    return saldo, extrato

def depositar (saldo, valor, extrato, /):
    if (valor < 0):
        print("Error: Digite um valor válido")
    else: 
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Operação realizada com sucesso!")  

    return saldo, extrato

def exibir_extrato (saldo, extrato="extrato"):
    print("\n ============== Extrato ===============")
    print(extrato)
    print(f"Saldo R$: {saldo:.2f}")

def cadastrar_usuario (usuarios):
    cpf = input("informe o cpf")
    usuario = filtrar_usuarios(cpf, usuarios)
    if usuario:
        print("Cpf já cadastrados")
        return
    
    nome = input("informe o nome: ")
    data_nascimento = input("informe a data de nascimento: ")
    endereco = input("informe o endereço: ")

    usuarios.append({"nome" : nome, "data_nascimento" : data_nascimento, "endereco" : endereco, "cpf" : cpf})
    print ("usuario criado")

def criar_conta (agencia, numero_conta, usuarios):
    cpf = input("informe o cpf: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if(usuario):
        print("conta criada: ")
        return {"agencia" : agencia, "numero_conta" : numero_conta, "usuario" : usuario}
    
    print ("usuario nao encontrado")


def filtrar_usuarios (cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None;
        

while True:
    print(menu)
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        valor = float(input("Digite o valor que deseja depositar: "))
        
        saldo, extrato = depositar(saldo, valor, extrato)
          

    elif opcao == "2":
        valor = float(input("Digite o valor que deseja sacar: "))

        saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES); 

    elif opcao == "3":
        exibir_extrato(saldo, extrato=extrato)    
    elif opcao == "4":
        cadastrar_usuario(usuarios)
    elif opcao == "5":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
     
        if conta:
            contas.append(conta) 


    elif opcao == "6":
        break

    else:
        print("Opção Invalida, favor digitar uma opção válida!")