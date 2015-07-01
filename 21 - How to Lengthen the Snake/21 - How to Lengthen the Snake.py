# Libaries import

import pygame
import time
import random
#==============================================================================
# Functions

# Finish the game process (pygame surface)
def GameExit():

    # Unintilize the modules that have previously initialized 
    pygame.quit()

    # Quit the surface (End of the program)
    quit()
    
#============================================================================== 
# Show a message on screen
def MessageToScreen(gameDisplay, textPos,msg, color):

    # Type of font (ex: "arial", "comicsansms", "None")
    typeFont = None

    # Size of the font
    sizeFont = 25

    # Standard font to screen output
    FONT = pygame.font.SysFont(typeFont, sizeFont)

    # Tells if the text will be smooth borders or not
    ANTIALIAS = True

    # Put the text on a new surface (PyGame not provides a way to do that in a existing surface)
    screenText = FONT.render(msg, ANTIALIAS, color)

    # Put the surface screenText on the gameDisplay surface 
    gameDisplay.blit(screenText, textPos)

     # Render the text on screen
    pygame.display.update()
    
#==============================================================================
# Draw a snake
def DrawSnake(surface, color, snakeCoord, blockSize):

    # Constants to a better representation
    
    X_AXIS = 0
    Y_AXIS = 1

    # For each coordinate in the list of snake coordinates (take only the coordinate, not the list of coordinates)
    for XnY in snakeCoord:

        # Draw the current part of snake
        pygame.draw.rect(surface, color, [XnY[X_AXIS], XnY[Y_AXIS], blockSize,blockSize])

#==============================================================================
# Primary module
def Main():

    # Initialize PyGame (return sucessful inicialization or not)
    pygame.init()

    # Define some colors (RGB)
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    GREEN = (0, 155, 0)

    # The defined size of the screen
    SCREEN_WIDTH = 800   
    SCREEN_HEIGHT = 600
    SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

    # Camera view for the player see the game
    gameDisplay = pygame.display.set_mode(SCREEN_SIZE) # BOTTOM NOTE 1

    # Title of the window representing the name of the game
    GAME_NAME = "Slither"
    
    # Set the title of window
    pygame.display.set_caption(GAME_NAME)

    # Tells the the game will not quit or finish by now
    gameLoop = True

    # Tells to the game receive actions until the end of the game
    gameOver = False

    # Size of the blocks of the game
    BLOCK_SIZE = 10
    
    # Coordinates to put text on screen
    textScreen = (SCREEN_WIDTH / 2 ,  SCREEN_HEIGHT / 2)

    # Receive values to exchange the Snake position
    changePos = {'x': 0, 'y': 0} 

    # Tells how much the snake position will change
    BLOCK_CHANGE = 10

    # Tells how many frames the computer will show for second
    FPS = 15

    # Receive a clock to control Frames per second
    clock = pygame.time.Clock()

    # The size of the apple puts limits in the last possible and random position on screen
    SCREEN_LIMIT = {'x': SCREEN_WIDTH - BLOCK_SIZE, 'y': SCREEN_HEIGHT - BLOCK_SIZE }

    # While in the game loop
    while gameLoop == True:

        # Initialize the vector of vectors to store coordinates of the snake    
        snakeCoord = []

        # Start with the snake with one block size
        snakeLength = 1

        # Put the snake in the inital position
        posSnake = {'x': SCREEN_WIDTH / 2, 'y': SCREEN_HEIGHT / 2}

        # Generate an random x and y axis positions
        randomX = random.randrange(0, SCREEN_LIMIT['x'], BLOCK_SIZE)
        randomY = random.randrange(0, SCREEN_LIMIT['y'], BLOCK_SIZE)

        # Create an apple in a random position
        posApple = {'x': randomX, 'y': randomY}

        # While the not game over...
        while gameOver == False:

            # Check the events that are hapenning in the game
            for event in pygame.event.get():

                # Print they in console
                print(event)

                # If the event correspond to the exit or quit of PyGame
                if event.type == pygame.QUIT:

                    # Finish the game process
                    GameExit()

                # If the player press some key...
                elif event.type == pygame.KEYDOWN:

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

            # Change the snake position
            posSnake['x'] += changePos['x']
            posSnake['y'] += changePos['y']

            # If the snake position is same as the apple 
            if posSnake['x'] == posApple['x'] and posSnake['y'] == posApple['y']:

                # Snake eat the apple, so...

                # Snake grows
                snakeLength += 1

                # Generate an random x and y axis positions
                randomX = random.randrange(0, SCREEN_LIMIT['x'], BLOCK_SIZE)
                randomY = random.randrange(0, SCREEN_LIMIT['y'], BLOCK_SIZE)

                # Create a new apple in a random position
                posApple = {'x': randomX, 'y': randomY}

                # Create an apple in a random position
                posApple = {'x': randomX, 'y': randomY}

            # Or if the snake overpass the limits of screen # BOTTOM NOTE 3
            elif posSnake['x'] < 0 or posSnake['x'] >= SCREEN_WIDTH or posSnake['y'] < 0 or posSnake['y'] >= SCREEN_HEIGHT:

                # Put end in the play, in the next iterative in while loop
                gameOver = True

            # Store the position of the only part of snake
            snakeHead = []

            # Receive the position of the snake head
            snakeHead.append(posSnake['x'])
            snakeHead.append(posSnake['y'])

            # Receive coordinates of the blocks
            snakeCoord.append(snakeHead)

            # If the actual size of snake is bigger than the defined size (apples that ate + 1)
            if len(snakeCoord) > snakeLength:

                # Delete the last block of the snake (keep the defined size on screen)
                del snakeCoord[0]

            # Clean the screen 
            gameDisplay.fill(WHITE)

            # Draw the snake on screen
            DrawSnake(gameDisplay, GREEN, snakeCoord, BLOCK_SIZE)

            # Apple array to the draw function
            arrayApple = (posApple['x'] , posApple['y'], BLOCK_SIZE, BLOCK_SIZE)

            # Draw the Apple
            pygame.draw.rect(gameDisplay, RED, arrayApple)

            # Render on screen
            pygame.display.update()

            # Check if the snake make a collision with itself...
            # Begin from the second element
            for snakePart in snakeCoord[:-1]: # '[:-1]' Begin to check after the last elemment (snake head)

                # If a collision happened with snake head
                if snakeHead == snakePart:

                    # Snake died. Game over
                    gameOver = True

            # Control the update with Frames per second
            clock.tick(FPS) # BOTTOM NOTE 2

        # Clear the screen
        gameDisplay.fill(WHITE)
        
        # Output game over message
        MessageToScreen(gameDisplay, textScreen, "GAME OVER! Try Again? (y / n)", RED)

        # Confirm if the player answered above question or not
        playerAnswer = False

        # While player not answer the question...
        while playerAnswer == False:

            # Check for player answer
            for event in pygame.event.get():

                # Print the events in console
                print(event)

                # If the event correspond a press of a key...
                if event.type == pygame.KEYDOWN:                     
                
                    # If the player pressed the 'y' button
                    if event.key == pygame.K_y:

                        # Restart the game loop
                        gameOver = False
                        playerAnswer = True

                    # If the player pressed the 'n' button
                    elif event.key == pygame.K_n:

                        # Turn the variable value to go out the loop (end of the game)
                        gameLoop = False
                        playerAnswer = True

                # If the event correspond to the exit or quit of PyGame
                elif event.type == pygame.QUIT:

                        # Finish the game process
                        GameExit()


    # Finish the game process
    GameExit()
        
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

3 - This is be impossible if the first condition is true, because the position of the apple
can be only a valid position on the screen, and not off it

"""
