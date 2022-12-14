# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#Не уверена, что я правильно поняла задачу.

x = bool(int(input("Введите значение х: 0 для False или 1 для True: ")))
y = bool(int(input("Введите значение y: 0 для False или 1 для True: ")))
z = bool(int(input("Введите значение z: 0 для False или 1 для True: ")))
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")

if (not(x or y or z)) == ((not x) and (not y) and (not z)):
    print ("Утверждение верно!")
    
