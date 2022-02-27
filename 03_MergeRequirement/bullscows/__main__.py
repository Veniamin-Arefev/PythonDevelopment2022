import argparse
import re
import sys
import urllib.request

from bullscows import *


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('dictionary',
                        # nargs='?',
                        type=str,
                        help='Dictionary for game',
                        )
    parser.add_argument('length',
                        nargs='?',
                        default=5,
                        type=int,
                        help='Length of the secret word',
                        )
    return parser.parse_args()


sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
args = parse_args()


def ask(prompt: str, valid: list[str] = None) -> str:
    if valid:
        while (temp := input(prompt)) not in valid:
            pass
    else:
        temp = input(prompt)
    return temp


def inform(format_string: str, bulls: int, cows: int) -> None:
    return print(format_string.format(bulls, cows))


with urllib.request.urlopen(args.dictionary) as file:
    words = list(filter(lambda x: len(x) == args.length, file.read().decode().split()))

print(f'You guessed the secret word with {gameplay(ask, inform, words)} attempts')
