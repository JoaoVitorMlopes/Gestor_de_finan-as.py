transacoes = []
def registrar_transacao(tipo, valor, categoria):
    transacao = {
        'tipo': tipo,
        'valor': valor,
        'categoria': categoria
    }
    transacoes.append(transacao)
    print("Transação registrada com sucesso!")
def exibir_saldo():
    saldo = 0
    for transacao in transacoes:
        if transacao['tipo'] == 'entrada':
            saldo += transacao['valor']
        else:
            saldo -= transacao['valor']
    print("Saldo atual: R$", saldo)
def exibir_transacoes():
    for transacao in transacoes:
        print("Tipo:", transacao['tipo'])
        print("Valor: R$", transacao['valor'])
        print("Categoria:", transacao['categoria'])
        print("------------------------")

while True:
    print("1 - Registrar entrada de dinheiro")
    print("2 - Registrar saída de dinheiro")
    print("3 - Exibir saldo")
    print("4 - Exibir transações")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        valor = float(input("Digite o valor da entrada: "))
        categoria = input("Digite a categoria da entrada: ")
        registrar_transacao('entrada', valor, categoria)
    elif opcao == '2':
        valor = float(input("Digite o valor da saída: "))
        categoria = input("Digite a categoria da saída: ")
        registrar_transacao('saída', valor, categoria)
    elif opcao == '3':
        exibir_saldo()
    elif opcao == '4':
        exibir_transacoes()
    elif opcao == '5':
        break
    else:
        print("Opção inválida. Tente novamente.")
