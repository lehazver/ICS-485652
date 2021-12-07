from prettytable import PrettyTable
from data1 import dt

x = PrettyTable()

x.field_names = ["Підприємство", "Вид основних засобів", "Залишок 1.01.18", "Надійшло у 2018",
                 "Вибуло у 2018", "Залишок на 1.01.19", "Зміни вартості за рік"]
for i in range(0, len(dt)):
    x.add_rows(
        [
            dt[i]
        ]
    )


def opentable():
    print('\nАНАЛІЗ РУХУ ОСНОВНИХ ЗАСОБІВ')
    print(x)
