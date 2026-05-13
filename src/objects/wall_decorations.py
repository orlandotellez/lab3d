# Decoraciones de pared: TV, pizarra, aire acondicionado, cubo

from ursina import *
from src.constants import COLOR_PIZARRA, COLOR_TV, COLOR_AIRE_CUERPO, COLOR_AIRE_REJA, COLOR_PUERTA, COLOR_PUERTA_NEGRA


def create_tv(x_center, wall_z, sign=1):
    """Crea un TV en la pared."""
    face_z = wall_z - sign * 0.5
    z = face_z - sign * 0.03
    Entity(model='cube',
           scale=(7, 4, 0.05),
           rotation=(0, -30, 0),
           position=(x_center, 3.8, z), color=COLOR_TV)


def create_front_tv():
    """Crea el TV de la pared frontal."""
    create_tv(-5, 10, sign=1)


def create_blackboard(x_center, wall_z, sign=1):
    """Crea una pizarra en la pared."""
    face_z = wall_z - sign * 0.5
    z = face_z - sign * 0.03
    Entity(model='cube',
           scale=(7, 3.8, 0.05),
           position=(x_center, 3.5, z), color=COLOR_PIZARRA)


def create_front_blackboard():
    """Crea la pizarra de la pared frontal."""
    create_blackboard(3, 11.8, sign=1)


def create_air_conditioner_side(x_center, wall_z, sign=1):
    """Crea un aire acondicionado en pared lateral."""
    face_z = wall_z - sign * 0.5
    z = face_z - sign * 0.03

    # Cuerpo principal
    Entity(model='cube',
           scale=(0.4, 1.8, 5),
           position=(x_center, 5.2, z),
           color=COLOR_AIRE_CUERPO)

    # Raja negra por donde sale el aire
    Entity(model='cube',
           scale=(0.45, 0.15, 4.5),
           position=(x_center, 4.5, z),
           color=COLOR_AIRE_REJA)


def create_front_air_conditioner():
    """Crea el aire acondicionado al lado de la puerta (pared derecha)."""
    create_air_conditioner_side(8.3, -2, sign=-1)


def create_back_cube():
    """Crea un cubo negro en la pared de atrás."""
    Entity(model='cube',
           scale=(2, 2, 10),
           position=(0, 4, -14.7),
           color=COLOR_TV)


def create_back_door(x_center, z_position):
    """Crea una puerta en la pared de atrás, orientada hacia adentro."""
    Entity(model='cube',
           scale=(2, 4, 0.05),
           position=(x_center, 2.5, z_position),
           color=COLOR_PUERTA)


def create_back_black_door(x_center, z_position):
    Entity(model='cube',
           scale=(2, 4, 0.05),
           position=(x_center, 2.5, z_position),
           color=COLOR_PUERTA_NEGRA)


def create_back_doors():
    """Crea dos puertas en la pared de atrás, a la par del cubo."""
    create_back_door(-5.9, -11.3)
    create_back_door(-3, -11.3)
    create_back_black_door(5, -11)
