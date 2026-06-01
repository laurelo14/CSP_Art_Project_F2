import simple_animation as sa
import math
import random
import time
randInt = 20
octopus = {"x": 300, "y": 450, "w": 180, "h": 186, "eyeRadius": 12, "state": "idle"}
#foodObject = {"x": 0, "y": 0, "h" : 50, "w" : 50, "c" : "blue", "eaten": False}


#def draw_object():
    
#    sa.set_fill_color(foodObject["c"])
#    oval(foodObject["x"],foodObject["y"],foodObject["w"],foodObject["h"])

def oval(center_x,center_y,width,height):
    """Draws a solid circle given its center point and radius."""
    width = width//2
    height = height//2
    sa._canvas.create_oval(center_x - width, center_y - height, center_x + width, center_y + height, 
                        fill=sa._fill_color, outline=sa._outline_color, width=sa._line_thickness)

def tentacle(startX, startY, endX, endY,height):
    #add mid modi
    midX = (startX + endX)//2
    midY = (startY + endY)//2
    points = [
        (startX, startY),
        (midX, midY+(height//3)),
        (endX, endY),
        (endX, endY),]
    sa._canvas.create_polygon(points, fill=sa._fill_color, outline=sa._outline_color, width=sa._line_thickness,smooth=1)
    
def draw_octopus(centreX,centreY,width,height, eyes):
    # add food and stuff. interactivity.
    # draws an octopus
    # DUPLICATED makes the point SHARP.
    # import random and mouse might be able to move the octopus
    # mouse moves objects to octopus to interact with
    # SEE canvas.bind(sequence,callback)
    # "<Button-1>"
    # fromsimpleanimationstarter: def update_mouse(event):
    #    global _mouse_x, _mouse_y
    #    _mouse_x = event.x
    #    _mouse_y = event.y
    #_canvas.bind('<Motion>', update_mouse)
    
    sa.set_fill_color("red")
    
  
    
    
    
    
    length = width
    offset = height//4
    
    tentacle(centreX,centreY+offset,centreX-length,centreY+length,height)
    tentacle(centreX,centreY+offset,centreX+length,centreY+length,height)
    tentacle(centreX,centreY+offset,centreX-length,centreY,height)
    tentacle(centreX,centreY+offset,centreX+length,centreY,height)
    
    oval(centreX,centreY,width,height)
    if eyes == "open":
        sa.set_fill_color("blue")
    else:
        pass
    eyeOffset = width//2
    sa.fill_circle(centreX-eyeOffset,centreY,octopus["eyeRadius"])
    sa.fill_circle(centreX+eyeOffset,centreY,octopus["eyeRadius"])
    
    if eyes == "closed":
        sa.draw_line(centreX-eyeOffset+octopus["eyeRadius"],centreY,centreX-eyeOffset-octopus["eyeRadius"],centreY)
        sa.draw_line(centreX+eyeOffset+octopus["eyeRadius"],centreY,centreX+eyeOffset-octopus["eyeRadius"],centreY)
    
    



def draw_frame(frame_number, elapsed_seconds, width, height):
    """Draws one frame of an animation. Called approx 60 times per second."""
    

    sa.fill_background("white") # Clear the background for this frame
   
     # Example Animation: A moving circle
   # x_ball = sa.loop_motion(0, width, 5.0, frame_number) # x coordinate
    
    #sa.set_fill_color("red")
    
   # sa.fill_circle(x_ball, height / 2, 40)


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
    

    global randInt

    
    repeat_octopus = 60

    if (frame_number % repeat_octopus == 0):
        randInt = random.randint(0,20)
        
    
    
    #leftClickX, leftClickY = sa._leftClick_x, sa._leftClick_y
    
    
    #if (leftClickX - 20 <mouseX <leftClickX  + 20) and (leftClickY - 20 <mouseY <leftClickY  + 20):
    


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
    

    
    w_octopus = sa.oscillate_frames(octopus["w"],octopus["w"]+randInt,repeat_octopus, frame_number)
    h_octopus = sa.oscillate_frames(octopus["h"],octopus["h"]-randInt,repeat_octopus, frame_number)
    if octopus["state"] == "idle":
        if (frame_number % repeat_octopus)  < (repeat_octopus // 2):
            if (frame_number % repeat_octopus*12)< (repeat_octopus // 2)and randInt>15:
                draw_octopus(octopus["x"],octopus["y"],w_octopus,h_octopus,"closed")
            else:
                draw_octopus(octopus["x"],octopus["y"],w_octopus,h_octopus,"open")
        
            
        
        else:
            draw_octopus(octopus["x"],octopus["y"],w_octopus,h_octopus,"open")
            
        #sa.draw_fish(x_fish, yoctopus["eyeRadius"_fish, 50, fish_color, "left")

    #if (octopus["x"]- octopus["w"]//2 <mX< octopus["x"] + octopus["w"]//2) and (octopus["y"]- octopus["h"]//2 <mX< octopus["y"] + octopus["h"]//2):
    #    foodObject["eaten"] = True
    #    octopus["state"] = "active"
    #    time1 = time.datetime.now()
    #    print(time1)
    #    if time1 > time.datetime.now +2:
    #        print("done")
    
   # if foodObject["eaten"] == False:
        
    #    foodObject["x"], foodObject["y"] = mX, mY
    #    draw_object()
    #
    #draw_octopus(400,300,400,400)
    
    # Draw the information text
    #sa.set_fill_color("black")
    #sa.draw_text(40, 50, f"Frame number: {frame_number}")
    #sa.draw_text(40, 80, f"Elapsed Time: {elapsed_seconds:.1f} seconds")
    #sa.draw_text(40, 110, f"Mouse x: {sa.get_mouse_x()}")
    #sa.draw_text(40, 140, f"Mouse y: {sa.get_mouse_y()}")
    #sa.draw_text(40, 160, f"click x: {sa._leftClick_x}")
    #sa.draw_text(40, 180, f"click y: {sa._leftClick_y}")





if __name__ == "__main__":
        # Launch the wrapper and tell it to use our draw_frame function
    sa.start(draw_frame)


