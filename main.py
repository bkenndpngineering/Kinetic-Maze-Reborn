from Kinect_Skeleton_Tracker.tracker import Tracker
import pygame
import numpy
from interact import Button

t = Tracker()
t.run()
f = t.getFrame()
while f is None:
    f = t.getFrame()

pygame.init()
SCREEN_WIDTH = f.shape[1]
SCREEN_HEIGHT = f.shape[0]
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Skeleton Viewer')
clock = pygame.time.Clock()

prog_running = True

while prog_running:
    frame = t.getFrame()
    frame = (255*frame)
    frame = frame.swapaxes(0, 1)
    frame = pygame.surfarray.make_surface(frame)
    display.blit(frame, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            prog_running = False

    # API usage for reference
    angle = t.calculate_angle("RIGHT_HAND", "LEFT_HAND")
    difference = t.calculate_difference("RIGHT_HAND", "LEFT_HAND")
    coordinatesLeftHand = t.get_coordinates("LEFT_HAND")
    coordinatesRightHand = t.get_coordinates("RIGHT_HAND")
    coordinatesLeftElbow = t.get_coordinates("LEFT_ELBOW")
    coordinatesRightElbow = t.get_coordinates("RIGHT_ELBOW")

    if angle is not None:
        if (coordinatesLeftHand[1] < coordinatesLeftElbow[1]):
            print("RIGHT HAND ABOVE ELBOW")
        else:
            print("RIGHT HAND NOT ABOVE ELBOW")

        if (coordinatesRightHand[1] < coordinatesRightElbow[1]):
            print("LEFT HAND ABOVE ELBOW")
        else:
            print("LEFT HAND NOT ABOVE ELBOW")
    else:
        print("NO USER DETECTED")

    pygame.display.update()
    clock.tick(60)

t.stop()
pygame.quit()
quit()
