# Lab3D - walls.py
# Las paredes del laboratorio

from ursina import *
from src.constants import AZUL_PARED, AZUL_VENTANA, COLOR_CORTINA, COLOR_TV

COLOR_MARCO = color.black
COLOR_PARED = color.hex('#5b667d')
COLOR_CORITNAS = color.hex('#7f716e')
COLOR_PIZARRA = color.hex('#b8b6b7')

def create_window(z_center, wall_x, sign=1):
    face_x = wall_x - sign * 0.5
    x      = face_x - sign * 0.03
    Entity(model='cube', scale=(0.05, 3.5, 3),
           position=(x, 4.0, z_center), color=COLOR_MARCO)
    Entity(model='cube', scale=(0.05, 3, 2.3),
           position=(x - sign * 0.001, 4.0, z_center), color=AZUL_VENTANA)

def create_side_window_row(wall_x, sign=1):
    for i in range(3):
        create_window(-9 + i * 2.5, wall_x, sign)
    for i in range(3):
        create_window(0.7 + i * 2.5, wall_x, sign)

def create_door(z_center, wall_x, sign=1):
    face_x = wall_x - sign * 0.5
    x      = face_x - sign * 0.03
    Entity(model='cube', scale=(0.05, 5, 3),
           position=(x, 2.0, z_center), color=COLOR_PARED)

def create_side_door(wall_x, sign=1):
    create_door(9.5, wall_x, sign)

def create_curtain(x_center, wall_z, sign=1):
    face_z = wall_z - sign * 0.5
    z      = face_z - sign * 0.03
    Entity(model='cube', scale=(20, 4, 0.05),
           position=(x_center, 4, z), color=COLOR_CORITNAS)

def create_front_back_curtains():
    for x in (-8, 8):
        create_curtain(x, 12, sign=1)

def create_tv(x_center, wall_z, sign=1):
    face_z = wall_z - sign * 0.5
    z      = face_z - sign * 0.03
    Entity(model='cube', 
           scale=(7, 4, 0.05),
         rotation=(0, -30, 0),  
           position=(x_center, 3.8, z), color=color.black)

def create_front_tv():
    create_tv(-5, 10, sign=1)   # ← llama a create_tv, centrada en x=0

def create_blackboard(x_center, wall_z, sign=1):
    face_z = wall_z - sign * 0.5
    z      = face_z - sign * 0.03
    Entity(model='cube', 
           scale=(7, 3.8, 0.05),
           position=(x_center, 3.5, z), color=COLOR_PIZARRA)

def create_front_blackboard():
    create_blackboard(3, 11.8, sign=1)   # ← llama a create_tv, centrada en x=0


def create_walls():
    Entity(model='cube', scale=(18,6,1), position=(0,3,12),
           color=AZUL_PARED, collider='box')
    Entity(model='cube', scale=(18,6,1), position=(0,3,-12),
           color=AZUL_PARED, collider='box')
    create_side_door(7.8, sign=-1)
    create_front_back_curtains()
    create_front_tv()
    create_front_blackboard()
    Entity(model='cube', scale=(1,6,24), position=(-9,3,0),
           color=AZUL_PARED, collider='box')
    create_side_window_row(-9, sign=-1)
    Entity(model='cube', scale=(1,6,24), position=(9,3,0),
           color=AZUL_PARED, collider='box')
    create_side_window_row(9, sign=1)
