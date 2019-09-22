"""Essa caceta."""


def criptografar(mensagem, chave=None):
    """."""
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
                        (alt - 25) or alt
                elif 64 < lista[x] < 91:
                    lista[x] += (lista[x] + alt) > 90 and \
                        (alt - 25) or alt
            mensagem_final += chr(lista[x])
    print(mensagem_final[::-1])


def descriptografar(mensagem, chave=None):
    """."""
    mensagem_final = ''
    if mensagem:
        lista = []
        alt = chave and int(chave) or 5
        for x in range(len(mensagem)):
            lista.append(ord(mensagem[x]))
            print(lista)
            if 96 < lista[x] < 123:
                lista[x] -= (lista[x] - alt) > 96 and \
                    alt or (alt - 25)
            elif 64 < lista[x] < 91:
                lista[x] -= (lista[x] - alt) > 64 and \
                    alt or (alt - 25)
            lista[x] = chr(lista[x])
            mensagem_final += lista[x]
    print(mensagem_final[::-1])


def tratar_chave(chave):
    """."""
    lista = []
    for x in range(len(chave)):
        if ord(chave[x]) == 32:
            pass
        else:
            if 96 < ord(chave[x]) < 123:
                lista.append(ord(chave[x]) - 96)
            elif 64 < ord(chave[x]) < 91:
                lista.append(ord(chave[x]) - 64)
    alt = int(sum(lista) / len(lista))
    print(alt)
    return alt

continuar = 's'

while continuar == 's':
    crip_decript = input("Deseja criptografar ou criptografar? (c/d)\n")
    string = input("Insira a mensagem para criptografar ou descriptografar:\n")
    key = input("Insira a chave ou nao escreva " +
                "nada para usar a chave padrao:\n")
    if key != "" and key != " ":
        chave = tratar_chave(chave=key)
    else:
        chave = None
    if crip_decript == 'c':
        criptografar(mensagem=string, chave=chave or None)
    else:
        descriptografar(mensagem=string, chave=chave or None)
    continuar = input("Deseja continuar? (s/n)\n")
