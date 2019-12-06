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

    angle = t.calculate_angle("RIGHT_HAND", "LEFT_HAND")
    print(angle)
    if angle is not None:
                if t.returnY("LEFT_HAND") < t.returnY("LEFT_ELBOW") and t.returnY("RIGHT_HAND") < t.returnY("RIGHT_ELBOW"):
                    print("Got angle:", angle)

                else:
                    print("Hands not above elbow")
            else:
                #self.kmm.set_velocity(self.kmm.ramp_down())
                print("No user detected")
                #sw.updateTimer(firstTime,timer_on)
    '''
t.stop()
cv2.destroyAllWindows()
