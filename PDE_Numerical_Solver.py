import numpy as np
import quaternion

dt = 0.001 #Timestep (seconds)
maxTime = 900.0 #Total simulation time (seconds)

thrust_file = open("Thrust.txt").read().split("\n")
#drag_file = open("Drag.txt").read().split("\n")
#gravity_file = open("Gravity.txt").read().split("\n")
#mass_file = open("Mass.txt").read().split("\n")
#thrust_torque_file = open("Torque_Thrust.txt").read().split("\n")
#drag_torque_file = open("Torque_Drag.txt").read().split("\n")
#gravity_torque_file = open("Torque_Gravity.txt").read().split("\n")
#moment_of_intertia_file = open("MOI.txt").read().split("\n")

orientation = np.array([0.0, 1.0, 0.0]) #Orientation vector of the rocket (x-z horizontal)
angular_velocity = np.array([0.0, 0.0, 0.0]) #Angular velocity vector of the rocket (radians/sec)

position = np.array([0.0, 0.0, 0.0]) #Position of the CoM of the rocket (m)
velocity = np.array([0.0, 0.0, 0.0]) #Velocity of the CoM of the rocket (m/s)

thrust_array = []
for line in thrust_file[0:len(thrust_file)-1]:
    arr = line.split(' ')
    arr[0] = float(arr[0])
    arr[1] = float(arr[1])
    thrust_array.append(arr)
thrust_array.append([maxTime+0.1, 0.0])
thrust_array.append([maxTime+0.2, 0.0])
thrust = {}
for i in range(int(maxTime/dt)):
    time = i*dt
    j = 0
    while(time>thrust_array[j][0]):
        j+=1
    t_start = thrust_array[j-1][0]
    t_end = thrust_array[j][0]
    f_start = thrust_array[j-1][1]
    f_end = thrust_array[j][1]
    thrust[time] = (f_end-f_start)/(t_end-t_start)*(time-t_start)+f_start
    
