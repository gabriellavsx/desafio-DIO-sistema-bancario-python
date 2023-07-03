menu = """
===============MENU===============
Escolha uma opção:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor do depósito: "))
        if valor>0:
            saldo = saldo + valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido.")
    
    elif opcao =="s":
        valor = float(input("Digite o valor do saque: "))
        if (valor>saldo):
            print("Falha na operação! Você não tem saldo suficiente para esse saque.")
        elif(valor>limite):
            print("Falha na operação! O valor do saque excede o limite.")
        elif(numero_saques>=LIMITE_SAQUES):
            print("Falha na operação! Número máximo de saque excedido.")
        elif (valor>0):
            saldo = saldo - valor
            numero_saques = numero_saques +1
            extrato += f"Saque: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor digitado é inválido.")

    elif opcao == "e":
        print("\n==================EXTRATO=======================")
        print("Não foram realizadas movimentações nessa conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}\n")
        print("==================================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novemente a operação desejada.")
