import matplotlib.pyplot as plt

buildings_Yniversam = [44048, 500, 200]
buildings_Dnipryanka = [22456,365,123]
Cars_Yniversam = [5564,2571,135]
Cars_Dnipryanka = [10087,15972,58]
transport_Yniversam = [0,0,0,]
transport_Dnipryanka = [206,34,50]
inventory_Yniversam=[116,64,23]
inventory_Dnipryanka=[34,23,25]
year = ['Залишок на 1.01.2018', 'Надійшло у 2018', 'Вибуток у 2018']

plt.plot(year,buildings_Yniversam,label = "Будівлі(Універсам 22)")
plt.plot(year,buildings_Dnipryanka,label = "Будівлі(Дніпрянка)")
plt.plot(year,Cars_Yniversam,label = "Машини та обладнання(Універсам 22)")
plt.plot(year,Cars_Dnipryanka,label = "Машини та обладнання(Дніпрянка)")
plt.plot(year,transport_Yniversam,label = "Транспортні засоби(Універсам 22)")
plt.plot(year,transport_Dnipryanka,label = "Транспортні засоби(Дніпрянка)")
plt.plot(year,inventory_Yniversam,label = "Інструмент та інвентар(Універсам 22)")
plt.plot(year,inventory_Dnipryanka,label = "Інструмент та інвентар(Дніпрянка)")
plt.xlabel("Рік")
plt.ylabel("Ціна")
plt.legend()
plt.grid(True)

def graph():
    plt.show()