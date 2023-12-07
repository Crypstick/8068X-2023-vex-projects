#pragma once
#include "vex.h"

class PID
{
public:
  float error = 0;
  float kp = 1.75; //1.675
  float ki = 0;
  float kd = 1.6; //1.6
  float starti = 15;
  float settle_error = 0;
  float settle_time = 0;
  float timeout = 6000;
  float accumulated_error = 0;
  float previous_error = 0;
  float output = 0;
  float time_spent_settled = 0;
  float time_spent_running = 0;

  PID(float error, float kp, float ki, float kd, float starti, float settle_error, float settle_time, float timeout);

  PID(float error, float kp, float ki, float kd, float starti);

  float compute(float error);

  bool is_settled();
};