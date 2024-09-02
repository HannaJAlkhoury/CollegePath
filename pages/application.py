import streamlit as st
import json
from PIL import Image
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
@st.cache_data
def load_lottiefile(filepath: str):
     with open(filepath, "r") as f:
          return json.load(f)
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode() 
@st.cache_data
def imgprint(path):
     img = Image.open(path)
     st.image(img)
     return    
#Page Config     
icon = Image.open("images/cap.png")
st.set_page_config(page_title="كيفية التقديم على المفاضلة في سوريا", page_icon=icon, layout= "wide")
hide_pages(["AAST","sp","majors","universities","application","DU", "Website", "AU",'ANTU','MU','QAU','ASPU','EBU','HPU','ANU','ANU','JU','AUST','SU','IU','CU','WPU','YU','RU','WU','IUST','SPU','AIU','KU','HU','SVU','EU','TU','TAU','BU','HIAST'])
#Page Style in CSS
Page_header=f"""
<style> 
#MainMenu {{visibility: hidden;}}
footer {{visibility: hidden;}}
[data-testid="stHeader"] {{
background: linear-gradient(to right, #0073cc,#205090);
height:3rem;
}}
.css-fblp2m {{
color: #0070C0;
font-size: 2rem;
}}
.st-emotion-cache-hsmt6w{{
background-color:#ffffff;
color:#0070C0;
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
    padding: 0rem 1.5rem 1.4rem;
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
    padding: 0rem 1rem 3rem;
}}
</style>"""
st.markdown(Page_header, unsafe_allow_html=True)
with st.sidebar:
     st.write("###")
     logo = Image.open("images/logo.png")
     st.image(logo)
     st.write("###")
     st.write('<a href="Website" target="_self" class=".st-emotion-cache-g2ydmt" style="display: inherit;border-bottom: 2px solid #205090; border-radius:6px;background-color:#ffffff ; padding:10px; text-align: center; color:#000000; font-weight: 700; font-size: 1.1rem; text-decoration: none; "> الصفحة الرئيسية ‎ ‎<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-house-door-fill" viewBox="0 0 20 20"><path d="M6.5 14.5v-3.505c0-.245.25-.495.5-.495h2c.25 0 .5.25.5.5v3.5a.5.5 0 0 0 .5.5h4a.5.5 0 0 0 .5-.5v-7a.5.5 0 0 0-.146-.354L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.354 1.146a.5.5 0 0 0-.708 0l-6 6A.5.5 0 0 0 1.5 7.5v7a.5.5 0 0 0 .5.5h4a.5.5 0 0 0 .5-.5"/></svg></a>' , unsafe_allow_html=True)
     st.write('<a href="#" target="_self" class=".st-emotion-cache-g2ydmt" style="display: inherit;border-bottom: 2px solid #205090; border-radius:6px;background-color:#9BE5FF ; padding:10px; text-align: center; color:#ffffff; font-weight: 600; font-size: 1rem; text-decoration: none; "> المفاضلة ‎ ‎<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-card-list" viewBox="0 0 20 20"><path d="M14.5 3a.5.5 0 0 1 .5.5v9a.5.5 0 0 1-.5.5h-13a.5.5 0 0 1-.5-.5v-9a.5.5 0 0 1 .5-.5zm-13-1A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h13a1.5 1.5 0 0 0 1.5-1.5v-9A1.5 1.5 0 0 0 14.5 2z"/><path d="M5 8a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7A.5.5 0 0 1 5 8m0-2.5a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7a.5.5 0 0 1-.5-.5m0 5a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7a.5.5 0 0 1-.5-.5m-1-5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0M4 8a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0m0 2.5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0"/><svg></a>' , unsafe_allow_html=True)
     st.write('<a href="sp" target="_self" class=".st-emotion-cache-g2ydmt" style="display: inherit;border-bottom: 2px solid #205090;border-radius:6px;background-color:#ffffff; padding:10px; text-align: center; color:#000000; font-weight: 600; font-size: 1rem; text-decoration: none; "> شرح عن الاختصاصات الجامعية ‎ ‎<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-mortarboard-fill" viewBox="0 0 20 20"><path d="M8.211 2.047a.5.5 0 0 0-.422 0l-7.5 3.5a.5.5 0 0 0 .025.917l7.5 3a.5.5 0 0 0 .372 0L14 7.14V13a1 1 0 0 0-1 1v2h3v-2a1 1 0 0 0-1-1V6.739l.686-.275a.5.5 0 0 0 .025-.917z"/><path d="M4.176 9.032a.5.5 0 0 0-.656.327l-.5 1.7a.5.5 0 0 0 .294.605l4.5 1.8a.5.5 0 0 0 .372 0l4.5-1.8a.5.5 0 0 0 .294-.605l-.5-1.7a.5.5 0 0 0-.656-.327L8 10.466z"/><svg></a>', unsafe_allow_html=True)
     st.write('<a href="universities" target="_self" class=".st-emotion-cache-g2ydmt" style="display: inherit;border-bottom: 2px solid #205090;border-radius:6px;background-color:#ffffff; padding:10px; text-align: center; color:#000000; font-weight: 600; font-size: 1rem; text-decoration: none; "> البحث عن الجامعة ‎ ‎<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-bank2" viewBox="0 0 20 20"><path d="M8.277.084a.5.5 0 0 0-.554 0l-7.5 5A.5.5 0 0 0 .5 6h1.875v7H1.5a.5.5 0 0 0 0 1h13a.5.5 0 1 0 0-1h-.875V6H15.5a.5.5 0 0 0 .277-.916zM12.375 6v7h-1.25V6zm-2.5 0v7h-1.25V6zm-2.5 0v7h-1.25V6zm-2.5 0v7h-1.25V6zM8 4a1 1 0 1 1 0-2 1 1 0 0 1 0 2M.5 15a.5.5 0 0 0 0 1h15a.5.5 0 1 0 0-1z"/><svg></a>', unsafe_allow_html=True)
     st.write('<a href="majors" target="_self" class=".st-emotion-cache-g2ydmt" style="display: inherit;border-bottom: 2px solid #205090;border-radius:6px;background-color:#ffffff; padding:10px; text-align: center; color:#000000; font-weight: 600; font-size: 1rem; text-decoration: none; "> البحث عن الفرع ‎ ‎<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-search" viewBox="0 0 20 20"><path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0"/><svg></a>', unsafe_allow_html=True)    
     st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">', unsafe_allow_html=True)
     st.write('<h4 style="margin-inline-start: 8%;"><a href="https://www.instagram.com/collegepath_insta?igsh=MWcyNTh4Z2d6dG84cA==" style="color:#ffffff;"><svg xmlns="http://www.w3.org/2000/svg" width="35%" height="45" fill="currentColor" class="bi bi-instagram" viewBox="0 0 25 25"><path d="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.9 3.9 0 0 0-1.417.923A3.9 3.9 0 0 0 .42 2.76C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.048 3.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.333 1.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.9 3.9 0 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 16 8s-.01-2.445-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.9 3.9 0 0 0-.923-1.417A3.9 3.9 0 0 0 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0zm-.717 1.442h.718c2.136 0 2.389.007 3.232.046.78.035 1.204.166 1.486.275.373.145.64.319.92.599s.453.546.598.92c.11.281.24.705.275 1.485.039.843.047 1.096.047 3.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.5 2.5 0 0 1-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.5 2.5 0 0 1-.92-.598 2.5 2.5 0 0 1-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.233s.008-2.388.046-3.231c.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92s.546-.453.92-.598c.282-.11.705-.24 1.485-.276.738-.034 1.024-.044 2.515-.045zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 0 0-1.92m-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217m0 1.441a2.667 2.667 0 1 1 0 5.334 2.667 2.667 0 0 1 0-5.334"/></svg></a><a href="https://youtube.com/@college_path?si=WoMkxc9VCI4ON0wv" style="color:#ffffff;"><svg xmlns="http://www.w3.org/2000/svg" width="30%" height="45" fill="currentColor" class="bi bi-youtube" viewBox="0 0 25 25"><path d="M8.051 1.999h.089c.822.003 4.987.033 6.11.335a2.01 2.01 0 0 1 1.415 1.42c.101.38.172.883.22 1.402l.01.104.022.26.008.104c.065.914.073 1.77.074 1.957v.075c-.001.194-.01 1.108-.082 2.06l-.008.105-.009.104c-.05.572-.124 1.14-.235 1.558a2.01 2.01 0 0 1-1.415 1.42c-1.16.312-5.569.334-6.18.335h-.142c-.309 0-1.587-.006-2.927-.052l-.17-.006-.087-.004-.171-.007-.171-.007c-1.11-.049-2.167-.128-2.654-.26a2.01 2.01 0 0 1-1.415-1.419c-.111-.417-.185-.986-.235-1.558L.09 9.82l-.008-.104A31 31 0 0 1 0 7.68v-.123c.002-.215.01-.958.064-1.778l.007-.103.003-.052.008-.104.022-.26.01-.104c.048-.519.119-1.023.22-1.402a2.01 2.01 0 0 1 1.415-1.42c.487-.13 1.544-.21 2.654-.26l.17-.007.172-.006.086-.003.171-.007A100 100 0 0 1 7.858 2zM6.4 5.209v4.818l4.157-2.408z"/><svg></a><a href="https://www.facebook.com/profile.php?id=61565154959875&sfnsn=wa&mibextid=RUbZ1f" style="color:#ffffff;"><svg xmlns="http://www.w3.org/2000/svg" width="35%" height="45" fill="currentColor" class="bi bi-facebook" viewBox="0 0 25 25"><path d="M16 8.049c0-4.446-3.582-8.05-8-8.05C3.58 0-.002 3.603-.002 8.05c0 4.017 2.926 7.347 6.75 7.951v-5.625h-2.03V8.05H6.75V6.275c0-2.017 1.195-3.131 3.022-3.131.876 0 1.791.157 1.791.157v1.98h-1.009c-.993 0-1.303.621-1.303 1.258v1.51h2.218l-.354 2.326H9.25V16c3.824-.604 6.75-3.934 6.75-7.951"/><svg></a></h4>', unsafe_allow_html=True)
Page_button=f"""
          <style>
          body {{
               text-align: right;
          }} 
          .css-n81u42 {{
          font-weight: bolder;
          text-align: right;
          color: #0070C0;
          background-color:#FFFFFF;
          border: 1px solid #0070C0;
          }}
          .css-g2ydmt{{
          background-color: transparent;
          border: 0px;
          }}
          p, ol, ul, dl {{
          font-size: 1.1rem;
          font-weight: BOLD;
          }}
          .css-qdgm74 p{{
          color: #00B0F0;
          }}
          .st-emotion-cache-z5fcl4 {{
    width: 100%;
    padding: 0rem 1rem 3rem;
}}
.st-emotion-cache-n81u42 {{
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: flex-end;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 0rem;
    min-height: 38.4px;
    margin: 0px;
    line-height: 1.6;
    width: 100%;
    user-select: none;
    background-color: #f8f9fa;
    color: #000000;
    border: 1px solid rgb(0 176 240 / 0%);
    align-content: center;
    border-bottom-color:#00b0f0;
}}
</style>
          """
if 1==1:
     st.write("###")
     hide_img_fss = '''
          <style>
          button[title="View fullscreen"]{
             visibility: hidden;}
          </style>
          '''
     st.markdown(hide_img_fss, unsafe_allow_html=True)
     st.markdown(Page_button, unsafe_allow_html=True)
     with st.container():
          st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'> ما هي المفاضلة؟ </h2>", unsafe_allow_html=True)
          st.markdown("<h5 style='text-align: right; color: #000000;'> المفاضلة هي النظام الذي يتم من خلاله قبول الطلاب الحاصلين على الشهادة الثانوية بكافة أنواعها \n (علمي، أدبي، مهني.. إلخ) بالفروع الجامعية المختلفة للجامعات العامة والخاصة والمعاهد </h5>", unsafe_allow_html=True)
          st.write("---")
     with st.container():     
          st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'>: قبل التقدم على المفاضلة </h2>" , unsafe_allow_html=True)
          st.markdown("<h4 style='text-align: right; color: #0070C0;'>: أولاً </h4>" , unsafe_allow_html=True)
          st.markdown("<h5 style='text-align: right; color: #000000;'> يترتب على الطالب تحديد الاختصاص أو مجموعة الاختصاصات الجامعية التي تناسبه ويمكنه الاستعانة بالشرح المفصل الذي نقدمه على منصتنا وننصح الجميع بالاطلاع عليها  </h5>", unsafe_allow_html=True)
          st.markdown("<h4 style='text-align: right; color: #0070C0;'>: ثانياً </h4>" , unsafe_allow_html=True)
          st.markdown("<h5 style='text-align: right; color: #000000;'> تحديد الجامعات التي تناسب مكان سكن الطالب وإمكانياته المادية والاختصاصات التي يرغبها  </h5>" , unsafe_allow_html=True)
          st.markdown("<h4 style='text-align: right; color: #0070C0;'>: ثالثاً </h4>" , unsafe_allow_html=True)
          st.markdown("<h5 style='text-align: right; color: #000000;'> اذهب لقسم البحث عن الفرع وجد أكواد الأفرع الجامعية التي ترغب بالتقديم عليها وسجلها مع اسم الاختصاص والجامعة بالترتيب من الأكثر تحبيذاً للأقل تحبيذاً </h5>", unsafe_allow_html=True)
          st.markdown("<h4 style='text-align: right; color: #0070C0;'>: رابعاً </h4>" , unsafe_allow_html=True)
          st.markdown("<h5 style='text-align: right; color: #000000;'> على الطالب أيضاً اختيار بعض البدائل في حال عدم قبوله في الأفرع المرادة ونحن ننصح بالإكثار من البدائل وذلك خوفاً على الطالب من أن ترفض جميع رغباته التي قدمها في المفاضلة بسبب ارتفاع علامات القبول في الكثير من الأفرع بين حد العلامات الذي يؤهل الطالب للتقديم على الفرع (ويسمى المفاضلة الأولى) والحد الذي يقبل به الطلاب (ويسمى المفاضلة الثانية أو النتائج) </h5>", unsafe_allow_html=True)
          st.write("---")
          st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'>: بعض المصطلحات الهامة التي يجب فهمها </h2>", unsafe_allow_html=True)
          st.write("###")
          left, right = st.columns(2)
          with left:
               imgprint("images/photo.webp") 
          with right:    
               a1= st.button(" السنة التحضيرية ", type="primary")  
               if a1 == True:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> على الراغبين بدراسة أحد الاختصاصات الطبية (الطب البشري، طب الأسنان أو الصيدلة) في جامعة حكومية التقديم على السنة التحضيري حيث يدخل معدلهم في هذه السنة مع معدل البكلوريا في فرزهم على الاختصاصات المختلفة </h5>", unsafe_allow_html=True)
                    b1=st.button("⏏")
               a7= st.button(" الافتراضي ", type="primary")  
               if a7 == True:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> هو الدراسة عبر الجامعة الافتراضية السورية حيث يدرس الطالب فيها كلياً عبر الانترنت حيث يحق للطالب أن يسجل ويدرس في الجامعة الافتراضية بالإضافة إلى أي فرع آخر في أي جامعة (أي يمكن للطالب أن يدرس الهندسة المعلوماتية بالجامعة الافتراضية بالإضافة إلى دراسة الرياضيات في جامعة دمشق) </h5>", unsafe_allow_html=True)
                    st.markdown("<h5 style='text-align: right; color: #00B0F0;'>: يتم التقديم على الجامعة الافتراضية عبر موقعها الرسمي </h5>", unsafe_allow_html=True)
                    st. write("<a href='#' id='https://svuonline.org/ar'>https://svuonline.org/ar</a>", unsafe_allow_html=True)
                    b7=st.button("⏏")
               a8= st.button(" التعليم المفتوح ", type="primary")  
               if a8 == True:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> تتيح الجامعات الحكومية إمكانية دراسة تخصصات متعددة عبر التعليم المفتوح حيث يمكن للطالب دراسة فرع في التعليم المفتوح بالإضافة لفرعه الرئيسي، من التخصصات المتاحة الإعلام، الدراسات القانونية، إدارة المشروعات الصغيرة والمتوسطة،المحاسبة، الترجمة والتربية  </h5>", unsafe_allow_html=True)
                    b8=st.button("⏏")
               a81= st.button(" المعاهد العليا والتقانية ", type="primary")  
               if a81 == True:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> المعاهد العليا شبيهة بالكليات من حيث سنوات الدراسة والإجازات الممنوحة، أما المعاهد التقانية فتكون سنوات الدراسة فيها سنتان والهدف منها هو تخريج خبراء في مجالات تطبيقية في مختلف المجالات التي يتطلبها سوق العمل </h5>", unsafe_allow_html=True)
                    st.markdown("<h5 style='text-align: right; color: #00b0f0;'>  الطلاب المتفوقون في المعاهد التقانية قد يحق لهم الالتحاق ببعض الاختصاصات الجامعية  الموافقة بعد تخرجهم من المعهد </h5>", unsafe_allow_html=True)
                    b81=st.button("⏏")
               a88= st.button("  اختبارات القبول ", type="primary")  
               if a88 == True:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> يتطلب التقديم على بعض الاختصاصات ومن أهمها العمارة واللغة الإنجليزية والفرنسية وبعض كليات الفنون وبعض المعاهد النجاح باختبارات اضافية، يرجى قراءة ملف البي دي إف لمعرفة التفاصيل  </h5>", unsafe_allow_html=True)
                    with open("exams.pdf", "rb") as pdf_file:
                         PDFbyte = pdf_file.read()
                         st.download_button(label=" اضغط لتنزيل الملف ",
                         data=PDFbyte,
                         file_name="اختبارات.pdf",
                         mime='application/octet-stream')
                    b88=st.button("⏏") 
               a2= st.button(" الطلب العام ", type="primary")  
               if a2 == True:
                    c2="<h5 style='text-align: right; color: #000000;'>يقدم الطالب على أحد الفروع في جامعة حكومية للدراسة مجاناً </h5>"
                    st.markdown(c2, unsafe_allow_html=True)
                    b2=st.button("⏏") 
               a3= st.button(" الطلب الموازي ", type="primary")  
               if a3 == True:
                    c3="<h5 style='text-align: right; color: #000000;'> يقدم الطالب على أحد الفروع في جامعة حكومية للدراسة مقابل مبلغ مالي تتميز بحد أدنا للعلامات أقل بقليل من العام فتسمح للطالب الذي لم تمكنه علاماته من أن يقبل طلبه العام أن يدخل الفرع مقابل مبلغ مالي ضئيل نسبة لأقساط الجامعات الخاصة  </h5>"
                    st.markdown(c3, unsafe_allow_html=True)
                    st.markdown("<h5 style='text-align: right; color: #000000;'> لا تتغير أقساط التعليم الموازي على الطالب من سنة إلى أخرى بل تبقى ثابتة وتساوي الأقساط التي تم تحديدها له في السنة التي سجل بها </h5>", unsafe_allow_html=True)
                    b3=st.button("⏏")
               a4= st.button(" الطلب الخاص ", type="primary")  
               if a4 == True:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> يقدم الطالب على أحد الفروع في جامعة خاصة ويترتب عليه رسوم دراسية تفرضها الجامعة </h5>", unsafe_allow_html=True)
                    st.markdown("<h5 style='text-align: right; color: #000000;'> يتم التقديم على الفروع الطبية من خلال مفاضلة التعليم العالي أما التقديم على باقي الاختصاصات يتم عبر مفاضلات تحددها كل جامعة </h5>", unsafe_allow_html=True)
                    st.markdown("<h5 style='text-align: right; color: #000000;'> لا تتغير أقساط التعليم الخاص على الطالب من سنة إلى أخرى بل تبقى ثابتة وتساوي الأقساط التي تم تحديدها له في السنة التي سجل بها </h5>", unsafe_allow_html=True)
                    b4=st.button("⏏")
               a5= st.button(" منحة الجامعة الخاصة ", type="primary")  
               if a5 == True:
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  يقدم الطالب عبر مفاضلة وزارة التعليم العالي حصراً على منحة لدراسة أحد الفروع في جامعة خاصة مجانا دون رسوم دراسية وقد تقدم بعض الجامعات ميزات أخرى ويجب التواصل مع الجامعة لمعرفة كافة التفاصيل، لكن لا يحق للطالب في حال قبوله في أحد منح الجامعات الخاصة الاستنكاف عنه او تغيير رغبته </h5>", unsafe_allow_html=True)
                    b5=st.button("⏏")
               a6= st.button(" ملء الشواغر ", type="primary")  
               if a6 == True:                                
                    st.markdown("<h5 style='text-align: right; color: #000000;'> في الكثير من الأحيان قد يتوفر في الجامعات الخاصة بعض المقاعد الشاغرة بعد انتهاء المفاضلة عليها لذلك يتم اللجوء لمفاضلة ملء الشواغر حيث يتوفر بعض المقاعد ويكون الحد الأدنى للقبول أقل بقليل من ذلك للطلب الخاص ولا تختلف أبداً عن الطلب الخاص بأي شيء آخر إلا أن الطالب قد يضطر لدخول الجامعة في منتصف الفصل الدراسي أو يتم تأجيله فصلا كاملاً لذلك ينصح بالتقديم في المفاضلة الخاصة أولاً وعدم الانتظار لمفاضلة ملء الشواغر إلا عند رفض الطلب الخاص للفرع المطلوب </h5>", unsafe_allow_html=True)
                    b6=st.button("⏏")
               a13= st.button(" مفاضلة المحافظات الشرقية", type="primary")  
               if a13 == True:  
                    st.markdown("<h5 style='text-align: right; color: #000000;'> يستطيع أن يتقدم إليها جميع الطلاب السوريين ومن في حكمهم الحاصلين على الشهادة الثانوية العامة السورية من إحدى محافظات دير الزور – الحسكة –الرقة،  ويختار الطالب الجامعة التي يريد أن يداوم فيها ويعامل معاملة طلاب تلك الجامعة دون تفرقة  </h5>", unsafe_allow_html=True)
                    st.markdown("<h5 style='text-align: right; color: #00B0F0;'>  نحن ننصح أبناء المحافظات الشرقية بإضافة طلبات المحافظات الشرقية إلى مفاضلتهم لأنها تزيد من فرص قبولهم </h5>", unsafe_allow_html=True)
                    b13=st.button("⏏")
               a14= st.button(" مفاضلة أبناء أعضاء الهيئة التدريسية ", type="primary")  
               if a14 == True:  
                    st.markdown("<h5 style='text-align: right; color: #000000;'> يمكن أن يتقدم عليها أبناء أعضاء هيئة التدريس الحاليين في الجامعات الحكومية، وأبناء أعضاء هيئة البحث العلمي في مركز الدراسات والبحوث العلمية، وأبناء أعضاء هيئة التدريس الحاليين أو السابقين في المعاهد العليا التابعة لوزير التعليم العالي الذين أمضوا عشر سنوات على الأقل في هيئة التدريس أو البحث العلمي من ترك العمل لأسباب غير تأديبية، أو توفي أثناء الخدمة </h5>", unsafe_allow_html=True)
                    st.markdown("<h5 style='text-align: right; color: #000000;'>  تتميز هذه بأنه تتيح للطلاب المستفيدين القبول في الجامعات الحكومية بمعدلات أقل بكثير من أقرانهم لكن يترتب عليهم الحصول على وثيقة تثبت أنهم يحققون شروط التقدم على  هذه المفاضلة وأخذها معهم عند التقديم ويجب أن يكون لم يمض على تاريخ منح الوثيقة شهر واحد ويحصل عليها من ذاتية الجامعة أو المعهد  </h5>", unsafe_allow_html=True)
                    st.markdown("<h5 style='text-align: right; color: #00B0F0;'> يتم التقديم على هذه المفاضة عبر مراكز تقديم خاصة وليس عن بعد عبر الموقع كما باقي المفاضلات </h5>", unsafe_allow_html=True)
                    b14=st.button("⏏") 
               a14= st.button("مفاضلة ذوي الشهداء والجرحى والمفقودين ", type="primary")  
               if a14 == True:  
                    st.markdown("<h5 style='text-align: right; color: #000000;'> ويختص بأبناء وأشقاء وأزواج الشهداء، والجرحى بإعاقة كلية وجزئية، والجرحى بإعاقة لا تقل عن 30% ولا تزيد على 35% من المجندين والمجندين العسكريون الاحتياط، وأبناء الجرحى الذين يعانون من عجز كلي وجزئي لا يقل عن 70%، وأبناء المفقودين وأزواجهم من العسكريين في الجيش والقوات. القوات المسلحة ومن استشهدوا أو جرحوا أو فقدوا من قوى الأمن الداخلي بسبب الحرب أو العمليات العسكرية أو على يد العصابات الإرهابية أو العناصر المعادية، ومن أصيبوا أثناء القتال في ظل قوات الأمن الداخلية قيادة الجيش العربي السوري بنسبة عجز تصل إلى 40% بسبب الحرب أو العمليات العسكرية أو على يد العصابات الإرهابية أو العناصر المعادية. للحاصلين على شهادة الثانوية العامة يتم إثبات الحالة بوثيقة صادرة عن القيادة العامة للجيش والقوات المسلحة حصراً وفقاً للقوانين والأنظمة المعتمدة بها بالنسبة للطلاب الحاصلين على بطاقة الوطن الجريح عليهم تقديم نسخة من بطاقة الوطن الجريح بعد إبراز البطاقة الأصلية للمطابقة </h5>", unsafe_allow_html=True)
                    st.markdown("<h5 style='text-align: right; color: #000000;'> تتميز هذه بأنه تتيح للطلاب المستفيدين القبول في الجامعات الحكومية بمعدلات أقل بكثير من أقرانهم    </h5>", unsafe_allow_html=True)
                    st.markdown("<h5 style='text-align: right; color: #00B0F0;'> يتم التقديم على هذه المفاضة عبر مراكز تقديم خاصة وليس عن بعد عبر الموقع كما باقي المفاضلات </h5>", unsafe_allow_html=True)
                    b14=st.button("⏏")                 
          st.write("---") 
          st.markdown("<h2 style='text-align: right; color: #00B0F0; font-weight:bold;'>: التقديم على المفاضلة</h2>", unsafe_allow_html=True)  
          st.markdown("<h4 style='text-align: right; color: #0070C0;'>: للطلاب السوريين ومن بحكمهم </h4>" , unsafe_allow_html=True) 
          st.markdown("<h5 style='text-align: right; color: #000000;'>   التقديم على المفاضلة إلكتروني، على الطالب تنزيل تطبيق المفاضلة على الجوال أو الدخول إلى الموقع الرسمي للمفاضلة  </h5>", unsafe_allow_html=True)          
          st. write("<a href='Syria.shern.sy'>Syria.shern.sy</a>", unsafe_allow_html=True)
          st.markdown("<h5 style='text-align: right; color: #000000;'> يقوم الطالب بملء معلوماته الشخصية في الموقع ثم تصله رسالة نصية برمز التفعيل يقوم من خلاله الطالب بتفعيل حسابه والحصول على رمز المفاضلة الذي يجب ألا تتم مشاركته أبداً مع أي شخص </h5>", unsafe_allow_html=True)
          st.markdown("<h5 style='text-align: right; color: #000000;'> يتقدم الطالب على المفاضلة ويتوجب عليه التحقق من كل المعلومات بدقة متناهية قبل دفع رسوم الطلب وارساله </h5>", unsafe_allow_html=True)
          st.markdown("<h5 style='text-align: right; color: #000000;'> يتم الدفع الإلكتروني عبر تطبيق كاش موبايل لأم تي أن و سيرياتيل أو عبر حساب بنكي لأحد البنوك المعتمدة </h5>", unsafe_allow_html=True)
          st.markdown("<h4 style='text-align: right; color: #0070C0;'>: للطلاب السوريين الغير مقيمين </h4>" , unsafe_allow_html=True)
          st.markdown("<h5 style='text-align: right; color: #f03030;'> يتقدم الطالب على المفاضلة في أحد المراكز المختصة ولا يحق له التقدم إلكترونياً </h5>" , unsafe_allow_html=True)
          st.markdown("<h5 style='text-align: right; color: #000000;'> يتقدم إليها الطلاب السوريين الحاصلين على شهادة ثانوية غير سورية من مدرسة غير سورية مرخصة في الجمهورية العربية السورية في سنة القبول نفسها أو حاصلين على تلك الشهادة من الخارج بحيث تعادل تلك الشهادة الشهادة العامة السورية في نفس سنة القبول </h5>" , unsafe_allow_html=True)
          st.markdown("<h5 style='text-align: right; color: #000000;'> لا يحسم من معدلات هؤلاء الطلبة أبداً ولكن تؤخذ معدلاتهم بعد طي علامات (التربية الدينية -الرياضية -الموسيقى والفنون -السلوك) إن وجدت </h5>" , unsafe_allow_html=True)
          st.markdown("<h5 style='text-align: right; color: #000000;'> ملاحظة: على الطالب أن يحضر معه بعض الأوراق الثبوتية إلى المراكز المختصة (اقرأ الصفحة الثامنة من دليل الطالب الملحق أدناه) </h5>" , unsafe_allow_html=True)
          st.markdown("<h4 style='text-align: right; color: #0070C0;'>: للطلاب العرب والأجانب </h4>" , unsafe_allow_html=True)
          st.markdown("<h5 style='text-align: right; color: #f03030;'> يتقدم الطالب على المفاضلة في أحد المراكز المختصة ولا يحق له التقدم إلكترونياً </h5>" , unsafe_allow_html=True)
          st.markdown("<h5 style='text-align: right; color: #000000;'> يتقدم إليها الطلاب الذين لا يحملون الجنسية السورية وليسوا بحكم الطلاب السوريين الحاصلين على الشهادة الثانوية العامة السورية أو شهادة معادلة لها في نفس سنة القبول أو أو في السنة التي سبقتها </h5>" , unsafe_allow_html=True)
          st.markdown("<h5 style='text-align: right; color: #000000;'> لا يحسم من معدلات هؤلاء الطلبة أبداً ولكن تؤخذ معدلاتهم بعد طي علامات (التربية الدينية -الرياضية -الموسيقى والفنون -السلوك) إن وجدت </h5>" , unsafe_allow_html=True)
          st.markdown("<h5 style='text-align: right; color: #000000;'> ملاحظة: على الطالب أن يحضر معه بعض الأوراق الثبوتية إلى المراكز المختصة (اقرأ الصفحة الثامنة من دليل الطالب الملحق أدناه) </h5>" , unsafe_allow_html=True)
          st.write("---")
          st.markdown("<h3 style='text-align: right; color: #00B0F0;'>: ملاحظة </h3>", unsafe_allow_html=True)
          st.markdown("<h5 style='text-align: right; color: #000000;'> إن الشرح المدون أعلاه هو شرح مختصر و مبسط يكفي الأغلبية العظمى من المتقدمين على الجامعات في سوريا من السوريين المقيمين أو من في حكمهم الحاصلين على الشهادة الثانوية السورية لكن إذا كان لديك أي استفسار أو شك أو كنت طالب سوري غير مقيم أو عربي أو أجنبي فيرجى قراءة دليل الطالب للتقدم للمفاضلات الذي تصدره وزارة التعليم العالي والبحث العلمي سنوياً على صفحتها على تيليجرام  </h5>", unsafe_allow_html=True)
          st. write("<a href='https://t.me/mohesr_official_channel'> الصفحة الرسمية للوزارة على تيليتجرام </a>", unsafe_allow_html=True)
          with open("دليل_الطالب.pdf", "rb") as pdf_file1:
                         PDFbyte1 = pdf_file1.read()
                         st.download_button(label=" اضغط لتنزيل دليل الطالب ",
                         data=PDFbyte1,
                         file_name="دليل_الطالب.pdf",
                         mime='application/octet-stream')