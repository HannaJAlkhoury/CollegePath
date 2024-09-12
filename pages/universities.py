import streamlit as st
import json
from PIL import Image
from streamlit_option_menu import option_menu
from st_pages import hide_pages
import base64 
from pathlib import Path
#defying functions
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
def img_to_html(img_path):
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(
      img_to_bytes(img_path)
    )
    return img_html
def load_lottiefile(filepath: str):
     with open(filepath, "r") as f:
          return json.load(f)
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()    
#Page Config     
icon = Image.open("images/cap.png")
st.set_page_config(page_title="قائمة الجامعات العامة والخاصة في سورية", page_icon=icon, layout= "wide")
hide_pages(["AAST","sp","majors","universities","application","DU", "Website", "AU",'ANTU','MU','QAU','ASPU','EBU','HPU','ANU','ANU','JU','AUST','SU','IU','CU','WPU','YU','RU','WU','IUST','SPU','AIU','KU','HU','SVU','EU','TU','TAU','BU','HIAST'])
#Page Style in CSS
Page_header=f"""
<style> 
#MainMenu {{visibility: hidden;}}
footer {{visibility: hidden;}}
[data-testid="stHeader"] {{
background-color: #0070C0;
height:3.5rem;
content:"What color is your buggati?";
}}
.css-fblp2m {{
color: #0070C0;
font-size: 2rem;
}}
.st-emotion-cache-hsmt6w{{
background-color:#ffffff;
color:#0070C0;
background-image: url('list.svg');
}}
.css-hsmt6w{{
background-color: #FFFFFF;    
}}
.css-1wrgccu{{
background-color: #FFFFFF;
}}
.css-17wpp4c {{
border-bottom: 1px solid rgb(0, 176, 240);
}}
.st-emotion-cache-z5fcl4 {{
    width: 100%;
    padding: 0rem 1rem 3rem;
    }}
div[data-baseweb="base-input"] {{
    background-color: transparent !important;
}}
[data-testid="stAppViewContainer"] {{
    background-color: transparent !important;
}}  
.st-emotion-cache-17wpp4c{{border-bottom: 1px solid rgb(60 55 143 / 0%);}}
.st-emotion-cache-1n5xqho {{
    padding: 0.74rem 1.5rem 1.4rem;
}}
.st-emotion-cache-1oe5cao{{padding-top:3rem;}}
.st-emotion-cache-1dgmtll svg {{
    stroke: rgb(38 39 48 / 0%);
}}
.st-emotion-cache-1dgmtll{{
background-color:transparent;
visibility: hidden;
}}
.st-emotion-cache-1kyxreq {{
    display: flex;
    flex-flow: wrap;
    row-gap: 1rem;
    justify-content: space-around;
}}
body {{
               text-align: right;
          }}
          .css-emotion-cache-1kyxreq{{
          flex-flow: column;
          align-content: center;
          justify-content: center;
          }} 
          .st-emotion-cache-ocqkz7{{flex-wrap: wrap}}
          .st-emotion-cache-z5fcl4 {{
    width: 100%;
    padding: 1rem 1rem 3rem;
}}
</style>"""
st.markdown(Page_header, unsafe_allow_html=True)
with st.sidebar:
     st.write("###")
     logo = Image.open("images/logo.png")
     st.image(logo)
     st.write("###")
     st.write('<a href="Website" target="_self" class=".st-emotion-cache-g2ydmt" style="display: inherit;border-bottom: 2px solid #205090; border-radius:6px;background-color:#ffffff ; padding:10px; text-align: center; color:#000000; font-weight: 700; font-size: 1.1rem; text-decoration: none; "> الصفحة الرئيسية ‎ ‎<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-house-door-fill" viewBox="0 0 20 20"><path d="M6.5 14.5v-3.505c0-.245.25-.495.5-.495h2c.25 0 .5.25.5.5v3.5a.5.5 0 0 0 .5.5h4a.5.5 0 0 0 .5-.5v-7a.5.5 0 0 0-.146-.354L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.354 1.146a.5.5 0 0 0-.708 0l-6 6A.5.5 0 0 0 1.5 7.5v7a.5.5 0 0 0 .5.5h4a.5.5 0 0 0 .5-.5"/></svg></a>' , unsafe_allow_html=True)
     st.write('<a href="application" target="_self" class=".st-emotion-cache-g2ydmt" style="display: inherit;border-bottom: 2px solid #205090; border-radius:6px;background-color:#ffffff ; padding:10px; text-align: center; color:#000000; font-weight: 600; font-size: 1rem; text-decoration: none; "> المفاضلة ‎ ‎<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-card-list" viewBox="0 0 20 20"><path d="M14.5 3a.5.5 0 0 1 .5.5v9a.5.5 0 0 1-.5.5h-13a.5.5 0 0 1-.5-.5v-9a.5.5 0 0 1 .5-.5zm-13-1A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h13a1.5 1.5 0 0 0 1.5-1.5v-9A1.5 1.5 0 0 0 14.5 2z"/><path d="M5 8a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7A.5.5 0 0 1 5 8m0-2.5a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7a.5.5 0 0 1-.5-.5m0 5a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7a.5.5 0 0 1-.5-.5m-1-5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0M4 8a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0m0 2.5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0"/><svg></a>' , unsafe_allow_html=True)
     st.write('<a href="sp" target="_self" class=".st-emotion-cache-g2ydmt" style="display: inherit;border-bottom: 2px solid #205090;border-radius:6px;background-color:#ffffff; padding:10px; text-align: center; color:#000000; font-weight: 600; font-size: 1rem; text-decoration: none; "> شرح عن الاختصاصات الجامعية ‎ ‎<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-mortarboard-fill" viewBox="0 0 20 20"><path d="M8.211 2.047a.5.5 0 0 0-.422 0l-7.5 3.5a.5.5 0 0 0 .025.917l7.5 3a.5.5 0 0 0 .372 0L14 7.14V13a1 1 0 0 0-1 1v2h3v-2a1 1 0 0 0-1-1V6.739l.686-.275a.5.5 0 0 0 .025-.917z"/><path d="M4.176 9.032a.5.5 0 0 0-.656.327l-.5 1.7a.5.5 0 0 0 .294.605l4.5 1.8a.5.5 0 0 0 .372 0l4.5-1.8a.5.5 0 0 0 .294-.605l-.5-1.7a.5.5 0 0 0-.656-.327L8 10.466z"/><svg></a>', unsafe_allow_html=True)
     st.write('<a href="#" target="_self" class=".st-emotion-cache-g2ydmt" style="display: inherit;border-bottom: 2px solid #205090;border-radius:6px;background-color:#9BE5FF; padding:10px; text-align: center; color:#ffffff; font-weight: 600; font-size: 1rem; text-decoration: none; "> البحث عن الجامعة ‎ ‎<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-bank2" viewBox="0 0 20 20"><path d="M8.277.084a.5.5 0 0 0-.554 0l-7.5 5A.5.5 0 0 0 .5 6h1.875v7H1.5a.5.5 0 0 0 0 1h13a.5.5 0 1 0 0-1h-.875V6H15.5a.5.5 0 0 0 .277-.916zM12.375 6v7h-1.25V6zm-2.5 0v7h-1.25V6zm-2.5 0v7h-1.25V6zm-2.5 0v7h-1.25V6zM8 4a1 1 0 1 1 0-2 1 1 0 0 1 0 2M.5 15a.5.5 0 0 0 0 1h15a.5.5 0 1 0 0-1z"/><svg></a>', unsafe_allow_html=True)
     st.write('<a href="majors" target="_self" class=".st-emotion-cache-g2ydmt" style="display: inherit;border-bottom: 2px solid #205090;border-radius:6px;background-color:#ffffff; padding:10px; text-align: center; color:#000000; font-weight: 600; font-size: 1rem; text-decoration: none; "> البحث عن الفرع ‎ ‎<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-search" viewBox="0 0 20 20"><path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0"/><svg></a>', unsafe_allow_html=True)
     st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">', unsafe_allow_html=True)
     st.write('<h4 style="margin-inline-start: 8%;"><a href="https://www.instagram.com/collegepath_insta?igsh=MWcyNTh4Z2d6dG84cA==" style="color:#ffffff;"><svg xmlns="http://www.w3.org/2000/svg" width="35%" height="45" fill="currentColor" class="bi bi-instagram" viewBox="0 0 25 25"><path d="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.9 3.9 0 0 0-1.417.923A3.9 3.9 0 0 0 .42 2.76C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.048 3.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.333 1.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.9 3.9 0 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 16 8s-.01-2.445-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.9 3.9 0 0 0-.923-1.417A3.9 3.9 0 0 0 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0zm-.717 1.442h.718c2.136 0 2.389.007 3.232.046.78.035 1.204.166 1.486.275.373.145.64.319.92.599s.453.546.598.92c.11.281.24.705.275 1.485.039.843.047 1.096.047 3.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.5 2.5 0 0 1-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.5 2.5 0 0 1-.92-.598 2.5 2.5 0 0 1-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.233s.008-2.388.046-3.231c.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92s.546-.453.92-.598c.282-.11.705-.24 1.485-.276.738-.034 1.024-.044 2.515-.045zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 0 0-1.92m-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217m0 1.441a2.667 2.667 0 1 1 0 5.334 2.667 2.667 0 0 1 0-5.334"/></svg></a><a href="https://youtube.com/@college_path?si=WoMkxc9VCI4ON0wv" style="color:#ffffff;"><svg xmlns="http://www.w3.org/2000/svg" width="30%" height="45" fill="currentColor" class="bi bi-youtube" viewBox="0 0 25 25"><path d="M8.051 1.999h.089c.822.003 4.987.033 6.11.335a2.01 2.01 0 0 1 1.415 1.42c.101.38.172.883.22 1.402l.01.104.022.26.008.104c.065.914.073 1.77.074 1.957v.075c-.001.194-.01 1.108-.082 2.06l-.008.105-.009.104c-.05.572-.124 1.14-.235 1.558a2.01 2.01 0 0 1-1.415 1.42c-1.16.312-5.569.334-6.18.335h-.142c-.309 0-1.587-.006-2.927-.052l-.17-.006-.087-.004-.171-.007-.171-.007c-1.11-.049-2.167-.128-2.654-.26a2.01 2.01 0 0 1-1.415-1.419c-.111-.417-.185-.986-.235-1.558L.09 9.82l-.008-.104A31 31 0 0 1 0 7.68v-.123c.002-.215.01-.958.064-1.778l.007-.103.003-.052.008-.104.022-.26.01-.104c.048-.519.119-1.023.22-1.402a2.01 2.01 0 0 1 1.415-1.42c.487-.13 1.544-.21 2.654-.26l.17-.007.172-.006.086-.003.171-.007A100 100 0 0 1 7.858 2zM6.4 5.209v4.818l4.157-2.408z"/><svg></a><a href="https://www.facebook.com/profile.php?id=61565154959875&sfnsn=wa&mibextid=RUbZ1f" style="color:#ffffff;"><svg xmlns="http://www.w3.org/2000/svg" width="35%" height="45" fill="currentColor" class="bi bi-facebook" viewBox="0 0 25 25"><path d="M16 8.049c0-4.446-3.582-8.05-8-8.05C3.58 0-.002 3.603-.002 8.05c0 4.017 2.926 7.347 6.75 7.951v-5.625h-2.03V8.05H6.75V6.275c0-2.017 1.195-3.131 3.022-3.131.876 0 1.791.157 1.791.157v1.98h-1.009c-.993 0-1.303.621-1.303 1.258v1.51h2.218l-.354 2.326H9.25V16c3.824-.604 6.75-3.934 6.75-7.951"/><svg></a></h4>', unsafe_allow_html=True)
if 0==0:
     st.write("###")
     Page_button=f"""
          <style>
          body {{
               text-align: right;
          }}
          .css-emotion-cache-1kyxreq{{
          flex-flow: column;
          align-content: center;
          justify-content: center;
          }} 
          .st-emotion-cache-ocqkz7{{flex-wrap: wrap}}
          .st-emotion-cache-z5fcl4 {{
    width: 100%;
    padding: 0rem 1rem 3rem;
}}
          </styles>
          """
     hide_img_fss = '''
          <style>
          button[title="View fullscreen"]{
             visibility: hidden;}
          </style>
          '''
     st.markdown(hide_img_fss, unsafe_allow_html=True)
     st.markdown(Page_button, unsafe_allow_html=True) 
     iamgoat="true"
     selectuni = option_menu(
          menu_icon=None,
          menu_title=None,
          options=["الجامعات الخاصة", "الجامعات الحكومية"],
          icons=["houses","houses-fill"],
          default_index=1,
          orientation="horizontal",
          styles={
        "container": {"padding": "0!important", "background-color": "#eee"},
        "icon": {"font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "center", "margin":"0px", "--hover-color": "#ACD3FE"},
        "nav-link-selected": {"background-color": "00B0F0"},
    }
    ) 
     #This Website is fully made by student HANNA JOHN ALKHOURY
     if selectuni=="الجامعات الحكومية":
          l1, r1=st.columns((4,1))
          with r1:
               st.write("###")
               DUimage= Image.open("images/DU.jpeg")
               st.image(DUimage)
          with l1:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> جامعة دمشق </h2>" , unsafe_allow_html=True)
               l11,r11=st.columns(2)
               with l11:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: دمشق وريفها، درعا، القنيطرة، السويداء </h5>" , unsafe_allow_html=True)
               with r11:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 3041 </h5>" , unsafe_allow_html=True)      
                    st.write("<a href='http://www.damascusuniversity.edu.sy/' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>damascusuniversity.edu.sy</a>", unsafe_allow_html=True) 
                    st.write("<a href='DU' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---") 
          l2, r2=st.columns((4,1))
          with r2:
               st.write("###")
               AUimage= Image.open("images/AU.webp")
               st.image(AUimage)
          with l2:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> جامعة حلب </h2>" , unsafe_allow_html=True)
               l21,r21=st.columns(2)
               with l21:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: حلب وإدلب </h5>" , unsafe_allow_html=True)
               with r21:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 4742 </h5>" , unsafe_allow_html=True)      
                    st.write("<a href='https://www.alepuniv.edu.sy' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>alepuniv.edu.sy</a>", unsafe_allow_html=True) 
                    st.write("<a href='AU' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---")  
          l3, r3=st.columns((4,1))
          with r3:
               st.write("###")
               TUimage= Image.open("images/TU.webp")
               st.image(TUimage)
          with l3:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> جامعة تشرين </h2>" , unsafe_allow_html=True)
               l31,r31=st.columns(2)
               with l31:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: اللاذقية  </h5>" , unsafe_allow_html=True)
               with r31:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 3767 </h5>" , unsafe_allow_html=True)      
                    st.write("<a href='http://www.tishreen.edu.sy/' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>tishreen.edu.sy</a>", unsafe_allow_html=True) 
                    st.write("<a href='TU' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---") 
          l4, r4=st.columns((4,1))
          with r4:
               st.write("###")
               BUimage= Image.open("images/BU.webp")
               st.image(BUimage)
          with l4:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> جامعة البعث </h2>" , unsafe_allow_html=True)
               l41,r41=st.columns(2)
               with l41:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: حمص  </h5>" , unsafe_allow_html=True)
               with r41:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 5002 </h5>" , unsafe_allow_html=True)      
                    st.write("<a href='http://www.albaath-univ.edu.sy/' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>albaath-univ.edu.sy</a>", unsafe_allow_html=True) 
                    st.write("<a href='BU' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---")
          l5, r5=st.columns((4,1))
          with r5:
               st.write("###")
               TAUimage= Image.open("images/TAU.jpeg")
               st.image(TAUimage)
          with l5:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> جامعة طرطوس </h2>" , unsafe_allow_html=True)
               l51,r51=st.columns(2)
               with l51:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: طرطوس  </h5>" , unsafe_allow_html=True)
               with r51:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 7379 </h5>" , unsafe_allow_html=True)      
                    st.write("<a href='http://tartous-univ.edu.sy/' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>tartous-univ.edu.sy</a>", unsafe_allow_html=True) 
                    st.write("<a href='TAU' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---")
          l6, r6=st.columns((4,1))
          with r6:
               st.write("###")
               HUimage= Image.open("images/HU.webp")
               st.image(HUimage)
          with l6:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> جامعة حماه </h2>" , unsafe_allow_html=True)
               l61,r61=st.columns(2)
               with l61:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: حماه  </h5>" , unsafe_allow_html=True)
               with r61:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 7120 </h5>" , unsafe_allow_html=True)      
                    st.write("<a href='http://www.hama-univ.edu.sy/ar/' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>hama-univ.edu.sy</a>", unsafe_allow_html=True) 
                    st.write("<a href='HU' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---")
          l7, r7=st.columns((4,1))
          with r7:
               st.write("###")
               EUimage= Image.open("images/EU.jpeg")
               st.image(EUimage)
          with l7:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> جامعة الفرات </h2>" , unsafe_allow_html=True)
               l71,r71=st.columns(2)
               with l71:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: فقط للطلاب المؤهلين للتقديم على مفاضلة المحافظات الشرقية   </h5>" , unsafe_allow_html=True)
                    notbutton= st.button(" مفاضلة المحافظات الشرقية")  
                    if notbutton == True:  
                         st.markdown("<h5 style='text-align: right; color: #000000;'> يستطيع أن يتقدم إليها جميع الطلاب السوريين ومن في حكمهم الحاصلين على الشهادة الثانوية العامة السورية من إحدى محافظات دير الزور – الحسكة –الرقة،  ويختار الطالب الجامعة التي يريد أن يداوم فيها ويعامل معاملة طلاب تلك الجامعة دون تفرقة  </h5>", unsafe_allow_html=True)
                         st.markdown("<h5 style='text-align: right; color: #00B0F0;'>  نحن ننصح أبناء المحافظات الشرقية بإضافة طلبات المحافظات الشرقية إلى مفاضلتهم لأنها تزيد من فرص قبولهم </h5>", unsafe_allow_html=True)
                         litteralynotbutton=st.button("⏏")
               with r71:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 16033 </h5>" , unsafe_allow_html=True)      
                    st.write("<a href='http://www.alfuratuniv.edu.sy/' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>alfuratuniv.edu.sy</a>", unsafe_allow_html=True)
          st.write("---")
          l8, r8=st.columns((4,1))
          with r8:
               st.write("###")
               SVUimage= Image.open("images/SVU.png")
               st.image(SVUimage)
          with l8:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> الجامعة السورية الافتراضية </h2>" , unsafe_allow_html=True)
               l81,r81=st.columns(2)
               with l81:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> جامعة افتراضية يتم فيها التعليم عبر الإنترنت </h5>" , unsafe_allow_html=True)
               with r81:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 6896 </h5>" , unsafe_allow_html=True)      
                    st.write("<a href='http://svuonline.org/' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>svuonline.org</a>", unsafe_allow_html=True) 
                    st.write("<a href='SVU' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---")
          l9, r9=st.columns((4,1))
          with r9:
               st.write("###")
               RUimage= Image.open("images/REU.png")
               st.image(RUimage)
          with l9:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> جامعة بلاد الشام </h2>" , unsafe_allow_html=True)
               l91,r91=st.columns(2)
               with l91:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: دمشق  </h5>" , unsafe_allow_html=True)
               with r91:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 25620 </h5>" , unsafe_allow_html=True) 
                    st.markdown("<h5 style='text-align: right; color: #000000;'> الجامعة متخصصة بالعلوم الشرعية </h5>" , unsafe_allow_html=True)
          st.write("---")
          l10, r10=st.columns((4,1))
          with r10:
               st.write("###")
               HUimage= Image.open("images/Hiast.png")
               st.image(HUimage)
          with l10:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> المعهد العالي للعلوم التطبيقية والتكنولوجيا</h2>" , unsafe_allow_html=True)
               l101,r101=st.columns(2)
               with l101:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: دمشق و حلب  </h5>" , unsafe_allow_html=True)
               with r101:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 4894 </h5>" , unsafe_allow_html=True)      
                    st.write("<a href='https://hiast.edu.sy/ar' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>hiast.edu.sy</a>", unsafe_allow_html=True) 
                    st.write("<a href='HIAST' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---")
          l10, r10=st.columns((4,1))
          with r10:
               st.write("###")
               st.write("###")
               HUimage= Image.open("images/HIBA.png")
               st.image(HUimage)
          with l10:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> المعهد العالي لإدارة الأعمال</h2>" , unsafe_allow_html=True)
               l101,r101=st.columns(2)
               with l101:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: دمشق و حلب  </h5>" , unsafe_allow_html=True)
               with r101:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 21156 </h5>" , unsafe_allow_html=True)      
                    st.write("<a href='https://www.hiba.edu.sy/' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>hiba.edu.sy</a>", unsafe_allow_html=True) 
     if selectuni=="الجامعات الخاصة":
          st.markdown("<h5 style='text-align: center; color: #0070c0;'> جميع الرسوم الدراسية هي للعام الدراسي الحالي 2024/25  </h5>" , unsafe_allow_html=True)
          l1, r1=st.columns((4,1))
          with r1:
               st.write("###")
               DUimage= Image.open("images/KU.webp")
               st.image(DUimage)
          with l1:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> جامعة القلمون </h2>" , unsafe_allow_html=True)
               l11,r11=st.columns(2)
               with l11:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: ريف دمشق </h5>" , unsafe_allow_html=True)
               with r11:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 7069 </h5>" , unsafe_allow_html=True)      
                    st.write("<a href='http://www.uok.edu.sy/' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>uok.edu.sy</a>", unsafe_allow_html=True) 
                    st.write("<a href='KU' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---") 
          l2, r2=st.columns((4,1))
          with r2:
               st.write("###")
               AUimage= Image.open("images/AIU.webp")
               st.image(AUimage)
          with l2:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> الجامعة العربية الدولية </h2>" , unsafe_allow_html=True)
               l21,r21=st.columns(2)
               with l21:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: دمشق، ريف دمشق، درعا </h5>" , unsafe_allow_html=True)
               with r21:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 5091 </h5>" , unsafe_allow_html=True)      
                    st.write("<a href='http://www.aiu.edu.sy/' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>aiu.edu.sy</a>", unsafe_allow_html=True) 
                    st.write("<a href='AIU' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---")  
          l3, r3=st.columns((4,1))
          with r3:
               st.write("###")
               TUimage= Image.open("images/SPU.webp")
               st.image(TUimage)
          with l3:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> الجامعة السورية الخاصة </h2>" , unsafe_allow_html=True)
               l31,r31=st.columns(2)
               with l31:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: دمشق وريفها  </h5>" , unsafe_allow_html=True)
               with r31:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 5398 </h5>" , unsafe_allow_html=True)      
                    st.write("<a href='http://www.spu.edu.sy/' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>spu.edu.sy</a>", unsafe_allow_html=True) 
                    st.write("<a href='SPU' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---") 
          l4, r4=st.columns((4,1))
          with r4:
               st.write("###")
               BUimage= Image.open("images/IUST.webp")
               st.image(BUimage)
          with l4:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> الجامعة الدولية الخاصة للعلوم والتكنولوجيا </h2>" , unsafe_allow_html=True)
               l41,r41=st.columns(2)
               with l41:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: دمشق، ريف دمشق، درعا </h5>" , unsafe_allow_html=True)
               with r41:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 6683 </h5>" , unsafe_allow_html=True)      
                    st.write("<a href='http://www.iust.edu.sy/' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>iust.edu.sy</a>", unsafe_allow_html=True) 
                    st.write("<a href='IUST' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---")
          l5, r5=st.columns((4,1))
          with r5:
               st.write("###")
               TAUimage= Image.open("images/WU.webp")
               st.image(TAUimage)
          with l5:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> جامعة الوادي الدولية </h2>" , unsafe_allow_html=True)
               l51,r51=st.columns(2)
               with l51:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: حمص  </h5>" , unsafe_allow_html=True)
               with r51:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 13542 </h5>" , unsafe_allow_html=True)      
                    st.write("<a href='http://www.wiu.edu.sy/' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>wiu.edu.sy</a>", unsafe_allow_html=True) 
                    st.write("<a href='WU' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---")
          l6, r6=st.columns((4,1))
          with r6:
               st.write("###")
               HUimage= Image.open("images/RU.webp")
               st.image(HUimage)
          with l6:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> جامعة الرشيد </h2>" , unsafe_allow_html=True)
               l61,r61=st.columns(2)
               with l61:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: دمشق، ريف دمشق، درعا </h5>" , unsafe_allow_html=True)
               with r61:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 26937 </h5>" , unsafe_allow_html=True)      
                    st.write("<a href='https://ru.edu.sy/AboutUni/Index/AR' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>ru.edu.sy</a>", unsafe_allow_html=True) 
                    st.write("<a href='RU' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---")
          l7, r7=st.columns((4,1))
          with r7:
               st.write("###")
               EUimage= Image.open("images/YU.webp")
               st.image(EUimage)
          with l7:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> جامعة اليرموك </h2>" , unsafe_allow_html=True)
               l71,r71=st.columns(2)
               with l71:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: دمشق، ريف دمشق، درعا </h5>" , unsafe_allow_html=True)
               with r71:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 22149 </h5>" , unsafe_allow_html=True)      
                    st.write("<a href='https://site.ypu.edu.sy/' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>yup.edu.sy</a>", unsafe_allow_html=True) 
                    st.write("<a href='YU' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---")
          l8, r8=st.columns((4,1))
          with r8:
               st.write("###")
               SVUimage= Image.open("images/WPU.webp")
               st.image(SVUimage)
          with l8:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> الجامعة الوطنية الخاصة </h2>" , unsafe_allow_html=True)
               l81,r81=st.columns(2)
               with l81:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: حماه </h5>" , unsafe_allow_html=True)
               with r81:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 15944 </h5>" , unsafe_allow_html=True)      
                    st.write("<a href='http://www.wpu.edu.sy' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>wpu.edu.sy</a>", unsafe_allow_html=True) 
                    st.write("<a href='WPU' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---")
          l9, r9=st.columns((4,1))
          with r9:
               st.write("###")
               RUimage= Image.open("images/CU.webp")
               st.image(RUimage)
          with l9:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> جامعة قرطبة الخاصة </h2>" , unsafe_allow_html=True)
               l91,r91=st.columns(2)
               with l91:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: حلب والحسكة  </h5>" , unsafe_allow_html=True)
               with r91:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 25893 </h5>" , unsafe_allow_html=True) 
                    st.write("<a href='https://cpu.edu.sy/' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>cpu.edu.sy</a>", unsafe_allow_html=True)
                    st.write("<a href='CU' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---")
          l10, r10=st.columns((4,1))
          with r10:
               st.write("###")
               RUimage= Image.open("images/IU.webp")
               st.image(RUimage)
          with l10:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> جامعة الاتحاد الخاصة </h2>" , unsafe_allow_html=True)
               l101,r101=st.columns(2)
               with l101:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: الرقة، حلب، دمشق  </h5>" , unsafe_allow_html=True)
               with r101:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 25893 </h5>" , unsafe_allow_html=True) 
                    st.write("<a href='http://www.ipu.edu.sy/' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>ipu.edu.sy</a>", unsafe_allow_html=True)
                    st.write("<a href='IU' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---")
          l11, r11=st.columns((4,1))
          with r11:
               st.write("###")
               DUimage= Image.open("images/SU.webp")
               st.image(DUimage)
          with l11:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> جامعة الشهباء </h2>" , unsafe_allow_html=True)
               l111,r111=st.columns(2)
               with l111:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: حلب </h5>" , unsafe_allow_html=True)
               with r111:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 28618 </h5>" , unsafe_allow_html=True)      
                    st.write("<a href='http://su.edu.sy/ar/home' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>su.edu.sy</a>", unsafe_allow_html=True) 
                    st.write("<a href='SU' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---") 
          l12, r12=st.columns((4,1))
          with r12:
               st.write("###")
               AUimage= Image.open("images/AUST.webp")
               st.image(AUimage)
          with l12:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> الجامعة العربية الخاصة للعلوم والتكنولوجيا </h2>" , unsafe_allow_html=True)
               l121,r121=st.columns(2)
               with l121:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: حماه </h5>" , unsafe_allow_html=True)
               with r121:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 23203 </h5>" , unsafe_allow_html=True)      
                    st.write("<a href='http://aust.edu.sy/' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>aust.edu.sy</a>", unsafe_allow_html=True) 
                    st.write("<a href='AUST' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---")  
          l13, r13=st.columns((4,1))
          with r13:
               st.write("###")
               TUimage= Image.open("images/JU.webp")
               st.image(TUimage)
          with l13:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> جامعة الجزيرة </h2>" , unsafe_allow_html=True)
               l131,r131=st.columns(2)
               with l131:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات:  دير الزور سابقاً/ على طريق دمشق درعا حالياً  </h5>" , unsafe_allow_html=True)
               with r131:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 18758 </h5>" , unsafe_allow_html=True)      
                    st.write("<a href='https://jude.edu.sy/' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>jude.edu.sy</a>", unsafe_allow_html=True) 
                    st.write("<a href='JU' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---") 
          l14, r14=st.columns((4,1))
          with r14:
               st.write("###")
               st.write("###")
               BUimage= Image.open("images/ANU.webp")
               st.image(BUimage)
          with l14:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> جامعة الأندلس للعلوم الطبية </h2>" , unsafe_allow_html=True)
               l141,r141=st.columns(2)
               with l141:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: طرطوس </h5>" , unsafe_allow_html=True)
               with r141:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 6147 </h5>" , unsafe_allow_html=True)      
                    st.write("<a href='http://www.au.edu.sy/' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>au.edu.sy</a>", unsafe_allow_html=True) 
                    st.write("<a href='ANU' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---")
          l15, r15=st.columns((4,1))
          with r15:
               st.write("###")
               TAUimage= Image.open("images/HPU.webp")
               st.image(TAUimage)
          with l15:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> جامعة الحواش </h2>" , unsafe_allow_html=True)
               l151,r151=st.columns(2)
               with l151:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: حمص  </h5>" , unsafe_allow_html=True)
               with r151:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 14475 </h5>" , unsafe_allow_html=True)      
                    st.write("<a href='http://hpu.edu.sy/ar/index.php' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>hpu.edu.sy</a>", unsafe_allow_html=True) 
                    st.write("<a href='HPU' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---")
          l16, r16=st.columns((4,1))
          with r16:
               st.write("###")
               HUimage= Image.open("images/EBU.webp")
               st.image(HUimage)
          with l16:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> جامعة إيبلا </h2>" , unsafe_allow_html=True)
               l161,r161=st.columns(2)
               with l161:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: حلب </h5>" , unsafe_allow_html=True)
               with r161:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 28140 </h5>" , unsafe_allow_html=True)      
                    st.write("<a href='http://www.ebla.edu.sy/ar/home' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>ebla-uni.edu.sy</a>", unsafe_allow_html=True) 
                    st.write("<a href='EBU' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---")
          l17, r17=st.columns((4,1))
          with r17:
               st.write("###")
               EUimage= Image.open("images/ASPU.webp")
               st.image(EUimage)
          with l17:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> جامعة الشام الخاصة </h2>" , unsafe_allow_html=True)
               l171,r171=st.columns(2)
               with l171:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: دمشق، اللاذقية </h5>" , unsafe_allow_html=True)
               with r171:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 7253 </h5>" , unsafe_allow_html=True)      
                    st.write("<a href='https://www.aspu.edu.sy/site/arabic/index.php' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>aspu.edu.sy</a>", unsafe_allow_html=True) 
                    st.write("<a href='ASPU' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---")
          l18, r18=st.columns((4,1))
          with r18:
               st.write("###")
               SVUimage= Image.open("images/QAU.webp")
               st.image(SVUimage)
          with l18:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> جامعة قاسيون الخاصة </h2>" , unsafe_allow_html=True)
               l181,r181=st.columns(2)
               with l181:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: دمشق، ريف دمشق، درعا </h5>" , unsafe_allow_html=True)
               with r181:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 26761 </h5>" , unsafe_allow_html=True)      
                    st.write("<a href='https://qpu.edu.sy/' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>qpu.edu.sy</a>", unsafe_allow_html=True) 
                    st.write("<a href='QAU' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---")
          l19, r19=st.columns((4,1))
          with r19:
               RUimage= Image.open("images/MU.webp")
               st.image(RUimage)
          with l19:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> جامعة المنارة </h2>" , unsafe_allow_html=True)
               l191,r191=st.columns(2)
               with l191:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: اللاذقية  </h5>" , unsafe_allow_html=True)
               with r191:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 15478 </h5>" , unsafe_allow_html=True) 
                    st.write("<a href='http://manara.edu.sy/' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>manara.edu.sy</a>", unsafe_allow_html=True)
                    st.write("<a href='MU' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True)
          st.write("---")
          l20, r20=st.columns((4,1))
          with r20:
               st.write("###")
               st.write("###")
               st.write("###")
               RUimage= Image.open("images/ANTU.webp")
               st.image(RUimage)
          with l20:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> جامعة أنطاكيا السورية الخاصة </h2>" , unsafe_allow_html=True)
               l201,r201=st.columns(2)
               with l201:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: ريف دمشق  </h5>" , unsafe_allow_html=True)
               with r201:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  ترتيب الجامعة على العالم: 22149 </h5>" , unsafe_allow_html=True) 
                    st.write("<a href='http://asu.edu.sy/ar/home' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>asu.edu.sy</a>", unsafe_allow_html=True)
                    st.write("<a href='ANTU' target='_blank' class='.st-emotion-cache-g2ydmt' style='border: 1px solid #00B0F0; border-radius:5px; padding:6px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.2rem; text-decoration: none;'> ...اقرأ المزيد </a>", unsafe_allow_html=True) 
          st.write("---") 
          l20, r20=st.columns((4,1))
          with r20:
               RUimage= Image.open("images/AA.png")
               st.image(RUimage)
          with l20:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'>الأكاديمية العربية للعلوم والتكنولوجيا والنقل البحري</h2>" , unsafe_allow_html=True)
               l201,r201=st.columns(2)
               with l201:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظات: اللاذقية  </h5>" , unsafe_allow_html=True)
                    st.write("<a href='http://latakia.aast.edu/ar/' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>latakia.aast.edu</a>", unsafe_allow_html=True)
               with r201:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>الاكاديمية العربية هى إحدى منظمات جامعة الدول العربية المتخصصة فى التعليم ويشارك فى عضويتها الدول الأعضاء بجامعة الدول العربية. وتعمل الأكاديمية منذ ان انشئت عام 1972 في مجالات التعليم والتدريب والبحث العلمي و الإستشارات وخدمة المجتمع. وتقدم الاكاديمية خدماتها للطلاب والدارسين من كافة اقطار العالم العربى والافريقى فى كافة افرع المعرفة والعلوم والتكنولوجيا لاكثر من 45 عاماً</h5>" , unsafe_allow_html=True)
          st.write("---") 
          l20, r20=st.columns((4,1))
          with r20:
               RUimage= Image.open("images/TH.jpeg")
               st.image(RUimage)
          with l20:
               st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'>كلية اللاهوت الخاصة</h2>" , unsafe_allow_html=True)
               l201,r201=st.columns(2)
               with l201:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المحافظة: دمشق  </h5>" , unsafe_allow_html=True)
                    st.write("<a href='https://www.theologyfaculty.org/arabic/index.php' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>theologyfaculty.org</a>", unsafe_allow_html=True)
               with r201:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> كلّيّة اللاهوت الخاصّة، الكلّيّة الأولى في الجمهوريّة العربيّة السوريّة التي تُعنى بتدريس العلوم اللاَّهوتيّة، مقرّها مدينة دمشق، وتعود ملكيّتها إلى بطريركيّة الروم الملكيّين الكاثوليك </h5>" , unsafe_allow_html=True) 
