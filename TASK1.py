# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

week_day= int(input("Введите число от 1 до 7: "))
week_days = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]
if 1<= week_day <=7:
    print(f"Сегодня: {week_days[week_day-1]}")
else:
    print("Ошибка")
