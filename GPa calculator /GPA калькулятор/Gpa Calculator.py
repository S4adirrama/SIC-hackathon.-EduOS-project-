import numpy as np

# Author : Ruween Iddagoda

grade = 0;

print("Ваш GPA калькулятор")
print("Введите количество ваших предмет:")
no_of_modules = int(input(""))
st=0;
while(st<no_of_modules):
    print("Предмет №" + str(st + 1) + ":")
    weight = int(input())
    if(weight>=2 and weight<=5):
        grade += weight
        st+=1
    else:
        print("Это не ваша оценка")

GPA = grade / no_of_modules

print("-----------------------")
print("[ Ваш GPA: {:,.2f}".format(GPA))
print("-----------------------")
