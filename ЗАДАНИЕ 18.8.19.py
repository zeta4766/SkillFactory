n = int(input()) #Запросить количество билетов
if n >3:
    sale = 0.9
else:
    sale = 1
sum = 0
for i in range(n):
    years = int(input())    #Запросить возраст для каждого билета
    if 18 <= years < 25:    #Для людей от 18 до 25 лет билет стоит 990р, возможна скидка 10%
        sum += 990 * sale
    elif years >= 25:   #Для старших 25 билет стоит 1390р, возможна скидка 10%
        sum += 1390 * sale
print(sum)  #Сумма в итоге имеет тип float
