import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

click = " click"
dclick = "double_click"
hold = "hold"


while True:
    try:
	# SUBSTITUTE INSERT HERE WITH YOUR PUSHBULLET TOKEN
	push = os.popen("curl --header 'Access-Token: o.qwRX0BTs1O6BVqUoRqDRsqKFWY35jRDy' --data-urlencode active='true' --data-urlencode modified_after='1.4e+09' --get https://api.pushbullet.com/v2/pushes")
	line = push.readline()
	print line
	print push
	if click in line:
		GPIO.output(18,GPIO.HIGH)
       		time.sleep(3)
		GPIO.output(18,GPIO.LOW)
		# SUBSTITUTE INSERT HERE WITH YOUR PUSHBULLET TOKEN
		os.system("curl --header 'Access-Token: o.qwRX0BTs1O6BVqUoRqDRsqKFWY35jRDy' --request DELETE https://api.pushbullet.com/v2/pushes")
	if dclick in line:
		GPIO.output(18,GPIO.HIGH)
                time.sleep(1)
		# SUBSTITUTE INSERT HERE WITH YOUR PUSHBULLET TOKEN
                os.system("curl --header 'Access-Token: o.qwRX0BTs1O6BVqUoRqDRsqKFWY35jRDy' --request DELETE https://api.pushbullet.com/v2/pushes")
	if hold in line:
                time.sleep(0.2)
		GPIO.output(18,GPIO.LOW)
		# SUBSTITUTE INSERT HERE WITH YOUR PUSHBULLET TOKEN
                os.system("curl --header 'Access-Token: o.qwRX0BTs1O6BVqUoRqDRsqKFWY35jRDy' --request DELETE https://api.pushbullet.com/v2/pushes")

    except KeyboardInterrupt:
	# Turn LED off before stopping
	GPIO.output(18,GPIO.LOW)
       	break
    except IOError:
	# Print "Error" if communication error encountered
	print "Error"

