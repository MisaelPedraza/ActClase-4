import math
def main():
    #escribe tu código abajo de esta línea
    varphi = (1+sqrt(5))/2
    #print(varphi)
    n = float(input('Número: '))
    d = int(input('Decimales a mostrar: '))
    r = round(n * varphi, d)
    print('Razón áurea:', r)

if __name__ == '__main__':
    main()
