import pandas as pd
from dash import Dash, dcc, html
import plotly.express as plt
import datetime as dt

app = Dash(__name__)

def generate_layout():
  CAC40_index = pd.read_csv("/home/ubuntu//Projet_Linux_Git_Python/donnees.direct.csv", header = None, sep = ';')
  CAC40_index.columns = ["Date", "Index CAC40"]
  CAC40_index["Date"] = pd.to_datetime(CAC40_index["Date"], format = "%H:%M %d|%m|%Y")
  CAC40_index.index = CAC40_index["Date"]
  CAC40_index = CAC40_index.drop("Date", axis = 1)
  ts = plt.area(CAC40_index["Index CAC40"])
  ts.update_layout(yaxis_range = [0.90*min(CAC40_index["Index CAC40"]), 1.1*max(CAC40_index["Index CAC40"])])
  date = pd.to_datetime(CAC40_index.index[-1])
  CAC40_journalier = CAC40_index.loc[CAC40_index.index.date == date.date()]
  moyenne_jour = str(round(CAC40_journalier["Index CAC40"].mean(),2))
  volatilité_jour = str(round(CAC40_journalier["Index CAC40"].std(),2))
  fermeture_marché = str(CAC40_journalier["Index CAC40"][-4])
  ouverture_marché = str(CAC40_journalier["Index CAC40"][12])
  return html.Div(
		children = [html.H1(children = "Projet Edwin"), html.P("Evolution de l'index CAC40"), dcc.Graph(figure = ts), html.H2("Rapport quotidien sur l'index CAC40"), html.P(["Moyenne : " , moyenne_jour]), html.P(["Volatilité : " , volatilité_jour]), html.P(["Ouverture : " , ouverture_marché]), html.P(["Fermeture : " , fermeture_marché])]
		 )

app.layout = generate_layout

if __name__ == "__main__":
	app.run_server(host = "0.0.0.0", port = 8000)
