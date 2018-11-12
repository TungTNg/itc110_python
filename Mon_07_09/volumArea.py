# volumeArea.py
# a program which calculates the volume and surface are of a sphere from its radius, given as input

import math

def main():
    print('# This is a program which calculates the volume and surface are of a sphere')
    print()
    
    radius = float(input('Enter the radius of the sphere: '))
    volume = 4.0 / 3.0 * math.pi * math.pow(radius, 3)
    area = 4.0 * math.pi * math.pow(radius, 2)
    print()
    
    print('The volume of the sphere is:', round(volume, 5))
    print('The surface are of the sphere is:', round(area, 5))
    
main()
    