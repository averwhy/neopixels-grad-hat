import random

class Color:
    """Simple staticmethods to make colors easier"""

    @staticmethod
    def get_all() -> tuple:
        strings = [method for method in dir(Color) if method.startswith('__') is False and method.strip() not in ('none', 'get_all')]
        methods = []
        for s in strings:
            methods.append(getattr(Color, s))
        return methods

    @staticmethod
    def random() -> tuple:
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    @staticmethod
    def none() -> tuple:
        return (0, 0, 0)

    @staticmethod
    def red() -> tuple:
        return (255, 0, 0)

    @staticmethod
    def green() -> tuple:
        return (0, 255, 0)
    
    @staticmethod
    def blue() -> tuple:
        return (0, 0, 255)
    
    @staticmethod
    def white() -> tuple:
        return (255, 255, 255)
    
    @staticmethod
    def cyan() -> tuple:
        return (0, 153, 153)

    @staticmethod
    def pink() -> tuple:
        return (255, 51, 255)
    
    @staticmethod
    def gold() -> tuple:
        return (255,215,0)