# Lab3D - walls.py
# Las paredes del laboratorio

from ursina import *
from src.constants import AZUL_PARED

COLOR_MARCO   = color.black
COLOR_CRISTAL = color.rgb(140, 200, 230)

def create_window(z_center, wall_x, sign=1):
    face_x = wall_x - sign * 0.5
    x      = face_x - sign * 0.03

    # Marco: 1.8 x 1.8
    Entity(
        model='cube',
        scale=(0.05, 3.5, 3),
        position=(x, 4.0, z_center),
        color=COLOR_MARCO,
    )
    # Cristal: 1.5 x 1.5 
    Entity(
        model='cube',
        scale=(0.05, 3, 2.3),
        position=(x - sign * 0.001, 4.0, z_center),
        color=COLOR_CRISTAL,
    )

def create_side_window_row(wall_x, sign=1):
    for i in range(3):
        create_window(-9 + i * 2.5, wall_x, sign)
    for i in range(3):
        create_window(0.7 + i * 2.5, wall_x, sign)

def create_walls():
    Entity(model='cube', scale=(18,6,1), position=(0,3,12),
           color=AZUL_PARED, collider='box')
    Entity(model='cube', scale=(18,6,1), position=(0,3,-12),
           color=AZUL_PARED, collider='box')

    Entity(model='cube', scale=(1,6,24), position=(-9,3,0),
           color=AZUL_PARED, collider='box')
    create_side_window_row(-9, sign=-1)

    Entity(model='cube', scale=(1,6,24), position=(9,3,0),
           color=AZUL_PARED, collider='box')
    create_side_window_row(9, sign=1)
