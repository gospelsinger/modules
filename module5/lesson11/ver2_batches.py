import csv
import itertools
from typing import Iterable


def batched_combinations(it: Iterable, batch_size: int, max_batches: int | None = None):
    """
    Порциями возвращает сочетания для заданного кол-ва карт.
    Останавливается, когда исчерпан итератор или выдано `max_batches` партий.

    :param it: Iterable: итератор по сочетаниям для заданного кол-ва карт
    :param batch_size: int: количество сочетаний в одной партии
    :param max_batches: int | None: количество партий
    """
    batch_count = 0

    while True:
        if max_batches is not None and batch_count >= max_batches:
            break

        batch = list(itertools.islice(it, batch_size))
        if not batch:
            break
        yield batch

        batch_count += 1


suits = ["H", "D", "C", "S"]
ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
cards = ["".join(card) for card in itertools.product(ranks, suits)]

n = int(input("Enter number of cards: "))
combs_iterator = itertools.combinations(cards, n)
batch_size = 1_000_000
max_batches = 10


for part, batch in enumerate(batched_combinations(combs_iterator, batch_size, max_batches), start=1):
    with open(f"combs_of_{n}_cards_{part}.csv", "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(batch)