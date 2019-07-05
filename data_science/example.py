import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rows = columns = 1000
data = np.ones((rows, columns))
# print(data.sum())
df = pd.DataFrame(data)
# print(df)
# df = df.cumsum()
# plt.figure()
# plt.show(block=True)

ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2016", periods=1000))
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list("ABCD"))
df = df.cumsum()
df.plot()
plt.show()
