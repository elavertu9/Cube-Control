import RPi.GPIO as GPIO

LOW = GPIO.LOW
HIGH = GPIO.HIGH
OUT = GPIO.OUT

class Register() :

	def __init__(self, DATA_PIN, CLOCK_PIN, LATCH_PIN) :
		self.DATA_PIN = DATA_PIN
		self.CLOCK_PIN = CLOCK_PIN
		self.LATCH_PIN = LATCH_PIN
		self.register_pins = [self.DATA_PIN, self.CLOCK_PIN, self.LATCH_PIN]
		self.configure_pins_for_output()
	
	def configure_pins_for_output(self) :
		for pin in self.register_pins :
			GPIO.setup(pin, OUT)
			
	def shiftout(self, byte) :
		GPIO.output(self.LATCH_PIN, LOW)
		for x in range(16) :
			GPIO.output(self.DATA_PIN, (byte >> x) & 1)
			GPIO.output(self.CLOCK_PIN, HIGH)
			GPIO.output(self.CLOCK_PIN, LOW)
		GPIO.output(self.LATCH_PIN, HIGH)
	
	def shiftout_by_light_number(self, light_number) :
		self.shiftout(1 << (15 - light_number))
	
	def reset_lights(self) :
		self.shiftout(0)
