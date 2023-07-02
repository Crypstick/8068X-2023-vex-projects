#   please note to put this code in another place
#   because it won't work if you try to run it

# Library imports
from vex import *

# Robot configuration code
brain = Brain()
Remote = Controller(PRIMARY)
'''
#PID varibales
error = float()
kp = float()
ki = float()
kd = float()
starti = float()
settle_error = float()
settle_time = float()
timeout = float()
accumulated_error = float()
previous_error = float()
output = float()
time_spent_settled = float()
time_spent_running = float()
'''


#PID Code

#   Please change values according to what needs to be done
#   Genuinely have no idea what the hell the values are meant
#   to be, I think I gotta ask Zachary on what I gotta do to
#   get the values.

#   Usage: PID(error, kp, ki, kd, starti, settle_error, settle_time, timeout)
#   and somehow, BOOM!???? IDK ANYMORE MAN
class PID:
    def _init_(self, error, kp, ki, kd, starti, settle_error, settle_time, timeout):
        self.error = 0
        self.kp = 0
        self.ki = 0
        self.kd = 0
        self.starti = 0
        self.settle_error = 0
        self.settle_time = 0
        self.timeout = 0
        self.accumulated_error = 0
        self.previous_error = 0
        self.output = 0
        self.time_spent_settled = 0
        self.time_spent_running = 0

    def compute(self, error):
        pass

    def is_settled(self):
        pass
    