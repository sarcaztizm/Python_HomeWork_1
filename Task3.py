# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

print('Введите шестизначный номер билета')
number_of_ticket = int(input())
first_sum = 0
sec_sum = 0
temp = 100000
for i in range(3):
    sec_sum += number_of_ticket % 10
    first_sum += number_of_ticket // temp
    number_of_ticket %= temp
    temp //= 100
    number_of_ticket //= 10
print('Сумма первых трех чисел:',first_sum)
print('Сумма последний трех чисел:',sec_sum)
if first_sum == sec_sum:
    print('Билет счастливый')
else:
    print('Билет несчастливый')