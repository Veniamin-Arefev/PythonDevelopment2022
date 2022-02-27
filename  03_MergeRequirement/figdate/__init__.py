import random

from textdistance import hamming, bag

__all__ = ["bullscows", "gameplay"]
__author__ = 'Veniamin Arefev <veniamin.arefev@mail.ru>'


def bullscows(guess: str, secret: str) -> (int, int):
    return hamming.similarity(guess, secret), bag.similarity(guess, secret)


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    secret, attempt, number_of_tries = random.choice(words), '', 0
    while attempt != secret:
        attempt, number_of_tries = ask("Enter the word: ", end=''), number_of_tries + 1
        bulls, cows = bullscows(attempt, secret)
        inform("Bulls: {}, Cows: {}", bulls, cows)
    return number_of_tries


def ask(prompt: str, valid: list[str] = None) -> str:
    while (temp := input(prompt)) not in valid:
        pass
    return temp


def inform(format_string: str, bulls: int, cows: int) -> None:
    return print(format_string.format(bulls, cows))
