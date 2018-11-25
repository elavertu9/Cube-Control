from Light import Light
import time
import sys

class Plane() :

    def __init__(self, light_list) :
        self.lights = light_list
        self.turn_off_plane()

    def wait(self, seconds) :
        time.sleep(seconds)

    def turn_on_one_light(self, light_index, color) :
        self.lights[light_index].turn_color_on(color)

    def blink_one_light(self, light_index, color) :
        self.lights[light_index].blink_color(color)

    def turn_off_one_light(self, light_index) :
        self.lights[light_index].reset_light()

    def blink_plane(self, color) :
        self.turn_on_plane(color)
        self.wait(.5)
        self.turn_off_plane()

    def turn_on_plane(self, color) :
        for light in self.lights :
            light.turn_color_on(color)

    def turn_off_plane(self) :
        for light in self.lights :
            light.reset_light()
