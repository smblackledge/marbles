# Importing and initializing Pygame
import pygame
import random


class Gameboard:
    screen = pygame.Surface
    size = (840, 820)  # Opening and setting the window size

    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    BROWN = (247, 199, 141)

    edge = 3
    indent = 30
    side = 300
    width = side / 2

    margin = edge + indent
    x0 = margin
    y0 = margin

    # important x locations, left to right
    left = x0
    leftMiddle = x0 + side
    rightMiddle = x0 + side + width
    right = x0 + side + width + side

    # important y locations, top to bottom
    top = y0
    topMiddle = y0 + side
    bottomMiddle = y0 + side + width
    bottom = y0 + side + width + side

    #
    # Draw a blank board
    #
    layout = [
        [(left, topMiddle), (leftMiddle, topMiddle)],
        [(leftMiddle, topMiddle), (leftMiddle, top)],
        [(leftMiddle, top), (rightMiddle, top)],
        [(rightMiddle, top), (rightMiddle, topMiddle)],
        [(rightMiddle, topMiddle), (right, topMiddle)],
        [(right, topMiddle), (right, bottomMiddle)],
        [(right, bottomMiddle), (rightMiddle, rightMiddle)],
        [(rightMiddle, rightMiddle), (rightMiddle, bottom)],
        [(rightMiddle, bottom), (leftMiddle, bottom)],
        [(leftMiddle, bottom), (leftMiddle, bottomMiddle)],
        [(leftMiddle, bottomMiddle), (left, bottomMiddle)],
        [(left, bottomMiddle), (left, topMiddle)]
    ]

    def drawboard(self):
        for i in self.layout:
            pygame.draw.line(self.screen, self.BROWN, i[0], i[1], self.edge)


class Player:
    done = False  # Loop until the user clicks the close button.

    #
    # return random number from 1 to 6
    #
    def rolldie(self):
        return random.randrange(1, 7)


    #
    # main routine
    #
    def marbles(self):
        board.screen = pygame.display.set_mode(Gameboard.size)

        # Initialize the game engine
        pygame.init()

        pygame.display.set_caption("Marbles (the game)")  # Setting the window title
        clock = pygame.time.Clock()  # Used to manage how fast the screen updates

        # -------- Main Program Loop -----------
        while not self.done:
            # --- Main event loop
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:
                    print("Quitting")# If user clicked close
                    mygame.done = True  # Flag that we are done so we exit this loop

            # --- Game logic should go here

            # --- Drawing code should go here

            # First, clear the screen to white. Don't put other drawing commands
            # above this, or they will be erased with this command.
            board.screen.fill(board.WHITE)
            board.drawboard()
            myroll = self.rolldie()

            pygame.display.flip()  # --- Go ahead and update the screen with what we've drawn.

            clock.tick(60)  # --- Limit to 60 frames per second

        pygame.quit()  # Proper shutdown of a Pygame program


board = Gameboard()
mygame = Player()
mygame.marbles()
exit(0)

# input("Pause for enter...")

# --line--
# Draw on the screen a green line from (0, 0) to (100, 100)
# that is 5 pixels wide.
# pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
#
# --rectangle--
# Draw a rectangle
# pygame.draw.rect(screen, BLACK, [20, 20, 250, 100], 2)
#
# --ellipse--
# Draw an ellipse, using a rectangle as the outside boundaries
# pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)
#
# --arc--
# Draw an arc as part of an ellipse. Use radians to determine what
# angle to draw.
# pygame.draw.arc(screen, GREEN, [100, 100, 250, 200], PI / 2, PI, 2)
# pygame.draw.arc(screen, BLACK, [100, 100, 250, 200], 0, PI / 2, 2)
# pygame.draw.arc(screen, RED, [100, 100, 250, 200], 3 * PI / 2, 2 * PI, 2)
# pygame.draw.arc(screen, BLUE, [100, 100, 250, 200], PI, 3 * PI / 2, 2)
#
# --polygon--
# This draws a triangle using the polygon command.
# It is possible to list as many points as desired.  Note how the points
# are listed.  Each point is a list of two numbers, and the points
# themselves are nested in another list that holds all the points.
# pygame.draw.polygon(screen, BLACK, [[100,100], [0,200], [200,200]], 5)
#
#####
#
# --text--
# Text is slightly more complex. There are three things that need to be
# done. First, the program creates a variable that holds information about
# the font to be used, such as what typeface and how big.
#
# Second, the program creates an image of the text. One way to think of
# it is that the program carves out a “stamp” with the required letters
# that is ready to be dipped in ink and stamped on the paper.
#
# The third thing that is done is the program tells where this image of
# the text should be stamped( or “blit'ed”) to the screen.
#
# Select the font to use, size, bold, italics
# font = pygame.font.SysFont('Calibri', 25, True, False)
#
# Render the text. "True" means anti-aliased text.
# Black is the color. The variable BLACK was defined
# above as a list of [0, 0, 0]
# Note: This line creates an image of the letters,
# but does not put it on the screen yet.
# text = font.render("My text", True, BLACK)
#
# Put the image of the text on the screen at 250x250
# screen.blit(text, [250, 250])
#
# If score is an integer variable, the computer doesn't know how to add
# it to a string. You, the programmer, must convert the score to a string.
# Then add the strings together like this:
# text = font.render("Score: " + str(score), True, BLACK)
#
# --circle--
# Draw a circle around a point. The pos argument is the center of the
# circle, and radius is the size. The width argument is the thickness to
# draw the outer edge. If width is zero then the circle will be filled.
# pygame.draw.circle(Surface, color, pos, radius, width=0) -> Rect
#
