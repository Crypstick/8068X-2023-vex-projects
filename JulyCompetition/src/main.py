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
rightFrontMotor = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
rightMiddleMotor = Motor(Ports.PORT12, GearSetting.RATIO_18_1, False)
rightBackMotor = Motor(Ports.PORT13, GearSetting.RATIO_18_1, True)
leftFrontMotor = Motor(Ports.PORT5, GearSetting.RATIO_18_1, True)
leftMiddleMotor = Motor(Ports.PORT6, GearSetting.RATIO_18_1, True)
leftBackMotor = Motor(Ports.PORT7, GearSetting.RATIO_18_1, False)


rollerMotor_1 = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)
cataMotor_1 = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)

limit_button_h = Limit(brain.three_wire_port.h)

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


def remoteControl(Remote, rightFrontMotor, rightBackMotor, leftFrontMotor, leftBackMotor):
  while True:
    global x
    #init
    fwd = (Remote.axis3.position())
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

    #roller intake control
    if Remote.buttonL1.pressing():
      rollerMotor_1.set_velocity(100, PERCENT)
      rollerMotor_1.spin(FORWARD)
    elif Remote.buttonL2.pressing():
      rollerMotor_1.set_velocity(-100, PERCENT)
      rollerMotor_1.spin(FORWARD)
    else:
      rollerMotor_1.stop()

    #cata control + limit switch code
    if limit_button_h.pressing() == 0:
      cataMotor_1.set_velocity(100, PERCENT)
      cataMotor_1.spin(FORWARD)
      print("NOT PRESSED", limit_button_h.pressing())
    elif limit_button_h.pressing() == 1:
      cataMotor_1.stop()
      cataMotor_1.set_velocity(0, PERCENT)
      cataMotor_1.spin(FORWARD)
      cataMotor_1.stop()
      print("PRESSED", limit_button_h.pressing())
    if Remote.buttonR1.pressing() == True:
      while Remote.buttonR1.pressing() == True:
        cataMotor_1.set_velocity(100, PERCENT)
        cataMotor_1.spin(FORWARD)
    

remoteControl(Remote, rightFrontMotor, rightBackMotor, leftFrontMotor, leftBackMotor)

def autonCode():
#init
  global x
#moving forward to push alliance triball inside, TO CHANGE VALUES
  goStraight(1, -400)

  #to add roller back spin if applicable
  print("triball deposit COMPLETE")
  wait(500, MSEC)
  #to move closer to goal and punch alliance triball, TO CHANGE VALUES
  goStraight(1, 400)
  print("Moving back to starting zone for turning COMPLETE")
  wait(500, MSEC)
  #to rotate toward the alliance bar, TO CHANGE VALUES
  rotateRight(1, 360)
  print("Rotating toward alliance bar COMPLETE")
  wait(500, MSEC)
  #to move forward to push triball below bar toward our side, TO CHANGE VALUES
  goStraight(1, -400)
  print("Push triball below bar toward our side COMPLETE")
  wait(500, MSEC)
  #move back for matchload, TO CHANGE VALUES
  goStraight(1, 400)
  print("Moving back for matchload COMPLETE")
  wait(500, MSEC)

  #to add 360 rotation if cata requires

  #rotate back for matchload, TO CHANGE VALUES 
  rotateRight(1, 400)
  print("rotate back COMPLETE")
  
  wait(500, MSEC)

  #endgame code to be inserted. else, code for contact to elevation bar
  goStraight(1, 300)
  print("Moving toward elevation bar COMPLETE")
  wait(500, MSEC)
  #to insert further code. (rotate & contact with elevation bar TBD)
    
  x += 1


if x == 1:
  print("code COMPLETE")