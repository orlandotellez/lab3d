# Lab3D - player.py
# Controlador del jugador en primera persona

from ursina.prefabs.first_person_controller import FirstPersonController


def create_player():
    """Crea el jugador en primera persona."""
    player = FirstPersonController(
        position=(0, 2, 0),
        speed=5
    )

    player.gravity = 1

    return player