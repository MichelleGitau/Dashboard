import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

st.set_page_config(layout="wide", initial_sidebar_state="auto", page_icon="⚡", page_title='Quoted Companies'
                   ' at NSE')
path = "./stockdata.csv"
st.sidebar.header('Quoted Companies Trends')
st.sidebar.write('''There are 66 Companies listed at the Nairobi Securities Exchange here in Kenya.''')

data = pd.read_csv(path, encoding="ISO-8859-1", low_memory=False)

menu = ['Home', 'Trend Analysis', 'Contact' ]
selection = st.sidebar.selectbox("Dashboard ", menu)

if selection == 'Home':
    st.title('About Quoted Companies at NSE')
    st.subheader('Who Are We?')
    st.write('Quoted companies at NSE is a website that aims at giving you a price trend analysis for all '
             'the listed companies in order to help you make a sound investment decision. The data used is gathered'
             'from the Nairobi Securities Exchange daily trade prices. The price is determined as the average of the '
             'opening and closing price for each day.')
    st.subheader('Founders')
    st.write('Quoted Companies at NSE was founded by Michelle Gitau')

import plotly.graph_objects as go


if selection == 'Trend Analysis':
    st.header('Stock Price for the year 2020')

    menu2 = pd.unique(data['ticker'])
    selection2 = st.sidebar.selectbox('Select Company', menu2)
    graph_data = data[data['ticker'] == selection2]
    st.dataframe(graph_data)

    trace1 = go.Scatter(x=graph_data.month,
                        y=graph_data.price,
                        line=dict(color='green'),
                        name='Stock in Feb',
                        text=graph_data.ticker,
                        )
    df = [trace1]

    layout = dict(title='Stock Prices',
                  xaxis=dict(title='Month'),
                  yaxis=dict(title='Price'),
                  )
    fig = go.Figure(dict(data=df, layout=layout))
    fig.show()
    st.plotly_chart(fig, use_container_width=True, auto_open=False)

footer_temp = """
        <!-- CSS  -->
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" 
        type="text/css" rel="stylesheet" media="screen,projection"/>
        <link href="static/css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" 
        integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
        <footer class="page-footer grey darken-4">
        <div class="container" id="aboutapp">
        <div class="row">
        <div class="col l6 s12">
        <h5 class="white-text">Stock Price Analysis App</h5>
        <h6 class="grey-text text-lighten-4">This is Quoted Companies Trends.</h6>
        </div>
        <div class="col l3 s12">
        <h5 class="white-text">Connect With Us</h5>
        <ul>
        <a target="_blank" class="white-text">
        <i class="fab fa-facebook fa-4x"></i>
        </a>
        <a target="_blank" class="white-text">
        <i class="fab fa-linkedin fa-4x"></i>
        </a>
        <a target="_blank" class="white-text">
        </a>
        <a target="_blank" class="white-text">
        </a>
        </ul>
        </div>
        </div>
        </div>
        <div class="footer-copyright">
        <div class="container">
        </div>
        </div>
        </footer>
        """

if selection == 'Contact':
    st.header("About App")
    components.html(footer_temp, height=500)