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

def color_shift(colors: list = [], delay: float = 0.05):
    colors = [Color.red(), Color.green(), Color.blue()]
    for c in colors:
        for i in range(num_pixels):
            time.sleep(delay)
            pixels[i] = c
            pixels.show()

def alternate(clr: tuple, delay: float = 0.3):
    for i in range(num_pixels):
        if i % 2 != 0: # odd
            pixels[i] = clr
        else:
            pixels[i] = Color.none()
    pixels.show()
    time.sleep(delay)
    for i in range(num_pixels):
        if i % 2 == 0: # even
            pixels[i] = clr
        else:
            pixels[i] = Color.none()
    pixels.show()
    time.sleep(delay)

def dash(clr: tuple, length: int = 1, delay: float = 0.03):
    for i in range(num_pixels):
        pixels[i] = clr
        if i - length >= 0:
            pixels[i - length] = Color.none()
        pixels.show()
        time.sleep(delay)
    remainders = range(num_pixels - length, num_pixels)
    for i in remainders:
        pixels[i] = Color.none()
        pixels.show()
        time.sleep(delay)

def gradual_fill(clr: tuple, empty_after: bool = True, reverse_empty: bool = False, delay: float = 0.05):
    for i in range(num_pixels):
        pixels[i] = clr
        pixels.show()
        time.sleep(delay)
    if empty_after:
        if reverse_empty:
            for i in range(num_pixels):
                pixels[-i] = Color.none()
                pixels.show()
                time.sleep(delay)
        else:
            for i in range(num_pixels):
                pixels[i] = Color.none()
                pixels.show()
                time.sleep(delay)

try:
    while ACTIVE:
        gradual_fill(Color.cyan())

except KeyboardInterrupt:
    pixels.fill((0,0,0))
    pixels.show()