"""Trabalho semestral sobre criptografia."""


def tratar_mensagem(mensagem, chave=None, criptografar=True):
    """."""
    mensagem_final = ''
    if mensagem:
        print('Chegamos entao na funcao que vai criptografar a mensagem')
        lista = []
        alt = chave and int(chave) or 5
        if criptografar:
            print('Caso nao receba valor da chamada da funcao cada caractere' +
                  ' ira ser movido 5 casas, exemplo: A ira se tornar F')
            if chave:
                print(chave and 'No caso a funcao recebeu o valor de ' +
                      str(chave) + ' entao A se torna ' + chr(64 + alt))
        else:
            print('Caso nao receba valor da chamada da funcao cada caractere' +
                  ' ira ser movido 5 casas, exemplo: F ira se tornar A')
            if chave:
                print(chave and 'No caso a funcao recebeu o valor de ' +
                      str(chave) + ' entao A se torna ' + chr(64 - alt + 25))
        for x in range(len(mensagem)):
            lista.append(ord(mensagem[x]))
            if lista[x] == 32 and criptografar:
                pass
            else:
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
        print('Depois de transformar a frase obtemos a mensagem: ' +
              mensagem_final + '\nE por fim invertemos a mensagem obtendo:')
    print(mensagem_final[::-1])


def tratar_chave(chave):
    """."""
    lista = []
    print("Recebemos a chave desejada\nEm seguida transformamos todos os" +
          " caracteres em valores da tabela ASCII\nApos isso subtraimos os"
          " valores para que A seja igual a 1, B igual a 2 e assim por"
          " diante")
    for x in range(len(chave)):
        if ord(chave[x]) == 32:
            pass
        else:
            if 96 < ord(chave[x]) < 123:
                lista.append(ord(chave[x]) - 96)
            elif 64 < ord(chave[x]) < 91:
                lista.append(ord(chave[x]) - 64)
            elif 48 < ord(chave[x]) < 58:
                lista.append(ord(chave[x]) - 48)
    print('Terminamos com uma lista, somamos todos os valores da lista e ' +
          'dividimos pela quantidade de valores na lista')
    alt = int(sum(lista) / len(lista))
    print('O resultado e o valor ' + str(alt))
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
