from timer import *

print("Timer example:")

timer = Timer()

timer.set_timer_start()

print("Idle Time ...")
idle = 0 
for index in range(100):
    idle += index
    print(idle)

timer.set_timer_end()

print("Time elapsed:")
print("Began at: ", timer.get_timer_start() )
print("Ended at: ", timer.get_timer_end() )
print("Time Frame: ", timer.get_timer_difference() )