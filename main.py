# Lab3D - main.py
# Entry point del laboratorio 3D

from ursina import *

# Módulos del proyecto
from src.constants import *
from src.room.floor import create_floor
from src.room.walls import create_walls
from src.objects.computer import create_lab_layout
from src.lighting import create_lighting
from entities.player import create_player

# =========================
# APP
# =========================

app = Ursina()

window.title = 'Laboratorio 3D'
window.borderless = False
window.exit_button.visible = False
window.fps_counter.enabled = True


# =========================
# ESCENA
# =========================

create_floor()
create_walls()
create_lab_layout()
create_lighting()
create_player()


# =========================
# EJECUTAR
# =========================

app.run()