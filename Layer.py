import RPi.GPIO as GPIO
import time
import sys

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

  def turn_on_layer(self, which_layer) :
    GPIO.output(self.get_pin_number_if_layer_is_valid(which_layer), HIGH)

  def turn_off_layer(self, which_layer) :
    GPIO.output(self.get_pin_number_if_layer_is_valid(which_layer), LOW)

  def get_pin_number_if_layer_is_valid(self, which_layer) :
      return_value = 0
      if (which_layer > len(self.ground_pins)) or (which_layer < 0) :
        error_string = "Invalid Layer argument (" + which_layer + ")."
        sys.exit(error_string)
      else :
        return_value = self.ground_pins[which_layer]
      return return_value
