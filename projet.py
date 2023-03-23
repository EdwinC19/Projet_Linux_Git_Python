import pandas as pd
from dash import Dash, dcc, html
import matplotlib.pyplot as plt

CAC40_index = pd.read_csv("/home/ubuntu//Projet_Linux_Git_Python/données.direct.csv", index_col = 0, parse_dates = [0])
plt.plot(CAC40_index)

