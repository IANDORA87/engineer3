# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MITR

"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo
from gpiozero import Button
from gpiozero import sleep 


# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

sever = servo(17)
Button = Button(11)

while True:
    

    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
    if Button . is_pressed:
        print("Button is pressed");
        servo.min()
        time.sleep(0.03)
        servo.mid()
        time.sleep(0.03)
        servo.max()
        time.sleep(0.03)
    else:
        print("Button is not pressed")
        sleep(0.2)
        print(angle)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.02)
 
