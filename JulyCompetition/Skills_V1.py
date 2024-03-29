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



#Motor configurations
rightFrontMotor = Motor(Ports.PORT18, GearSetting.RATIO_18_1, True)
rightMiddleMotor = Motor(Ports.PORT19, GearSetting.RATIO_18_1, True)
rightBackMotor = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)
leftFrontMotor = Motor(Ports.PORT8, GearSetting.RATIO_18_1, True)
leftMiddleMotor = Motor(Ports.PORT7, GearSetting.RATIO_18_1, False)
leftBackMotor = Motor(Ports.PORT6, GearSetting.RATIO_18_1, True)


rollerMotor_1 = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
cataMotor_1 = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)

limit_switch_h = Limit(brain.three_wire_port.h)

#autonomous code blocks for simplification
def goStraight(speed, distance):
  rightFrontMotor.spin_for(FORWARD, distance, DEGREES, speed, PercentUnits, wait=False)
  rightMiddleMotor.spin_for(FORWARD, distance, DEGREES, speed, PercentUnits, wait=False)
  rightBackMotor.spin_for(FORWARD, distance, DEGREES, speed, PercentUnits, wait=False)
  leftFrontMotor.spin_for(FORWARD, distance, DEGREES, speed, PercentUnits, wait=False)
  leftMiddleMotor.spin_for(FORWARD, distance, DEGREES, speed, PercentUnits, wait=False)
  leftBackMotor.spin_for(FORWARD, distance, DEGREES, speed, PercentUnits, wait=True)

def rotateRight(speed, distance):
  rightFrontMotor.spin_for(FORWARD, -1*distance, DEGREES, speed, PercentUnits, wait=False)
  rightMiddleMotor.spin_for(FORWARD, -1*distance, DEGREES, speed, PercentUnits, wait=False)
  rightBackMotor.spin_for(FORWARD, -1*distance, DEGREES, speed, PercentUnits, wait=False)
  leftFrontMotor.spin_for(FORWARD, distance, DEGREES, speed, PercentUnits, wait=False)
  leftBackMotor.spin_for(FORWARD, distance, DEGREES, speed, PercentUnits, wait=False)
  leftBackMotor.spin_for(FORWARD, distance, DEGREES, speed, PercentUnits, wait=True)

def rotateLeft(speed, distance):
  rightFrontMotor.spin_for(FORWARD, distance, DEGREES, speed, PercentUnits, wait=False)
  rightMiddleMotor.spin_for(FORWARD, distance, DEGREES, speed, PercentUnits, wait=False)
  rightBackMotor.spin_for(FORWARD, distance, DEGREES, speed, PercentUnits, wait=False)
  leftFrontMotor.spin_for(FORWARD, -1*distance, DEGREES, speed, PercentUnits, wait=False)
  leftBackMotor.spin_for(FORWARD, -1*distance, DEGREES, speed, PercentUnits, wait=False)
  leftBackMotor.spin_for(FORWARD, -1*distance, DEGREES, speed, PercentUnits, wait=True)


def remote_driveTrain(Remote, rightFrontMotor, rightMiddleMotor, rightBackMotor, leftFrontMotor, leftMiddleMotor, leftBackMotor):
    #init
    fwd = Remote.axis1.position()
    sideways = Remote.axis3.position()
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

    #cata control + limit switch code
    if Remote.buttonY.pressing():
      while 1 == 1:
        cataMotor_1.stop()
        cataMotor_1.set_velocity(0,PERCENT)
    if limit_switch_h.pressing() == 0:
      cataMotor_1.set_velocity(100, PERCENT)
      cataMotor_1.spin(FORWARD)
      print("NOT PRESSED", limit_switch_h.pressing())
    elif limit_switch_h.pressing() == 1:
      cataMotor_1.stop()
      cataMotor_1.set_velocity(0, PERCENT)
      cataMotor_1.spin(FORWARD)
      cataMotor_1.stop()
      print("PRESSED", limit_switch_h.pressing())
    if Remote.buttonR1.pressing() == True:
      while Remote.buttonR1.pressing() == True:
        cataMotor_1.set_velocity(100, PERCENT)
        cataMotor_1.spin(FORWARD)
    
def remote_rollerIntake():
  #roller intake control
  if Remote.buttonL1.pressing():
    rollerMotor_1.set_velocity(100, PERCENT)
    rollerMotor_1.spin(FORWARD)
  elif Remote.buttonL2.pressing():
    rollerMotor_1.set_velocity(-100, PERCENT)
    rollerMotor_1.spin(FORWARD)
  else:
    rollerMotor_1.stop()

def remote_cataControl():
      #cata control + limit switch code
    if Remote.buttonY.pressing():
      while 1 == 1:
        cataMotor_1.stop()
        cataMotor_1.set_velocity(0,PERCENT)
    if limit_switch_h.pressing() == 0:
      cataMotor_1.set_velocity(100, PERCENT)
      cataMotor_1.spin(FORWARD)
      print("NOT PRESSED", limit_switch_h.pressing())
    elif limit_switch_h.pressing() == 1:
      cataMotor_1.stop()
      cataMotor_1.set_velocity(0, PERCENT)
      cataMotor_1.spin(FORWARD)
      cataMotor_1.stop()
      print("PRESSED", limit_switch_h.pressing())
    if Remote.buttonR1.pressing() == True:
      while Remote.buttonR1.pressing() == True:
        cataMotor_1.set_velocity(100, PERCENT)
        cataMotor_1.spin(FORWARD)

def autonomous():
#init
  global x
#moving forward to push alliance triball inside, TO CHANGE VALUES
  rightFrontMotor.spin_for(FORWARD, -600, DEGREES, wait=False)
  rightMiddleMotor.spin_for(FORWARD, -600, DEGREES, wait=False)
  rightBackMotor.spin_for(FORWARD, -600, DEGREES, wait=False)
  leftFrontMotor.spin_for(FORWARD, -600, DEGREES,  wait=False)
  leftMiddleMotor.spin_for(FORWARD, -600, DEGREES,  wait=False)
  leftBackMotor.spin_for(FORWARD, -600, DEGREES,  wait=True)
  print("triball deposit COMPLETE")
  wait(500, MSEC)

  #to move closer to goal and punch alliance triball, TO CHANGE VALUES
  rightFrontMotor.spin_for(FORWARD, 500, DEGREES, wait=False)
  rightMiddleMotor.spin_for(FORWARD, 500, DEGREES, wait=False)
  rightBackMotor.spin_for(FORWARD, 500, DEGREES, wait=False)
  leftFrontMotor.spin_for(FORWARD, 500, DEGREES,  wait=False)
  leftMiddleMotor.spin_for(FORWARD, 500, DEGREES,  wait=False)
  leftBackMotor.spin_for(FORWARD, 500, DEGREES,  wait=True)
  print("Moving back to starting zone for turning COMPLETE")
  wait(500, MSEC)
  
  #to rotate toward the alliance bar, TO CHANGE VALUES
  rightFrontMotor.spin_for(FORWARD, -1*185, DEGREES,  wait=False)
  rightMiddleMotor.spin_for(FORWARD, -1*185, DEGREES,  wait=False)
  rightBackMotor.spin_for(FORWARD, -1*185, DEGREES,  wait=False)
  leftFrontMotor.spin_for(FORWARD, 185, DEGREES, wait=False)
  leftBackMotor.spin_for(FORWARD, 185, DEGREES,  wait=False)
  leftBackMotor.spin_for(FORWARD, 185, DEGREES, wait=True)
  print("Rotating toward alliance bar COMPLETE")
  wait(500, MSEC)
  
  #to move forward to push triball below bar toward our side, TO CHANGE VALUES
  rightFrontMotor.spin_for(FORWARD, 500, DEGREES, wait=False)
  rightMiddleMotor.spin_for(FORWARD, 500, DEGREES, wait=False)
  rightBackMotor.spin_for(FORWARD, 500, DEGREES, wait=False)
  leftFrontMotor.spin_for(FORWARD, 500, DEGREES,  wait=False)
  leftMiddleMotor.spin_for(FORWARD, 500, DEGREES,  wait=False)
  leftBackMotor.spin_for(FORWARD, 500, DEGREES,  wait=True)
  print("Push triball below bar toward our side COMPLETE")
  wait(500, MSEC)
  
  #move back for matchload, TO CHANGE VALUES
  rightFrontMotor.spin_for(FORWARD, -400, DEGREES, wait=False)
  rightMiddleMotor.spin_for(FORWARD, -400, DEGREES, wait=False)
  rightBackMotor.spin_for(FORWARD, -400, DEGREES, wait=False)
  leftFrontMotor.spin_for(FORWARD, -400, DEGREES,  wait=False)
  leftMiddleMotor.spin_for(FORWARD, -400, DEGREES,  wait=False)
  leftBackMotor.spin_for(FORWARD, -400, DEGREES,  wait=True)
  print("Moving back for matchload COMPLETE")
  wait(500, MSEC)
    
  x += 1


if x == 1:
  print("code COMPLETE")

def driver_control():
  while True:
    remote_driveTrain(Remote, rightFrontMotor, rightMiddleMotor, rightBackMotor, leftFrontMotor, leftMiddleMotor, leftBackMotor)
    remote_rollerIntake()
    remote_cataControl()


comp = Competition(driver_control, autonomous)