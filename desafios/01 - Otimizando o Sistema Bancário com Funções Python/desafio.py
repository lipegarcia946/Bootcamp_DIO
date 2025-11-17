def criar_usuario(usuarios):
    cpf = input("Informe o CPF(apenas com números):")
    usuarios=encontrar_usuarios(cpf,usuarios)

    if usuarios:
        print("Já existe um usuário cadastrado com esse cpf")
        return

    nome= input("Informe o nome completo:")
    data_nascimento = input("Informe o data de nascimento no formato (dd/mm/aaaa): ")
    endereco =input("informe o enderço no formato (logradouro, nº - bairro - cidade/sigla estado) :")

    usuarios.append({"nome:", nome ,"data_nascimento:", data_nascimento,"cpf:", cpf, "endereco:", endereco})
    usuarios.append(data_nascimento)
    print("usuário criado com sucesso!")

def encontrar_usuarios(cpf, usuarios):
    usuario_encontrado=[usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_encontrado[0] if usuario_encontrado else None

def criar_conta(agencia, numero_conta,usuarios):
    cpf= input("informe o cpf do usuário")
    usuario = encontrar_usuarios(cpf,usuarios)
    if usuario:
        print("conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("nenhum usuario foi encontrado, fluxo de criação da conta encerrado!")

def realizar_saque(*, saldo,valor,limite,extrato,numero_saques,LIMITE_SAQUES):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")


def realizar_deposito(saldo,valor,extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return saldo, extrato
    else:
        print("Operação falhou! O valor informado é inválido.")

def ver_contas(contas):
    for conta in contas:
        linha = f"""\
        agencia: \t{conta["agencia"]}
        C/C:\t{conta["numero_conta"]}
        Titular:\t{conta["usuario"]["nome"]}
        """
    print("="*100)

def visualizar_extrato(saldo, /,*, extrato,):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
menu = """

[d ou D] Depositar
[s ou S] Sacar
[e ou E] Extrato
[q ou Q] Sair
[nc ou NC] Cadastrar Nova Conta
[vc ou VC] Vizualizar Contas]
[nu ou NU] Cadastrar Novo usuário]

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA= "0001"
usuarios = []
contas= []

while True:

    opcao = input(menu)

    if opcao == "d" or opcao == "D":
        valor = float(input("Informe o valor do depósito: "))
        mostra_saldo, mostra_extrato =realizar_deposito(saldo,valor,extrato)
        print(f"o saldo é {mostra_saldo:.2f} e o  {mostra_extrato}")

    elif opcao == "s" or opcao == "S":
        valor = float(input("Informe o valor do saque: "))
        mostra_saldo_saque, mostra_extrato_saque=realizar_saque(saldo=saldo,
                                                                valor=valor,
                                                                limite=limite,
                                                                extrato=extrato,
                                                                numero_saques=numero_saques,
                                                                limite_saques=LIMITE_SAQUES)
        print(f"o saldo do saque é {mostra_saldo_saque:.2f} e o extrato do saque é: {mostra_extrato_saque:.2f}")

    elif opcao == "e" or opcao == "E":
        ver_extrato =visualizar_extrato(saldo, extrato= extrato)
        print(ver_extrato)

    elif opcao == "nc" or opcao == "NC":
        numero_conta = len(contas) + 1
        nova_conta = criar_conta(AGENCIA,numero_conta,usuarios)
        if nova_conta:
            contas.append(nova_conta)

    elif opcao == "vc" or opcao == "VC":
        ver_contas(contas)

    elif opcao == "NU" or opcao == "NU":
     criar_usuario(usuarios)

    elif opcao == "q" or opcao == "Q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")