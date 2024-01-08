from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# Création de l'application
app = Dash(__name__)
df = pd.read_csv("https://raw.githubusercontent.com/chriszapp/datasets/main/books.csv", error_bad_lines=False)

df['publication_date'] = pd.to_datetime(df['publication_date'], errors='coerce')

df_sorted = df.sort_values(by=['ratings_count', 'average_rating'], ascending=False)

top_10_books = df_sorted.head(10)

fig = px.bar(top_10_books, x='title', y=['ratings_count', 'average_rating'], color='average_rating',
             labels={'ratings_count': 'Nombre de Votes', 'average_rating': 'Note Moyenne'},
             title='Top 10 des Livres par Nombre de Votes et Note Moyenne',
             hover_data=['  num_pages'])



app.layout = html.Div([
    html.H1("Top 10 des Livres par Nombre de Votes et Note Moyenne"),
    dcc.Graph(figure = fig),
    html.I('choisis un auteur :'),
    dcc.Dropdown(df['authors']),
    html.I('Chosis un nombre de pages : '),
    dcc.Input(id="input1", type="text", placeholder="")
])

if __name__ == '__main__':
    app.run_server(debug=True)
