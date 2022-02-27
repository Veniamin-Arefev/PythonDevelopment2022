import random

from textdistance import hamming, bag

__all__ = ["bullscows", "gameplay"]
__author__ = 'Veniamin Arefev <veniamin.arefev@mail.ru>'


def bullscows(guess: str, secret: str) -> (int, int):
    return hamming.similarity(guess, secret), bag.similarity(guess, secret)


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    secret, attempt, number_of_tries = random.choice(words), '', 0
    print(secret)
    while attempt != secret:
        attempt, number_of_tries = ask("Enter the word: "), number_of_tries + 1
        bulls, cows = bullscows(attempt, secret)
        inform("Bulls: {}, Cows: {}", bulls, cows)
    return number_of_tries
