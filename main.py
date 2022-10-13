import cmath
from math import atan, sqrt


def convertToPolar(complexNumber):
    realPart = complexNumber.real
    imaginaryPart = complexNumber.imag
    module = sqrt(realPart ** 2 + imaginaryPart ** 2)
    angle = (atan((imaginaryPart / realPart)) * 57.2958)
    #if angle < 0:
        #angle = 180 + angle
    return module, angle


def polarToComplex(r, theta):
    return r * cmath.exp(theta * 1j)


def main():
    print("Elige una opcion")
    print("1. Convertir a polar")
    print("2. Convertir a complejo")
    print("3. Sumar complejos")
    print("4. Restar complejos")
    print("5. Multiplicar complejos")
    print("6. Dividir complejos")

    option = int(input("Opcion: "))
    if option == 1:
        ComplexNumber = complex(input("Ingrese el numero complejo: "))
        Module, Angle = convertToPolar(ComplexNumber)
        print("El modulo es: ", Module)
        print("El angulo es: ", Angle)
    elif option == 2:
        moduloR = float(input("Ingrese el numero "))
        anguloTheta = (float(input("Ingrese el angulo "))) / 180 * cmath.pi
        intensidad = polarToComplex(moduloR, anguloTheta)
        print("La intensidad es: ", intensidad)
    elif option == 3:
        ComplexNumber1 = complex(input("Ingrese el primer numero complejo: "))
        ComplexNumber2 = complex(input("Ingrese el segundo numero complejo: "))
        ComplexNumber3 = ComplexNumber1 + ComplexNumber2
        print("La suma es: ", ComplexNumber3)
    elif option == 4:
        ComplexNumber1 = complex(input("Ingrese el primer numero complejo: "))
        ComplexNumber2 = complex(input("Ingrese el segundo numero complejo: "))
        ComplexNumber3 = ComplexNumber1 - ComplexNumber2
        print("La resta es: ", ComplexNumber3)
    elif option == 5:
        ComplexNumber1 = complex(input("Ingrese el primer numero complejo: "))
        ComplexNumber2 = complex(input("Ingrese el segundo numero complejo: "))
        ComplexNumber3 = ComplexNumber1 * ComplexNumber2
        print("La multiplicacion es: ", ComplexNumber3)
    elif option == 6:
        ComplexNumber1 = complex(input("Ingrese el primer numero complejo: "))
        ComplexNumber2 = complex(input("Ingrese el segundo numero complejo: "))
        ComplexNumber3 = ComplexNumber1 / ComplexNumber2
        print("La division es: ", ComplexNumber3)


if __name__ == '__main__':
    main()
