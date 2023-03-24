import pandas as pd
from dash import Dash, dcc, html
import plotly.express as plt

app = Dash(__name__)

def generate_layout():
	CAC40_index = pd.read_csv("/home/ubuntu//Projet_Linux_Git_Python/donnees.direct.csv", header = None, sep = ';')
	CAC40_index.columns = ["Date", "Index CAC40"]
	CAC40_index["Date"] = pd.to_datetime(CAC40_index["Date"], format = "%H:%M %d|%m|%Y")
	CAC40_index.index = CAC40_index["Date"]
	CAC40_index = CAC40_index.drop("Date", axis = 1)
	ts = plt.area(CAC40_index["Index CAC40"])
	ts.update_layout(yaxis_range = [0.90*min(CAC40_index["Index CAC40"]), 1.1*max(CAC40_index["Index CAC40"])])
	return html.Div(
			children = [html.H1(children = "Projet Edwin"), html.P("Evolution de l'index CAC40"), dcc.Graph(figure = ts)]
			)

app.layout = generate_layout

if __name__ == "__main__":
		app.run_server(host = "0.0.0.0", port = 8000)
