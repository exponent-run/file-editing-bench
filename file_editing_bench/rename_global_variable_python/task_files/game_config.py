# Global configuration for the game engine
GAME_SPD = 60  # Frames per second for the game loop

def initialize_game():
    global GAME_SPD
    print(f"Initializing game with {GAME_SPD} FPS")
    return GAME_SPD

def update_game_speed(new_speed):
    global GAME_SPD
    if 30 <= new_speed <= 144:
        GAME_SPD = new_speed
        return True
    return False

def get_frame_delay():
    # Calculate delay between frames in milliseconds
    return 1000 / GAME_SPD

class GameEngine:
    def __init__(self):
        self.frame_rate = GAME_SPD
    
    def run(self):
        while True:
            delay = 1000 / GAME_SPD
            # Game loop implementation...
            break  # Placeholder to avoid infinite loop

# Example usage
if __name__ == "__main__":
    engine = GameEngine()
    print(f"Current game speed: {GAME_SPD}")
    update_game_speed(120)
    print(f"Updated game speed: {GAME_SPD}")