import math

def cAOC(radius):
    Area=math.pi*radius**2
    return Area

def cMpg(miles, gallons):
    MPG = miles/gallons
    return MPG

def cFTC(F):
    C = (F - 32) * 5 / 9
    return C

def cDBP(x,y,x1,y1):
    c=math.sqrt((x1-x)**2+(y1-y)**2)
    return c