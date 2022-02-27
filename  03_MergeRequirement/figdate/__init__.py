import textdistance

__all__ = ["bullscows", "gameplay"]
__author__ = 'Veniamin Arefev <veniamin.arefev@mail.ru>'


def bullscows(attempt: str, mystery: str) -> (int, int):
    return textdistance.hamming.similarity(attempt, mystery), textdistance.bag.similarity(attempt, mystery)


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    pass
