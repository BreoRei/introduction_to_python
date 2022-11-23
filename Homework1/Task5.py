from math import hypot

# 5.Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D и 3D пространстве.


def point_coordinates():
    point_a = input("Введите координаты точки А разделенных пробелом: ").split()
    point_b = input("Введите координаты точки B разделенных пробелом: ").split()
    a_list = [int(i) for i in point_a]
    b_list = [int(i) for i in point_b]
    if len(a_list) == 2:
        dot_in_2d = round(hypot(b_list[0] - a_list[0], b_list[1] - a_list[1]), 2)
        print(f'Расстояние между точками А и В в 2D пространстве = {dot_in_2d}')
    elif len(a_list) == 3:
        dot_in_3d = round(hypot(b_list[0] - a_list[0], b_list[1] - a_list[1], b_list[2] - a_list[2]), 2)
        print(f'Расстояние между точками А и В в 3D пространстве = {dot_in_3d}')
    else:
        print('Для таких координат точек A и В невозможно найти точку')


point_coordinates()
