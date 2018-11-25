from Light import Light
from Plane import Plane
from Layer import Layer
from Register import Register
import RPi.GPIO as GPIO
import time

# Configuration Constants
SLEEP_DURATION = 1                  # In seconds, delay between lights
LOW = GPIO.LOW                      # Low, turns off
HIGH = GPIO.HIGH                    # High, turns on
MODE = GPIO.BCM                     # Set pin mode on board (BCM/BOARD)
WARNINGS = False                    # Enable Warnings

def reset_Environment() :
    GPIO.cleanup()

def wait(seconds) :
    time.sleep(seconds)

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
	
	register_0 = Register(20, 12, 16)

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

	layer_selector = Layer(ground_pins)
	
	register_0.shiftout(0b100000000000000)
	
	wait(3)
	
	register_0.reset_lights()

    # END TESTING
	print("Darkness approaching...")
	wait(2)
	reset_Environment()
