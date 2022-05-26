import time
import board
import neopixel
import typing
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
    if len(colors) == 0:
        colors = [Color.red(), Color.green(), Color.blue()]
    for c in colors:
        for i in range(num_pixels):
            time.sleep(delay)
            pixels[i] = c
            pixels.show()

def alternate(clr: typing.Union[tuple, typing.List[tuple]], delay: float = 0.3):
    if isinstance(clr, list):
        color_1 = clr[0]
        color_2 = clr[1]
    else:
        color_1 = clr
        color_2 = Color.none()
    for i in range(num_pixels):
        if i % 2 != 0: # odd
            pixels[i] = color_1
        else:
            pixels[i] = color_2
    pixels.show()
    time.sleep(delay)
    for i in range(num_pixels):
        if i % 2 == 0: # even
            pixels[i] = color_1
        else:
            pixels[i] = color_2
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

def strobe(clr: tuple, rate: float = 0.05):
    pixels.fill(clr)
    pixels.show()
    time.sleep(rate)
    pixels.fill(Color.none())
    pixels.show()
    time.sleep(rate)

def meet(clr1: tuple, clr2: tuple = None, reverse: bool = False, delay: float = 0.05):
    if clr2 is None:
        clr2 = clr1
    for i in range(int(num_pixels / 2) + 1):
        pixels[i] = clr1
        pixels[-i] = clr2
        pixels.show()
        time.sleep(delay)
    if not reverse:
        for i in range(int(num_pixels / 2) + 1):
            pixels[i] = Color.none()
            pixels[-i] = Color.none()
            pixels.show()
            time.sleep(delay)
    else:
        for i in range(int(num_pixels / 2) + 1, 0, -1):
            pixels[i] = Color.none()
            pixels[-i] = Color.none()
            pixels.show()
            time.sleep(delay)

def breathe(clr: tuple, speed: float = 1): # Does not work well with rgb values with low numbers
    # TODO: Rewrite this to subtract percentages of original numbers
    delta = speed / 510
    original_clr = clr
    for i in range(255):
        pixels.fill(clr)
        pixels.show()
        clr = (clr[0] - 1 if clr[0] - 1 >= 0 else 0,
        clr[1] - 1 if clr[1] - 1 >= 0 else 0,
        clr[2] - 1 if clr[2] - 1 >= 0 else 0
        )
        time.sleep(delta)
    time.sleep(delta * 75) # it'll be off for a little bit before gradually turning back on
    for i in range(255):
        pixels.fill(clr)
        pixels.show()
        clr = (clr[0] + 1 if clr[0] + 1 <= original_clr[0] else original_clr[0],
        clr[1] + 1 if clr[1] + 1 <= original_clr[1] else original_clr[1],
        clr[2] + 1 if clr[2] + 1 <= original_clr[2] else original_clr[2]
        )
        time.sleep(delta)

def quad_alternate(clr: tuple, clr2: tuple = None, delay: float = 0.5):
    zone = int(num_pixels / 4)
    z1 = range(0, zone)
    z2 = range(zone, (zone*2))
    z3 = range(zone*2, (zone*3))
    z4 = range(zone*3, num_pixels)
    if clr2 is None: clr2 = Color.none()
    for i in range(num_pixels):
        #z1 and z3 = clr1
        if i in z1 or i in z3:
            pixels[i] = clr
        #z2 and z4 = clr2
        else:
            pixels[i] = clr2
    pixels.show()
    time.sleep(delay)
    for i in range(num_pixels):
        #z2 and z4 = clr1
        if i in z2 or i in z4:
            pixels[i] = clr
        #z1 and z3 = clr2
        else:
            pixels[i] = clr2
    pixels.show()
    time.sleep(delay)

def all_random(delay=0.1):
    for i in range(num_pixels):
        pixels[i] = Color.random()
    pixels.show()
    time.sleep(delay)

# Main loop
try:
    while ACTIVE:
        all_random()
except KeyboardInterrupt:
    pixels.fill((0,0,0))
    pixels.show()