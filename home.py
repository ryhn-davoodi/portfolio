import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1,col2=st.columns(2)

with col1:
    st.image('images/photo.png')
with col2:
    st.title('Ryhn')
    content="""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident """
    st.info(content)

st.write('this is a test from creates some content out of columns and i want to makes it long in line to see how does it work')
df=pandas.read_csv("data.csv",sep=";")
col3,empty_col,col4=st.columns([1.5,0.5,1.5])
with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[source code]({'url'})")
with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[source code]({'url'})")




