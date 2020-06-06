from UFO import *
import turtle as tr
import time
tr.tracer(0)
tr.hideturtle()

ufo1 = (Ufo('Пришелец-1', 100, 100, 7, 150, 'green', 5, 6))
ufo1.show()
tr.update()
ufo2 = (Ufo('Пришелец-2', -100, -100, 5, 200, 'red', 3, 4))
ufo2.show()
while True:
    ufo1.Nastya()
    ufo1.random()
    ufo1.show()
    ufo2.Nastya()
    ufo2.random()
    ufo2.show()
    tr.update()

'''
ufo2 = (Ufo('Пришелец-2', -100, -100, 6, 200, 'red', 3, 4))
# 'ufo2.x = 0' - так работает, но нельзя
#ufo2.set_name('Новое имя')
# так нужно
ufo2.show()
#print(ufo2.get_name())
# ufo2.engine_grade = 'Super-Turbo UFO'
print(ufo2.engine_grade)
'''