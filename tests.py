Tests:
    while(1) :
        plane_0.turn_Off_One_Light()
        plane_0.turn_On_One_Light(0, "RED")
        wait(.1)
        plane_0.turn_On_One_Light(1, "RED")
        plane_0.turn_Off_One_Light(0)
        wait(.1)
        plane_0.turn_On_One_Light(3, "RED")
        plane_0.turn_Off_One_Light(1)
        wait(.1)
        plane_0.turn_On_One_Light(2, "RED")
        plane_0.turn_Off_One_Light(3)
        wait(.1)
        
        plane_0.turn_On_One_Light(0, "GREEN")
        plane_0.turn_Off_One_Light(2)
        wait(.1)
        plane_0.turn_On_One_Light(1, "GREEN")
        plane_0.turn_Off_One_Light(0)
        wait(.1)
        plane_0.turn_On_One_Light(3, "GREEN")
        plane_0.turn_Off_One_Light(1)
        wait(.1)
        plane_0.turn_On_One_Light(2, "GREEN")
        plane_0.turn_Off_One_Light(3)
        wait(.1)
        
        plane_0.turn_On_One_Light(0, "BLUE")
        plane_0.turn_Off_One_Light(2)
        wait(.1)
        plane_0.turn_On_One_Light(1, "BLUE")
        plane_0.turn_Off_One_Light(0)
        wait(.1)
        plane_0.turn_On_One_Light(3, "BLUE")
        plane_0.turn_Off_One_Light(1)
        wait(.1)
        plane_0.turn_On_One_Light(2, "BLUE")
        plane_0.turn_Off_One_Light(3)
        wait(.1)
        
        
        
		##############################################
        GPIO.output(layer_zero_pin, HIGH)
        plane_0.turn_on_plane("GREEN")
        wait(1)
        GPIO.output(layer_zero_pin, LOW)
        GPIO.output(layer_one_pin, HIGH)
        plane_0.turn_on_plane("BLUE")
        wait(1)
        GPIO.output(layer_one_pin, LOW)
        GPIO.output(layer_two_pin, HIGH)
        plane_0.turn_on_plane("RED")
        wait(1)
        GPIO.output(layer_two_pin, LOW)
        GPIO.output(layer_three_pin, HIGH)
        plane_0.turn_on_plane("GREEN")
        wait(1)
        GPIO.output(layer_three_pin, LOW)
        
        
        
        ##############################################
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
    # Test Commit




        ##############################################
shift_register_binary_matrix = [0b10000000, 0b1000000, 0b100000, 0b10000, 0b1000, 0b100, 0b10, 0b1]
	
	register_coordinates = { }
	register_coordinates["ZERO"] = 0b10000000
	register_coordinates["ONE"] = 0b1000000
	register_coordinates["TWO"] = 0b100000
	register_coordinates["THREE"] = 0b10000
	register_coordinates["FOUR"] = 0b1000
	register_coordinates["FIVE"] = 0b100
	register_coordinates["SIX"] = 0b10
	register_coordinates["SEVEN"] = 0b1
