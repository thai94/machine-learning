import numpy as np
import matplotlib.pyplot as plt

objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
x_pos = np.arange(len(objects))
performance = [10, 8, 6, 4, 2, 5]

plt.bar(x_pos, performance, align='center', alpha=0.5)
plt.xticks(x_pos, objects)

plt.ylabel('Usage')
plt.title('Programming language usage')
plt.show()
