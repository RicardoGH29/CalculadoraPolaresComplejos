import cmath
import math
from math import sqrt, atan


def convertToPolar(complexNumber):
    module, angleRad = cmath.polar(complexNumber)
    angle = math.degrees(angleRad)
    return module, angle


def polarToComplex(r, theta):
    theta = math.radians(theta)
    return r * cmath.exp(theta * 1j)

