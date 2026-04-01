# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(6, 4))
ax = plt.subplot(111)
# Draw lines
line_a = [0, 5]
line_b = [0, 5]
cross_line = [-2, 2]
ax.plot([0, 5], [0, 3], 'k-', label='Line a')
ax.plot([0, 5], [1.5, 4.5], 'k-', label='Line b')
ax.plot([-2, 2], [3, 1.5], 'k-', label='Transversal c')
# Mark angles
angles = [(2, 2), (3, 2), (2, 3), (3, 3)] # Approximate centers for arcs
for i in range(4):
    x, y = 1 + i*0.5, 1.5 + i*0.5
    ax.plot(x, y, 'ro')
ax.set_xlim(-1, 6)
ax.set_ylim(-1, 5)
plt.legend()
plt.title('Basic Three Lines Eight Angles')
plt.savefig('test_q1_basic.png', dpi=100)
plt.close()