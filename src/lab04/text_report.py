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