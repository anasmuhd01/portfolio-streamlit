import streamlit as st
import pandas

st.set_page_config(layout="wide")
df = pandas.read_csv("data.csv",sep=";")
col1, col2 = st.columns(2)

with col1:

    st.image("images(1)/photo.jpg",width=500)

content = """ 
As a recent graduate with a strong passion for programming and software development, 
I am excited to embark on a career as a Python developer. 
I possess a solid foundation in Python programming and 
a keen desire to learn and contribute in a dynamic team environment. 
My academic background has equipped me with problem-solving skills, an analytical mindset, 
and a determination to excel in the field of software development.
"""

with col2:
    st.title("Anas Muhammed")
    st.info(content)

content2 = "below you can find some of the apps i have built in python "
st.subheader(content2)

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