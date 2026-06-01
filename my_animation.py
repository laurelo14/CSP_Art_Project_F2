import simple_animation as sa
import math
import random
import time
randInt = 20
octopus = {"x": 400, "y": 300, "w": 120, "h": 124, "eyeRadius": 8, "state": "idle"}
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
    
    # Example Animation: A moving fish (a little more complicated) with changing colors
    
  #  repeat_fish = 300 # number of frames to repeat
  #  color_hue = (frame_number % repeat_fish) / repeat_fish
 #   fish_color = sa.hls_to_rgb_hex(color_hue, 0.5, 1.0)
    
  #  x_fish = sa.oscillate_frames(0, width-50, repeat_fish, frame_number)
  #  y_fish = sa.oscillate_motion(height//2, height//2 +100, 0.15, frame_number)
    
  #  if (frame_number % repeat_fish)  < (repeat_fish // 2):
  #      sa.draw_fish(x_fish, y_fish, 50, fish_color, "right")
  #  else:
  #      sa.draw_fish(x_fish, y_fish, 50, fish_color, "left")
    global randInt
    global foodObject
    
    repeat_octopus = 60

    if (frame_number % repeat_octopus == 0):
        randInt = random.randint(0,20)
        
    
    
    #leftClickX, leftClickY = sa._leftClick_x, sa._leftClick_y
    
    
    #if (leftClickX - 20 <mouseX <leftClickX  + 20) and (leftClickY - 20 <mouseY <leftClickY  + 20):
    
    
    
    
    
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
    mX, mY = sa.get_mouse_x(), sa.get_mouse_y()
    
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
        

