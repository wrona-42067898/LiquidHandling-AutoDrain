#Start with your reagent loaded on slot 2
#Ctrl + C at any time to abort the script

import pyautogui as pya
import time

pya.PAUSE = 1
pya.FAILSAFE = True

number_of_inputs = int(input("Number of inputs to prime (1-4): "))
prime_duration = int(input("Number of seconds to prime for: "))
prime_x, prime_y = 53, 348

input_coords = [(20,641), (20,670), (20,700), (20,730)]
dispense_list = [(80,640), (80,670), (80,700), (80,730), (80,640)] #last coords will place it back in the first position


def drag_input(start_x, start_y, end_x, end_y):
	pya.moveTo(start_x, start_y)
	pya.dragTo(end_x, end_y, 1, button="left")
	time.sleep(2)


def prime_input(x, y):
	pya.click(x, y, button='left')
	time.sleep(8)
	pya.mouseDown(prime_x, prime_y)
	time.sleep(prime_duration)
	pya.mouseUp()
	time.sleep(5)
	pya.click(x, y, button='left')
	time.sleep(8)


print ("Press Ctrl+C at any time to abort")


try:
	for i in range(number_of_inputs):
		prime_input(input_coords[i][0], input_coords[i][1])
		drag_input(dispense_list[i][0], dispense_list[i][1], dispense_list[i+1][0], dispense_list[i+1][1])
	print ("\nDone.")

except KeyboardInterrupt: #clean output if user manually breaks with Ctrl+C
	print('\nDone.')