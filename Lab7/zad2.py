import numpy as np
import matplotlib.pyplot as plt
import pylab


text = str("Було вже надвечір. Сонце світило стиха, без жари; і любо було поглянути, як воно розливалось по зелених вітах, по сукуватих, мохнатих дубах і по молодій травиці.")

def count_letters():
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'є', 'ж', 'з', 'и', 'і','ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',]

    for i in range(0, len(alphabet)):
        xdata = [alphabet[i]]
        ydata = [text.count(alphabet[i])]
        pylab.bar(xdata, ydata)
    pylab.title("Літери у тексті")
    pylab.show()
count_letters()
