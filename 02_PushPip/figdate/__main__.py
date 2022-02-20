import locale
import sys

from figdate import *

# locale.setlocale(locale.LC_ALL, '')
locale.setlocale(locale.LC_ALL, locale.normalize('ru'))

if 3 >= len(sys.argv) >= 1:
    print(date(*sys.argv[1:]))
else:
    print("Please run with 3 or less arguments")
