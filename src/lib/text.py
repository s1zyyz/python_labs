
import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """ Приводит текст к единому регистру, заменяет ё->е и схлопывает пробелы. """
    if casefold: 
        text = text.casefold() 
    else:
        text = text.lower() 
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е") 

    text = " ".join(text.split())  
    return text


def tokenize(text: str) -> list[str]:
    """ функция выделяет из текста отдельные слова с помощью регулярного выражения """
    return re.findall(r"\w+(?:-\w+)*", text)  


def count_freq(tokens: list[str]) -> dict[str,int]:
    '''
    Подсчитывает частоты, возвращает словарь (слово, количество)
    '''
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq

def top_n(freq: dict[str,int], n: int = 5) -> list[tuple[str,int]]:
    """ Возвращает топ-N по убыванию частоты; при равенстве — по алфавиту слова. """
    top = list(freq.items())
    top.sort(key=lambda x:(-x[1], x[0]))
    return top[:n]

""" if __name__ == "__main__":
  
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"
    print("normalize: прошел")

    assert tokenize("привет, мир!") == ["привет", "мир"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]
    print("tokenize: прошел")

    freq = count_freq(["a","b","a","c","b","a"])
    assert freq == {"a":3, "b":2, "c":1}
    print("count_freq: прошел")


    assert top_n(freq, 2) == [("a",3), ("b",2)]
    
   
    freq2 = count_freq(["bb","aa","bb","aa","cc"])
    assert top_n(freq2, 2) == [("aa",2), ("bb",2)]
    print("top_n: прошел")
    
    print("нормады") """
