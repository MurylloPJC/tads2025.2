import plotly.express as px
from plotly.graph_objects import Figure
from functions.download import download_data

def plot_ts(ticker:str) -> Figure:
    """
    Docstring for plot_ts
    
    :param ticker: Description
    :type ticker: str
    :return: Description
    :rtype: Figure
    """
    df = download_data(ticker)

    fig = px.line (
        df,
        x = 'Date',
        y = 'Close',
        title = f'{ticker} Stock Price'
    )

    return fig