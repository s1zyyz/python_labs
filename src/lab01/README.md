### Лабораторная работа 1

#### Задание 1

```python
a,b = input(),int(input())
print(f'Привет, {a}! Через год тебе будет {b+1}.')
```

![1](src/images/lab01/img01.png)

#### Задание 2

```python 
a,b = float(input().replace(',','.')),float(input().replace(',','.'))
print(f'sum={a+b}; avg={(a+b)/2:.2f}')```

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

