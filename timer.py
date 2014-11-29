#Terminal Timer by tony kyriakidis.

from time import sleep
from datetime import datetime, time
#time and date contain the values bellow
time = datetime.now().strftime('%H:%M:%S')
date = datetime.now().strftime('%d-%m-%Y')
#Print them out at the terminal at the start of the program.
print ("Time: %s ") % time
print ("Date: %s ") % date
print "\nTerminal Timer by Tony Kyriakidis. \nTo Exit press CTRL-C. \n"

#Define the timer function
def timer():
	while True:
		#take the input from the user
		try:
			task = raw_input('Timer Name:')
			minutes = int(raw_input('How many minutes? :'))
			#create minutes in seconds
			seconds = minutes * 60
		# if it's not a number
		except ValueError:
			print('Please enter a valid number.')
			continue
		print("The time now is: %s " % time)
		# The loop:
		for second in range(0, seconds):
			print str(seconds - second) + (" seconds to complete: %s | press CTRL-C to interupt") % task
			sleep(1)
		#When done print DONE.
		print ("\n\nTime is up for %s") % task

try:
	timer()
#Pressing CTRL-C interrupts and stops the timer.
except KeyboardInterrupt:
	print('\n\nKeyboard interruption. ')