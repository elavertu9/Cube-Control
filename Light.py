import RPi.GPIO as GPIO
import time

LOW = GPIO.LOW
HIGH = GPIO.HIGH
OUT = GPIO.OUT

class Light() :

  def __init__(self, RED, GREEN, BLUE) :
    self.pins_array = [RED, GREEN, BLUE]
    self.RED = RED
    self.GREEN = GREEN
    self.BLUE = BLUE
    self.configure_pins_for_output()
    self.reset_light()

  def configure_pins_for_output(self) :
    for pin in self.pins_array :
        GPIO.setup(pin, OUT)

  def wait(self, seconds) :
    time.sleep(seconds)

  def turn_color_on(self, color) :
    GPIO.output(self.get_pin_number_if_color_is_valid(color), HIGH)

  def turn_color_off(self, color) :
      GPIO.output(self.get_pin_number_if_color_is_valid(color), LOW)

  def blink_color(self, color) :
      self.turn_color_on(color)
      wait(.5)
      self.turn_color_off(color)

  def reset_light(self) :
     self.turn_color_off("RED")
     self.turn_color_off("GREEN")
     self.turn_color_off("BLUE")

  def get_pin_number_if_color_is_valid(self, color) :
     return_value = 0
     if color == "RED" :
        return_value = self.RED
     elif color == "GREEN" :
        return_value = self.GREEN
     elif color == "BLUE" :
        return_value = self.BLUE
     else :
        sys.exit("Invalid Color Option! Valid options are RED, GREEN, BLUE.")
     return return_value
