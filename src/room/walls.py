# Lab3D - walls.py
# Las paredes del laboratorio

from ursina import *
from src.constants import AZUL_PARED


def create_walls():
    """Crea las 4 paredes del laboratorio."""
    # Pared trasera
    Entity(
        model='cube',
        scale=(18, 6, 1),
        position=(0, 3, 12),
        color=AZUL_PARED,
        collider='box'
    )

    # Pared frontal
    Entity(
        model='cube',
        scale=(18, 6, 1),
        position=(0, 3, -12),
        color=AZUL_PARED,
        collider='box'
    )

    # Pared izquierda
    Entity(
        model='cube',
        scale=(1, 6, 24),
        position=(-9, 3, 0),
        color=AZUL_PARED,
        collider='box'
    )

    # Pared derecha
    Entity(
        model='cube',
        scale=(1, 6, 24),
        position=(9, 3, 0),
        color=AZUL_PARED,
        collider='box'
    )