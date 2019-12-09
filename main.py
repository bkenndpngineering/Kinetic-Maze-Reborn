import cv2
from Kinect_Skeleton_Tracker.tracker import Tracker

t = Tracker()
t.run()
f = t.getFrame()
while f is None:
    f = t.getFrame()

while True:
    f = t.getFrame()
    cv2.imshow("img", f)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

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

t.stop()
cv2.destroyAllWindows()
