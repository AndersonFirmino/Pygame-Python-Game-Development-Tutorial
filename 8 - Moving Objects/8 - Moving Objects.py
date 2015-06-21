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
changePos = {'x': 0}

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

                # The change variable will make the snake go left on screen
                changePos['x'] = - 10

            # If the player press the left key
            if event.key == pygame.K_RIGHT:

                # The change variable will make the snake go right on screen
                changePos['x'] = 10

    # Change the snake position
    posSnake['x'] += changePos['x']

    # Clean the screen 
    gameDisplay.fill(WHITE)

    # Array to the draw function
    arraySnake = (posSnake['x'], posSnake['y'], sizeSnake['x'], sizeSnake['y'])

    # Draw the Snake
    pygame.draw.rect(gameDisplay, BLACK, arraySnake)

    # Render on screen
    pygame.display.update()

# Unintilize the modules that have previously initialized 
pygame.quit()

# Quit the surface (End of the program)
quit()


#=========================================================================
# BOTTOM NOTES

"""
1 - pygame.display.setmode returns a surface that is, nothing more than a
a blank surface to draw things


"""
