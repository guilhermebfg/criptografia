def criptografar(mensagem, chave=None):
	mensagem_final = ''
	if mensagem:
		lista = []
		if chave:
			# Criptografa de acordo com a chave passada
			mensagem_final = ''
		else:
			# Criptografia padrao para quando nao houver chave
			for x in range(len(mensagem)):
				lista.append(mensagem[x])
				lista[x] = ord(lista[x])
			lista.reverse()
			for x in range(len(lista)):
				if lista[x] == 32:
					pass
				else:
					if 96 < lista[x] < 123:
						lista[x] += (lista[x] + 5) > 122 and \
							(5 - 26) or 5
					elif 64 < lista[x] < 91:
						lista[x] += (lista[x] + 5) > 90 and \
							(5 - 26) or 5
			for x in range(len(lista)):
				mensagem_final += chr(lista[x])
	return mensagem_final

def descriptografar(mensagem, chave=None):
	mensagem_final = ''
	if mensagem:
		lista = []
		if chave:
			mensagem_final = ''
		else:
			for x in range(len(mensagem)):
				lista.append(ord(mensagem[x]))
				lista[x] = chr((lista[x] - 5) > 96 and lista[x] - 5 or \
					(lista[x] - 5) > 64 and lista[x] - 5 or lista[x] -\
					[5 + 26])
			lista.reverse()
			for x in range(len(lista)):
				mensagem_final += lista[x]
	return mensagem_final

