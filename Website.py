import streamlit as st
#from streamlit_js_eval import streamlit_js_eval
from PIL import Image
from st_pages import hide_pages
#Page Config     
icon = Image.open("images/cap.png")
st.set_page_config(page_title="College Path-مسار الجامعة", page_icon=icon, layout= "wide")
hide_pages(["AAST","sp","majors","universities","application","DU", "Website", "AU",'ANTU','MU','QAU','ASPU','EBU','HPU','ANU','ANU','JU','AUST','SU','IU','CU','WPU','YU','RU','WU','IUST','SPU','AIU','KU','HU','SVU','EU','TU','TAU','BU','HIAST'])

#Page Style in CSS
SidebarStyle=f"""
.st-emotion-cache-15rnnt1{{visibility: hidden; height=0;padding=0;}}
.st-emotion-cache-9kd36y{{visibility: hidden;height=0;padding=0;}}
.st-emotion-cache-79elbk {{visibility: hidden;height=0;padding=0;}}
.st-emotion-cache-kgpedg{{padding: calc(1.375rem) 1.5rem 0rem;}}
.st-emotion-cache-1qdyr5 {{padding: 0rem 1.5rem 5rem;}}
"""
hide_img_fs = f'''
.e1yh3qqy2:hover .st-emotion-cache-1kw2d9g, .e1yh3qqy2:active .st-emotion-cache-1kw2d9g, .e1yh3qqy2:focus-visible .st-emotion-cache-1kw2d9g{{visibility: hidden;}}
.st-emotion-cache-1tg4cha svg{{visibility: hidden;}}     
'''
Page_header=f""" 
.st-emotion-cache-1tb82rd a:hover{{background-color:#E9E9E9; color:#000000;}}
.st-emotion-cache-1tb82rd a{{background-color:#FFFFFF; color:#222222;}}
.st-emotion-cache-gi0tri{{visibility: hidden;}}
#MainMenu {{visibility: hidden;}}
[data-testid="stHeader"] {{
background: linear-gradient(to right, #0073cc,#205090);
}}
.st-emotion-cache-1ibsh2c{{
padding: 3rem 1rem 3rem;
}}
.st-emotion-cache-yp5fhh{{background-color:#FFFFFF;}}
.pagebutton{{display: inherit;border-bottom: 2px solid #205090; border-radius:6px; padding:12px; text-align: center; color:#ffffff; font-weight: bolder; font-size: 1.2rem; text-decoration: none; transition: transform 0.3s ease-in-out;}}
.pagebutton:hover{{transform: scale(1.05);}}
"""
textwrap=f"""
.st-emotion-cache-1lvxfs7{{
    word-break: auto-phrase;
        text-wrap: auto
}}"""
st.markdown("<style>"+textwrap+Page_header+hide_img_fs+SidebarStyle+"</style>",unsafe_allow_html=True)
MK=700
#if width is not None:
     #MK=width
with st.sidebar:
          st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">', unsafe_allow_html=True)
          logo = Image.open("images/logo.png")
          st.image(logo)
          st.write("###")
          st.write("###")
          st.markdown('''<div style="background-color:#FFFFFF ; padding:10px;border-radius:9px;">
                      <a href="#" target="_self" class=".st-emotion-cache-g2ydmt" style="display: inherit; border-radius:6px;background-color:#00B0F0 ; padding:7px; margin:3; text-align: right; color:#FFFFFF; font-weight: 900; font-size: 1.1rem; text-decoration: none; "> الصفحة الرئيسية ‎ ‎<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-house-door-fill" viewBox="0 0 20 20"><path d="M6.5 14.5v-3.505c0-.245.25-.495.5-.495h2c.25 0 .5.25.5.5v3.5a.5.5 0 0 0 .5.5h4a.5.5 0 0 0 .5-.5v-7a.5.5 0 0 0-.146-.354L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.354 1.146a.5.5 0 0 0-.708 0l-6 6A.5.5 0 0 0 1.5 7.5v7a.5.5 0 0 0 .5.5h4a.5.5 0 0 0 .5-.5"/></svg></a>
                      <h6></h6>
                      <a href="application" target="_self" class=".st-emotion-cache-g2ydmt" style="display: inherit; border-radius:6px; padding:7px; margin:3;text-align: right; font-weight: 600; font-size: 1.1rem; text-decoration: none; "> المفاضلة ‎ ‎<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-card-list" viewBox="0 0 20 20"><path d="M14.5 3a.5.5 0 0 1 .5.5v9a.5.5 0 0 1-.5.5h-13a.5.5 0 0 1-.5-.5v-9a.5.5 0 0 1 .5-.5zm-13-1A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h13a1.5 1.5 0 0 0 1.5-1.5v-9A1.5 1.5 0 0 0 14.5 2z"/><path d="M5 8a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7A.5.5 0 0 1 5 8m0-2.5a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7a.5.5 0 0 1-.5-.5m0 5a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7a.5.5 0 0 1-.5-.5m-1-5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0M4 8a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0m0 2.5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0"/><svg></a>
                      <h6></h6>
                      <a href="sp" target="_self" class=".st-emotion-cache-g2ydmt" style="display: inherit; border-radius:6px; padding:7px; margin:3;text-align: right;  font-weight: 600; font-size: 1.1rem; text-decoration: none; "> شرح عن الاختصاصات الجامعية ‎ ‎<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-mortarboard-fill" viewBox="0 0 20 20"><path d="M8.211 2.047a.5.5 0 0 0-.422 0l-7.5 3.5a.5.5 0 0 0 .025.917l7.5 3a.5.5 0 0 0 .372 0L14 7.14V13a1 1 0 0 0-1 1v2h3v-2a1 1 0 0 0-1-1V6.739l.686-.275a.5.5 0 0 0 .025-.917z"/><path d="M4.176 9.032a.5.5 0 0 0-.656.327l-.5 1.7a.5.5 0 0 0 .294.605l4.5 1.8a.5.5 0 0 0 .372 0l4.5-1.8a.5.5 0 0 0 .294-.605l-.5-1.7a.5.5 0 0 0-.656-.327L8 10.466z"/><svg></a>
                      <h6></h6>
                      <a href="universities" target="_self" class=".st-emotion-cache-g2ydmt" style="display: inherit; border-radius:6px; padding:7px; margin:3;text-align: right;  font-weight: 600; font-size: 1.1rem; text-decoration: none; "> البحث عن الجامعة ‎ ‎<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-bank2" viewBox="0 0 20 20"><path d="M8.277.084a.5.5 0 0 0-.554 0l-7.5 5A.5.5 0 0 0 .5 6h1.875v7H1.5a.5.5 0 0 0 0 1h13a.5.5 0 1 0 0-1h-.875V6H15.5a.5.5 0 0 0 .277-.916zM12.375 6v7h-1.25V6zm-2.5 0v7h-1.25V6zm-2.5 0v7h-1.25V6zm-2.5 0v7h-1.25V6zM8 4a1 1 0 1 1 0-2 1 1 0 0 1 0 2M.5 15a.5.5 0 0 0 0 1h15a.5.5 0 1 0 0-1z"/><svg></a>
                      <h6></h6>
                      <a href="majors" target="_self" class=".st-emotion-cache-g2ydmt" style="display: inherit; border-radius:6px; padding:7px; margin:3;text-align: right;  font-weight: 600; font-size: 1.1rem; text-decoration: none; "> البحث عن الفرع ‎ ‎<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-search" viewBox="0 0 20 20"><path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0"/><svg></a>
                      </div>''', unsafe_allow_html=True)    
          st.write("###")
          st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">', unsafe_allow_html=True)
          st.write('<h4 style="margin-inline-start: 8%;"><style>svg:hover{transform: scale(1.1);}</style><a href="https://www.instagram.com/collegepath_insta?igsh=MWcyNTh4Z2d6dG84cA==" style="color:#ffffff;background-color:Transparent; transition: transform 0.3s ease-in-out;"><svg xmlns="http://www.w3.org/2000/svg" width="35%" height="45" fill="currentColor" class="bi bi-instagram" viewBox="0 0 25 25"><path d="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.9 3.9 0 0 0-1.417.923A3.9 3.9 0 0 0 .42 2.76C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.048 3.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.333 1.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.9 3.9 0 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 16 8s-.01-2.445-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.9 3.9 0 0 0-.923-1.417A3.9 3.9 0 0 0 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0zm-.717 1.442h.718c2.136 0 2.389.007 3.232.046.78.035 1.204.166 1.486.275.373.145.64.319.92.599s.453.546.598.92c.11.281.24.705.275 1.485.039.843.047 1.096.047 3.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.5 2.5 0 0 1-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.5 2.5 0 0 1-.92-.598 2.5 2.5 0 0 1-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.233s.008-2.388.046-3.231c.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92s.546-.453.92-.598c.282-.11.705-.24 1.485-.276.738-.034 1.024-.044 2.515-.045zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 0 0-1.92m-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217m0 1.441a2.667 2.667 0 1 1 0 5.334 2.667 2.667 0 0 1 0-5.334"/></svg></a><a href="https://youtube.com/@college_path?si=WoMkxc9VCI4ON0wv?sub_confirmation=1" style="color:#ffffff;background-color:Transparent;transition: transform 0.3s ease-in-out;"><svg xmlns="http://www.w3.org/2000/svg" width="30%" height="45" fill="currentColor" class="bi bi-youtube" viewBox="0 0 25 25"><path d="M8.051 1.999h.089c.822.003 4.987.033 6.11.335a2.01 2.01 0 0 1 1.415 1.42c.101.38.172.883.22 1.402l.01.104.022.26.008.104c.065.914.073 1.77.074 1.957v.075c-.001.194-.01 1.108-.082 2.06l-.008.105-.009.104c-.05.572-.124 1.14-.235 1.558a2.01 2.01 0 0 1-1.415 1.42c-1.16.312-5.569.334-6.18.335h-.142c-.309 0-1.587-.006-2.927-.052l-.17-.006-.087-.004-.171-.007-.171-.007c-1.11-.049-2.167-.128-2.654-.26a2.01 2.01 0 0 1-1.415-1.419c-.111-.417-.185-.986-.235-1.558L.09 9.82l-.008-.104A31 31 0 0 1 0 7.68v-.123c.002-.215.01-.958.064-1.778l.007-.103.003-.052.008-.104.022-.26.01-.104c.048-.519.119-1.023.22-1.402a2.01 2.01 0 0 1 1.415-1.42c.487-.13 1.544-.21 2.654-.26l.17-.007.172-.006.086-.003.171-.007A100 100 0 0 1 7.858 2zM6.4 5.209v4.818l4.157-2.408z"/><svg></a><a href="https://www.facebook.com/profile.php?id=61565154959875&sfnsn=wa&mibextid=RUbZ1f" style="color:#ffffff;background-color:Transparent;transition: transform 0.3s ease-in-out;"><svg xmlns="http://www.w3.org/2000/svg" width="35%" height="45" fill="currentColor" class="bi bi-facebook" viewBox="0 0 25 25"><path d="M16 8.049c0-4.446-3.582-8.05-8-8.05C3.58 0-.002 3.603-.002 8.05c0 4.017 2.926 7.347 6.75 7.951v-5.625h-2.03V8.05H6.75V6.275c0-2.017 1.195-3.131 3.022-3.131.876 0 1.791.157 1.791.157v1.98h-1.009c-.993 0-1.303.621-1.303 1.258v1.51h2.218l-.354 2.326H9.25V16c3.824-.604 6.75-3.934 6.75-7.951"/><svg></a></h4>', unsafe_allow_html=True)  
#st.write("###")
#st.markdown('''<div style="position: relative; width: 100%; height: 0; padding-top: 56.2225%;padding-bottom: 0; box-shadow: 0 0 0 0 ; margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden;border-radius: 8px; will-change: transform;"><iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"src="https://www.canva.com/design/DAGs7BmdSac/DQsAO4HxDHl4--BTkjHwkA/view?embed" ></iframe></div>''',unsafe_allow_html=True)
image,txt=st.columns((1,2))
with image:
     tn = Image.open("images/mthumbnail.webp")                             
     st.image(tn)
with txt:
     st.markdown("<h3 style='text-align: center; color: #00B0F0; font-weight:bold;'> ابحث عن أي جامعة أو اختصاص </h3>", unsafe_allow_html=True)          
     st.markdown("<h4 style='text-align: center; color: #000000;'> إن موقع مسار الجامعة مصمم لمساعدة الطلاب الذين تخرجوا من المرحلة الثانوية أو الطلاب الجامعيين الذين يريدون تغيير فرعهم الجامعي على اختيار الجامعة والاختصاص المناسبين لهم  </h4>", unsafe_allow_html=True)

st.write("---")
st.markdown("<h3 style='text-align: center; color: #00B0F0; font-weight:bold;'>يحتوي الموقع على جميع المعلومات التي يحتاجها الطالب</h3>", unsafe_allow_html=True)
st.write('<a href="application" target="_self" class="pagebutton" style="display: inherit;border-bottom: 2px solid #205090; border-radius:6px;background-image: linear-gradient(to right, #71C2FF, #A3C2EB); padding:12px; text-align: center; color:#ffffff; font-weight: bolder; font-size: 1.2rem; text-decoration: none; ">  شرح مفصل عن المفاضلة ‎ ‎<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-card-list" viewBox="0 0 20 20"><path d="M14.5 3a.5.5 0 0 1 .5.5v9a.5.5 0 0 1-.5.5h-13a.5.5 0 0 1-.5-.5v-9a.5.5 0 0 1 .5-.5zm-13-1A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h13a1.5 1.5 0 0 0 1.5-1.5v-9A1.5 1.5 0 0 0 14.5 2z"/><path d="M5 8a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7A.5.5 0 0 1 5 8m0-2.5a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7a.5.5 0 0 1-.5-.5m0 5a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7a.5.5 0 0 1-.5-.5m-1-5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0M4 8a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0m0 2.5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0"/><svg></a>' , unsafe_allow_html=True)
st.write('<a href="sp" target="_self" class="pagebutton" style="display: inherit;border-bottom: 2px solid #205090;border-radius:6px;background-image: linear-gradient(to right, #9BE5FF, #87cefa); padding:12px; text-align: center; color:#ffffff; font-weight: bolder; font-size: 1.2rem; text-decoration: none; "> شرح عن الاختصاصات الجامعية ‎ ‎<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-mortarboard-fill" viewBox="0 0 20 20"><path d="M8.211 2.047a.5.5 0 0 0-.422 0l-7.5 3.5a.5.5 0 0 0 .025.917l7.5 3a.5.5 0 0 0 .372 0L14 7.14V13a1 1 0 0 0-1 1v2h3v-2a1 1 0 0 0-1-1V6.739l.686-.275a.5.5 0 0 0 .025-.917z"/><path d="M4.176 9.032a.5.5 0 0 0-.656.327l-.5 1.7a.5.5 0 0 0 .294.605l4.5 1.8a.5.5 0 0 0 .372 0l4.5-1.8a.5.5 0 0 0 .294-.605l-.5-1.7a.5.5 0 0 0-.656-.327L8 10.466z"/><svg></a>', unsafe_allow_html=True)
st.write('<a href="universities" target="_self" class="pagebutton" style="display: inherit;border-bottom: 2px solid #205090;border-radius:6px;background-image: linear-gradient(to right, #9BE5FF, #A2E6E8); padding:12px; text-align: center; color:#ffffff; font-weight: bolder; font-size: 1.2rem; text-decoration: none; "> ترتيب الجامعات والأقساط الدراسية ‎ ‎<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-bank2" viewBox="0 0 20 20"><path d="M8.277.084a.5.5 0 0 0-.554 0l-7.5 5A.5.5 0 0 0 .5 6h1.875v7H1.5a.5.5 0 0 0 0 1h13a.5.5 0 1 0 0-1h-.875V6H15.5a.5.5 0 0 0 .277-.916zM12.375 6v7h-1.25V6zm-2.5 0v7h-1.25V6zm-2.5 0v7h-1.25V6zm-2.5 0v7h-1.25V6zM8 4a1 1 0 1 1 0-2 1 1 0 0 1 0 2M.5 15a.5.5 0 0 0 0 1h15a.5.5 0 1 0 0-1z"/><svg></a>', unsafe_allow_html=True)
st.write('<a href="majors" target="_self" class="pagebutton" style="display: inherit;border-bottom: 2px solid #205090;border-radius:6px;background-image: linear-gradient(to right, #A2E6E8, #99EBCA); padding:12px; text-align: center; color:#ffffff; font-weight: bolder; font-size: 1.2rem; text-decoration: none; "> أكواد المفاضلة وعلامات القبول‎ ‎<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-search" viewBox="0 0 20 20"><path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0"/><svg></a>', unsafe_allow_html=True)
st.write("---")
st.markdown("<h3 style='text-align: right; color: #00B0F0;font-weight:bold;'> للتواصل معنا</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: right; color: #000000;'>إن الموقع من تصميم وتطوير الطلاب حنا جون الخوري، بولص الخوري وأبي الزحيلي من فريق <a href='https://youtube.com/@college_path?si=WoMkxc9VCI4ON0wv?sub_confirmation=1' target='_blank' class='.st-emotion-cache-g2ydmt' style='padding:3px; text-align: centered; color:#00b0f0; font-weight: bolder; '>مسار الجامعة</a></h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: right; color: #000000;'>🙋🏻‍♂️ إذا كان لديكم أي استفسار، اقتراح أو تعليق نتمنى منكم ارساله لنا، رأيكم يهمنا</h4>", unsafe_allow_html=True)
contactform = """
<form action="https://formsubmit.co/contact.collegepath@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="الاسم" required>
     <input type="email" name="email" placeholder=" ادخل بريدك الإلكتروني لنتواصل معك" required>
     <textarea name="message" placeholder="..."></textarea>
     <button type="submit">ارسل</button>
</form>
"""
st.markdown(contactform, unsafe_allow_html=True)
def local_css(file_name):
     with open(file_name) as f:
          st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")
st.markdown("<h4 style='text-align: right; color: #000000;'> إذا تعرضتم لأي مشكلة أثناء الإرسال يمكنكم مراسلتنا مباشرة على الإيميل</h4>", unsafe_allow_html=True)
st.write("<a href='mailto:contact.collegepath@gmail.com' target='_blank' class='.st-emotion-cache-g2ydmt' style='padding:3px; text-align: right; color:#00B0F0; font-weight: bolder; font-weight: 600; font-size: 1.3rem; text-decoration: underline;'>Contact.CollegePath @gmail.com  </a>", unsafe_allow_html=True)   
st.write("###")