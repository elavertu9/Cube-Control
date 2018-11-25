from Light import Light
from Plane import Plane
import RPi.GPIO as IO
import time

# Configuration Constants
SLEEP_DURATION = 1                  # In seconds, delay between lights
LOW = IO.LOW                      # Low, turns off 
HIGH = IO.HIGH                    # High, turns on
MODE = IO.BCM                     # Set pin mode on board (BCM/BOARD)
WARNINGS = False 
                   # Enable Warnings
if __name__ == "__main__" : 
	IO.setmode(MODE)
	IO.setwarnings(WARNINGS)
	IO.cleanup()

	OE = 21
	DATA = 20
	CP = 12
	SHIFT = 16
	MR = 25
	x=1                       
	IO.setup(DATA,IO.OUT)            # initialize GPIO Pins as an output.
	IO.setup(SHIFT,IO.OUT)
	IO.setup(CP,IO.OUT)
	IO.setup(MR,IO.OUT)
	while 1:       
		print("BITCHES")                        # execute loop forever
		for y in range(8):            # loop for counting up 8 times
			IO.output(DATA,HIGH)            # pull up the data pin for every bit.
			time.sleep(.5)            # wait for 100ms
			IO.output(CP,HIGH)            # pull CLOCK pin high
			time.sleep(0.5)
			IO.output(CP,LOW)            # pull CLOCK pin down, to send a rising edge
			IO.output(DATA,LOW)            # clear the DATA pin
			IO.output(SHIFT,HIGH)            # pull the SHIFT pin high to put the 8 bit data out parallel
			time.sleep(0.5)
			IO.output(SHIFT,LOW)            # pull down the SHIFT pin
		print("HOES")
		for y in range(8):            # loop for counting up 8 times
			IO.output(DATA,LOW)            # clear the DATA pin, to send 0
			time.sleep(0.5)            # wait for 100ms
			IO.output(CP,HIGH)            # pull CLOCK pin high
			time.sleep(0.5)
			IO.output(CP,LOW)            # pull CLOCK pin down, to send a rising edge
			IO.output(DATA,LOW)            # keep the DATA bit low to keep the countdown
			IO.output(SHIFT,HIGH)            # pull the SHIFT pin high to put the 8 bit data out parallel
			time.sleep(0.5)
			IO.output(SHIFT, LOW)
		print("GET MONEY")
		#~ for y in range(8):
			#~ IO.output(DATA, HIGH)            # pull up the data pin for every bit.
			#~ time.sleep(0.1)            # wait for 100ms
			#~ IO.output(CP,HIGH)            # pull CLOCK pin high
			#~ time.sleep(0.1)
			#~ IO.output(CP,LOW)            # pull CLOCK pin down, to send a rising edge
			#~ IO.output(DATA,LOW)            # clear the DATA pin
			#~ IO.output(SHIFT,HIGH)            # pull the SHIFT pin high to put the 8 bit data out parallel
			#~ time.sleep(0.1)
			#~ IO.output(SHIFT,LOW)            # pull down the SHIFT pin
		
	
	

