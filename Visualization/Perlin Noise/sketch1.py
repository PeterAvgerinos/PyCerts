from p5 import *

def setup():
    size(640, 360)
    no_stroke()
    background(204)

def draw():
    if mouse_is_pressed:
        fill(random_uniform(255), random_uniform(127), random_uniform(51), 127)
    else:
        fill(255, 15)

    circle_size = random_uniform(low=10, high=80)

    circle((mouse_x, mouse_y), circle_size)

def key_pressed(event):
    background(204)

# p5 supports different backend to render sketches, viz "vispy" for both 2D and 3D sketches and "skia" for 2D sketches
# Default renderer is set to "vispy"
run(renderer="vispy")

