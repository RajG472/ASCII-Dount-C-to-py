import math
import os
import time

# Function to get ANSI color codes
def set_color(color):
    colors = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m"
    }
    return colors.get(color.lower(), "\033[37m")  # default white

# Get user input
size = int(input("Enter size (1-10): "))
color_input = input("Enter color (e.g., red, green, blue): ")
color = set_color(color_input)

A, B = 0, 0
R1, R2 = 1, 2
K2 = 5

# Adjust donut size
R2 = R2 + (size - 5) * 0.2
K1 = 10 / (R1 + R2)

print("\033[2J")  # clear screen

while True:
    b = [' '] * 1760
    z = [0] * 1760

    j = 0
    while j < 6.28:
        i = 0
        while i < 6.28:
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e

            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * n + t * m))
            o = int(x + 80 * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))

            if 22 > y > 0 and 0 < x < 80 and D > z[o]:
                z[o] = D
                b[o] = ".,-~:;=!*#$@"[N if N > 0 else 0]
            i += 0.02
        j += 0.07

    print("\033[H", end="")  # move cursor home
    for k in range(1760):
        print(color + b[k], end=("" if k % 80 else "\n"))
    A += 0.04
    B += 0.02
    time.sleep(0.03)
