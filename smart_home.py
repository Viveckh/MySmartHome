from adafruit_circuitplayground.express import cpx
import time

room_temperature = 0

while True:
    room_temperature = (cpx.temperature * 1.8) +32
    if room_temperature > 65:
        print("Control temp")
        # cpx.play_file("sounds/coin.wav")
        # Turn on the AC through Alexa Smart Plug
    if cpx.button_b:
        cpx.play_tone(262, 1.0)
    if cpx.touch_A1:
        cpx.play_tone(262, 0.5)
    if cpx.shake():
        print("Shake detected!")

    print((room_temperature, cpx.light))