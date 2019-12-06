# derived from https://github.com/dpengineering/kinetic-maze/blob/master/kinetic_maze/physics.py
from RPi_ODrive import ODrive_Ease_Lib
import odrive.enums
import time
from odrive_config import *

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

        self.od.motor.config.current_lim = MOTOR_CURRENT_LIMIT
        self.od.motor.config.calibration_current = MOTOR_CALIBRATION_CURRENT

        # wait for motor to finish calibrating
        self.od.requested_state = odrive.enums.AXIS_STATE_MOTOR_CALIBRATION
        while self.od.current_state != odrive.enums.AXIS_STATE_IDLE:
            pass

        # wait for oscillations to die down
        time.sleep(CALIBRATION_DELAY_TIME)

        self.od.cycle_trigger.config.gpio_pin_num = CYCLE_TRIGGER_GPIO_PIN
        self.od.cycle_trigger.config.enabled = True

        self.od.encoder.config.bandwidth = ENCODER_BANDWIDTH
        self.od.controller.config.vel_gain = CONTROLLER_VEL_GAIN

        self.od.trap_traj.config.vel_limit = TRAJECTORY_VEL_LIMIT
        self.od.trap_traj.config.accel_limit = TRAJECTORY_ACCEL_LIMIT
        self.od.trap_traj.config.decel_limit = TRAJECTORY_DECEL_LIMIT
        self.od.trap_traj.config.A_per_css = TRAJECTORY_AMPS_PER_ACCELERATION

        self.home()

    def home(self):
        self.od.cycle_trigger.last_edge_hit.has_hit = False
        self.od.set_vel(HOMING_VELOCITY)
        while not self.od.cycle_trigger.last_edge_hit.has_hit:
            pass

        # find first edge
        first_edge = self.od.cycle_trigger.last_edge_hit.hit_location

        second_edge = self.od.cycle_trigger.last_edge_hit.hit_location

# physics.py