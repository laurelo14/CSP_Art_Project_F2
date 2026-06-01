import simple_animation as sa


def draw_frame(frame_number, elapsed_seconds, width, height):
    """Draws one frame of an animation. Called approx 60 times per second."""
    

        # Draws a blue ocean starting at the left edge (x=0) and halfway down the screen (y=300)
    sa.draw_ocean(0, 50, "#008CFF")                 # 1. Background layer: New Royal Blue (Higher up)
    sa.draw_foreground_ocean(0, 200, "#5CBAFF")      # 2. Foreground layer: New slightly darker light blue (Lower down)0)
    
    # Draws a smooth, brownish-yellow wavy sand layer at the bottom 10% of a 600px tall canvas
    sa.draw_wavy_sand(0, 540, "#D2B48C", 100)
    
    sa.set_line_thickness(5)
    sa.set_outline_color("green")
    sa.draw_curve([(700, 600), (600, 500), (700, 400)])
    sa.draw_curve([(700, 400), (800, 300), (700, 200)])
    sa.draw_curve([(750, 650), (650, 550), (750, 450)])
    sa.draw_curve([(750, 450), (850, 350), (700, 200)])
    
    sa.draw_seaweed(200, 600, 0.5, "green")
    sa.draw_seaweed(150, 600, 1, "green")
    sa.set_outline_color("#5d6e5f")
    sa.draw_seaweed(100, 600, 1.6, "#5d6e5f")
    

    sa.set_line_thickness(0)
    sa.set_outline_color("#b8d3ff")
    sa.draw_dolphin(300, 100, 2, "#b8d3ff")

    
    
       #bubbles, starfish, shark angie
    sa.draw_circle(700, 380, 25)
    sa.set_fill_color("white")

    sa.draw_circle(40, 50, 20)
    sa.set_fill_color("white")

    sa.draw_circle(200, 500, 10)
    sa.set_fill_color("white")

    sa.draw_circle(300, 35, 10)
    sa.set_fill_color("white")

    sa.draw_circle(350, 30, 5)
    sa.set_fill_color("white")

    sa.draw_circle(500, 200, 20)
    sa.set_fill_color("white")
    
    sa.draw_circle(400, 300, 40)
    sa.set_fill_color("white")

    sa.draw_circle(200, 290, 20)
    sa.set_fill_color("white")

     sa.draw_circle(100, 500, 20)
    sa.set_fill_color("white")

    sa.draw_starfish(500, 300, 50, "yellow", 6)
    
    sa.draw_shark(500,300,200,"blue", "left")
    
if __name__ == "__main__":
        # Launch the wrapper and tell it to use our draw_frame function
    sa.start(draw_frame)

