import pygame

# Initialize PyGame (return sucessful inicialization or not)
sucessInit = pygame.init()

# Test to see if the inicialization ocorred right
#print sucessInit

# The defined size of the screen
SCREEN_SIZE = (600,800)

# Camera view for the player see the game
gameDisplay = pygame.display.set_mode(SCREEN_SIZE) # BOTTOM NOTE 1

# Update the screen
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
