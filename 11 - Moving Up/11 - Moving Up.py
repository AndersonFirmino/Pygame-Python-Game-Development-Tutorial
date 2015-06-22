import pygame

# Initialize PyGame (return sucessful inicialization or not)
pygame.init()

# Define some colors (RGB)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

# The defined size of the screen
SCREEN_SIZE = (600,800)

# Camera view for the player see the game
gameDisplay = pygame.display.set_mode(SCREEN_SIZE) # BOTTOM NOTE 1

# Set the title of window
pygame.display.set_caption('Slither')

# Tells the the game will not quit or finish by now
gameExit = False

# Coordinates and size to draw the Snake
posSnake = {'x': 300, 'y': 300}
sizeSnake = {'x': 10, 'y': 10}

# Receive values to exchange the Snake position
changePos = {'x': 0, 'y': 0}

# Receive a clock to control Frames per second
clock = pygame.time.Clock()

# While the end of game not comes (while gameExit == False)
while not gameExit:

    # Check the events that are hapenning in the game
    for event in pygame.event.get():

        # Print they in console
        print(event)

        # If an event correspond to the exit or quit of PyGame
        if event.type == pygame.QUIT:

            # Change the loop variable to go out of loop
            gameExit = True

        # If the player press some key...
        if event.type == pygame.KEYDOWN:

            # If the player press the left key
            if event.key == pygame.K_LEFT:

                # Make the snake go left on screen
                changePos['x'] = - 10
                changePos['y'] = 0

            # If the player press the left key
            elif event.key == pygame.K_RIGHT:

                # Make the snake go right on screen
                changePos['x'] = 10
                changePos['y'] = 0

            elif event.key == pygame.K_UP:

                # Make the snake go up on screen
                changePos['y'] = -10
                changePos['x'] = 0

            elif event.key == pygame.K_DOWN:

                # Make the snake go down on screen
                changePos['y'] = 10
                changePos['x'] = 0

    # Change the snake position
    posSnake['x'] += changePos['x']
    posSnake['y'] += changePos['y']

    # Clean the screen 
    gameDisplay.fill(WHITE)

    # Array to the draw function
    arraySnake = (posSnake['x'], posSnake['y'], sizeSnake['x'], sizeSnake['y'])

    # Draw the Snake
    pygame.draw.rect(gameDisplay, BLACK, arraySnake)

    # Render on screen
    pygame.display.update()

    # Control the update with Frames per second
    clock.tick(15) # BOTTOM NOTE 2

# Unintilize the modules that have previously initialized 
pygame.quit()

# Quit the surface (End of the program)
quit()


#=========================================================================
# BOTTOM NOTES

"""
1 - pygame.display.setmode returns a surface that is, nothing more than a
a blank surface to draw things

2- Avoide change the Frames per Second to turn the difficulty or speed of your game,
because change it cause more processing than just change the coordinates or other
variables

"""
