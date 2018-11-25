from Light import Light
from Plane import Plane
import RPi.GPIO as GPIO
import time

# Configuration Constants
SLEEP_DURATION = 1                  # In seconds, delay between lights
LOW = GPIO.LOW                      # Low, turns off 
HIGH = GPIO.HIGH                    # High, turns on
MODE = GPIO.BCM                     # Set pin mode on board (BCM/BOARD)
WARNINGS = False 
                   # Enable Warnings

def reset_Environment() :
    GPIO.cleanup()

def wait(seconds) :
    time.sleep(seconds);

if __name__ == "__main__" : 

	# Configure mode and pins for output
	GPIO.setmode(MODE)
	GPIO.setwarnings(WARNINGS)
    
	# TESTING
	print("Let there be light!");
    
	# INSERT TEST BELOW
    
    # GPIO pin numbers
	pins = [[20,24,25], [9,10,6], [5,27,11], [26,19, 13]]
	ground_pins = [21,16,12,18]
    
    
	column_0 = Light(pins[0][0], pins[0][1], pins[0][2])
	column_1 = Light(pins[1][0], pins[1][1], pins[1][2])
	column_2 = Light(pins[2][0], pins[2][1], pins[2][2])
	column_3 = Light(pins[3][0], pins[3][1], pins[3][2])
   
	light_list_0 = [column_0]
	light_list_1 = [column_1]
	light_list_2 = [column_2]
	light_list_3 = [column_3]
    
	plane_0 = Plane(light_list_0)
	plane_1 = Plane(light_list_1)
	plane_2 = Plane(light_list_2)
	plane_3 = Plane(light_list_3)
    
	plane_list = [plane_0, plane_1, plane_2, plane_3]
    
	for pin in ground_pins :
		GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, LOW)
		
	for plane in plane_list :
		plane.turn_off_plane()
		
	GPIO.output(ground_pins[0], HIGH)
		
	for plane in plane_list :
		plane.turn_on_plane("GREEN")
		wait(1)
		plane.turn_off_plane()
			
	GPIO.output(ground_pins[0], LOW)
	GPIO.output(ground_pins[1], HIGH)
		
	for plane in plane_list :
		plane.turn_on_plane("GREEN")
		wait(1)
		plane.turn_off_plane()
			
	GPIO.output(ground_pins[1], LOW)
	GPIO.output(ground_pins[2], HIGH)
		
	for plane in plane_list :
		plane.turn_on_plane("GREEN")
		wait(1)
		plane.turn_off_plane()
		
	GPIO.output(ground_pins[2], LOW)
	GPIO.output(ground_pins[3], HIGH)
    
	for plane in plane_list :
		plane.turn_on_plane("GREEN")
		wait(1)
		plane.turn_off_plane()
    
	GPIO.output(ground_pins[3], LOW)
    
    
    
    #~ plane = {}
    #~ plane[0] = plane_0
    #~ plane[1] = plane_1
    #~ plane[2] = plane_2
    #~ plane[3] = plane_3
    
    #~ GPIO.setup(layers[0], GPIO.OUT)
    #~ GPIO.setup(layers[1], GPIO.OUT)
    #~ GPIO.setup(layers[2], GPIO.OUT)
    #~ GPIO.setup(layers[3], GPIO.OUT)
	
    #~ while 1:
		#~ GPIO.output(layers[0], HIGH)
		#~ plane_0.turn_on_plane("BLUE")
	
    #~ GPIO.output(layers[0], HIGH)
    #~ GPIO.output(layers[1], LOW)
    
    #~ while 1:
    #~ counter = 0
    #~ col = 0
    #~ while 1:
		
	    #~ for h in range(3):
			#~ for i in range(4):
				#~ GPIO.output(layers[i],HIGH)
			
				#~ for j in range(4):
					#~ GPIO.output(pins[j][col],HIGH)
				#~ wait(.001)
				#~ for j in range(4):
					#~ GPIO.output(pins[j][col],LOW)
				
				#~ GPIO.output(layers[i],LOW)
				#~ counter = counter + 1
				
			
			#~ if (counter%100) == 0:
				#~ counter = 0
				#~ if col == 2:
					#~ col = 0
				#~ else:
					#~ col = col + 1
			

    #~ plane[0].turn_off_plane()
    #~ plane[1].turn_off_plane()
    #~ plane[2].turn_off_plane()
    #~ plane[3].turn_off_plane()
	
    #~ plane[0].turn_on_plane("BLUE")
    #~ plane[1].turn_on_plane("RED")
    #~ plane[2].turn_on_plane("GREEN")
    
    
    
    
    # END TESTING
	print("Darkness approaching...")
	wait(2)
	reset_Environment()
