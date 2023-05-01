
def binario(n):
    if n == 0:
        return '0'

    base2 = ''
    while n > 0:
        resto = n % 2
        base2 = str(resto) + base2
        n //= 2

    return base2

def mdc_exp(a, b, n):
    n_binario = binario(b)
    mult = 1

    for i in range(len(n_binario)):
        if n_binario[i] == '1':
            exp = 1
            for j in range(i):
                exp = (exp * 2) % n
            mult = mult * ((a ** exp) % n)

    return mult % n

a, b, n = map(int, input("Digite a base a, o expoente b e o módulo n, separados por espaço: ").split())

resultado = mdc_exp(a, b, n)

print(f"{a} elevado a {b} modulo {n} é igual a {resultado}")
