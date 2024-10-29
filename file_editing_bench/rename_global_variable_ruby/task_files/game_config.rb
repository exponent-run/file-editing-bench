# Global configuration for the Pixel Adventure game engine
$screen_res = {width: 1920, height: 1080}

module GameEngine
  class Display
    def self.initialize_screen
      puts "Initializing display with resolution #{$screen_res[:width]}x#{$screen_res[:height]}"
      @window_size = $screen_res
    end
  end

  class AssetLoader
    def self.scale_sprites
      scale_factor = ($screen_res[:width] / 1920.0)
      puts "Scaling game assets by factor of #{scale_factor}"
    end
  end
end

# Example usage
if __FILE__ == $PROGRAM_NAME
  GameEngine::Display.initialize_screen
  GameEngine::AssetLoader.scale_sprites
  
  # Allow runtime resolution changes
  $screen_res = {width: 1280, height: 720}
  GameEngine::Display.initialize_screen
end