from Kinect_Skeleton_Tracker.tracker import Tracker
import pygame
import numpy
from interact import Button
from physics import KineticMazeMotor
import math

# map function
# (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


t = Tracker()
t.run()
f = t.getFrame()
while f is None:
    f = t.getFrame() # wait until good frame exists

pygame.init()
SCREEN_WIDTH = f.shape[1]
SCREEN_HEIGHT = f.shape[0]
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Skeleton Viewer')
clock = pygame.time.Clock()

largeFont = pygame.font.Font("libs/PressStart2P-Regular.ttf", 22)

button1 = Button(100, 50, 50, 50, "Start")

motor = KineticMazeMotor()

prog_running = True
gamestate_started = False

while prog_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            prog_running = False

    frame = t.getFrame()
    frame = (255*frame)
    frame = frame.swapaxes(0, 1)
    frame = pygame.surfarray.make_surface(frame)
    display.blit(frame, (0,0))

    if gamestate_started == False:
        button1.draw(display)
    else:
        # draw scoreboard?
        pass

    # API usage for reference
    angle = t.calculate_angle("RIGHT_HAND", "LEFT_HAND")
    difference = t.calculate_difference("RIGHT_HAND", "LEFT_HAND")
    coordinatesRightHand = t.get_coordinates("LEFT_HAND")
    coordinatesLeftHand = t.get_coordinates("RIGHT_HAND")
    coordinatesRightElbow = t.get_coordinates("LEFT_ELBOW")
    coordinatesLeftElbow = t.get_coordinates("RIGHT_ELBOW")

    if angle is not None:

        if gamestate_started == True:
            if (coordinatesLeftHand[1] < coordinatesLeftElbow[1]) and (coordinatesRightHand[1] < coordinatesRightElbow[1]):
                #print(angle)
                # angles is from 0 to 90 degrees. multiple play styles
                # map to velocity
                L_height = 0
                R_height = 0

                if (coordinatesRightHand[1] < coordinatesLeftHand[1]):
                    # right hand above left...
                    # velocity positive
                    R_height =  (angle - 0) * (SCREEN_HEIGHT-10 - 0) / (90 - 0) + 0
                    # map 0, 90, 0 screen_height -10
                    angle *= 1
                else:
                    # velocity negative
                    #
                    L_height = (angle - 0) * (SCREEN_HEIGHT - 10 - 0) / (90 - 0) + 0
                    angle *= -1


                pygame.draw.rect(display, (100, 25, 25), (10, 10, 20, L_height))
                pygame.draw.rect(display, (100, 25, 25), (SCREEN_WIDTH-30, 10, 20, R_height))

                ########## DO ODRIVE THINGS ############

                # angle to velocity conversion?
                # motion smoother?
                motor.set_velocity(motor.adjust_angle(math.radians(angle)))

                ########################################



            else:
                newText = largeFont.render("PUT HANDS ABOVE ELBOWS", True, (255, 0, 0))
                display.blit(newText, (0, 0))
                #print("PUT HANDS ABOVE ELBOWS")
                motor.set_velocity(motor.ramp_down())

        else:
            if button1.inBox(coordinatesRightHand[0], coordinatesRightHand[1]):
                button1.push()
                if button1.get_pushed() == True:
                    gamestate_started = True
                    button1.reset()

            # for user convenience
            pygame.draw.circle(display, (0,0,255), (int(coordinatesRightHand[0]), int(coordinatesRightHand[1])), 10)

    else:
        newText = largeFont.render("NO USER DETECTED", True, (255, 0, 0))
        display.blit(newText, (0, 0))
        #print("NO USER DETECTED")

    pygame.display.update()
    clock.tick(60)

t.stop()
pygame.quit()
quit()
