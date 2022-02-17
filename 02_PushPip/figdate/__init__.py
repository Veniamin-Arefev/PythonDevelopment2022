import time
from pyfiglet import figlet_format

__all__ = ["date"]
__author__ = 'Veniamin Arefev <veniamin.arefev@mail.ru>'


def date(my_format='%Y %d %b, %A', font='graceful'):
    text = time.strftime(my_format)
    return figlet_format(text, font)
