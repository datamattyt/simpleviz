import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

np.random.seed(42)
x = np.random.rand(100)
y = 2 * x + np.random.normal(0, 0.1, 100)

data = pd.DataFrame({'x':x, 'y':y})

sns.set_theme(style='whitegrid')

plt.figure(figsize=(10,6))
scatter_plot = sns.regplot(x='x',y='y',data=data,scatter_kws={'s':50,'alpha':0.6}, line_kws={'color':'red'})

scatter_plot.set_title('Scatter Plot with Regression Line', fontsize=15)
scatter_plot.set_xlabel('X Axis', fontsize=15)
scatter_plot.set_ylabel('Y Axis', fontsize=15)

plt.show()
