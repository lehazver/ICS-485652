import numpy as np
import matplotlib.pyplot as plt
import pylab

name = str("По весні 1663 року двоє подорожніх, верхи на добрих конях, ізближались до Києва з Білогородського шляху. Один був молодий собі козак, збройний, як до війни; другий по одежі і по сивій бороді, сказать би, піп, а по шаблюці під рясою, по пістолях за поясом і по довгих шрамах на виду — старий 'козарлюга'.")
def count_sign():
    symbols=[",", ':', '?', '!', '.', ';', '-']
    for i in range(0, len(symbols)):
        xdata=[symbols[i]]
        ydata=[name.count(symbols[i])]
        pylab.bar(xdata, ydata)

    pylab.title("Знаки у тексті")
    pylab.show()
count_sign()
