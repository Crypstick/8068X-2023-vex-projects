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

rightFrontMotor = Motor(Ports.PORT15, GearSetting.RATIO_18_1, True)
rightBackMotor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
leftFrontMotor = Motor(Ports.PORT18, GearSetting.RATIO_18_1, False)
leftBackMotor = Motor(Ports.PORT9, GearSetting.RATIO_18_1, False)

Punchermotor_1 = Motor(Ports.PORT8, GearSetting.RATIO_36_1, True)

limit_switch_a = Limit(brain.three_wire_port.a)

fwd = Remote.axis3.position()
sideways = Remote.axis1.position()
leftTrain = fwd + sideways
rightTrain = fwd - sideways

x = int()

def autonCode():
  global x
  #init
  fwd = Remote.axis3.position()
  sideways = Remote.axis1.position()
  leftTrain = fwd + sideways
  rightTrain = fwd - sideways
  print(limit_switch_a.pressing())

#turning from start point to angle toward goal, TO CHANGE VALUES
  rightFrontMotor.spin_for(FORWARD, 400, DEGREES, wait=False) 
  rightBackMotor.spin_for(FORWARD, 400, DEGREES, wait=True)
  print("Turning COMPLETE")
  wait(500, MSEC)
#to move closer to goal and punch alliance triball, TO CHANGE VALUES
  rightFrontMotor.spin_for(FORWARD, 360, DEGREES, wait=False)
  rightBackMotor.spin_for(FORWARD, 360, DEGREES, wait=False)
  leftFrontMotor.spin_for(FORWARD, 360, DEGREES, wait=False)
  leftBackMotor.spin_for(FORWARD, 360, DEGREES, wait=True)
  print("Moving closer to goal COMPLETE")
  wait(500, MSEC)
#to rotate toward the diagonal boundary, TO CHANGE VALUES
  rightFrontMotor.spin_for(FORWARD, 360, DEGREES, wait=False)
  rightBackMotor.spin_for(FORWARD, 360, DEGREES, wait=False)
  leftFrontMotor.spin_for(FORWARD, -360, DEGREES, wait=False)
  leftBackMotor.spin_for(FORWARD, -360, DEGREES, wait=True)
  print("Rotating toward diagonal boundary COMPLETE")
  wait(500, MSEC)
#to move toward the diagonal boundary, TO CHANGE VALUES
  rightFrontMotor.spin_for(FORWARD, 200, DEGREES, wait=False)
  rightBackMotor.spin_for(FORWARD, 200, DEGREES, wait=False)
  leftFrontMotor.spin_for(FORWARD, 200, DEGREES, wait=False)
  leftBackMotor.spin_for(FORWARD, 200, DEGREES, wait=True)
  print("Moving toward diagonal boundary COMPLETE")
  wait(500, MSEC)
#engage claw to pick up new triball, TO CHANGE VALUE

#move back, TO CHANGE VALUES
  rightFrontMotor.spin_for(FORWARD, -200, DEGREES, wait=False)
  rightBackMotor.spin_for(FORWARD, -200, DEGREES, wait=False)
  leftFrontMotor.spin_for(FORWARD, -200, DEGREES, wait=False)
  leftBackMotor.spin_for(FORWARD, -200, DEGREES, wait=True)
  print("Moving back COMPLETE")
  wait(500, MSEC)
#rotate back, TO CHANGE VALUES
  rightFrontMotor.spin_for(FORWARD, 360, DEGREES, wait=False)
  rightBackMotor.spin_for(FORWARD, 360, DEGREES, wait=False)
  leftFrontMotor.spin_for(FORWARD, -360, DEGREES, wait=False)
  leftBackMotor.spin_for(FORWARD, -360, DEGREES, wait=True)
  print("rotate back COMPLETE")
  wait(500, MSEC)
#to let go of claw grip and fire, TO CHANGE VALUES

#endgame code to be inserted. else, code for contact to elevation bar
  rightFrontMotor.spin_for(FORWARD, 300, DEGREES, wait=False)
  rightBackMotor.spin_for(FORWARD, 300, DEGREES, wait=False)
  leftFrontMotor.spin_for(FORWARD, 300, DEGREES, wait=False)
  leftBackMotor.spin_for(FORWARD, 300, DEGREES, wait=True)
  print("Moving toward elevation bar COMPLETE")
  wait(500, MSEC)
  #to insert further code. (rotate & 4bar + claw contact with elevation bar TBD)
  x += 1

def remoteControl(Remote, rightFrontMotor, rightBackMotor, leftFrontMotor, leftBackMotor):
  while True:
   
    #init
    fwd = Remote.axis3.position()
    sideways = Remote.axis1.position()
    leftTrain = fwd + sideways
    rightTrain = fwd - sideways
    print(limit_switch_a.pressing())
   
    #drivetrain
    rightFrontMotor.set_velocity(rightTrain, PERCENT)
    rightBackMotor.set_velocity(rightTrain, PERCENT)
    leftFrontMotor.set_velocity(leftTrain, PERCENT)
    leftBackMotor.set_velocity(leftTrain, PERCENT)
    rightFrontMotor.spin(FORWARD)
    rightBackMotor.spin(FORWARD)
    leftFrontMotor.spin(FORWARD)
    leftBackMotor.spin(FORWARD)
    if limit_switch_a.pressing() == False:
      Punchermotor_1.set_velocity(50, PERCENT)
      Punchermotor_1.spin(FORWARD)
    elif limit_switch_a.pressing() == True:
      Punchermotor_1.set_velocity(0, PERCENT)
      Punchermotor_1.spin(FORWARD)
      Punchermotor_1.stop()
    if Remote.buttonR2.pressing() == True:
      while Remote.buttonR2.pressing() == True:
        Punchermotor_1.set_velocity(100, PERCENT)
        Punchermotor_1.spin(FORWARD)

    '''''
    if Remote.buttonR2.pressing():
      Punchermotor_1.set_velocity(50, PERCENT)
      while limit_switch_a.pressing != True:
        Punchermotor_1.spin(FORWARD)
    else:
      Punchermotor_1.stop()
    if Remote.buttonR2.pressing() and limit_switch_a.pressing == True:
      Punchermotor_1.set_velocity(50, PERCENT)
      while limit_switch_a == True:
        Punchermotor_1.spin(FORWARD)
    else:
      Punchermotor_1.stop()
      '''


    




remoteControl(Remote, rightFrontMotor, rightBackMotor, leftFrontMotor, leftBackMotor)