import streamlit as st 
from PIL import Image

# --- GENERAL SETTINGS ---
page_title = 'Digital CV | Elia Roysandi Manurun'
page_icon = ':wave:'
name = 'Elia Roysandi Manurun'
description = '''
Junior Data Science, cleaning the data, and make machine learning models 
'''

st.set_page_config(page_title=page_title, page_icon=page_icon)


# --- PROJECT --- 
st.title('My Project')
st.write('#')


with st.container():
    col1,col2 = st.columns(2)
    with col1:
        st.image(Image.open('assets/profile-pic.jpeg'),width=240)
    with col2:
        st.subheader('Data Science | Machine Learning Modeling ')
        st.write('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry')
        st.markdown('[Visit My Repo](https://www.google.com/search?client=firefox-b-d&sca_esv=599792272&sxsrf=ACQVn0-xithNFIToled7QBX6rxZ3FDRn1A:1705671054855&q=fungsi+sidebar+adalah&tbm=isch&source=lnms&sa=X&ved=2ahUKEwiv48_qx-mDAxWS6jgGHT8wDvkQ0pQJegQIDBAB&biw=923&bih=732&dpr=1.25#imgrc=jq6-mZWqKjKOrM)')
    col3,col4 = st.columns(2)
    with col3:
        st.image(Image.open('assets/profile-pic.jpeg'),width=240)
    with col4:
        st.subheader('Data Science | Machine Learning Modeling ')
        st.write('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry')
        st.markdown('[Visit My Repo](https://www.google.com/search?client=firefox-b-d&sca_esv=599792272&sxsrf=ACQVn0-xithNFIToled7QBX6rxZ3FDRn1A:1705671054855&q=fungsi+sidebar+adalah&tbm=isch&source=lnms&sa=X&ved=2ahUKEwiv48_qx-mDAxWS6jgGHT8wDvkQ0pQJegQIDBAB&biw=923&bih=732&dpr=1.25#imgrc=jq6-mZWqKjKOrM)')

with st.container():
    col1,col2 = st.columns(2)
    with col1:
        st.image(Image.open('assets/profile-pic.jpeg'),width=240)
    with col2:
        st.subheader('Data Science | Machine Learning Modeling ')
        st.write('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry')
        st.markdown('[Visit My Repo](https://www.google.com/search?client=firefox-b-d&sca_esv=599792272&sxsrf=ACQVn0-xithNFIToled7QBX6rxZ3FDRn1A:1705671054855&q=fungsi+sidebar+adalah&tbm=isch&source=lnms&sa=X&ved=2ahUKEwiv48_qx-mDAxWS6jgGHT8wDvkQ0pQJegQIDBAB&biw=923&bih=732&dpr=1.25#imgrc=jq6-mZWqKjKOrM)')

with st.container():
    col1,col2 = st.columns(2)
    with col1:
        st.image(Image.open('assets/profile-pic.jpeg'),width=240)
    with col2:
        st.subheader('Data Science | Machine Learning Modeling ')
        st.write('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry')
        st.markdown('[Visit My Repo](https://www.google.com/search?client=firefox-b-d&sca_esv=599792272&sxsrf=ACQVn0-xithNFIToled7QBX6rxZ3FDRn1A:1705671054855&q=fungsi+sidebar+adalah&tbm=isch&source=lnms&sa=X&ved=2ahUKEwiv48_qx-mDAxWS6jgGHT8wDvkQ0pQJegQIDBAB&biw=923&bih=732&dpr=1.25#imgrc=jq6-mZWqKjKOrM)')

with st.container():
    col1,col2 = st.columns(2)
    with col1:
        st.image(Image.open('assets/profile-pic.jpeg'),width=240)
    with col2:
        st.subheader('Data Science | Machine Learning Modeling ')
        st.write('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry')
        st.markdown('[Visit My Repo](https://www.google.com/search?client=firefox-b-d&sca_esv=599792272&sxsrf=ACQVn0-xithNFIToled7QBX6rxZ3FDRn1A:1705671054855&q=fungsi+sidebar+adalah&tbm=isch&source=lnms&sa=X&ved=2ahUKEwiv48_qx-mDAxWS6jgGHT8wDvkQ0pQJegQIDBAB&biw=923&bih=732&dpr=1.25#imgrc=jq6-mZWqKjKOrM)')




# --- SIDEBAR --- 
st.sidebar.title('List Project')
# st.sidebar.markdown('')
st.sidebar.markdown('''
#### Machine Learning
- 
- 
##
### Data Analysis
- 
- 
##
### Artifial intelligence
- 
-


''')