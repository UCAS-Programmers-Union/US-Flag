import turtle
turtle.speed(10)
# Using US Flag dimensions found here: https://en.wikipedia.org/wiki/Flag_of_the_United_States#Design

FLAG_WIDTH = 950
FLAG_HEIGHT = 500
CANTON_WIDTH = 380
CANTON_HEIGHT = 269.23
STRIPE_WIDTH_CANTON = 570
STRIPE_WIDTH = 950
STRIPE_HEIGHT = 38.46
STAR_SPACING_X = 31.66
STAR_SPACING_Y = 26.90
STAR_DIAMETER = 12

def create_star(size, color):
    angle = 150
    turtle.fillcolor(color)
    turtle.begin_fill()

    for side in range(5):
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.right(72 - angle)
    turtle.end_fill()

def create_stripe(stripe_width, stripe_height):
    turtle.begin_fill()
    
    for iteration in range(2):
        turtle.forward(stripe_width)
        turtle.right(90)
        turtle.forward(stripe_height)
        turtle.right(90)
    
    turtle.end_fill()

    turtle.up()
    turtle.right(90)
    turtle.forward((stripe_height * 2))
    turtle.left(90)
    turtle.down()

def create_star_rows(canton_width, canton_height, star_spacing_x, star_spacing_y, star_diameter):
    for iteration in range(4):
        for iteration_iteration in range(5):
            create_star(star_diameter, (255, 255, 255))
            turtle.up()
            turtle.forward((star_spacing_x * 2))
            turtle.down()
        create_star(star_diameter, (255, 255, 255))

        turtle.up()
        turtle.right(90)
        turtle.forward(star_spacing_y)
        turtle.right(90)
        turtle.forward(star_spacing_x + star_diameter)
        turtle.down()

        for iteration_iteration in range(4):
            create_star(star_diameter, (255, 255, 255))
            turtle.up()
            turtle.forward((star_spacing_y * 2) + 7)
            turtle.down()
        create_star(star_diameter, (255, 255, 255))

        turtle.up()
        turtle.forward(star_spacing_x)
        turtle.left(90)
        turtle.forward(star_spacing_y)
        turtle.left(90)
        turtle.down()

# Creating the red square on which I will create the stripes and union.
turtle.color((178, 34, 52))

turtle.begin_fill()
for iteration in range(2):
    turtle.forward(FLAG_WIDTH)
    turtle.right(90)
    turtle.forward(FLAG_HEIGHT)
    turtle.right(90)

turtle.end_fill()

# Creating the stripes.
turtle.color((255, 255, 255))

turtle.up()
turtle.forward(380)
turtle.right(90)
turtle.forward(STRIPE_HEIGHT)
turtle.left(90)
turtle.down()

for iteration in range(2):
    create_stripe(STRIPE_WIDTH_CANTON, STRIPE_HEIGHT)

# Manually create the last stripe touching the canton and reposition turtle.
turtle.begin_fill()
    
for iteration in range(2):
    turtle.forward(STRIPE_WIDTH_CANTON)
    turtle.right(90)
    turtle.forward(STRIPE_HEIGHT)
    turtle.right(90)
    
turtle.end_fill()

turtle.up()
turtle.right(90)
turtle.forward((STRIPE_HEIGHT * 2))

# Reposition turtle to front of flag.
turtle.right(90)
turtle.forward(CANTON_WIDTH)
turtle.right(180)
turtle.down()

for iteration in range(2):
    create_stripe(STRIPE_WIDTH, STRIPE_HEIGHT)

# Create the last stripe manually.
turtle.begin_fill()

for iteration in range(2):
    turtle.forward(STRIPE_WIDTH)
    turtle.right(90)
    turtle.forward(STRIPE_HEIGHT)
    turtle.right(90)
    
turtle.end_fill()

turtle.up()

# Reposition the turtle to the starting position.
turtle.home()

# Change color of turtle to blue.
turtle.color((60, 59, 110))

# Create the canton.
turtle.begin_fill()

for iteration in range(2):
    turtle.forward(CANTON_WIDTH)
    turtle.right(90)
    turtle.forward(CANTON_HEIGHT)
    turtle.right(90)

turtle.end_fill()

turtle.up()
turtle.color((255, 255, 255))
turtle.forward(STAR_SPACING_X)
turtle.right(90)
turtle.forward(STAR_SPACING_Y)
turtle.left(90)
turtle.down()
create_star_rows(CANTON_WIDTH, CANTON_HEIGHT, STAR_SPACING_X, STAR_SPACING_Y, STAR_DIAMETER)
for iteration_iteration in range(5):
    create_star(STAR_DIAMETER, (255, 255, 255))
    turtle.up()
    turtle.forward((STAR_SPACING_X * 2))
    turtle.down()
create_star(STAR_DIAMETER, (255, 255, 255))
