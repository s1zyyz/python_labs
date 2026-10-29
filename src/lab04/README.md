## ЛР4 —  Файлы: TXT/CSV и отчёты по текстовой статистике

### Задание 1


```python 
import sys
from pathlib import *
import argparse

from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv
import argparse
from src.lab04.io_txt_csv import read_text



parser = argparse.ArgumentParser(description="Генерация текстового отчета")
parser.add_argument("--input", type=str, default="data/input.txt", help="Путь к входному файлу")
parser.add_argument("--encoding", type=str, default="utf-8", help="Кодировка файла")

args = parser.parse_args()

text = read_text(args.input, encoding=args.encoding)

try:
 
    text = read_text(args.input, encoding=args.encoding)
    
except FileNotFoundError:
    
    sys.exit("Ошибка: файл data/input.txt не найден")

tokens = tokenize(normalize(text))
freq = count_freq(tokens)

write_csv(top_n(freq, len(freq)), "data/report.csv", header=("word", "count"))

print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(freq)}")
print("Топ-5:", top_n(freq, 5))
for word, count in top_n(freq, 5):
        print(f"{word}:{count}")
```
### Задание 2
```python
import sys
from pathlib import *

from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv

try:
    text = read_text("data/input.txt")
except FileNotFoundError:
    sys.exit("Ошибка: файл data/input.txt не найден")

tokens = tokenize(normalize(text))
freq = count_freq(tokens)

write_csv(top_n(freq, len(freq)), "data/report.csv", header=("word", "count"))

print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(freq)}")
print("Топ-5:", top_n(freq, 5))
for word, count in top_n(freq, 5):
        print(f"{word}:{count}")


```
ТЕСТ

ТЕРМИНАЛ

![](../../images/lab04/testa1.png)

CSV

![](../../images/lab04/testa2.png)

Обработка пустого файла

![](../../images/lab04/testa3.png)


![](../../images/lab04/testa4.png)

Тест кодировки cp1251

![](../../images/lab04/testa5.png)

