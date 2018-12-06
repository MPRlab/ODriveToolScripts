#!/usr/bin/env python3

from __future__ import print_function

import odrive
from odrive.enums import *
import time
import math
import sys, os



if __name__ == "__main__":

	# Find a connected ODrive (this will block until you connect one)
	print("finding an odrive, wait a second...")
	my_drive = odrive.find_any()

	print("The bus voltage is " + str(my_drive.vbus_voltage) + "V")

	# List all the configs
	print("Axis config setting: " + odrive.axis0.config + "\n")
	print("Motor config setting: " + odrive.axis0.motor.config + "\n")
	print("Encoder config setting: " + odrive.axis0.encoder.config + "\n")


	# Erase Current Configuration
	text = input("Would you like to erase the existing configuration (y/n): ")
	if (text == "y"):
		my_drive.erase_configuration()
		print("configuration erased")



	# Set some hardware parameters temporarily
	print("Set some hardware parameters\n")

	# Set brake restance
	br_string = input("Input brake resistance in Ohms here: ")
	my_drive.config.brake_resistance = float(br_string)


	# Set number of pole pairs
	pp_string = input("Input number of pole pairs here: ")
	my_drive.axis0.motor.config.pole_pairs = float(pp)


	# If you are getting "ERROR_PHASE_RESISTANCE_OUT_OF_RANGE" error from the encoders
	# you may want to uncomment the line belowup the calibration max voltage to 5.0 V or higher 
	# my_drive.axis0.motor.config.resistance_calib_max_voltage = 5.0

	# Set the encoder CPR
	cpr_string = input("Input the counts per revolution of the encoder: ")
	my_drive.axis0.encoder.config.cpr = float(cpr_string)

	# Set whether the encoder uses an index pulses
	enc_index_string = input("Does the encoder have an index signal?(y/n): ")
	while(1):

		if(enc_index_string == "y"):
			my_drive.axis0.encoder.config.use_index = True
			break
		elif(enc_index_string == "n"):
			my_drive.axis0.encoder.config.use_index = False
			break
		else:
			enc_index_string = input("Please type 'y' or 'n': ")




""" Uncomment this code to set the control gains 

	my_drive.axis0.controller.config.vel_integrator_gain = 0
	my_drive.axis0.controller.config.vel_gain = 0.0001
	print("position gain:",my_drive.axis0.controller.config.pos_gain, " (counts/s)/counts")
	print("vel integrator gain:",my_drive.axis0.controller.config.vel_integrator_gain, " A/((counts/s) * s)")
	print("velocity gain gain:",my_drive.axis0.controller.config.vel_gain, " A/(counts/sec)")

"""



	my_drive.save_configuration()
	print("The new configuration is now saved on the odrive for axis 0. We will now reboot to ensure the configuration.\n")
	print("run 'odrivetool' from the terminal, set the state to closed loop control and try sending a position command when it boots up again")
	my_drive.reboot()

