import string

def get_words(filename: str, punctuation=string.punctuation) -> list[str]:
    with open(filename, "r", encoding="utf8") as f:
        words = [word.strip(punctuation) for word in f.read().lower().split()]
        words = [word for word in words if word]
    return words

def get_words_dict(words: list[str]) -> dict[str, int]:
    words_dict = {}
    for word in words:
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] +=1
    return words_dict


filename = input("Введите название файла: ")
words = get_words(filename)
words_dict = get_words_dict(words)
print(f"Количество слов: {len(words)}")
print(f"Количество уникальных слов: {len(words_dict)}")
print("Все использованные слова:")
for word, count in words_dict.items():
    print(f"{word}: {count}")