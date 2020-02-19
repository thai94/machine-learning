import numpy as np
import matplotlib.pyplot as plt

means_frank = (90, 55, 40, 65)
means_guido = (85, 62, 54, 20)


fig, ax = plt.subplots()

index = np.arange(len(means_frank))

bar_width = 0.35

bar1 = plt.bar(index, means_frank, bar_width, color='b', label='Frank')
bar2 = plt.bar(index+bar_width, means_guido,
               bar_width, color='g', label='Guido')

plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')
plt.xticks(index + bar_width, ('A', 'B', 'C', 'D'))
plt.legend()


plt.show()
