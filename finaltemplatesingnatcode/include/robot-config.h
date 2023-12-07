using namespace vex;

extern brain Brain;

// VEXcode devices

extern motor rightFrontMotor;
extern motor rightMiddleMotor;
extern motor rightBackMotor;
extern motor leftFrontMotor;
extern motor leftMiddleMotor;
extern motor leftBackMotor;

extern motor rollerMotor;
extern motor cataMotor;

extern digital_out wall_solenoid;
extern inertial inertialSensor;
extern rotation cataRotationSensor;
extern controller Remote;

/**
 * Used to initialize code/tasks/devices added using tools in VEXcode Pro.
 * 
 * This should be called at the start of your int main function.
 */
void  vexcodeInit( void );