# Library imports
from vex import *

#Brain should be defined by default
brain = Brain()
x = int()

#Motor configurations
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

def autonSkillsCode():
    #init code
    global x
    #moving toward red starting point triball, TO CHANGE VALUES
    rightFrontMotor.spin_for(FORWARD, 400, DEGREES, wait=False)
    rightMiddleMotor.spin_for(FORWARD, 400, DEGREES, wait=False)
    rightBackMotor.spin_for(FORWARD, 400, DEGREES, wait=False)
    leftFrontMotor.spin_for(FORWARD, 400, DEGREES, wait=False)
    leftMiddleMotor.spin_for(FORWARD, 400, DEGREES, wait=False)
    leftBackMotor.spin_for(FORWARD, 400, DEGREES, wait=True)
    print("Moving toward red starting point triball COMPLETE")
    wait(500, MSEC)
    #moving toward red match load bar, TO CHANGE VALUES
    rightFrontMotor.spin_for(FORWARD, 400, DEGREES, wait=False)
    rightMiddleMotor.spin_for(FORWARD, 400, DEGREES, wait=False)
    rightBackMotor.spin_for(FORWARD, 400, DEGREES, wait=False)
    leftFrontMotor.spin_for(FORWARD, 400, DEGREES, wait=False)
    leftMiddleMotor.spin_for(FORWARD, 400, DEGREES, wait=False)
    leftBackMotor.spin_for(FORWARD, 400, DEGREES, wait=True)
    print("Moving toward red match load bar COMPLETE")
    wait(500, MSEC)
    #MATCH LOAD bEgInS, TO CHANGE VALUES
    for i in range(0,46):
        cataMotor_1.spin_for(FORWARD, 400, DEGREES, wait=True)
    print("MATCHLOAD COMPLETE")
    wait(500,MSEC)
    '''
    TO INSERT REST OF CODE TO PUSH THE TRIBALLS LATER
    '''