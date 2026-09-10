price = int(input())
discount = int(input())
vat = int(input())
base = price * (1-discount/100)
vata = base * (vat/100)
total = base + vata
print(f'База после скидки: {base:.2f} ₽')
print(f'НДС:               {vata:.2f} ₽')
print(f'Итого к оплате:    {total:.2f} ₽')