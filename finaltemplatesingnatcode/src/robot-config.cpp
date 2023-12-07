#include "vex.h"

using namespace vex;
using signature = vision::signature;
using code = vision::code;

// A global instance of brain used for printing to the V5 Brain screen
brain  Brain;

// VEXcode device constructors
motor rightFrontMotor = motor(PORT11, ratio6_1, false);
motor rightMiddleMotor = motor(PORT12, ratio6_1, false);
motor rightBackMotor = motor(PORT13, ratio6_1, false);
motor leftFrontMotor = motor(PORT1, ratio6_1, true);
motor leftMiddleMotor = motor(PORT2, ratio6_1, true);
motor leftBackMotor = motor(PORT3, ratio6_1, true);

motor rollerMotor = motor(PORT8, ratio6_1, true);
motor cataMotor = motor(PORT10, ratio6_1, true);

digital_out wall_solenoid = digital_out(Brain.ThreeWirePort.H);
inertial inertialSensor = inertial(PORT9); // to change port number accordingly
rotation cataRotationSensor = rotation(PORT15, false); // to change port number and reverse boolean accordingly 

controller Remote = controller(primary);

// VEXcode generated functions



/**
 * Used to initialize code/tasks/devices added using tools in VEXcode Pro.
 * 
 * This should be called at the start of your int main function.
 */
void vexcodeInit( void ) {
  rightFrontMotor.setBrake(brake);
  rightMiddleMotor.setBrake(brake);
  rightBackMotor.setBrake(brake);
  leftFrontMotor.setBrake(brake);
  leftMiddleMotor.setBrake(brake);
  leftBackMotor.setBrake(brake);
  inertialSensor.calibrate();
}