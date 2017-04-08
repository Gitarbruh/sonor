import RPi.GPIO as GPIO
from flask import Flask,render_template
import time

app = Flask(__name__)

@app.route("/Bats/<action>")
def Bats(action):
 if action == "reading":


   GPIO.setmode(GPIO.BCM)
   TRIG = 20
   ECHO = 26
   print ("Distance Measurement in progress")

   GPIO.setup(TRIG,GPIO.OUT)
   GPIO.setup(ECHO,GPIO.IN)

   GPIO.output(TRIG,False)
   print("Waiting for sensor to settle")
   time.sleep(2)


   GPIO.output(TRIG, True)
   time.sleep(0.00001)
   GPIO.output(TRIG, False)


   while GPIO.input(ECHO)== 0:
    pulse_start = time.time()
 
   while GPIO.input(ECHO)== 1:
    pulse_end = time.time()


   pulse_duration = pulse_end - pulse_start 
   distance = pulse_duration*17150
   distance = round(distance, 2)
   
 else:
   message="unknown command"
 GPIO.cleanup();
  
 return render_template('main.html', action=action, distance=distance)
if __name__ == "__main__":
  app.run(host='0.0.0.0',port =80, debug= True)
 

