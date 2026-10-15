import sys

from src.lib.text import normalize, tokenize, count_freq, top_n

raw_text = sys.stdin.read()
if raw_text.strip() == '':
    raise ValueError('Empty string')

clean = normalize(raw_text)
tokens = tokenize(clean)

total_w = len(tokens)
unique = len(set(tokens))

freq_dict = count_freq(tokens)
top_5 = top_n(freq_dict)

print(f'Всего слов: {total_w}')
print(f'Уникальных слов: {unique}')
print('Топ-5:')

for word, count in top_5:
    print(f'{word}:{count}')
