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

rightFrontMotor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
rightBackMotor = Motor(Ports.PORT5, GearSetting.RATIO_18_1, True)
leftFrontMotor = Motor(Ports.PORT4, GearSetting.RATIO_18_1, False)
leftBackMotor = Motor(Ports.PORT6, GearSetting.RATIO_18_1, False)

Punchermotor_1 = Motor(Ports.PORT5, GearSetting.RATIO_36_1, False)
clawMotor_1 = Motor(Ports.PORT6, GearSetting.RATIO_18_1, False)

fourBarMotorRight = Motor(Ports.PORT9, GearSetting.RATIO_18_1, False) #test out if reverse, havent done it
fourBarMotorLeft = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True) #test out if reverse as well, havent done it either

limit_switch_a = Limit(brain.three_wire_port.a)
# Brain should be defined by default


def remoteControl(Remote, rightFrontMotor, rightBackMotor, leftFrontMotor, leftBackMotor):
  while True:
   
   #init
   fwd = Remote.axis3.position()
   sideways = Remote.axis1.position()
   leftTrain = fwd + sideways
   rightTrain = fwd - sideways

   #drivetrain
   rightFrontMotor.set_velocity(rightTrain, PERCENT)
   rightBackMotor.set_velocity(rightTrain, PERCENT)
   leftFrontMotor.set_velocity(leftTrain, PERCENT)
   leftBackMotor.set_velocity(leftTrain, PERCENT)
   rightFrontMotor.spin(FORWARD)
   rightBackMotor.spin(FORWARD)
   leftFrontMotor.spin(FORWARD)
   leftBackMotor.spin(FORWARD)

   # Punchermotor control
   #charge to certain position and then release after a certain degree
   
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

   #claw control
   if Remote.buttonL2.pressing():
      clawMotor_1.set_velocity(50, PERCENT)
      clawMotor_1.spin(FORWARD)
   elif Remote.buttonL1.pressing():
      clawMotor_1.set_velocity(-50, PERCENT)
      clawMotor_1.spin(FORWARD)
   else:
      clawMotor_1.stop()

   if Remote.buttonA.pressing(): #change buttonA to whichever we actually using
      fourBarMotorRight.set_velocity(25, PERCENT)
      fourBarMotorLeft.set_velocity(25, PERCENT)
      fourBarMotorRight.spin(FORWARD)
      fourBarMotorLeft.spin(FORWARD)
   elif Remote.buttonB.pressing(): #change buttonB to whichever we actually using
      fourBarMotorRight.set_velocity(-25, PERCENT)
      fourBarMotorLeft.set_velocity(-25, PERCENT)
      fourBarMotorRight.spin(FORWARD)
      fourBarMotorLeft.spin(FORWARD)
   else:
      fourBarMotorRight.stop()
      fourBarMotorLeft.stop()



remoteControl(Remote, rightFrontMotor, rightBackMotor, leftFrontMotor, leftBackMotor)


def autonCode():
#turning from start point to angle toward goal, TO CHANGE VALUES
   rightFrontMotor.spin_for(FORWARD, 400, DEGREES, wait=False) 
   rightBackMotor.spin_for(FORWARD, 400, DEGREES, wait=False)
   wait(500, MSEC)
#to move closer to goal and punch alliance triball, TO CHANGE VALUES
   rightFrontMotor.spin_for(FORWARD, 360, DEGREES, wait=False)
   rightBackMotor.spin_for(FORWARD, 360, DEGREES, wait=False)
   leftFrontMotor.spin_for(FORWARD, 360, DEGREES, wait=False)
   leftBackMotor.spin_for(FORWARD, 360, DEGREES, wait=False)
   Punchermotor_1.spin_for(FORWARD, 360-Punchermotor_1.position(), DEGREES, wait=True)
   wait(200, MSEC)
#to rotate toward the diagonal boundary, TO CHANGE VALUES
   rightFrontMotor.spin_for(FORWARD, 360, DEGREES, wait=False)
   rightBackMotor.spin_for(FORWARD, 360, DEGREES, wait=False)
   leftFrontMotor.spin_for(FORWARD, -360, DEGREES, wait=False)
   leftBackMotor.spin_for(FORWARD, -360, DEGREES, wait=False)
   wait(200, MSEC)
#to move toward the diagonal boundary, TO CHANGE VALUES
   rightFrontMotor.spin_for(FORWARD, 200, DEGREES, wait=False)
   rightBackMotor.spin_for(FORWARD, 200, DEGREES, wait=False)
   leftFrontMotor.spin_for(FORWARD, 200, DEGREES, wait=False)
   leftBackMotor.spin_for(FORWARD, 200, DEGREES, wait=False)
   wait(200, MSEC)
#engage claw to pick up new triball, TO CHANGE VALUE
   clawMotor_1.spin_for(FORWARD, 360, DEGREES, wait=False)
   clawMotor_1.stop() #assuming default mode is hold, else change it :)

#move back, TO CHANGE VALUES
   rightFrontMotor.spin_for(FORWARD, -200, DEGREES, wait=False)
   rightBackMotor.spin_for(FORWARD, -200, DEGREES, wait=False)
   leftFrontMotor.spin_for(FORWARD, -200, DEGREES, wait=False)
   leftBackMotor.spin_for(FORWARD, -200, DEGREES, wait=False)
#rotate back, TO CHANGE VALUES
   rightFrontMotor.spin_for(FORWARD, -360, DEGREES, wait=False)
   rightBackMotor.spin_for(FORWARD, -360, DEGREES, wait=False)
   leftFrontMotor.spin_for(FORWARD, 360, DEGREES, wait=False)
   leftBackMotor.spin_for(FORWARD, 360, DEGREES, wait=False)
   wait(200, MSEC)
#to let go of claw grip and fire, TO CHANGE VALUES
   clawMotor_1.spin_for(FORWARD, -250, DEGREES, wait=True)
   Punchermotor_1.spin_for(FORWARD, 360, DEGREES, wait=True)

#endgame code to be inserted. else, code for contact to elevation bar
   rightFrontMotor.spin_for(FORWARD, -300, DEGREES, wait=False)
   rightBackMotor.spin_for(FORWARD, -300, DEGREES, wait=False)
   leftFrontMotor.spin_for(FORWARD, -300, DEGREES, wait=False)
   leftBackMotor.spin_for(FORWARD, -300, DEGREES, wait=False)
   #to insert further code. (rotate & 4bar + claw contact with elevation bar TBD)

autonCode()