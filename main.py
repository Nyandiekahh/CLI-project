import json
import random
import pygame
from player import Player
from game_state import GameState

pygame.init()
pygame.mixer.init()

# ANSI color codes
class Colors:
    """
    ANSI color codes for console output.
    """
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'

