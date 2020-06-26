from adafruit_circuitplayground.express import cpx

# To change colors of all neopixels
cpx.pixels.fill((0, 75, 255))

# In order to turn of a neopixel
# cpx.pixels[0] = (0, 0, 0)

# Run this forever
while True:
    # Set neopixels to rainbow colors
    cpx.pixels[0] = (255, 0, 0) 
    cpx.pixels[1] = (255, 85, 0)
    cpx.pixels[2] = (255, 255, 0)
    cpx.pixels[3] = (0, 255, 0)
    cpx.pixels[4] = (34, 139, 34)
    cpx.pixels[5] = (0, 255, 255)
    cpx.pixels[6] = (0, 0, 255)
    cpx.pixels[7] = (0, 0, 139)
    cpx.pixels[8] = (255, 0, 255)
    cpx.pixels[9] = (75, 0, 130)

    # Turn D13 Led Light on/off depending on the state of the switch
    if cpx.switch:
        cpx.red_led = True
    else:
        cpx.red_led = False

    # While button a/b is pressed, change color of a pixel
    if cpx.button_a:
        cpx.pixels[2] = (0, 0, 255)
    elif cpx.button_b:
        cpx.pixels[7] = (0, 255, 0)
    else:
        cpx.pixels.fill((0, 0, 0))