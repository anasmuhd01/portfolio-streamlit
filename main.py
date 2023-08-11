import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:

    st.image("images(1)/photo.png")

content = """ 
this is a  sample content"""

with col2:
    st.title("Anas Muhammed")
    st.info(content)

tab1 = st.container()


tab1.write("below you can find some of the apps i have built in python")

content2 = "below you can find some of the apps i have built in python "
st.write(content2)

df = pandas.read_csv("data.csv",sep=";")
col3, col4 = st.columns(2)

with col3:
    for index, row in df[:10].iterrows():
        st.title(row["title"])
        st.write(row["description"])
        st.image("images(1)/"+ row["image"])
        st.write(f"[soure code]({row['url']})")
with col4:
    for index, row in df[10:].iterrows():
        st.title(row["title"])
        st.write(row["description"])
        st.image("images(1)/" + row["image"])