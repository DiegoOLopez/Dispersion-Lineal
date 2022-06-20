###### LIBRERIAS IMPORTADAS ######
import array
import math
import matplotlib.pyplot as plt

def main():
    ###### CONTADOR ######
    i = 0
    ###### VARIABLES PRINCIPALES ######
    valorX = []
    valorY = []
    valor = []
    ###### OPERACIONES PRIMARIAS ######
    valorXY = []
    valorX2 = []
    valorY2 = []
    sumaR = 0
    sumaX = 0
    sumaY = 0
    sumaXY = 0
    sumaX2 = 0
    sumaY2 = 0
    ###### INSTRUCCION REPETICION __AGREGAR MAS CONDICIONES PARA EVITAR ERRORES__ ######
    repeticion = int(input("Ingresa el numero de valores: "))


    if repeticion <= 0:
        print("Error en la ejecucion del programa, ingrese un valor positivo")
    elif repeticion == 1:
        print("Hay en total " + str(repeticion) + " valor")
    elif repeticion >= 2:
        print("Hay en total " + str(repeticion) + " valores")
    else:
        print("Ingrese un dato valido")
    

    ###### REGISTRO DE DATOS ######
    for i in range(1, repeticion + 1):
        valor.append(i)
        valorX.append(int(input("Ingresa el " + str(i) + " valor de X: ")))
        valorY.append(int(input("Ingresa el " + str(i) + " valor de Y: ")))
    

    # print(valor)
    # print(valorX)
    # print(valorY)


    ###### OBTENCION DE XY, X^2, Y^2
    for i in range(0, repeticion):
        valorXY.append(valorX[i]*valorY[i])
        valorX2.append(valorX[i]**2)
        valorY2.append(valorY[i]**2)
        sumaR += valor[i]
        sumaX += valorX[i]
        sumaY += valorY[i]
        sumaXY += valorXY[i]
        sumaX2 += valorX2[i]
        sumaY2 += valorY2[i]

    ##### IMPRESION DE TABLA ####

    print('######################################################')
    print('#   N   #   X   #   Y   #   XY   #   X^2   #   Y^2   #')
    print('#-------#-------#-------#--------#---------#---------#')
    for l in range(0 , repeticion):
        print('#   ' + str(valor[l]) + '   #   ' + str(valorX[l]) + '   #   ' + str(valorY[l]) + '   #    ' + str(valorXY[l]) +  '    #   ' + str(valorX2[l]) + '    #    ' + str(valorY2[l]) + "    #")
    print('#=======#=======#=======#========#=========#=========#')
    print('#   ' + str(sumaR) + '   #   ' + str(sumaX) + '   #   ' + str(sumaY) + '   #    ' + str(sumaXY) +  '    #   ' + str(sumaX2) + '    #    ' + str(sumaY2) + "    #")
    print('######################################################')

    # print(valorXY)
    # print(valorX2)
    # print(valorY2)
    # print(sumaX)
    ###### DECLARACION DE VARIABLES Y PROMEDIOS ######
    n = repeticion
    proXN = sumaX/n
    proYN = sumaY/n
    ###### OBTENCION DE B ######
    valorB = (sumaXY - n * (proXN) * (proYN)) / (sumaX2 - n * (proXN)**2)
    ###### OBTENCION DE A ######
    valorA = (proYN) - ((valorB) * (proXN))

    ###### IMPRESION DE VALORES A Y B ######
    print('El valor de b es: ' + str(valorB))
    print('El valor de a es: ' + str(valorA))
    ###### OBTENCION DE VARIABLES INDEPENDIENTES ###### 
    valoresI = []
    repeticionVI = int(input("¿Cuantos valores independientes habra en la graficacion?: "))


    for j in range(1, repeticionVI + 1):
        valoresI.append(int(input("Ingresa el " + str(j) + " valor independiente: ")))
    
    ##### Calculo del valor de X y tambien de Y
    valorI = max(valoresI)
    GraficacionY = (valorA) + ((valorB)*(valorI))
    GraficacionX = max(valorX)
    
    ###### Se ######
    Se = 0.0
    Se = math.sqrt((sumaY2)-((valorA)*(sumaY))-((valorB)*(sumaXY)))/(n-2)
    # print(Se)

    ###### R cuadrada ######
    r2 = (((valorA)*(sumaY))+((valorB)*(sumaXY))-((n)-proYN**2))/((sumaY2)-((n)-proYN**2))
    # print(r2)

    ###### Raiz cuadrada de R cuadrada ######
    raizR = math.sqrt(r2)
    # print(raizR)
    ###### IMPRESION DE VARIABLES
    for m in range(1, repeticionVI + 1):
        GraficacionR = (valorA) + ((valorB)*(valorI))
        print('El valor de Y' + str(m) + '  es de: ' + str(GraficacionR))
    print('El valor de Se es: ' + str(Se))
    print('El valor de R cuadrada es: ' + str(r2))
    print('El valor de la raiz de R cuadrada es de ' + str(raizR))
    ###### CANVAS ######
    x = valorX
    y = valorY

    xa = [0, GraficacionX]
    ya = [valorA, GraficacionY]

    plt.plot(x,y, 'o', label= "datos")
    plt.plot(xa,ya, label= "linea")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.title('Grafica de corelacion')
    plt.legend(loc=4)
    plt.show()

if __name__ == '__main__':
    main()