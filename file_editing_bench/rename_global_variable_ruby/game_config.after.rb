# Global configuration for the Pixel Adventure game engine
$display_resolution = {width: 1920, height: 1080}

module GameEngine
  class Display
    def self.initialize_screen
      puts "Initializing display with resolution #{$display_resolution[:width]}x#{$display_resolution[:height]}"
      @window_size = $display_resolution
    end
  end

  class AssetLoader
    def self.scale_sprites
      scale_factor = ($display_resolution[:width] / 1920.0)
      puts "Scaling game assets by factor of #{scale_factor}"
    end
  end
end

# Example usage
if __FILE__ == $PROGRAM_NAME
  GameEngine::Display.initialize_screen
  GameEngine::AssetLoader.scale_sprites
  
  # Allow runtime resolution changes
  $display_resolution = {width: 1280, height: 720}
  GameEngine::Display.initialize_screen
end