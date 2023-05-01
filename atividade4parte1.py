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
            mult = mult * (a**2**i % n)
    return mult % n

a = int(input("Base a: "))
b = int(input("Expoente b: "))
n = int(input("Modulo n: "))


print("{} elevado a {} modulo {} é igual a ".format(a,b,n) + str(mdc_exp(a,b,n)))