import csv
import itertools


suits = ["H", "D", "C", "S"]
ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
cards = ["".join(card) for card in itertools.product(ranks, suits)]

''' Устанавливаю лимит, чтобы программа не подвисла, или не сожрала всю память на компьютере.
Соответствует количеству сочетаний для 7 или 45 карт, на практике искать все сочетания для кол-ва карт
между этими значениями будет проблематично (уже для 7 карт у меня файл получился 3гб) + время выполнения'''
limit = 133_784_560

n = int(input("Enter number of cards: "))
combs_iterator = itertools.islice(itertools.combinations(cards, n), limit)


with open(f"combs_of_{n}_cards.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(combs_iterator)