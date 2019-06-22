import RPi.GPIO as GPIO
import mfrc522.SimpleMFRC522 as SM
import lcddriver
import time
import requests
import json


# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = lcddriver.lcd()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
reader = SM()
URL = "http://127.0.0.1:8000/store/"
# Main body of code
try:
    while True:
        # Remember that your sentences can only be 16 characters long!
        print("Writing to display")
        display.lcd_clear() # Write line of text to first line of display

        display.lcd_display_string("Pointez ici !", 1) # Write line of text to first line of display
        display.lcd_display_string("", 2) # Write line of text to first line of display
        id,text = reader.read()
        print(id)
        print(text)
        
        rfid = id
        PARAMS = {'rfid': rfid }

        r = requests.get(url=URL,params=PARAMS)
        text=r.text
        
        print(text)

        if (text == "OK"):
            print("ok")
            GPIO.output(7,True)
            time.sleep(1)
            GPIO.output(7,False)
            display.lcd_clear() # Write line of text to first line of display

            display.lcd_display_string("Hello", 1) # Write line of text to first line of display

            display.lcd_display_string(text,2) # Write line of text to first line of display
        else:
            display.lcd_clear() # Write line of text to first line of display

            display.lcd_display_string("Error", 1) # Write line of text to first line of display            
            
            
        time.sleep(2)
            
except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
            print("Cleaning up!")
            display.lcd_clear()
finally:
    GPIO.cleanup()