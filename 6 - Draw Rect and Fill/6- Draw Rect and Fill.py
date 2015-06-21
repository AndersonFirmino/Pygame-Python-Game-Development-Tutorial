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

# While the end of game not comes (gameExit == False)
while not gameExit:

    # Check the events that are hapenning in the game
    for event in pygame.event.get():

        # Print they in console
        print(event)

        # If an event correspond to the exit or quit of PyGame
        if event.type == pygame.QUIT:

            # Change the loop variable to go out of loop
            gameExit = True

    # Change the screen color
    gameDisplay.fill(WHITE)

    # Coordinates and size to draw the black rect
    posBlackRect = {'x': 400, 'y': 300}
    sizeBlackRect = {'x': 10, 'y': 10}

    # Array to the draw function
    arrayBlackRect = (posBlackRect['x'], posBlackRect['y'], sizeBlackRect['x'], sizeBlackRect['y'])

    # Draw the black rect
    pygame.draw.rect(gameDisplay, BLACK, arrayBlackRect)

    # Coordinates and size to draw the red rect
    posRedRect= {'x': 200, 'y': 200}
    sizeRedRect = {'x': 50, 'y': 50}

    # Array to the draw function
    arrayRedRect = (posRedRect['x'], posRedRect['y'], sizeRedRect['x'], sizeRedRect['y'])

    # Draw the red rect
    pygame.draw.rect(gameDisplay, RED, arrayRedRect )

    # Render on screen
    pygame.display.update()
                                
    

# Unintilize the modules that have previously initialized 
pygame.quit()

# Quit the surface (End of the program)
quit()

#  Another function to update the screen
# pygame.display.flip() # BOTTOM NOTES 2


#=========================================================================
# BOTTOM NOTES

"""
1 - pygame.display.setmode returns a surface that is, nothing more than a
a blank surface to draw things

2 - pygame.display.flip() is the previous and disoptimized  version of pygame.display.update().
".update" haves the improvement to only update a specific part of the surface, if some correctly argumment
was passed

"""
