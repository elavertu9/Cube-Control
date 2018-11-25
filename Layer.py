import RPi.GPIO as GPIO
import time

LOW = GPIO.LOW
HIGH = GPIO.HIGH
OUT = GPIO.OUT

class Layer() :

  def __init__(self, ground_pins_list) :
    self.ground_pins = ground_pins_list
    self.configure_pins_for_output()
    self.turn_off_all_pins()

  def configure_pins_for_output(self) :
    for pin in ground_pins :
        GPIO.setup(pin, GPIO.OUT)

  def turn_off_all_pins(self) :
    for pin in ground_pins :
        GPIO.output(pin, LOW)
