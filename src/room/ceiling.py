# El techo del laboratorio

from ursina import *
from src.constants import COLOR_PISO, COLOR_TECHO, COLOR_TECHO_BORDE


def create_ceiling():
    """Crea el techo del laboratorio con rectángulos grandes."""

    # Techo principal
    Entity(
        model='cube',
        scale=(22, 0.2, 26),
        position=(0, 7, 0),
        color=COLOR_TECHO,
        collider='box'
    )

    # Patrón de rectángulos grandes con lados grises
    # Dimensiones de los rectángulos del patrón
    rect_width = 4
    rect_depth = 4
    rect_height = 0.1  # Altura del borde del rectángulo
    gap = 0.3  # Espacio entre rectángulos

    # Crear grilla de rectángulos
    for x in range(-8, 9, rect_width + int(gap)):
        for z in range(-10, 11, rect_depth + int(gap)):
            # Posición del rectángulo
            pos_x = x + rect_width / 2
            pos_z = z + rect_depth / 2
            pos_y = 6.05  # Debajo del techo

            # Crear los 4 lados del rectángulo (borde de color gris)
            side_thickness = 0.1

            # Lado frontal
            Entity(
                model='cube',
                scale=(rect_width, rect_height, side_thickness),
                position=(pos_x, pos_y, pos_z + rect_depth / 2),
                color=COLOR_TECHO_BORDE
            )

            # Lado trasero
            Entity(
                model='cube',
                scale=(rect_width, rect_height, side_thickness),
                position=(pos_x, pos_y, pos_z - rect_depth / 2),
                color=COLOR_TECHO_BORDE
            )

            # Lado izquierdo
            Entity(
                model='cube',
                scale=(side_thickness, rect_height, rect_depth),
                position=(pos_x - rect_width / 2, pos_y, pos_z),
                color=COLOR_TECHO_BORDE
            )

            # Lado derecho
            Entity(
                model='cube',
                scale=(side_thickness, rect_height, rect_depth),
                position=(pos_x + rect_width / 2, pos_y, pos_z),
                color=COLOR_TECHO_BORDE
            )
