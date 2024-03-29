"""Trabalho semestral sobre criptografia."""


def tratar_mensagem(mensagem, chave=None, criptografar=True):
    """."""
    mensagem_final = ''
    if mensagem:
        lista = []
        alt = chave and int(chave) or 5
        for x in range(len(mensagem)):
            lista.append(ord(mensagem[x]))
            if criptografar:
                if 96 < lista[x] < 123:
                    lista[x] += (lista[x] + alt) > 122 and \
                        (alt - 25) or alt
                elif 64 < lista[x] < 91:
                    lista[x] += (lista[x] + alt) > 90 and \
                        (alt - 25) or alt
            else:
                if 96 < lista[x] < 123:
                    lista[x] -= (lista[x] - alt) > 96 and \
                        alt or (alt - 25)
                elif 64 < lista[x] < 91:
                    lista[x] -= (lista[x] - alt) > 64 and \
                        alt or (alt - 25)
            mensagem_final += chr(lista[x])
    print(mensagem_final[::-1])


def tratar_chave(chave):
    """."""
    lista = []
    for x in range(len(chave)):
        if 96 < ord(chave[x]) < 123:
            lista.append(ord(chave[x]) - 96)
        elif 64 < ord(chave[x]) < 91:
            lista.append(ord(chave[x]) - 64)
        elif 48 < ord(chave[x]) < 58:
            lista.append(ord(chave[x]) - 48)
    alt = int(sum(lista) / len(lista))
    return alt

while True:
    crip_decript = input("Deseja criptografar ou descriptografar? (c/d)\n")
    mensagem = input("Insira a mensagem para criptografar" +
                     " ou descriptografar:\n")
    key = input("Insira a chave ou nao escreva " +
                "nada para usar a chave padrao:\n")
    chave = (key.strip()) and tratar_chave(chave=key)
    tratar_mensagem(mensagem=mensagem, chave=chave or None,
                    criptografar=(crip_decript == 'c') and True or False)
    continuar = input("Deseja continuar? (s/n)\n")
    if continuar != "s":
        break
