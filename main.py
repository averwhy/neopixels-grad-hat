import time
import board
import neopixel
from colors import Color

pixel_pin = board.D18
num_pixels = 60
ORDER = neopixel.GRB
ACTIVE = True

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)   

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def color_shift(delay: float = 0.1):
    colors = [Color.red(), Color.green(), Color.blue()]
    for c in colors:
        for i in range(num_pixels):
            time.sleep(delay)
            pixels[i] = c


try:
    while ACTIVE:
        color_shift()
        time.sleep(0.1 * 60.0)
except KeyboardInterrupt:
    pixels.fill((0,0,0))
    pixels.show()