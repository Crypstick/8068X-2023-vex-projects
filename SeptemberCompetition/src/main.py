#region VEXcode Generated Robot Configuration
from vex import *

# wait for rotation sensor to fully initialize
wait(30, MSEC)


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration
# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       kevinorjalo                                                  #
# 	Created:      26/07/2023, 12:14:28                                         #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Robot configuration code
brain = Brain()
Remote = Controller(PRIMARY)


#Motor configurations
rightFrontMotor = Motor(Ports.PORT1, GearSetting.RATIO_6_1, False)
rightMiddleMotor = Motor(Ports.PORT2, GearSetting.RATIO_6_1, False)
rightBackMotor = Motor(Ports.PORT3, GearSetting.RATIO_6_1, True)
rightDriveSmart = MotorGroup(rightFrontMotor, rightMiddleMotor, rightBackMotor)
leftFrontMotor = Motor(Ports.PORT20, GearSetting.RATIO_6_1, False)
leftMiddleMotor = Motor(Ports.PORT19, GearSetting.RATIO_6_1, False)
leftBackMotor = Motor(Ports.PORT18, GearSetting.RATIO_6_1, True)
leftDriveSmart = MotorGroup(leftFrontMotor, leftMiddleMotor, leftBackMotor)
driveTrain = DriveTrain(leftDriveSmart, rightDriveSmart, units=MM)


rightFrontMotor.set_stopping(BRAKE)
rightMiddleMotor.set_stopping(BRAKE)
rightBackMotor.set_stopping(BRAKE)
leftFrontMotor.set_stopping(BRAKE)
leftMiddleMotor.set_stopping(BRAKE)
leftBackMotor.set_stopping(BRAKE)


# wait for rotation sensor to initialise
wait(30, MSEC)


rollerMotor_1 = Motor(Ports.PORT10, GearSetting.RATIO_6_1, True)
cataMotor_1 = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)

limit_switch_h = Limit(brain.three_wire_port.a)
wall_solonoid = DigitalOut(brain.three_wire_port.h)

wall_solonoid.set(False)

#autonomous code blocks for simplification
def goStraight(speed, distance):
  leftFrontMotor.spin_for(FORWARD, distance, DEGREES, speed, PERCENT, wait=False)
  leftMiddleMotor.spin_for(FORWARD, distance, DEGREES, speed, PERCENT, wait=False)
  leftBackMotor.spin_for(FORWARD, distance, DEGREES, speed, PERCENT, wait=False)
  rightFrontMotor.spin_for(FORWARD, distance, DEGREES, speed, PERCENT, wait=False)
  rightMiddleMotor.spin_for(FORWARD, distance, DEGREES, speed, PERCENT, wait=False)
  rightBackMotor.spin_for(FORWARD, distance, DEGREES, speed, PERCENT, wait=True)

def rotateRight(speed, distance):
  leftFrontMotor.spin_for(FORWARD, -1*distance, DEGREES, speed, PERCENT, wait=False)
  leftMiddleMotor.spin_for(FORWARD, -1*distance, DEGREES, speed, PERCENT, wait=False)
  leftBackMotor.spin_for(FORWARD, -1*distance, DEGREES, speed, PERCENT, wait=False)
  rightFrontMotor.spin_for(FORWARD, distance, DEGREES, speed, PERCENT, wait=False)
  rightMiddleMotor.spin_for(FORWARD, distance, DEGREES, speed, PERCENT, wait=False)
  rightBackMotor.spin_for(FORWARD, distance, DEGREES, speed, PERCENT, wait=True)

def rotateLeft(speed, distance):
  leftFrontMotor.spin_for(FORWARD, distance, DEGREES, speed, PERCENT, wait=False)
  leftMiddleMotor.spin_for(FORWARD, distance, DEGREES, speed, PERCENT, wait=False)
  leftBackMotor.spin_for(FORWARD, distance, DEGREES, speed, PERCENT, wait=False)
  rightFrontMotor.spin_for(FORWARD, -1*distance, DEGREES, speed, PERCENT, wait=False)
  rightMiddleMotor.spin_for(FORWARD, -1*distance, DEGREES, speed, PERCENT, wait=False)
  rightBackMotor.spin_for(FORWARD, -1*distance, DEGREES, speed, PERCENT, wait=True)


def autonomous():
  rotateLeft(80, 500)
  # #moving forward to push alliance triball inside, TO CHANGE VALUES
  # rightFrontMotor.spin_for(FORWARD, -600, DEGREES, wait=False)
  # rightMiddleMotor.spin_for(FORWARD, -600, DEGREES, wait=False)
  # rightBackMotor.spin_for(FORWARD, -600, DEGREES, wait=False)
  # leftFrontMotor.spin_for(FORWARD, -600, DEGREES,  wait=False)
  # leftMiddleMotor.spin_for(FORWARD, -600, DEGREES,  wait=False)
  # leftBackMotor.spin_for(FORWARD, -600, DEGREES,  wait=True)
  # print("triball deposit COMPLETE")
  # wait(500, MSEC)

  # #to move closer to goal and punch alliance triball, TO CHANGE VALUES
  # rightFrontMotor.spin_for(FORWARD, 500, DEGREES, wait=False)
  # rightMiddleMotor.spin_for(FORWARD, 500, DEGREES, wait=False)
  # rightBackMotor.spin_for(FORWARD, 500, DEGREES, wait=False)
  # leftFrontMotor.spin_for(FORWARD, 500, DEGREES,  wait=False)
  # leftMiddleMotor.spin_for(FORWARD, 500, DEGREES,  wait=False)
  # leftBackMotor.spin_for(FORWARD, 500, DEGREES,  wait=True)
  # print("Moving back to starting zone for turning COMPLETE")
  # wait(500, MSEC)
  
  # #to rotate toward the alliance bar, TO CHANGE VALUES
  # rightFrontMotor.spin_for(FORWARD, -1*185, DEGREES,  wait=False)
  # rightMiddleMotor.spin_for(FORWARD, -1*185, DEGREES,  wait=False)
  # rightBackMotor.spin_for(FORWARD, -1*185, DEGREES,  wait=False)
  # leftFrontMotor.spin_for(FORWARD, 185, DEGREES, wait=False)
  # leftBackMotor.spin_for(FORWARD, 185, DEGREES,  wait=False)
  # leftBackMotor.spin_for(FORWARD, 185, DEGREES, wait=True)
  # print("Rotating toward alliance bar COMPLETE")
  # wait(500, MSEC)
  
  # #to move forward to push triball below bar toward our side, TO CHANGE VALUES
  # rightFrontMotor.spin_for(FORWARD, 500, DEGREES, wait=False)
  # rightMiddleMotor.spin_for(FORWARD, 500, DEGREES, wait=False)
  # rightBackMotor.spin_for(FORWARD, 500, DEGREES, wait=False)
  # leftFrontMotor.spin_for(FORWARD, 500, DEGREES,  wait=False)
  # leftMiddleMotor.spin_for(FORWARD, 500, DEGREES,  wait=False)
  # leftBackMotor.spin_for(FORWARD, 500, DEGREES,  wait=True)
  # print("Push triball below bar toward our side COMPLETE")
  # wait(500, MSEC)
  
  # #move back for matchload, TO CHANGE VALUES
  # rightFrontMotor.spin_for(FORWARD, -400, DEGREES, wait=False)
  # rightMiddleMotor.spin_for(FORWARD, -400, DEGREES, wait=False)
  # rightBackMotor.spin_for(FORWARD, -400, DEGREES, wait=False)
  # leftFrontMotor.spin_for(FORWARD, -400, DEGREES,  wait=False)
  # leftMiddleMotor.spin_for(FORWARD, -400, DEGREES,  wait=False)
  # leftBackMotor.spin_for(FORWARD, -400, DEGREES,  wait=True)
  # print("Moving back for matchload COMPLETE")
  # wait(500, MSEC)




def driver_drivetrain():
  while True:
    #init
    fwd = Remote.axis1.position() * -1
    sideways = Remote.axis3.position() 
    rightTrain = fwd - sideways
    leftTrain = fwd + sideways


    #drivetrain
    rightDriveSmart.set_velocity(rightTrain, PERCENT)
    leftDriveSmart.set_velocity(leftTrain, PERCENT)

    # rightFrontMotor.set_velocity(rightTrain, PERCENT)
    # rightMiddleMotor.set_velocity(rightTrain, PERCENT)
    # rightBackMotor.set_velocity(rightTrain, PERCENT)
    # leftFrontMotor.set_velocity(leftTrain, PERCENT)
    # leftMiddleMotor.set_velocity(leftTrain, PERCENT)
    # leftBackMotor.set_velocity(leftTrain, PERCENT)


    rightDriveSmart.spin(FORWARD)
    leftDriveSmart.spin(FORWARD)

    


def driver_rollerIntake():
  if Remote.buttonL1.pressing():
    rollerMotor_1.set_velocity(100, PERCENT)
    rollerMotor_1.spin(FORWARD)
  elif Remote.buttonR1.pressing():
    rollerMotor_1.set_velocity(-100, PERCENT)
    rollerMotor_1.spin(FORWARD)
  else:
    rollerMotor_1.stop()

def driver_pneumatics():
  if Remote.buttonY.pressing():
      wall_solonoid.set(True)
  else:
      wall_solonoid.set(False)


    #cata control + limit switch code
'''
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
  '''
def driver_catacontrol():
  if Remote.buttonR2.pressing() == True:
    while Remote.buttonR2.pressing() == True:
      cataMotor_1.set_velocity(100, PERCENT)
      cataMotor_1.spin(FORWARD)
  else:
    cataMotor_1.set_velocity(0, PERCENT)
    cataMotor_1.stop()

def driver_control():

    while 1:
        driver_drivetrain()
        driver_rollerIntake()
        driver_catacontrol()
        driver_pneumatics()

'driver_control(Remote, rightFrontMotor, rightMiddleMotor, rightBackMotor, leftFrontMotor, leftMiddleMotor, leftBackMotor)'
competition = Competition(driver_control(), autonomous)