# El piso del laboratorio

from ursina import *
from src.constants import COLOR_PISO


def create_floor():
    """Crea el piso del laboratorio."""
    return Entity(
        model='cube',
        scale=(22, 1, 26),
        position=(0, -0.5, 0),
        color=COLOR_PISO,
        collider='box'
    )
