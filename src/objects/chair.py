# Lab3D - chair.py
# Sillas de oficina reclinables

from ursina import *
import math
from src.constants import COLOR_PLATEADO, COLOR_PLATEADO_OSCURO, AZUL_BASE


def create_chair(x, z, angle=0):
    """Crea una silla de oficina reclinable plateada con patas azules.

    Args:
        x: Posición X de la silla
        z: Posición Z de la silla
        angle: Ángulo de rotación de la silla
    """

    # Grupo para rotar toda la silla
    chair = Entity(position=(x, 0, z), rotation_y=angle)

    # =========================
    # PATAS (plateadas, 4 patas en las esquinas)
    # =========================

    posiciones = [
        (0.22, 0.22),   # frente derecha
        (-0.22, 0.22),  # frente izquierda
        (0.22, -0.22),  # atrás derecha
        (-0.22, -0.22)  # atrás izquierda
    ]

    for pat_x, pat_z in posiciones:
        Entity(
            model='cube',
            scale=(0.08, 0.5, 0.08),
            position=(pat_x, 0.25, pat_z),
            color=COLOR_PLATEADO,
            parent=chair
        )

    # =========================
    # ESTRUCTURA (plateado)
    # =========================

    # Plataforma del asiento
    Entity(
        model='cube',
        scale=(0.5, 0.08, 0.5),
        position=(0, 0.54, 0),
        color=COLOR_PLATEADO,
        parent=chair
    )

    # =========================
    # ASIENTO (azul - cojín)
    # =========================

    # Cojín azul
    Entity(
        model='cube',
        scale=(0.35, 0.06, 0.35),
        position=(0, 0.61, 0),
        color=AZUL_BASE,
        parent=chair
    )

    # =========================
    # RESPALDO (plateado, reclinable)
    # =========================

    # Estructura del respaldo
    Entity(
        model='cube',
        scale=(0.48, 0.7, 0.08),
        position=(0, 0.9, -0.21),
        rotation_x=-10,  # Reclinado hacia atrás
        color=COLOR_PLATEADO,
        parent=chair
    )

    # Cojín del respaldo (azul)
    Entity(
        model='cube',
        scale=(0.35, 0.4, 0.04),
        position=(0, 0.95, -0.18),
        rotation_x=-10,
        color=AZUL_BASE,
        parent=chair
    )

    # =========================
    # SOPORTE RESPALDO
    # =========================

    # Barra que conecta respaldo con el asiento
    Entity(
        model='cube',
        scale=(0.06, 0.35, 0.06),
        position=(0, 0.55, -0.17),
        rotation_x=-10,
        color=COLOR_PLATEADO_OSCURO,
        parent=chair
    )

    return chair