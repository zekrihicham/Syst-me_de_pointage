import RPi.GPIO as GPIO
import mfrc522.SimpleMFRC522 as SM


GPIO.setmode(GPIO.BCM)

reader = SM()

try:
    text = raw_input('Enter New Data for writing to card : ')
    print("Now place your tag to write")
    reader.write(text)
    print("data was written successfull")
finally:
    GPIO.cleanup()