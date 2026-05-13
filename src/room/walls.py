# Las paredes del laboratorio 

from ursina import *
from src.constants import AZUL_PARED
from src.objects.walls import (
    create_side_door,
    create_front_back_curtains,
    create_side_window_row,
)
from src.objects.wall_decorations import (
    create_front_tv,
    create_front_blackboard,
    create_front_air_conditioner,
    create_back_cube,
    create_back_doors,
)


def create_walls():
    """Crea todas las paredes del laboratorio."""

    # Pared frontal (dividida en dos mitades)
    # Mitad inferior (color original)
    Entity(model='cube', scale=(18, 3, 1), position=(0, 1.5, 12),
           color=AZUL_PARED, collider='box')
    # Mitad superior (blanco)
    Entity(model='cube', scale=(18, 3, 1), position=(0, 4.5, 12),
           color=color.white, collider='box')

    # Pared trasera (dividida en dos mitades)
    Entity(model='cube', scale=(18, 3, 1), position=(0, 1.5, -12),
           color=AZUL_PARED, collider='box')
    Entity(model='cube', scale=(18, 3, 1), position=(0, 4.5, -12),
           color=color.white, collider='box')

    create_side_door(7.8, sign=-1)
    create_front_back_curtains()
    create_front_tv()
    create_front_blackboard()
    create_front_air_conditioner()
    create_back_cube()
    create_back_doors()

    # Pared izquierda (dividida en dos mitades)
    Entity(model='cube', scale=(1, 3, 24), position=(-9, 1.5, 0),
           color=AZUL_PARED, collider='box')
    Entity(model='cube', scale=(1, 3, 24), position=(-9, 4.5, 0),
           color=color.white, collider='box')
    create_side_window_row(-9, sign=-1)

    # Pared derecha (dividida en dos mitades)
    Entity(model='cube', scale=(1, 3, 24), position=(9, 1.5, 0),
           color=AZUL_PARED, collider='box')
    Entity(model='cube', scale=(1, 3, 24), position=(9, 4.5, 0),
           color=color.white, collider='box')
    create_side_window_row(9, sign=1)
