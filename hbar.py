### Generate a horizontal bar chart

import matplotlib.pyplot as plt
import numpy as np

plt.rcdefaults()
fig, ax = plt.subplots()

y = tuple(x['variablethatgoesonyaxis'])
y_pos = np.arange(len(y))

ax.barh(y_pos, x['variablethatgoesonxaxis'])
ax.set_yticks(y_pos)
ax.set_yticklabels(y)
ax.invert_yaxis()
ax.set_title('Your barchart title')

# Forces tidy plot lay-out
plt.tight_layout()

# Save the figure
plt.savefig('hbar.pdf')
