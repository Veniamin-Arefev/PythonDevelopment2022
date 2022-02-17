import locale
import sys

from figdate import *

locale.setlocale(locale.LC_ALL, '')
# locale.setlocale(locale.LC_ALL, 'Russian_Russia')
if 3 >= len(sys.argv) >= 1:
    print(date(*sys.argv[1:]))
