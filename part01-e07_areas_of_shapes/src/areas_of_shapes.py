#!/usr/bin/env python3

import math


def main():
    while True:
        shape = input('Choose a shape (triangle, rectangle, circle): ')
        if shape == '':
            break
        else:
            if shape == 'rectangle':
                r_width = int(input("Give width of the rectangle: "))
                r_height = int(input("Give height of the rectangle: "))
                print(f"The area is {r_height * r_width}")
            elif shape == 'triangle':
                t_base = int(input("Give base of the triangle: "))
                t_height = int(input("Give height of the triangle: "))
                print(f"The area is {0.5*t_base*t_height}")
            elif shape == 'circle':
                c_radius = int(input("Give radius of the circle: "))
                print(f"The area is {math.pi * c_radius ** 2}")
            else:
                print('Unknown shape!')


if __name__ == "__main__":
    main()
