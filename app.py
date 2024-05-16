
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import verify, getreference
st.set_page_config(
    page_title='FACE ID',

)
class MultiApp:
    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            'title': title,
            'function': function
        })

    def run(self):
        with st.sidebar:
            app = option_menu(menu_title='Option',
                              options=['Thêm gương mặt', 'Xác thực'],
                              icons=['house-fill','person-circle'],
                              styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                              )
            
        if app=='Thêm gương mặt':
            getreference.app()
        if app=='Xác thực':
            verify.app()
            


app = MultiApp()
app.run()
st.title('FACE ID')
