import simple_animation as sa


def draw_frame(frame_number, elapsed_seconds, width, height):
    """Draws one frame of an animation. Called approx 60 times per second."""
    
    #sa.fill_background("blue")
    
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

    
if __name__ == "__main__":
        # Launch the wrapper and tell it to use our draw_frame function
    sa.start(draw_frame)
