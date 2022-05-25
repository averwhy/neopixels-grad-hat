from typing import Tuple


import random

class Color:
    """Simple staticmethods to make colors easier"""

    @staticmethod
    def random() -> Tuple:
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    @staticmethod
    def red() -> Tuple:
        return (255, 0, 0)

    @staticmethod
    def green() -> Tuple:
        return (0, 255, 0)
    
    @staticmethod
    def blue() -> Tuple:
        return (0, 0, 255)
    
    @staticmethod
    def white() -> Tuple:
        return (255, 255, 255)
    
    @staticmethod
    def cyan() -> Tuple:
        return (0, 153, 153)

    @staticmethod
    def pink() -> Tuple:
        return (255, 51, 255)
    
    @staticmethod
    def gold() -> Tuple:
        return (255,215,0)