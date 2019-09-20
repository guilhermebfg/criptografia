def criptografar(mensagem, chave=None):
	mensagem_final = ''
	if mensagem:
		lista = []
		alt = chave and int(chave) or 5
		for x in range(len(mensagem)):
			lista.append(ord(mensagem[x]))
			if lista[x] == 32:
				pass
			else:
				if 96 < lista[x] < 123:
					lista[x] += (lista[x] + alt) > 122 and \
						(alt - 26) or alt
				elif 64 < lista[x] < 91:
					lista[x] += (lista[x] + alt) > 90 and \
						(alt - 26) or alt
			mensagem_final += chr(lista[x])
	return mensagem_final[::-1]

def descriptografar(mensagem, chave=None):
	mensagem_final = ''
	if mensagem:
		lista = []
		if chave:
			mensagem_final = ''
		else:
			for x in range(len(mensagem)):
				lista.append(ord(mensagem[x]))
				lista[x] = chr((lista[x] - alt) > 96 and lista[x] - alt or \
					(lista[x] - alt) > 64 and lista[x] - alt or lista[x] -\
					[alt + 26])
			lista.reverse()
			for x in range(len(lista)):
				mensagem_final += lista[x]
	return mensagem_final
