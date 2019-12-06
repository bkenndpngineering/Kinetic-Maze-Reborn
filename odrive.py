from RPi_ODrive import ODrive_Ease_Lib

class KineticMazeMotor:
    def __init__(self):
        self.od = None

    def connect(self):
        o = ODrive_Ease_Lib.find_ODrives()
        if len(o) != 1:
            print("Could not find ODrive")
            return False
        else:
            od = o[0]
            print("Found ODrive")
            self.od = ODrive_Ease_Lib.ODrive_Axis(od.axis0)  # axis one or zero?
            return True

    def initialize(self):
        # ODrive:
        # need to configure current settings
        # need to precalibrate motor and encoder
        MOTOR_CURRENT_LIMIT =
        MOTOR_CALIBRATION_CURRENT =
        AXIS_STATE_MOTOR_CALIBRATION =
        
