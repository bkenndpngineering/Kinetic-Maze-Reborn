from Kinect_Skeleton_Tracker.tracker import Tracker
from highscores import Scoreboard
import pygame
import numpy
from interact import Button
from physics import KineticMazeMotor
import math
import sys
import time

import odrive
from odrive.enums import *

# map function
# (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
# Unsure of what the above comments are, leaving in case useful - X
t = Tracker()
t.run()
f = t.getFrame()
while f is None:
    f = t.getFrame() # wait until good frame exists

pygame.init()
SCREEN_WIDTH = f.shape[1]
SCREEN_HEIGHT = f.shape[0]
#display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Kinetic Maze v.3')
clock = pygame.time.Clock()

#Timer/Scoreboard Init
sb = Scoreboard(3, (120, 600))
startTime = 0

#GUI fonts and buttons
largeFont = pygame.font.Font("assets/PressStart2P-Regular.ttf", 22)
#Main screen buttons
startButton = Button(100, 50, 50, 50, "Start", 2)
scoreButton = Button(100, 50, 400, 50, "Scores", 2)

#Scoreboard screen buttons
backButton = Button(100, 50, 200, 300, "Back", 2) #on scoreboard

#Admin screen buttons
adminQuitButton = Button(100, 50, 50, 50, "Quit", 2)
adminBackButton = Button(100, 50, 400, 50, "Back", 2)

#Game

#motor = KineticMazeMotor()
prog_running = True
gamestate = 'main'
while prog_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            prog_running = False

    #Get the OpenCV frame from tracker, convert to pygame
    frame = t.getFrame()
    frame = (255*frame)
    frame = frame.swapaxes(0, 1)
    frame = pygame.surfarray.make_surface(frame)
    frame = pygame.transform.flip(frame, True, False)
    display.blit(frame, (0,0))

    #Draw buttons here, button presses go later
    if gamestate == 'main': #Draw main menu
        startButton.draw(display)
        scoreButton.draw(display)

    if gamestate == 'scoreboard':
        backButton.draw(display)
        #display scoreboard or whatever
        firstName,firstScore = sb.getEntry(1)
        secondName,secondScore = sb.getEntry(2)
        thirdName,thirdScore = sb.getEntry(3)

        header = "PLACE | NAME | SCORE"
        one = "1st | " + firstName + "  | "+ str(firstScore)
        two = "2nd | " + secondName + "  | "+ str(secondScore)
        three = "3rd | " + thirdName + "  | "+ str(thirdScore)

        newText = largeFont.render(header, True, (255, 0, 0))
        largeSize = largeFont.size(header)
        display.blit(newText, (SCREEN_WIDTH/2 - newText.get_rect().width / 2, SCREEN_HEIGHT/2 - newText.get_rect().height / 2 - 50))

        newText = largeFont.render(one, True, (255, 0, 0))
        display.blit(newText, (SCREEN_WIDTH/2 - newText.get_rect().width / 2, SCREEN_HEIGHT/2 - newText.get_rect().height / 2 - 25))

        newText = largeFont.render(two, True, (255, 0, 0))
        display.blit(newText, (SCREEN_WIDTH/2 - newText.get_rect().width / 2, SCREEN_HEIGHT/2 - newText.get_rect().height / 2))

        newText = largeFont.render(three, True, (255, 0, 0))
        display.blit(newText, (SCREEN_WIDTH/2 - newText.get_rect().width / 2, SCREEN_HEIGHT/2 - newText.get_rect().height / 2 + 25))


    if gamestate == 'admin':
        adminQuitButton.draw(display)
        adminBackButton.draw(display)



    # API usage for reference, get coords of all joints in format [x,y]
    angle = t.calculate_angle("RIGHT_HAND", "LEFT_HAND")
    difference = t.calculate_difference("RIGHT_HAND", "LEFT_HAND")
    coordinatesRightHand = t.get_coordinates("LEFT_HAND")
    coordinatesLeftHand = t.get_coordinates("RIGHT_HAND")
    coordinatesRightElbow = t.get_coordinates("LEFT_ELBOW")
    coordinatesLeftElbow = t.get_coordinates("RIGHT_ELBOW")

    #coordinatesLeftHip = t.get_coordinates("LEFT_HIP")
    #coordinatesRightHip = t.get_coordinates("RIGHT_HIP")
    coordinatesLeftKnee = t.get_coordinates("LEFT_KNEE")
    coordinatesRightKnee = t.get_coordinates("RIGHT_KNEE")

    if angle is not None:

        #check for button press to bring up admin screen, or button to quit and shutoff

        if gamestate == 'game':

            #if end sensor tripped (game end):
            #endTime = int(time.time())
            #elapsed = endTime - startTime
            #print("Time elapsed: ", elapsed)
            #sb.checkScores(elapsed)
            #Input name, etc
            #gamestate = "main"
            #startButton.reset()

            if (coordinatesLeftHand[1] < coordinatesLeftElbow[1]) and (coordinatesRightHand[1] < coordinatesRightElbow[1]):
                #print(angle)
                # angles is from 0 to 90 degrees. multiple play styles
                # map to velocity
                L_height = 0
                R_height = 0

                if (coordinatesRightHand[1] < coordinatesLeftHand[1]):
                    # right hand above left, velocity positive
                    R_height =  (angle - 0) * (SCREEN_HEIGHT-10 - 0) / (90 - 0) + 0
                    # map 0, 90, 0 screen_height -10
                    angle *= 1
                else:
                    # velocity negative
                    L_height = (angle - 0) * (SCREEN_HEIGHT - 10 - 0) / (90 - 0) + 0
                    angle *= -1

                #Draw the angle magnitude indicator rectangles on the side of the game
                pygame.draw.rect(display, (100, 25, 25), (10, 10, 20, L_height))
                pygame.draw.rect(display, (100, 25, 25), (SCREEN_WIDTH-30, 10, 20, R_height))

                ########## ODRIVE THINGS ############

                #motor.set_velocity(motor.adjust_angle(math.radians(angle)))

                ########################################

                #AFK tracker to quit to menu without saving if afk probably goes around here
                #If AFK, run the autosolve (called TAS for some reason)

            else:
                newText = largeFont.render("PUT HANDS ABOVE ELBOWS", True, (255, 0, 0))
                largeSize = largeFont.size("PUT HANDS ABOVE ELBOWS")
                display.blit(newText, (SCREEN_WIDTH/2 - newText.get_rect().width / 2, SCREEN_HEIGHT/2 - newText.get_rect().height / 2))
                #motor.set_velocity(motor.ramp_down())

        elif gamestate == 'main':
            halfWidth = SCREEN_WIDTH/2 #Main menu gui
            if startButton.inBox(int(halfWidth - (int(coordinatesRightHand[0] - halfWidth))), int(coordinatesRightHand[1])) and startButton.inBox(int(halfWidth - (int(coordinatesLeftHand[0] - halfWidth))), int(coordinatesLeftHand[1])):
                startButton.push()
                if startButton.get_pushed() == True:
                    gamestate = 'game'
                    #Mech: Trigger ball dropper
                    startButton.reset()
                    startTime = int(time.time())

            if scoreButton.inBox(int(halfWidth - (int(coordinatesRightHand[0] - halfWidth))), int(coordinatesRightHand[1])) and scoreButton.inBox(int(halfWidth - (int(coordinatesLeftHand[0] - halfWidth))), int(coordinatesLeftHand[1])):
                scoreButton.push()
                if scoreButton.get_pushed() == True:
                    gamestate = 'scoreboard'
                    scoreButton.reset()



        elif gamestate == 'scoreboard':
            halfWidth = SCREEN_WIDTH/2
            if backButton.inBox(int(halfWidth - (int(coordinatesRightHand[0] - halfWidth))), int(coordinatesRightHand[1])) and backButton.inBox(int(halfWidth - (int(coordinatesLeftHand[0] - halfWidth))), int(coordinatesLeftHand[1])):
                backButton.push()
                if backButton.get_pushed() == True:
                    gamestate = 'main'
                    backButton.reset()

        elif gamestate == 'admin':
            halfWidth = SCREEN_WIDTH/2
            if adminQuitButton.inBox(int(halfWidth - (int(coordinatesRightHand[0] - halfWidth))), int(coordinatesRightHand[1])) and adminQuitButton.inBox(int(halfWidth - (int(coordinatesLeftHand[0] - halfWidth))), int(coordinatesLeftHand[1])):
                adminQuitButton.push()
                if adminQuitButton.get_pushed() == True:
                    self.od = odrive.find_any()
                    self.od.reboot()
                    t.stop()
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()

            if adminBackButton.inBox(int(halfWidth - (int(coordinatesRightHand[0] - halfWidth))), int(coordinatesRightHand[1])) and adminBackButton.inBox(int(halfWidth - (int(coordinatesLeftHand[0] - halfWidth))), int(coordinatesLeftHand[1])):
                adminBackButton.push()
                if adminBackButton.get_pushed() == True:
                    gamestate = 'main'
                    adminBackButton.reset()

        elif gamestate == 'name':
            pass #name input screen



        # for user convenience, draw both left and right hands
        pygame.draw.circle(display, (0,0,255), (int(halfWidth - (int(coordinatesRightHand[0] - halfWidth))), int(coordinatesRightHand[1])), 10)
        pygame.draw.circle(display, (255,0,0), (int(halfWidth - (int(coordinatesLeftHand[0] - halfWidth))), int(coordinatesLeftHand[1])), 10)


    else:
        newText = largeFont.render("NO USER DETECTED", True, (255, 0, 0))
        largeSize = largeFont.size("NO USER DETECTED")
        display.blit(newText, (SCREEN_WIDTH/2 - newText.get_rect().width / 2, SCREEN_HEIGHT/2 - newText.get_rect().height / 2))



    #events loop for pygame misc.
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: #autosolve, press a
                print("Beginning autosolve\n")

                with open("./configs/tas.json", "r") as f:
                    route = json.load(f)
                path = route["path"]
                for step in path:
                    if step["kind"] == "pause":
                        time.sleep(step["duration"])
                    elif step["kind"] == "move":
                        motor.go_to_angle(step["target"],
                                        direction=step.get("direction"),
                                        max_velocity=step.get("max_velocity"),
                                        max_accel=step.get("max_accel"),
                                        max_decel=step.get("max_decel"))

                    else:
                        raise ValueError("Invalid step kind %r" % (step["kind"],))

                print("Autosolve complete\n")


    pygame.display.update()
    clock.tick(60)


#Stuff if prog_running loop broken
t.stop()
pygame.quit()
quit()
