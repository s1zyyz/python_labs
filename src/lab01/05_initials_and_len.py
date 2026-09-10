fio = input()
words = fio.split()
initials = ''.join(w[0].upper() for w in words) + '.'
length = len(' '.join(words))
print(f"Инициалы: {initials}")
print(f"Длина (символов): {length}")