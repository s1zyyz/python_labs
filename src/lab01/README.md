### Лабораторная работа 1

#### Задание 1

```python
a,b = input(),int(input())
print(f'Привет, {a}! Через год тебе будет {b+1}.')
```

![1](https://github.com/s1zyyz/python_labs/blob/3f6a09734244336466c9edac6f5647d60d367ce9/src/images/lab01/img01.png)

#### Задание 2

```python 
a,b = float(input().replace(',','.')),float(input().replace(',','.'))
print(f'sum={a+b}; avg={(a+b)/2:.2f}')
```

![2](https://github.com/s1zyyz/python_labs/blob/e8ebd7e9235c59783db39050d06e29a0a306430b/src/images/lab01/img02.png)


#### Задание 3

```python
price = int(input())
discount = int(input())
vat = int(input())
base = price * (1-discount/100)
vata = base * (vat/100)
total = base + vata
print(f'База после скидки: {base:.2f} ₽')
print(f'НДС:               {vata:.2f} ₽')
print(f'Итого к оплате:    {total:.2f} ₽')
```
![3](https://github.com/s1zyyz/python_labs/blob/e8ebd7e9235c59783db39050d06e29a0a306430b/src/images/lab01/img03.png)


#### Задание 4

```python
m = int(input())
print(f'{m//60}:{m%60:02d}')
```

![4](https://github.com/s1zyyz/python_labs/blob/3f6a09734244336466c9edac6f5647d60d367ce9/src/images/lab01/img04.png)


#### Задание 5

```python
fio = input()
words = fio.split()
initials = ''.join(w[0].upper() for w in words) + '.'
length = len(' '.join(words))
print(f"Инициалы: {initials}")
print(f"Длина (символов): {length}")
```

![5](https://github.com/s1zyyz/python_labs/blob/3f6a09734244336466c9edac6f5647d60d367ce9/src/images/lab01/img05.png)

