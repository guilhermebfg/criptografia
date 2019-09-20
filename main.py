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
					if 96 < lista[x] < 123:
						lista[x] += (lista[x] + 5) > 122 and \
							(5 - 26) or 5
					elif 64 < lista[x] < 91:
						lista[x] += (lista[x] + 5) > 90 and \
							(5 - 26) or 5
			for x in range(len(lista)):
				chave_final += chr(lista[x])
	return chave_final
