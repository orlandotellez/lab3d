# Lab3D - compass.py
# Brújula 3D pegada a la cámara para orientación en ejes X, Y, Z

from ursina import *
from src.constants import COLOR_UI_FONDO, COLOR_UI_TEXTO, COLOR_UI_CYAN


def create_compass():
    """Crea y retorna la brújula como objeto 3D attached a la cámara."""

    # Crear un holder que será hijo de la cámara - esquina superior derecha
    compass_holder = Entity(
        parent=camera.ui,
        position=(0.85, 0.92),
        scale=(0.25, 0.12),
    )

    # Panel de fondo más visible
    bg = Entity(
        parent=compass_holder,
        model='quad',
        scale=(1, 1),
        color=COLOR_UI_FONDO,
        border_radius=10,
    )

    # Borde decorativo
    border = Entity(
        parent=compass_holder,
        model='quad',
        scale=(1.05, 1.05),
        color=COLOR_UI_CYAN,
    )

    # Texto de dirección cardinal - más grande
    direction_text = Text(
        parent=compass_holder,
        text='N',
        position=(0, 0.15),
        scale=5,
        origin=(0, 0),
        color=COLOR_UI_CYAN,
    )

    # Texto de ejes - más legible
    axes_text = Text(
        parent=compass_holder,
        text='X+ (ESTE)\nY: 2m',
        position=(0, -0.2),
        scale=2,
        origin=(0, 0),
        color=COLOR_UI_TEXTO,
    )

    # Función que actualiza la brújula
    def update_compass():
        # Obtener rotación del player/cámara
        # Primero intentar obtener del player si existe
        if hasattr(camera, 'player'):
            yaw = camera.player.rotation_y
            pitch = camera.player.rotation_x
        else:
            # Usar la cámara directamente
            yaw = camera.rotation_y
            pitch = camera.rotation_x

        # Normalizar yaw a 0-360
        yaw = yaw % 360
        if yaw < 0:
            yaw += 360

        # Determinar dirección cardinal
        if 337.5 <= yaw or yaw < 22.5:
            cardinal = 'N'
        elif 22.5 <= yaw < 67.5:
            cardinal = 'NE'
        elif 67.5 <= yaw < 112.5:
            cardinal = 'E'
        elif 112.5 <= yaw < 157.5:
            cardinal = 'SE'
        elif 157.5 <= yaw < 202.5:
            cardinal = 'S'
        elif 202.5 <= yaw < 247.5:
            cardinal = 'SW'
        elif 247.5 <= yaw < 292.5:
            cardinal = 'W'
        else:
            cardinal = 'NW'

        direction_text.text = cardinal

        # Determinar eje y altura
        height = int(camera.y)

        if abs(pitch) > 45:
            axis = 'Y'
            axis_desc = 'ARRIBA' if pitch < 0 else 'ABAJO'
        else:
            if 45 <= yaw < 135:
                axis = 'Z-'
                axis_desc = 'SUR'
            elif 135 <= yaw < 225:
                axis = 'X-'
                axis_desc = 'OESTE'
            elif 225 <= yaw < 315:
                axis = 'Z+'
                axis_desc = 'NORTE'
            else:
                axis = 'X+'
                axis_desc = 'ESTE'

        axes_text.text = f'{axis} ({axis_desc})\nY: {height}m'

    # Crear secuencia que se repite
    seq = Sequence(0.1, Func(update_compass), loop=True)
    seq.start()

    return compass_holder