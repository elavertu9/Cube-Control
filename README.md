


># Term Project: The Cube
*Note: The follow files are not finished. They are a work
      in progress.*

You will see `self` as a parameter for a lot of the methods...

This is Python's class method syntax. Think of it as `this`

being passed as a parameter. In reality, you do NOT supply the

argument for `self` when you call the method.

## I. Light.py
**Constructor :**
```python
  Light(self, RED, GREEN, BLUE)
```

 - `RED`, `GREEN`, `BLUE` correspond to their pin numbers.
      Creates a Light object by accepting color pin
      numbers in the order above. The constructor
      automatically configures the pins for output
      and sets all pins to LOW.

- **Methods:**
	- *Valid `color` arguments: "RED", "GREEN", "BLUE"*

```python
    def configure_pins_for_output(self)
    def wait(self, seconds)
    def turn_color_on(self, color)
    def turn_color_off(self, color)
    def blink_color(self color)
    def reset_light(self)
    def get_pin_number_if_color_is_valid(self, color)
```

## II. Plane.py
**Constructor :**
```python
  Plane(self, light_list)  
```

- `light_list` is a list of the Light objects you
      have initialized that lay in the same plane.
      Creates a Plane object that allows you to
      control a group of LED's at a time. The constructor
      also sets all pins to LOW connected to every Light
      object in the light_list.

 - **Methods :**
    - *(Valid `color` arguments: "RED", "GREEN", "BLUE")*

 ```python
    def wait(self, seconds)
    def turn_on_one_light(self, light_index, color)
    def blink_one_light(self, light_index, color)
    def turn_off_one_light(self, light_index)
    def blink_plane(self, color)
    def turn_on_plane(self, color)
    def turn_off_plane(self)
```

## III. Layer.py
 **Constructor :**
```python
  Layer(self, ground_pins_list)  
```

  - `ground_pins_list` is a list of the connected ground
      pin numbers. The constructor sets up the pins for output
      and turns them to LOW by default. Creates a Layer object
      that allows you to control which layer of the cube is turned
      on. This is is achieved by turning certain layers on and
      off. I do not supply you with power management so you
      may shoot yourself in the foot if you'd like :)

 - **Methods :**

```python
   def configure_pins_for_output(self)
   def turn_off_all_pins(self)
   def turn_on_layer(self, which_layer)
   def turn_off_layer(self, which_layer)
   def get_pin_number_if_layer_is_valid(self, which_layer)
```

## IV. Register.py
  **Constructor :**
```python
	Register(self, DATA_PIN, CLOCK_PIN, LATCH_PIN)
```

	- `DATA_PIN`, `CLOCK_PIN`, `LATCH_PIN` correspond to the
	   register pin numbers. Creates a Register object by accepting
	   the register pin numbers in the order above. The Register
	   object has a few methods to assist in bit shifting. The 
	   Register constructor automatically configures the pins 
	   for output. 
	   
	- **Methods :**

```python
	def configure_pins_for_output(self)
	def shiftout(self, byte)
	def shiftout_by_light_number(self, light_number)
	def reset_lights(self)
```

## V. test.py
  * A file including a bunch of random code that I felt
    may be needed again. A lot of it is Light patterns and
    tests we have ran while building.
