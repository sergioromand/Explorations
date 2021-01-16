import pandas as pd
import matplotlib.pyplot as plt

# Let's read in some data!
bond_data = pd.read_csv("data/bond_data.csv", index_col="Date", parse_dates=True)

bond_data.plot.line()
plt.show()
