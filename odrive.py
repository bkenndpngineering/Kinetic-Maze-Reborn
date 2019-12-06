from RPi_ODrive import ODrive_Ease_Lib
import odrive.enums
import time

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
        print("Initializing ODrive")
        # ODrive:
        # need to configure current settings?
        # need to precalibrate motor and encoder?

        MOTOR_CURRENT_LIMIT = #
        self.od.motor.config.current_lim = MOTOR_CURRENT_LIMIT
        MOTOR_CALIBRATION_CURRENT = #
        self.od.motor.config.calibration_current = MOTOR_CALIBRATION_CURRENT

        # wait for motor to finish calibrating
        self.od.requested_state = odrive.enums.AXIS_STATE_MOTOR_CALIBRATION
        while self.od.current_state != odrive.enums.AXIS_STATE_IDLE:
            pass

        # wait for oscillations to die down
        CALIBRATION_DELAY_TIME = #
        time.sleep(CALIBRATION_DELAY_TIME)

        CYCLE_TRIGGER_GPIO_PIN = #
        self.od.cycle_trigger.config.gpio_pin_num = CYCLE_TRIGGER_GPIO_PIN
        self.od.cycle_trigger.config.enabled = True

