from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

window.title = 'Laboratorio 3D'
window.borderless = False
window.exit_button.visible = False
window.fps_counter.enabled = True


# =========================
# COLORES
# =========================

AZUL_PARED = color.hex('#274790')
COLOR_PISO = color.hex('#181825')
COLOR_MESA = color.black


# =========================
# PISO
# =========================

floor = Entity(
    model='cube',
    scale=(22, 1, 26),
    position=(0, -0.5, 0),
    color=COLOR_PISO,
    collider='box'
)


# =========================
# PAREDES
# =========================

# pared trasera
Entity(
    model='cube',
    scale=(18, 6, 1),
    position=(0, 3, 12),
    color=AZUL_PARED,
    collider='box'
)

# pared frontal
Entity(
    model='cube',
    scale=(18, 6, 1),
    position=(0, 3, -12),
    color=AZUL_PARED,
    collider='box'
)

# pared izquierda
Entity(
    model='cube',
    scale=(1, 6, 24),
    position=(-9, 3, 0),
    color=AZUL_PARED,
    collider='box'
)

# pared derecha
Entity(
    model='cube',
    scale=(1, 6, 24),
    position=(9, 3, 0),
    color=AZUL_PARED,
    collider='box'
)


# =========================
# FUNCION CREAR PC
# =========================

def crear_pc(x, z):

# una sola mesa para las 4 computadoras (más ancha)
    Entity(
        model='cube',
        scale=(7, 0.2, 1.2),
        position=(x, 1, z),
        color=COLOR_MESA,
        collider='box'
    )

    # base sólida de madera negra (cubrimiento completo)
    Entity(
        model='cube',
        scale=(7, 0.8, 1.2),
        position=(x, 0.6, z),
        color=COLOR_MESA,
        collider='box'
    )

   
    # crear 4 computadoras por mesa
    for i in range(4):
        offset_x = (i - 1.5) * 2  # más espacio entre PCs
        
        # monitor
        Entity(
            model='cube',
            scale=(0.9, 0.6, 0.08),
            position=(x + offset_x, 1.55, z),
            color=color.black
        )

        # pantalla
        Entity(
            model='cube',
            scale=(0.75, 0.45, 0.01),
            position=(x + offset_x, 1.55, z - 0.045),
            color=color.azure
        )

        # base monitor
        Entity(
            model='cube',
            scale=(0.08, 0.3, 0.08),
            position=(x + offset_x, 1.25, z),
            color=color.gray
        )

        # teclado
        Entity(
            model='cube',
            scale=(0.8, 0.05, 0.3),
            position=(x + offset_x, 1.12, z - 0.35),
            color=color.dark_gray
        )


# =========================
# DISTRIBUCION
# =========================

# 2 columnas x 4 mesas = 8 mesas, cada una con 4 PCs = 32 computadoras
columnas = [-5, 5]  # más separadas para un pasillo más amplio

for col_idx, x in enumerate(columnas):
    for fila in range(4):
        z = -9 + (fila * 5)  # menos espacio entre mesas
        crear_pc(x=x, z=z)


# =========================
# ILUMINACION
# =========================

DirectionalLight(
    y=15,
    z=10,
    shadows=True
)

AmbientLight(
    color=color.rgba(120, 120, 120, 0.4)
)


# =========================
# JUGADOR
# =========================

player = FirstPersonController(
    position=(0, 2, 0),
    speed=5
)

player.gravity = 1


# =========================
# EJECUTAR
# =========================

app.run()
