#!/usr/bin/env python

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm


def MY_FREQ(digit):
    return {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6}.get(digit, -1)


c = canvas.Canvas('ex.pdf')

# 14159265358979323846264338327950288419716939937510582

# count = 0
c_x = 0
c_y = 0

# new line after every 26 tabs

for i in '3760642169':
    # print(int(i)%6)
    c.drawImage('whistle_tabs/0{}.png'.format(MY_FREQ(int(i) % 6)), 13+23*c_x,
                                              730 - 105*c_y, 22, 95)
    # count += 1
    c_x += 1

    if c_x == 20:
        c_y += 1
        c_x = 0

c.showPage()
c.save()
