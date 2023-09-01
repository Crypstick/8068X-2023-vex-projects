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
rightFrontMotor = Motor(Ports.PORT1, GearSetting.RATIO_6_1, True)
rightMiddleMotor = Motor(Ports.PORT9, GearSetting.RATIO_6_1, True)
rightBackMotor = Motor(Ports.PORT10, GearSetting.RATIO_6_1, False)
rightDriveSmart = MotorGroup(rightFrontMotor, rightMiddleMotor, rightBackMotor)
leftFrontMotor = Motor(Ports.PORT19, GearSetting.RATIO_6_1, False)
leftMiddleMotor = Motor(Ports.PORT11, GearSetting.RATIO_6_1, False)
leftBackMotor = Motor(Ports.PORT20, GearSetting.RATIO_6_1, True)
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


rollerMotor_1 = Motor(Ports.PORT3, GearSetting.RATIO_6_1, True)
cataMotor_1 = Motor(Ports.PORT13, GearSetting.RATIO_18_1, True)

wall_solonoid = DigitalOut(brain.three_wire_port.a)
wall_solonoid.set(False)

pneumaticActivationButton = int()

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


def skillsAuton():
   goStraight(80, 1500)
   wait(200, MSEC)
   rotateRight(50, 200)
   wait(200, MSEC)
   rollerMotor_1.set_velocity(100, PERCENT)
   rollerMotor_1.spin(REVERSE)
   goStraight(80, 800)
   wait(200, MSEC)
   rollerMotor_1.set_velocity(0, PERCENT)
   rollerMotor_1.spin(FORWARD)
   goStraight(80, -800)
   wait(200, MSEC)
   rotateLeft(50, 180)
   wait(200, MSEC)
   goStraight(80, -800)
   wait(200, MSEC)

def driver_drivetrain():
  #init
  fwd = Remote.axis3.position()
  sideways = Remote.axis1.position() 
  rightTrain = fwd + sideways
  leftTrain = fwd - sideways

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

def toggle(boolean):
  if boolean == False:
    while boolean == False:
      boolean = False
  elif boolean == True:
    while boolean == True:
      boolean = True

def driver_pneumatics():
  global pneumaticActivationButton
  # if pneumaticActivationButton == 1:
  #   wall_solonoid.set(True)
  #   if Remote.buttonB.pressing():
  #     pneumaticActivationButton = 0
  #     print("Pneumatic Disabled")
  #     pass
  # elif pneumaticActivationButton == 0:
  #   wall_solonoid.set(False)
  #   if Remote.buttonY.pressing():
  #     pneumaticActivationButton = 1
  #     print("Pneumatic Activated")
  if Remote.buttonY.pressing():
    pneumaticActivationButton = 1
    if pneumaticActivationButton == 1:
      wall_solonoid.set(True)
      print("Pneumatic is working!!!!")
  elif Remote.buttonB.pressing():
    pneumaticActivationButton = 0
    wall_solonoid.set(False)
    if pneumaticActivationButton == 0:
      wall_solonoid.set(False)
      print("Pneumatic is disabled!!!")
  #   pneumaticActivationButton = True
  #   wall_solonoid.set(True)
  # else:
  #   pneumaticActivationButton = False

def driver_catacontrol():
  if Remote.buttonR2.pressing() == True:
    while Remote.buttonR2.pressing() == True:
      cataMotor_1.set_velocity(100, PERCENT)
      cataMotor_1.spin(FORWARD)
  else:
    cataMotor_1.set_velocity(0, PERCENT)
    cataMotor_1.stop()

def driver_control():
    solenoidActive = False
    while True:
        driver_drivetrain()
        driver_rollerIntake()
        driver_catacontrol()
        driver_pneumatics()
