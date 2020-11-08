import picar_4wd as fc
import time
import numpy as np
import math

# Specifies the max range of the Ultrasonic Sensor by 10 degree increments
t_angles = range(-100, 100, 10)

# Sets the servo and the sensor up
distance = fc.Ultrasonic(fc.Pin('D8'), fc.Pin('D9'))
a = fc.Servo(fc.PWM("P0"), 0)

# Declares map size to be drawn
map_size = 21

# Finds the center of the map
center = map_size // 2

# Draws a map of the given size with zero integers
t_map = np.zeros((map_size,map_size), 'int16')

# Finds the appropriate scale 
scale = round(150 / map_size)*2

# Places a lucky number 7 in the center of the map to show the location of the car.
t_map[center,center] = 7

#test
test1 = 1
    

# Main loop to measure the distance to map out what is infront 
for angle in t_angles:
    
    # Sets the angle to which to start
    a.set_angle(angle)
    
    # Sensor gets distance
    reading = distance.get_distance()
    
    # found out that without a time gap the servo fails to move
    time.sleep(.1)
    
    
    # Sensor's max reading is 130cm, and returns a -2
    if reading is -2:
        print("angle reading: " + str(angle) + " degrees")
        print("The distance is past the max of 130cm")

    # Plots a 1 where an item is found and plots onto scaled map
    else:
        print("angle reading: " + str(angle) + " degrees")
        print("distance " + str(reading) + "cm")
        x = (round(math.cos((math.radians(angle + 90))) * reading) / scale)
        y = (round(math.sin((math.radians(angle + 90))) * reading) / scale)
        t_map[center-round(y)][center+round(x)] = test1
        test1 += 1


print(t_map[:center+1, :map_size-1])

