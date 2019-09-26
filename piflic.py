#original URL:https://www.instructables.com/id/PiFlic-Flic-wireless-smart-button-Raspberry-Pi/
# PIFLIC 
# RASPBERRY PI AND FLIC WIRELESS SMART BUTTON TOGETHER
# BY ACMECORPORATION

import time
import os
import grovepi
from grovepi import *

# Connect the Grove LED to digital port D4
ledblue = 4
ledred = 2
ledgreen = 3
buzzer = 8

pinMode(ledblue,"OUTPUT")
pinMode(ledred,"OUTPUT")
pinMode(ledgreen,"OUTPUT")
grovepi.pinMode(buzzer,"OUTPUT")
time.sleep(1)
click = " click"
dclick = "double_click"
hold = "hold"


while True:
    try:
	# SUBSTITUTE INSERT HERE WITH YOUR PUSHBULLET TOKEN
	push = os.popen("curl --header 'Access-Token: INSERT HERE' --data-urlencode active='true' --data-urlencode modified_after='1.4e+09' --get https://api.pushbullet.com/v2/pushes")
	line = push.readline()
	print line
	print push
	if click in line:
		grovepi.digitalWrite(buzzer,1)
		time.sleep(.2)
		grovepi.digitalWrite(buzzer,0)
        	digitalWrite(ledblue,1)
       		time.sleep(2)
       		digitalWrite(ledblue,0)
      		time.sleep(1)
		# SUBSTITUTE INSERT HERE WITH YOUR PUSHBULLET TOKEN
		os.system("curl --header 'Access-Token: INSERT HERE' --request DELETE https://api.pushbullet.com/v2/pushes")
	if dclick in line:
		grovepi.digitalWrite(buzzer,1)
                time.sleep(.2)
                grovepi.digitalWrite(buzzer,0)
		time.sleep(.1)
		grovepi.digitalWrite(buzzer,1)
                time.sleep(.2)
                grovepi.digitalWrite(buzzer,0)
                digitalWrite(ledred,1)
                time.sleep(2)
                digitalWrite(ledred,0)
                time.sleep(1)
		# SUBSTITUTE INSERT HERE WITH YOUR PUSHBULLET TOKEN
                os.system("curl --header 'Access-Token: INSERT HERE' --request DELETE https://api.pushbullet.com/v2/pushes")
	if hold in line:
		grovepi.digitalWrite(buzzer,1)
                time.sleep(.6)
                grovepi.digitalWrite(buzzer,0)
                digitalWrite(ledgreen,1)
                time.sleep(2)
                digitalWrite(ledgreen,0)
                time.sleep(1)
		# SUBSTITUTE INSERT HERE WITH YOUR PUSHBULLET TOKEN
                os.system("curl --header 'Access-Token: INSERT HERE' --request DELETE https://api.pushbullet.com/v2/pushes")

    except KeyboardInterrupt:	# Turn LED off before stopping
       	digitalWrite(ledblue,0)
	digitalWrite(ledred,0)
        digitalWrite(ledgreen,0)
       	break
    except IOError:				# Print "Error" if communication error encountered
       	print "Error"


