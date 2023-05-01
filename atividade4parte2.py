import random


def cria_dois_primos(n_caracteres):
    n_caracteres = max(1, min(n_caracteres, 6))

    limite_inferior = 10 ** (n_caracteres - 1)
    limite_superior = 10 ** n_caracteres - 1

    p = random.randint(limite_inferior, limite_superior)
    q = random.randint(limite_inferior, limite_superior)

    while p == q or p % 2 == 0 or q % 2 == 0:
        p = random.randint(limite_inferior, limite_superior)
        q = random.randint(limite_inferior, limite_superior)

    n_iteracoes = 50
    if not eh_primo_miller_rabin(p, n_iteracoes):
        return cria_dois_primos(n_caracteres)
    if not eh_primo_miller_rabin(q, n_iteracoes):
        return cria_dois_primos(n_caracteres)

    return p, q


def eh_primo_miller_rabin(n, k):
    if n == 2 or n == 3:
        return True
    if n == 1 or n % 2 == 0:
        return False

    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for i in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)


def mdce(a, b):
    if b == 0:
        return [1, 0, a]
    else:
        x, y, d = mdce(b, a % b)
        return [y, x-(a//b) * y, d]


def invmod(a, n):
    if mdc(a, n) != 1:
        return "O inverso modular não existe"
    else:
        x, y, d = mdce(a, n)
        return x % n


def string_para_numeros(mensagem):
    return [ord(c) for c in mensagem]


def numeros_para_string(numeros):
    return ''.join([chr(n) for n in numeros])


def criptografar(mensagem, n, e):
    mensagem_criptografada = []
    mensagem_numero = string_para_numeros(mensagem)
    for mensagem_em_numero in mensagem_numero:
        mensagem_criptografada.append(pow(int(mensagem_em_numero), e, n))
    return mensagem_criptografada


def descriptografar(mensagem_criptografada, n, d):
    mensagem_descriptografada = []
    for mensagem_numerica in mensagem_criptografada:
        mensagem_descriptografada.append(pow(int(mensagem_numerica), d, n))
    return numeros_para_string(mensagem_descriptografada)

decisao = True
while decisao:
    escolha = int(input("Criptografar uma mensagem = 1.\nDecifrar uma mensagem = 2.\nSua escolha: "))
    if escolha == 1:
        m = input("Digite sua mensagem: ")
        k = int(input("Quantidade de algoritmos para criação das chaves: "))

        p, q = cria_dois_primos(k)
        n = p*q
        fn = (p-1) * (q-1)
        e = random.randint(2, fn - 1)
        while mdc(e, fn) != 1:
            e = random.randint(2, fn - 1)
        d = invmod(e, fn)

        print(f"Chave Pública (n,e): {[n, e]}")
        print(f"Chave Privada (n, d): {[n, d]}")

        msg_criptografada = criptografar(m, n, e)
        print(msg_criptografada)
        decisao = False
    elif escolha == 2:
        msg_criptografada = input("Lista da mensagem criptografada: ")
        msg_criptografada = eval(msg_criptografada)

        n = int(input("Chave privada (n): "))
        d = int(input("Chave privada (d): "))
        print(descriptografar(msg_criptografada, n, d))
        decisao = False
    else:
        print("Número invalido. Escolher apenas 1 ou 2.\n")

