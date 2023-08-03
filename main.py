from dateutil.parser import parse
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
df = pd.read_excel('IRData.xlsx', engine="openpyxl", parse_dates= ['Effective Date'])

#Plot
x = df['Effective Date'].values
y1 = df['Rate (%)'].values
#asdasdasdasd
### Plot
fig, ax = plt.subplots(1, 1, figsize=(10,5), dpi= 120)
plt.plot(x, y1, color='tab:red')
plt.ylim(-0.5, 8)
plt.title('SOFR rates', fontsize=16)
plt.hlines(y=0, xmin=np.min(df['Effective Date']), xmax=np.max(df['Effective Date']), linewidth=.5)
plt.show()
