# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       kevinorjalo                                                  #
# 	Created:      23/05/2023, 17:48:49                                         #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Robot configuration code
brain = Brain()
Remote = Controller(PRIMARY)
x = int()

rightFrontMotor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
rightMiddleMotor = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
rightBackMotor = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
leftFrontMotor = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)
leftMiddleMotor = Motor(Ports.PORT5, GearSetting.RATIO_18_1, True)
leftBackMotor = Motor(Ports.PORT6, GearSetting.RATIO_18_1, False)

Punchermotor_1 = Motor(Ports.PORT5, GearSetting.RATIO_36_1, False)
rollerMotor_1 = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)
cataMotor_1 = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)

limit_switch_a = Limit(brain.three_wire_port.a)

#PID Code

#   Please change values according to what needs to be done
#   Genuinely have no idea what the hell the values are meant
#   to be, I think I gotta ask Zachary on what I gotta do to
#   get the values.

#   Usage: PID(error, kp, ki, kd, starti, settle_error, settle_time, timeout)
#   and somehow, BOOM!???? IDK ANYMORE MAN

class PID:
    def _init_(self, error, kp, ki, kd, starti, settle_error, settle_time, timeout):
        self.error = 0
        self.kp = 0
        self.ki = 0
        self.kd = 0
        self.starti = 0
        self.settle_error = 0
        self.settle_time = 0
        self.timeout = 0
        self.accumulated_error = 0
        self.previous_error = 0
        self.output = 0
        self.time_spent_settled = 0
        self.time_spent_running = 0

    def compute(self, error):
        pass

    def is_settled(self):
        pass
  


def remoteControl(Remote, rightFrontMotor, rightBackMotor, leftFrontMotor, leftBackMotor):
  while True:
    global x
    #init
    fwd = Remote.axis3.position()
    sideways = Remote.axis1.position()
    leftTrain = fwd + sideways
    rightTrain = fwd - sideways


    #drivetrain
    rightFrontMotor.set_velocity(rightTrain, PERCENT)
    rightMiddleMotor.set_velocity(rightTrain, PERCENT)
    rightBackMotor.set_velocity(rightTrain, PERCENT)
    leftFrontMotor.set_velocity(leftTrain, PERCENT)
    leftMiddleMotor.set_velocity(leftTrain, PERCENT)
    leftBackMotor.set_velocity(leftTrain, PERCENT)
    rightFrontMotor.spin(FORWARD)
    rightMiddleMotor.spin(FORWARD)
    rightBackMotor.spin(FORWARD)
    leftFrontMotor.spin(FORWARD)
    leftMiddleMotor.spin(FORWARD)
    leftBackMotor.spin(FORWARD)

    # Punchermotor control
    if Remote.buttonR2.pressing():
      Punchermotor_1.set_velocity(50, PERCENT)
      while limit_switch_a.pressing != True:
          Punchermotor_1.spin(FORWARD)
      sleep(10, MSEC)
    else:
      Punchermotor_1.stop()
    if Remote.buttonR2.pressing() and limit_switch_a.pressing == True:
      Punchermotor_1.set_velocity(50, PERCENT)
      while limit_switch_a == True:
          Punchermotor_1.spin(FORWARD)
      sleep(10, MSEC)
    else:
      Punchermotor_1.stop()

    #roller intake control
    if Remote.buttonL2.pressing():
      rollerMotor_1.set_velocity(100, PERCENT)
      rollerMotor_1.spin(FORWARD)
    elif Remote.buttonL1.pressing():
      rollerMotor_1.set_velocity(-100, PERCENT)
      rollerMotor_1.spin(FORWARD)
    else:
      rollerMotor_1.stop()

    #cata control
    if Remote.buttonX.pressing():
      cataMotor_1.set_velocity(100, PERCENT)
      cataMotor_1.spin(FORWARD)
    else:
      cataMotor_1.stop()


remoteControl(Remote, rightFrontMotor, rightBackMotor, leftFrontMotor, leftBackMotor)

def autonCode():
#init
  global x
#moving forward to push alliance triball inside, TO CHANGE VALUES
  rightFrontMotor.spin_for(FORWARD, 400, DEGREES, wait=False)
  rightMiddleMotor.spin_for(FORWARD, 400, DEGREES, wait=False)
  rightBackMotor.spin_for(FORWARD, 400, DEGREES, wait=False)
  leftFrontMotor.spin_for(FORWARD, 400, DEGREES, wait=False)
  leftMiddleMotor.spin_for(FORWARD, 400, DEGREES, wait=False)
  leftBackMotor.spin_for(FORWARD, 400, DEGREES, wait=True)
  #to add roller back spin if applicable
  print("triball deposit COMPLETE")
  wait(500, MSEC)
  #to move closer to goal and punch alliance triball, TO CHANGE VALUES
  rightFrontMotor.spin_for(FORWARD, -400, DEGREES, wait=False)
  rightMiddleMotor.spin_for(FORWARD, -400, DEGREES, wait=False)
  rightBackMotor.spin_for(FORWARD, -400, DEGREES, wait=False)
  leftFrontMotor.spin_for(FORWARD, -400, DEGREES, wait=False)
  leftMiddleMotor.spin_for(FORWARD, -400, DEGREES, wait=False)
  leftBackMotor.spin_for(FORWARD, -400, DEGREES, wait=True)
  print("Moving back to starting zone for turning COMPLETE")
  wait(500, MSEC)
  #to rotate toward the alliance bar, TO CHANGE VALUES
  rightFrontMotor.spin_for(FORWARD, 360, DEGREES, wait=False)
  rightMiddleMotor.spin_for(FORWARD, 360, DEGREES, wait=False)
  rightBackMotor.spin_for(FORWARD, 360, DEGREES, wait=False)
  leftFrontMotor.spin_for(FORWARD, -360, DEGREES, wait=False)
  leftBackMotor.spin_for(FORWARD, -360, DEGREES, wait=False)
  leftBackMotor.spin_for(FORWARD, -360, DEGREES, wait=True)
  print("Rotating toward alliance bar COMPLETE")
  wait(500, MSEC)
  #to move forward to push triball below bar toward our side, TO CHANGE VALUES
  rightFrontMotor.spin_for(FORWARD, 400, DEGREES, wait=False)
  rightMiddleMotor.spin_for(FORWARD, 400, DEGREES, wait=False)
  rightBackMotor.spin_for(FORWARD, 400, DEGREES, wait=False)
  leftFrontMotor.spin_for(FORWARD, 400, DEGREES, wait=False)
  leftMiddleMotor.spin_for(FORWARD, 400, DEGREES, wait=False)
  leftBackMotor.spin_for(FORWARD, 400, DEGREES, wait=True)
  print("Push triball below bar toward our side COMPLETE")
  wait(500, MSEC)
  #move back for matchload, TO CHANGE VALUES
  rightFrontMotor.spin_for(FORWARD, -400, DEGREES, wait=False)
  rightMiddleMotor.spin_for(FORWARD, -400, DEGREES, wait=False)
  rightBackMotor.spin_for(FORWARD, -400, DEGREES, wait=False)
  leftFrontMotor.spin_for(FORWARD, -400, DEGREES, wait=False)
  leftMiddleMotor.spin_for(FORWARD, -400, DEGREES, wait=False)
  leftBackMotor.spin_for(FORWARD, -400, DEGREES, wait=True)
  print("Moving back for matchload COMPLETE")
  wait(500, MSEC)

  #to add 360 rotation if cata requires

  #rotate back for matchload, TO CHANGE VALUES 
  rightFrontMotor.spin_for(FORWARD, -400, DEGREES, wait=False)
  rightMiddleMotor.spin_for(FORWARD, -400, DEGREES, wait=False)
  rightBackMotor.spin_for(FORWARD, -400, DEGREES, wait=False)
  leftFrontMotor.spin_for(FORWARD, 400, DEGREES, wait=False)
  leftMiddleMotor.spin_for(FORWARD, 400, DEGREES, wait=False)
  leftBackMotor.spin_for(FORWARD, 400, DEGREES, wait=True)
  print("rotate back COMPLETE")
  
  wait(500, MSEC)

  #endgame code to be inserted. else, code for contact to elevation bar
  rightFrontMotor.spin_for(FORWARD, 300, DEGREES, wait=False)
  rightBackMotor.spin_for(FORWARD, 300, DEGREES, wait=False)
  leftFrontMotor.spin_for(FORWARD, 300, DEGREES, wait=False)
  leftBackMotor.spin_for(FORWARD, 300, DEGREES, wait=True)
  print("Moving toward elevation bar COMPLETE")
  wait(500, MSEC)
  #to insert further code. (rotate & contact with elevation bar TBD)
    
  x += 1


if x == 1:
  print("code COMPLETE")