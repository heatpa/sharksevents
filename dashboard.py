# -*- coding: utf-8 -*-

import pandas as pd
import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
from PIL import Image

image1 = Image.open('C:\\Users\\Tech\\TriSharksEventDashboard\\trisharks.jpg')

st.set_page_config(
    page_title='Trisharks 2023 Events Dashboard',
    page_icon=image1,
    layout="wide",
)

t1,t2=st.columns((0.15,1))

t1.image(image1,width=120)
t2.header('    2023 Event Dashboard')


df=pd.read_csv('SharksEvents.csv')

cell_renderer =  JsCode("""
function(params) {return `<a href=${params.value} target="_blank">${params.value}</a>`}
""")

gb = GridOptionsBuilder.from_dataframe(df)
#gb.configure_pagination(paginationPageSize=140) #Add pagination
gb.configure_side_bar() #Add a sidebar
gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
gb.configure_column('Date',pinned='left')
gb.configure_column('Event',pinned='left',
                    cellRenderer=JsCode(
        """function(params) {return `<a href=${params.value.a} target="_blank">${params.value.b}  </a>`}"""),
    valueGetter=JsCode("""function(params) {return {a: params.data.Website, b:params.data.Event} }"""),
    )

gb.configure_column("Website",headerName="Website",cellRenderer=cell_renderer)
gridOptions = gb.build()

grid_response = AgGrid(
    df,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=False,
    theme='blue', #Add theme color to the table
    enable_enterprise_modules=True,
    height=350, 
    width='100%',
    reload_data=True,
    allow_unsafe_jscode=True
)   
    
