import time
import math

def rotate_cube():
    cube = [
        "   +---+---+---+",
        " /           / |",
        "+-----------+  |",
        "|           |  |",
        "|           | /",
        "|           |/",
        "+-----------+"
    ]

    angle = 0
    rotation_speed = 0.1

    while True:
        for i in range(4):
            rotated_cube = []
            rotation_matrix = [
                [math.cos(angle), -math.sin(angle)],
                [math.sin(angle), math.cos(angle)]
            ]

            for line in cube:
                rotated_line = ""
                for char in line:
                    if char == "+":
                        rotated_line += char
                    elif char == "-":
                        rotated_line += char
                    elif char == "|":
                        rotated_line += char
                    elif char == "/":
                        rotated_line += char
                    elif char == "\\":
                        rotated_line += char
                    else:
                        x = line.index(char)
                        y = cube.index(line)
                        rotated_x = round(rotation_matrix[0][0] * x + rotation_matrix[0][1] * y)
                        rotated_y = round(rotation_matrix[1][0] * x + rotation_matrix[1][1] * y)
                        rotated_line += cube[rotated_y][rotated_x]
                rotated_cube.append(rotated_line)

            for line in rotated_cube:
                print(line)
            time.sleep(0.2)
            cube.insert(0, cube.pop())
            angle += rotation_speed

rotate_cube()