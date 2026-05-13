# Sistema de iluminación del laboratorio

from ursina import *
from src.constants import COLOR_LUZ_AMBIENTE


def create_lighting():
    """Crea la iluminación del laboratorio."""
    DirectionalLight(
        y=15,
        z=10,
        shadows=True
    )

    AmbientLight(
        color=COLOR_LUZ_AMBIENTE
    )
