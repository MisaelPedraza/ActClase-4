import math
def main():
    #escribe tu código abajo de esta línea
    from math import sqrt
    x1 = int(input('x1= '))
    y1 = int(input('y1= '))
    x2 = int(input('x2= '))
    y2 = int(input('y2= '))
    d = sqrt(((x2-x1)**2) + ((y2-y1)**2))
    print('distancia=', d)

if __name__ == '__main__':
    main()
