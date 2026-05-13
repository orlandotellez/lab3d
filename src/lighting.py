# Sistema de iluminación del laboratorio

from ursina import *


def create_lighting():
    """Crea la iluminación del laboratorio."""
    DirectionalLight(
        y=15,
        z=10,
        shadows=True
    )

    AmbientLight(
        color=color.rgba(120, 120, 120, 0.4)
    )
