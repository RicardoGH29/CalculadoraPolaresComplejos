import cmath
import math
from math import sqrt, atan


def convertToPolar(complexNumber):
    realPart = complexNumber.real
    imaginaryPart = complexNumber.imag
    module = sqrt(realPart ** 2 + imaginaryPart ** 2)
    angle = (atan((imaginaryPart / realPart)) * 57.2958)
    #if angle < 0:
        #angle = 180 + angle
    return module, angle


def polarToComplex(r, theta):
    theta = math.radians(theta)
    return r * cmath.exp(theta * 1j)

