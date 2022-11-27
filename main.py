import time
import board
import neopixel
import typing
import os
import mouse
import multiprocessing
from colors import Color

pixel_pin = board.D18
num_pixels = 60
ORDER = neopixel.GRB
ACTIVE = True
CURRENT_MODE = 0
CURRENT_STYLE = 0

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

class rainbow_cycle:
    def __init__(self, rate: float = 0.001):
        for j in range(255):
            for i in range(num_pixels):
                pixel_index = (i * 256 // num_pixels) + j
                pixels[i] = wheel(pixel_index & 255)
            pixels.show()
            time.sleep(rate)
    @staticmethod
    def styles():
<<<<<<< HEAD
        return ((0.001,),
        (0.0,),
        (0.1,),
        ) # all args must be a tuple

class color_shift:
    def __init__(self, rate: float = 0.05, colors: list = []):
        if len(colors) == 0:
            colors = [Color.red(), Color.green(), Color.blue()]
        for c in colors:
            for i in range(num_pixels):
                time.sleep(rate)
                pixels[i] = c
                pixels.show()
    @staticmethod
    def styles():
        return ((0.05,),
        (0.01,),
        (0.005,),
        (0.001,), 
        (0.1,)
        )

class alternate:
    def __init__(self, clr: typing.Union[tuple, typing.List[tuple]], delay: float = 0.3):
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
    @staticmethod
    def styles():
        style_list = []
        style_list.append(([Color.blue(), Color.gold()], 0.2)) # SNHU colors :>
        for c in Color.get_all():
            style_list.append((c(), 0.3)) # add color with rate of 0.05
            style_list.append((c(), 0.1)) # add same color with faster rate
            style_list.append((c(), 0.6)) # add same color with slow rate
        return style_list

class dash:
    def __init__(self, clr: tuple, length: int = 1, delay: float = 0.03):
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
    @staticmethod
    def styles():
        style_list = []
        for c in Color.get_all():
            style_list.append((c(), 3))
            style_list.append((c(), 6))
            style_list.append((c(), 9))
        return style_list

class gradual_fill:
    def __init__(self, clr: tuple, empty_after: bool = True, reverse_empty: bool = False, delay: float = 0.05):
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
    @staticmethod
    def styles():
        style_list = []
        for c in Color.get_all():
            style_list.append((c(), True, False))
            style_list.append((c(), True, True))
            style_list.append((c(), True, False, 0.01))
            style_list.append((c(), True, True, 0.01))
        return style_list

class strobe:
    def __init__(self, clr: tuple, rate: float = 0.05):
        pixels.fill(clr)
        pixels.show()
        time.sleep(rate)
        pixels.fill(Color.none())
        pixels.show()
        time.sleep(rate)
=======
        return (0.001, 0.0, 0.1)

class stop:
    def __init__(self):
        pixels.fill(Color.none())
        pixels.show()
    @staticmethod
    def styles():
        return (None,)

class color_shift:
    def __init__(self, rate: float = 0.05, colors: list = []):
        if len(colors) == 0:
            colors = [Color.red(), Color.green(), Color.blue()]
        for c in colors:
            for i in range(num_pixels):
                time.sleep(rate)
                pixels[i] = c
                pixels.show()
    @staticmethod
    def styles():
        return (0.05, 0.01, 0.005, 0.001, 0.1)

class alternate:
    def __init__(self, clr: typing.Union[tuple, typing.List[tuple]], delay: float = 0.3):
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
>>>>>>> 72b93d19ad8520d7a2d75bb3eb3f134cd69ae98f
    @staticmethod
    def styles():
        style_list = []
        for c in Color.get_all():
<<<<<<< HEAD
            style_list.append((c(),))
            style_list.append((c(), 0.01))
            style_list.append((c(), 0.5))
        return style_list

=======
            style_list.append((c, 0.3)) # add color with rate of 0.05
            style_list.append((c, 0.1)) # add same color with faster rate
            style_list.append((c, 0.6)) # add same color with slow rate
        return style_list

class dash:
    def __init__(self, clr: tuple, length: int = 1, delay: float = 0.03):
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
    @staticmethod
    def styles():
        style_list = []
        for c in Color.get_all():
            style_list.append((c, 3))
            style_list.append((c, 6))
            style_list.append((c, 9))
        return style_list

class gradual_fill:
    def __init__(self, clr: tuple, empty_after: bool = True, reverse_empty: bool = False, delay: float = 0.05):
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
    @staticmethod
    def styles():
        style_list = []
        for c in Color.get_all():
            style_list.append((c, True, False))
            style_list.append((c, True, True))
            style_list.append((c, True, False, 0.01))
            style_list.append((c, True, True, 0.01))
            style_list.append((c, True, False, 0.5))
            style_list.append((c, True, True, 0.5))
        return style_list

class strobe:
    def __init__(self, clr: tuple, rate: float = 0.05):
        pixels.fill(clr)
        pixels.show()
        time.sleep(rate)
        pixels.fill(Color.none())
        pixels.show()
        time.sleep(rate)
    @staticmethod
    def styles():
        style_list = []
        for c in Color.get_all():
            style_list.append((c))
            style_list.append((c, 0.01))
            style_list.append((c, 0.5))
        return style_list

>>>>>>> 72b93d19ad8520d7a2d75bb3eb3f134cd69ae98f
class meet:
    def __init__(self, clr1: tuple, clr2: tuple = None, reverse: bool = False, delay: float = 0.05):
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
    @staticmethod
    def styles():
        style_list = []
        for c in Color.get_all():
<<<<<<< HEAD
            style_list.append((c(), None, False))
            style_list.append((c(), None, True))
            style_list.append((c(), None, False, 0.01))
            style_list.append((c(), None, True, 0.01))
            style_list.append((c(), None, False, 0.5))
            style_list.append((c(), None, True, 0.5))
=======
            style_list.append((c, None, False))
            style_list.append((c, None, True))
            style_list.append((c, None, False, 0.01))
            style_list.append((c, None, True, 0.01))
            style_list.append((c, None, False, 0.5))
            style_list.append((c, None, True, 0.5))
>>>>>>> 72b93d19ad8520d7a2d75bb3eb3f134cd69ae98f
        return style_list

class breathe:
    def __init__(self, clr: tuple, speed: float = 1): # Does not work well with rgb values with low numbers
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
    @staticmethod
    def styles():
        style_list = []
        for c in Color.get_all():
<<<<<<< HEAD
            style_list.append((c(),))
            style_list.append((c(), 2))
            style_list.append((c(), 4))
=======
            style_list.append((c))
            style_list.append((c, 2))
            style_list.append((c, 4))
>>>>>>> 72b93d19ad8520d7a2d75bb3eb3f134cd69ae98f
        return style_list

class quad_alternate:
    def __init__(self, clr: tuple, clr2: tuple = None, delay: float = 0.5):
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
    @staticmethod
    def styles():
        style_list = []
        for c in Color.get_all():
<<<<<<< HEAD
            style_list.append((c(), None))
            style_list.append((c(), None, 0.1))
            style_list.append((c(), None, 0.8))
=======
            style_list.append((c, None))
            style_list.append((c, None, 0.1))
            style_list.append((c, None, 0.8))
>>>>>>> 72b93d19ad8520d7a2d75bb3eb3f134cd69ae98f
        return style_list

class all_random:
    def __init__(self, delay: float = 0.1):
        for i in range(num_pixels):
            pixels[i] = Color.random()
        pixels.show()
        time.sleep(delay)
    @staticmethod
    def styles():
<<<<<<< HEAD
        return ((0.1,), (0.5,), (0.05,))

class stop:
    def __init__(self, none=None):
        pixels.fill(Color.none())
        pixels.show()
    @staticmethod
    def styles():
        return((None,),)
=======
        return ([0.1, 0.5, 0.05])
>>>>>>> 72b93d19ad8520d7a2d75bb3eb3f134cd69ae98f
    

MODE_DICT = {0: rainbow_cycle, 1: color_shift, 2: alternate, 3: quad_alternate, 4: dash, 5: gradual_fill,
             6: breathe, 7: strobe, 8: all_random, 9: stop}
MODE_MAX = len(MODE_DICT) - 1
LAST_MODE = 0
LAST_STYLE = 0
ACTIVE_MODE = None

def _left_click():
    global CURRENT_MODE # because threading
    global CURRENT_STYLE
    # Change mode
    if (CURRENT_MODE + 1) > MODE_MAX:
        CURRENT_MODE = 0
    else:
        CURRENT_MODE += 1
    CURRENT_STYLE = 0
    pixels.fill(Color.none())

def _right_click():
    global CURRENT_STYLE 
    # Change style (color, etc)
    if func.styles()[0] is None: # has no styles
        return
    if (CURRENT_STYLE + 1) > (len(func.styles()) - 1): # exceeded all styles
            CURRENT_STYLE = 0 # return to first one
    else:
        CURRENT_STYLE += 1
    pixels.fill(Color.none())

mouse.on_click(_left_click)
mouse.on_right_click(_right_click)

<<<<<<< HEAD
def run_mode(func, args):
=======
def run_mode(func, *args):
>>>>>>> 72b93d19ad8520d7a2d75bb3eb3f134cd69ae98f
    while ACTIVE:
        func(*args)

# Main loop
try:
    while ACTIVE:
        if ACTIVE_MODE is None:
            func = MODE_DICT[CURRENT_MODE] # get mode class
            if func.styles()[0] is None: # has no styles
                ACTIVE_MODE = multiprocessing.Process(target=run_mode, args=(func,)) # Run with no args
            else:
                ACTIVE_MODE = multiprocessing.Process(target=run_mode, args=(func, func.styles()[CURRENT_STYLE])) # run with style args
            ACTIVE_MODE.start() # start that process
            LAST_MODE = CURRENT_MODE
            LAST_STYLE = CURRENT_STYLE
<<<<<<< HEAD
            print("Reloaded process")
=======
            print("set")
>>>>>>> 72b93d19ad8520d7a2d75bb3eb3f134cd69ae98f
        if LAST_MODE != CURRENT_MODE or LAST_STYLE != CURRENT_STYLE: # if changes, this runs
            ACTIVE_MODE.terminate() # stop process
            ACTIVE_MODE = None # set to None so that the above if statement runs
            stop() # turn all lights off
<<<<<<< HEAD
except KeyboardInterrupt:
    ACTIVE_MODE.terminate()
    stop()
ACTIVE_MODE.terminate()
stop()
=======
            print("reset")
except KeyboardInterrupt:
    ACTIVE_MODE.terminate()
    stop()
>>>>>>> 72b93d19ad8520d7a2d75bb3eb3f134cd69ae98f
