import textwrap

def menu():
    menu = """\n
    ===============MENU===============
    Escolha uma opção:

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /): # "/" no final do argumento -> positional only
    if valor>0:
        saldo +=valor
        extrato += f"Depósito:\t R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):#keyword only
    if (valor>saldo):
        print("Falha na operação! Você não tem saldo suficiente para esse saque.")
    elif(valor>limite):
        print("Falha na operação! O valor do saque excede o limite.")
    elif(numero_saques>=limite_saques):
        print("Falha na operação! Número máximo de saque excedido.")
    elif (valor>0):
        saldo -= valor
        numero_saques = numero_saques +1
        extrato += f"Saque:\tR$ {valor:.2f}\n"
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor digitado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato): #positional only and keyword only
    print("==============EXTRATO===================")
    print("Não foram realizadas movimnetações." if not extrato else extrato)
    print(f"Saldo:\tR$ {saldo:.2f}")
    print("=========================================")

def criar_usuario(usuarios):
    cpf = input("Digite o CPF(somente números):  ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("CPF já existente!")
        return
    
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("DIgite sua data de nascimento (dd-mm-aaaa)")
    endereco = input("Digite o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "Endereço": endereco})
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF(somente números):  ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com suceeso! ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario":usuario}
    print("Usuário não encontrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            CC::\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}"""
        print("===============================")
        print(textwrap.dedent(linha))

       

def main():
    LIMITE_SAQUES = 3
    NUM_AGENCIA = "126-1"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []


    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input('Digite o valor do depósito: '))
            saldo, extrato = depositar(saldo, valor ,extrato)

        elif opcao =="s":
            valor = float(input("Digite o valor do saque: "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) +1
            conta = criar_conta(NUM_AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta+=1

        elif opcao == "lc":
            listar_contas(contas)
        
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novemente a operação desejada.")


main()