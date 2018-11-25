# Cube
Raspberry Pi controlled LED RGB Cube

Eli's a Bitch

Note: The follow files are not finished. They are a work
      in progress.

I. Light.py
-----------
  *Light(RED, GREEN, BLUE)
    * `RED`, `GREEN`, `BLUE` correspond to their pin numbers.
      Creates a Light object by accepting color pin
      numbers in the order above. The constructor
      automatically configures the pins for output
      and sets all pins to LOW.

  *Methods:
    *(Valid color arguments: "RED", "GREEN", "BLUE")*
    *configure_pins_for_output() -> Called by constructor
    *wait(seconds)
    *turn_color_on(color)
    *turn_color_off(color)
    *blink_color(color)
    *reset_light() -> Called by constructor
    *get_pin_number_if_color_is_valid()

II. Plane.py
------------
  *Plane(light_list)
    * light_list is a list of the Light objects you
      have initialized that lay in the same plane.
      Creates a Plane object that allows you to
      control a group of LED's at a time. The constructor
      also sets all pins to LOW connected to every Light
      object in the light_list.

  *Methods:
    *(Valid color arguments: "RED", "GREEN", "BLUE")*
    *wait(seconds)
    *turn_on_one_light(light_index, color)
    *blink_one_light(light_index, color)
    *turn_off_one_light(light_index)
    *blink_plane(color)
    *turn_on_plane(color)
    *turn_off_plane()

III. Layer.py
-------------
  *Layer(ground_pins_list)
    * ground_pins_list is a list of the connected ground
      pin numbers. The constructor sets up the pins for output
      and turns them to LOW by default. Creates a Layer object
      that allows you to control which layer of the cube is turned
      on. This is is achieved by turning certain layers on and
      off. I do not supply you with power management so you
      may shoot yourself in the foot if you'd like :)

  *Methods:
    *configure_pins_for_output() -> Called by constructor
    *turn_off_all_pins() -> Called by constructor

IV. test.py
-----------
  * A file including a bunch of random code that I felt
    may be needed again. A lot of it is Light patterns and
    tests we have ran while building.
