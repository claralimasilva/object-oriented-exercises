from ClaraBank import ContaCorrente, ClaraCard

conta_Clara = ContaCorrente('Clara', '123.456.789-00', 1147, 369825)

conta_Clara.consultar_saldo()

#depositando na continha
conta_Clara.depositar(50)
conta_Clara.consultar_saldo()

time.sleep(1)

#sacando um dinheirinho
#conta_Clara.sacar_dinheiro(25)

print('-' * 20)

print('Extrato')
conta_Clara.consultar_saldo()
conta_Clara.consultar_limite_chequeespecial()

print('-' * 20)
conta_Clara.consultar_historico()

print('-' * 20)
#transferindo dinheiro
conta_Pedro = ContaCorrente('Pedro', '987.654.321-00', 2222, 131313)
conta_Clara.consultar_saldo()
conta_Clara.transferir(20, conta_Pedro)

print('Clara transferiu dinheiro.') 
conta_Clara.consultar_saldo()

print('-' * 20)
print('Pedro recebeu dinheiro.')
conta_Pedro.consultar_saldo()