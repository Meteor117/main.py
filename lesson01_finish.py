# 1st programm
print(9**0.5*5)
print(15.0)#правильный результат

#2nd programm
print(9.99>9.98 and 1000 !=1000.1)
print(True)#правильный результат

#3rd programm
#вычисление суммы срединных данных чисел 1234 и 5678
x=1234
print((x%1000//10))
y=5678
print((y%1000//10))
print((x%1000//10)+(y%1000//10))
print(90)#правильный результат

#4th programm
# сравнение 13.42 и 42.13
x=13.42
print(round(x%1*100))
y=42.13
print(round(y%1*100))
print(round(x%1*100)==int(y) or (round(y%1*100)==x))
print(True)#правильный результат