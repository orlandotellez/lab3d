# Lab3D - objects/walls.py
# Elementos de pared: ventanas, puertas, cortinas

from ursina import *
from src.constants import AZUL_VENTANA

COLOR_MARCO = color.black
COLOR_PARED = color.hex('#5b667d')
COLOR_CORITNAS = color.hex('#7f716e')


def create_window(z_center, wall_x, sign=1):
    """Crea una ventana con marco y vidrio."""
    face_x = wall_x - sign * 0.5
    x = face_x - sign * 0.03
    Entity(model='cube', scale=(0.05, 3.5, 3),
           position=(x, 4.0, z_center), color=COLOR_MARCO)
    Entity(model='cube', scale=(0.05, 3, 2.3),
           position=(x - sign * 0.001, 4.0, z_center), color=AZUL_VENTANA)


def create_side_window_row(wall_x, sign=1):
    """Crea una fila de ventanas en una pared lateral."""
    for i in range(3):
        create_window(-9 + i * 2.5, wall_x, sign)
    for i in range(3):
        create_window(0.7 + i * 2.5, wall_x, sign)


def create_door(z_center, wall_x, sign=1):
    """Crea una puerta."""
    face_x = wall_x - sign * 0.5
    x = face_x - sign * 0.03
    Entity(model='cube', scale=(0.05, 5, 3),
           position=(x, 2.0, z_center), color=COLOR_PARED)


def create_side_door(wall_x, sign=1):
    """Crea una puerta en una pared lateral."""
    create_door(9.5, wall_x, sign)


def create_curtain(x_center, wall_z, sign=1):
    """Crea una cortina."""
    face_z = wall_z - sign * 0.5
    z = face_z - sign * 0.03
    Entity(model='cube', scale=(20, 4, 0.05),
           position=(x_center, 4, z), color=COLOR_CORITNAS)


def create_front_back_curtains():
    """Crea cortinas en las paredes frontal y trasera."""
    for x in (-8, 8):
        create_curtain(x, 12, sign=1)