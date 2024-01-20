from pathlib import Path 
import streamlit as st 
from PIL import Image

# --- PATH SETTING --- 
current_dir = Path(__file__).parent if '__file__' in locals() else path.cwd()
css_file = current_dir / 'styles' / 'style.css'
resume_file = current_dir / 'assets' / 'CV_Elia-Roysandi-Manurun.pdf'
profile_pic = current_dir / 'assets' / 'profile-pic.jpeg'


# --- GENERAL SETTINGS ---
page_title = 'Digital CV | Elia Roysandi Manurun'
page_icon = ':wave:'
name = 'Elia Roysandi Manurun'
description = '''
Junior Data Science, cleaning the data, and make machine learning models 
'''
email = 'eliaroysandimanurun@gmail.com'
social_media = {
    'YouTube': 'https://www.youtube.com/channel/UCXJAIKpMldpOrgRq0qiy5pA',
    'LinkedIn': 'https://www.linkedin.com/in/elia-roysandi-manurun-6bba93253/',
    'GitHub': 'https://github.com/Elroy71',
    'Instagram': 'https://www.instagram.com/eliaroysandi.m/'

}

projects = {
    '':'',
    '':'',
    '':''
}


st.set_page_config(page_title=page_title, page_icon=page_icon)



# --- SIDEBARR --- 
st.sidebar.title('👋Hello Guys!')
st.sidebar.markdown('---')




# --- LOAD CSS, PDF & PROFILE PIC --- 
with open(css_file)as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
with open(resume_file,'rb') as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# -- HERO SECTION -- 
col1, col2 = st.columns(2, gap='small')
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(name)
    st.write(description)
    st.download_button(
        label='📃Download Resume',
        data=PDFbyte,
        file_name = resume_file.name,
        mime='application/octet-stream'
    )
    st.write('📨',email)


# --- SOCIAL LINKS --- 
st.write('#')
cols = st.columns(len(social_media))
for index, (platform, link) in enumerate(social_media.items()):
    cols[index].write(f'[{platform}]({link})')


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('#')
st.subheader('Experience & Qualifications')
st.write('''
✓ 6 Month experience in data science and artificial intelligence\n
✓ Proficient in cleaning data and visualizing data\n
✓ Strong hands on experience and knowledge in python and excel\n
''')


# --- SKILLS --- 
st.write('#')
st.subheader('Hard Skills')
st.write('''
- Programming : Python(Numpy, Pandas), SQL, PHP, HTML, CSS
- Data Visualization : PowerBI, Matplotlib, Seaborn
- Modeling : ---------------------------------------
- Databases : MySQL
''')



