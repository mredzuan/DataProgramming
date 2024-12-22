
# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
np.random.seed(0)
df = pd.DataFrame(np.random.rand(100, 2), columns=['A', 'B'])
df['C'] = df['A'] + df['B']
df['D'] = np.sqrt(df['A'])

plt.scatter(df['C'], df['D'])
plt.show()






# %%
1+1

# %%


1/2
# %%
