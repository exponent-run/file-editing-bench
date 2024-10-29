# Main game configuration settings
import pygame
from typing import Tuple

# Controls the frame rate of the game engine
GAME_SPD = 60

def get_display_settings() -> Tuple[int, int]:
    """Returns the display width and height based on game speed"""
    if GAME_SPD <= 30:
        return (800, 600)  # Lower resolution for slower speeds
    else:
        return (1920, 1080)

def update_game_timing(delta_time: float) -> float:
    """Calculate the game timing based on frame rate"""
    return delta_time * (60 / GAME_SPD)

def initialize_game() -> None:
    """Sets up the game with the configured speed"""
    pygame.init()
    clock = pygame.time.Clock()
    clock.tick(GAME_SPD)
    print(f"Game initialized at {GAME_SPD} FPS")

def get_animation_frames(total_frames: int) -> int:
    """Calculate animation frames based on game speed"""
    return int(total_frames * (GAME_SPD / 60))
