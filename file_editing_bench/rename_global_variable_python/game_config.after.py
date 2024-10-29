# Global configuration for the game engine
FRAMES_PER_SECOND = 60  # Frames per second for the game loop

def initialize_game():
    global FRAMES_PER_SECOND
    print(f"Initializing game with {FRAMES_PER_SECOND} FPS")
    return FRAMES_PER_SECOND

def update_game_speed(new_speed):
    global FRAMES_PER_SECOND
    if 30 <= new_speed <= 144:
        FRAMES_PER_SECOND = new_speed
        return True
    return False

def get_frame_delay():
    # Calculate delay between frames in milliseconds
    return 1000 / FRAMES_PER_SECOND

class GameEngine:
    def __init__(self):
        self.frame_rate = FRAMES_PER_SECOND
    
    def run(self):
        while True:
            delay = 1000 / FRAMES_PER_SECOND
            # Game loop implementation...
            break  # Placeholder to avoid infinite loop

# Example usage
if __name__ == "__main__":
    engine = GameEngine()
    print(f"Current game speed: {FRAMES_PER_SECOND}")
    update_game_speed(120)
    print(f"Updated game speed: {FRAMES_PER_SECOND}")