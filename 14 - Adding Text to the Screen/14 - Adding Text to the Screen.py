# Libaries import

import pygame
#==============================================================================
# Functions

# Show a message on screen
def MessageToScreen(msg, color):

    # Standard font to screen output
    FONT = pygame.font.SysFont(None, 25) # CHANGE THIS VALUES TO MEANING VALUES

    # Configure the font that will be printed with a text message, ? argumment and with a color
    screenText = FONT.render(msg, True, color)

    # Continue by here...



# Primary function
def Main():

    # Initialize PyGame (return sucessful inicialization or not)
    pygame.init()

    # Define some colors (RGB)
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)

    # The defined size of the screen
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 800
    SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

    # Camera view for the player see the game
    gameDisplay = pygame.display.set_mode(SCREEN_SIZE) # BOTTOM NOTE 1

    # Set the title of window
    pygame.display.set_caption('Slither')

    # Tells the the game will not quit or finish by now
    gameExit = False

    # Coordinates and size to draw the Snake
    posSnake = {'x': SCREEN_WIDTH / 2, 'y': SCREEN_HEIGHT / 2}
    sizeSnake = {'x': 10, 'y': 10}

    # Receive values to exchange the Snake position
    changePos = {'x': 0, 'y': 0}

    # Tells how much the snake position will change
    BLOCK_CHANGE = 10

    # Tells how many frames the computer will show for second
    FPS = 15

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
                    changePos['x'] = -BLOCK_CHANGE
                    changePos['y'] = 0

                # If the player press the left key
                elif event.key == pygame.K_RIGHT:

                    # Make the snake go right on screen
                    changePos['x'] = BLOCK_CHANGE
                    changePos['y'] = 0

                elif event.key == pygame.K_UP:

                    # Make the snake go up on screen
                    changePos['y'] = -BLOCK_CHANGE
                    changePos['x'] = 0

                elif event.key == pygame.K_DOWN:

                    # Make the snake go down on screen
                    changePos['y'] = BLOCK_CHANGE
                    changePos['x'] = 0

                # If the snake overpass the limits of screen...
                if posSnake['x'] < 0 or posSnake['x'] >= SCREEN_WIDTH or posSnake['y'] < 0 or posSnake['y'] >= SCREEN_HEIGHT:

                    # End the game
                    gameExit = True

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
        clock.tick(FPS) # BOTTOM NOTE 2

    # Unintilize the modules that have previously initialized 
    pygame.quit()

    # Quit the surface (End of the program)
    quit()
    
#================================================================================
# Game execution
Main()


#================================================================================
# BOTTOM NOTES
"""
1 - pygame.display.setmode returns a surface that is, nothing more than a
a blank surface to draw things

2- Avoide change the Frames per Second to turn the difficulty or speed of your game,
because change it cause more processing than just change the coordinates or other
variables

"""
