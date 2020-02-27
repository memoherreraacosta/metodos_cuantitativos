from math import sqrt, log, cos, sin, pi

def box_muller(r1, r2):
    x1 = sqrt(-2*log(r1))*cos(2*r2*pi)
    x2 = sqrt(-2*log(r2))*sin(2*r1*pi)
    return x1, x2
