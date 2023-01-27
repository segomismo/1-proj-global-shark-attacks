import pandas as pd
pd.set_option('display.max_columns', None)
import numpy as np

import pylab as plt
import seaborn as sns

tiburones_ori = pd.read_csv("../data/attacks.csv", encoding= "ISO-8859-1")

tiburones = tiburones_ori.copy()

print(tiburones.head())