print("Bem vindo ao banco! Escolha uma opção:\n" )

menu= """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Saldo
[5] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        print ("Depósito")
        valor=float(input("Digite a quantia: R$"))
       
        if valor > 0:
            saldo += valor
            extrato += f"Deposito no valor de R${valor:.2f}.\n"
        else: print ("Inválido! Não é possivel depositar valores negativos.")

    elif opcao == "2":
        print("Saque")
        valor = float(input("Digite a quantia desejada: R$" ))
       
        excedeu_saldo = valor > saldo
       
        excedeu_limite = valor > limite
       
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
                print ("Operação inválida! Você não tem saldo para essa operação.")
       
        elif excedeu_limite:
                print ("Operação inválida! Você excedeu os limites disponíveis para saques.")

        elif excedeu_saques:
                print ("Operação Inválida. Você não tem mais saques disponíveis.")

        elif valor >0:
                saldo -= valor
                extrato += f"Saque no valor de R$ {valor:.2f}\n"
                numero_saques += 1
                
        else: print ("Inválido! Não é possivel sacar valores negativos.")
           
    elif opcao == "3":
        if extrato == "":
        	print ("Não há Movimentações.")
        else:
      	  print(extrato)
      	  print("Saldo atual: R$", saldo)
      	  
    elif opcao == "4":
    	print ("Saldo atual da conta: R$ ", saldo)

    elif opcao == "5":
        print("Obrigado por usar o banco!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
