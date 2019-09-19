def criptografar(mensagem, chave=None):
	chave_final = ''
	if mensagem:
		if chave:
			# Criptografa de acordo com a chave passada
			chave_final = ''
		else:
			# Criptografia padrao para quando nao houver chave
			lista = []
			for x in range(len(mensagem)):
				lista.append(mensagem[x])
				lista[x] = ord(lista[x])
			lista.reverse()
			for x in range(len(lista)):
				if lista[x] == 32:
					pass
				else:
					lista[x] += 5
			for x in range(len(lista)):
				chave_final += chr(lista[x]) 
	return chave_final, lista

def descriptografar(mensagem, chave=None)