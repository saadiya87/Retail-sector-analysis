import streamlit as st
import base64
from PIL import Image
import numpy as np
import pickle
import pandas as pd
import os
os.chdir(r"C:\Users\swtsa\OneDrive\Desktop\excelr")

main_bg = "index2.jpg"
main_bg_ext = "jpg"

side_bg = "index.jpg"
side_bg_ext = "jpg"


st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
   .sidebar .sidebar-content {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)
   
path=r"retail_ecommerce_u.csv"
get_data = pd.read_csv(path)

df=get_data

nav = st.sidebar.radio('Pages',['Home','Prediction'])
if nav == 'Home':
    col1, col2, col3 = st.beta_columns([1,10,1])
    with col1:
        st.write("")

    with col2:
        st.image("main.jpg",width=650)

    with col3:
        st.write("")
df.drop_duplicates(keep=False,inplace=True)
df=df.drop(["RecencyCluster","FrequencyCluster","RevenueCluster","OverallScore",#"DayDiff","DayDiff2","DayDiff3","DayDiffMean","DayDiffStd", 
                "Segment_High-Value","Segment_Low-Value","Segment_Mid-Value"],axis=1)

z = pd.DataFrame(df['NextPurchaseDayRange'])
if nav == 'Prediction':
    st.header('Prediction')
    st.dataframe(df)
    x = st.number_input("CustomerID: ",min_value=df['CustomerID'].min(),max_value=df['CustomerID'].max())
    z = pd.DataFrame(df.loc[df['CustomerID'] == x])

    if st.button("Predict"):
        if z.iloc[0,-1] == 1:
            st.subheader("Customer Status")
            st.success('The Customer {} is likely to shop next month'.format(x))
        else:
            st.subheader("Customer Status")
            st.warning('The Customer {} is not likely to shop next month'.format(x))
           











