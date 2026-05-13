# Estaciones de trabajo con PCs

from ursina import *
import math
from src.constants import COLOR_MESA, COLOR_MONITOR, COLOR_PANTALLA, COLOR_BASE_MONITOR, COLOR_TECLADO
from src.objects.chair import create_chair


def create_computer_station(x, z):
    """Crea una estación de trabajo con 4 computadoras."""

    # Mesa única para las 4 PCs (más ancha)
    Entity(
        model='cube',
        scale=(7, 0.2, 1.2),
        position=(x, 1, z),
        color=COLOR_MESA,
        collider='box'
    )

    # Base sólida de madera negra (cubrimiento completo)
    Entity(
        model='cube',
        scale=(7, 0.8, 1.2),
        position=(x, 0.6, z),
        color=COLOR_MESA,
        collider='box'
    )

    # Crear 4 computadoras por mesa
    for i in range(4):
        offset_x = (i - 1.5) * 2  # más espacio entre PCs

        # Monitor
        Entity(
            model='cube',
            scale=(0.9, 0.6, 0.08),
            position=(x + offset_x, 1.55, z),
            color=COLOR_MONITOR
        )

        # Pantalla
        Entity(
            model='cube',
            scale=(0.75, 0.45, 0.01),
            position=(x + offset_x, 1.55, z - 0.045),
            color=COLOR_PANTALLA
        )

        # Base monitor
        Entity(
            model='cube',
            scale=(0.08, 0.3, 0.08),
            position=(x + offset_x, 1.25, z),
            color=COLOR_BASE_MONITOR
        )

        # Teclado
        Entity(
            model='cube',
            scale=(0.8, 0.05, 0.3),
            position=(x + offset_x, 1.12, z - 0.35),
            color=COLOR_TECLADO
        )

        # Silla (detrás de cada compu, orientada hacia la mesa)
        create_chair(x=x + offset_x, z=z - 1.5)


def create_lab_layout():
    """Crea la distribución completa del laboratorio."""
    # 2 columnas x 4 mesas = 8 mesas, cada una con 4 PCs = 32 computadoras
    columnas = [-5, 5]  # más separadas para un pasillo más amplio

    for col_idx, x in enumerate(columnas):
        for fila in range(4):
            z = -9 + (fila * 5)  # menos espacio entre mesas
            create_computer_station(x=x, z=z)
