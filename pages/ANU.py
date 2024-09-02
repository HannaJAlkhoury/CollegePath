import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from st_pages import hide_pages
from openpyxl import load_workbook
icon = Image.open("images/cap.png")
st.set_page_config(page_title="College Path- جامعة الأندلس", page_icon=icon, layout= "wide")
def cost(unicost):
    for costs in unicost:
        if len(costs)==5:  
            st.markdown("<h4 style='text-align: right; color: #0070c0;'>"+ costs[0] +"</h4>" , unsafe_allow_html=True) 
            st.markdown("<h5 style='text-align: right; color: #000000;'> رسم الساعة المعتمد للسوريين المقيمين ومن بحكمهم:"+ costs[1] +" ليرة سورية</h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'>الحد الأعلى لرسم السنة الدراسية:"+ costs[2] +" ليرة سورية </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> للسوريين غير المقيمين:"+ costs[3] +" دولار أمريكي </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> للعرب والأجانب :"+ costs[4] +" دولار أمريكي </h5>" , unsafe_allow_html=True)
        if len(costs)==3:  
            st.markdown("<h4 style='text-align: right; color: #0070c0;'>"+ costs[0] +"</h4>" , unsafe_allow_html=True) 
            st.markdown("<h5 style='text-align: right; color: #000000;'> رسم الساعة المعتمد للسوريين المقيمين ومن بحكمهم:"+ costs[1] +" ليرة سورية </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'>الحد الأعلى لرسم السنة الدراسية:"+ costs[2] +" ليرة سورية </h5>" , unsafe_allow_html=True)
        if len(costs)==2:
            st.markdown("<h4 style='text-align: right; color: #0070c0;'>"+ costs[0] +"</h4>" , unsafe_allow_html=True) 
            st.markdown("<h5 style='text-align: right; color: #000000;'> رسم الساعة المعتمد للسوريين المقيمين ومن بحكمهم:"+ costs[1] +" ليرة سورية </h5>" , unsafe_allow_html=True)
    return
hide_pages(["AAST","sp","majors","universities","application","DU","DU", "Website", "AU",'ANTU','MU','QAU','ASPU','EBU','HPU','ANU','ANU','JU','AUST','SU','IU','CU','WPU','YU','RU','WU','IUST','SPU','AIU','KU','HU','SVU','EU','TU','TAU','BU','HIAST'])
Page_header=f"""
<style> 
.st-emotion-cache-hsmt6w{{
background-color:#ffffff;
color:#0070c0;
font-weight:bolder;
}}
a{{
color:#000000;
text-decoration:none;
}}
body {{
    text-align: right;
}}
[data-testid="stHeader"] {{
background-color: #0070C0;
height:3.5rem;
}}
.css-fblp2m {{
color: #0070C0;
font-size: 2rem;
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
hr{{
margin-top:0;
}}
.css-grcmwr{{
gap:0;
}}
h2{{
padding-top:0rem;
}}
.css-1kyxreq{{
justify-content:center;
}}
button[title="View fullscreen"]{{
visibility: hidden;}}
.css-z5fcl4 {{
    width: 100%;
    padding: 4rem 2rem 2rem;}}
    .st-emotion-cache-z5fcl4 {{
    width: 100%;
    padding: 1rem 6% 3rem;
    }}
    #MainMenu {{visibility: hidden;}}
footer {{visibility: hidden;}}
.st-emotion-cache-17wpp4c{{border-bottom: 1px solid rgb(60 55 143 / 0%);}}
.st-emotion-cache-1dgmtll svg {{
    stroke: transparent;
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
</style>"""
st.markdown(Page_header, unsafe_allow_html=True)
with st.sidebar:
    logo = Image.open("images/logo.png")
    st.image(logo)
    st.write("###")
    select = option_menu(
        menu_icon="bank2",
        menu_title="جامعة الأندلس",
        options=["معلومات عن الجامعة", "على الخريطة"],
        icons=["mortarboard","globe-europe-africa"],
        default_index=0,
        key=None,
        styles={"nav-link": {"--hover-color": "#ACD3FE"},}          
    )
    st.write("<a href='javascript:window.top.close();' target='_self' class='.st-emotion-cache-g2ydmt' style='border: 1px solid transparent; border-radius:5px; padding:5px; text-align: centered; color:#ffffff; font-weight: 400; font-size: 1rem; text-decoration: none; background-color:transparent; padding-width:100%;'><svg xmlns='http://www.w3.org/2000/svg' width='40' height='40' fill='currentColor' class='bi bi-house-door-fill' viewBox='0 0 34 34'><path d='M6.5 14.5v-3.505c0-.245.25-.495.5-.495h2c.25 0 .5.25.5.5v3.5a.5.5 0 0 0 .5.5h4a.5.5 0 0 0 .5-.5v-7a.5.5 0 0 0-.146-.354L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.354 1.146a.5.5 0 0 0-.708 0l-6 6A.5.5 0 0 0 1.5 7.5v7a.5.5 0 0 0 .5.5h4a.5.5 0 0 0 .5-.5'/><svg></a>", unsafe_allow_html=True)
if select=="على الخريطة":
    st.write("###")
    st.markdown("<h2 style='text-align: right; color: #00B0F0;'>🗺 على الخريطة</h2>" , unsafe_allow_html=True)
    st.write("###")
    gmap="""<p><iframe src="https://www.google.com/maps/d/embed?mid=1KLk-PEAaOKGkDvqTCisV5A-PjowU7Oo&ehbc=2E312F" width="100%" height="600" style="border:10;" allowfullscreen="True" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></p>"""
    st.markdown(gmap, unsafe_allow_html=True)
if select=="معلومات عن الجامعة":
    st.write("###")
    st.markdown("<h2 style='text-align: right; color: #00B0F0;'> جامعة الأندلس للعلوم الطبية </h2>" , unsafe_allow_html=True)
    st.write("###")
    selectuni = option_menu(
          menu_icon=None,
          menu_title=None,
          options=["المنشآت التابعة","الرسوم الدراسية","كليات الجامعة","نظرة عامة"],
          icons=["houses","coin","bank","stack-overflow"],
          default_index=3,
          orientation="horizontal",
          styles={
        "container": {"padding": "0!important", "background-color": "#eee"},
        "icon": {"font-size": "18px"}, 
        "nav-link": {"font-size": "18px", "text-align": "center", "margin":"0px", "--hover-color": "#ACD3FE"},
        "nav-link-selected": {"background-color": "00B0F0"},
    }
    )
    st.write("---")
    if selectuni=="نظرة عامة":
        l,r= st.columns(2)
        with l:
            image=Image.open("pictures/ANU.jpeg")
            st.image(image)
        with r:
            st.write("<a href='https://au.edu.sy/ar/home' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'> الموقع الإلكتروني🌐 </a>", unsafe_allow_html=True)
            st.write("<a href='https://www.google.com/maps/place/Al+Andalus+University+for+Medical+Sciences/@35.09785,36.182429,16.25z/data=!4m6!3m5!1s0x1523ec0f8ecef327:0xcd3c39c5aae06c64!8m2!3d35.0985634!4d36.1875486!16s%2Fm%2F043lk3t?authuser=0&entry=ttu' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'> الموقع على الخريطة🗺  </a>", unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> نوع الجامعة : خاصة </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> ترتيب الجامعة على سوريا حسب ويبوميتريكس : 8 </h5>" , unsafe_allow_html=True)
        st.write("---")
        st.markdown("<h2 style='text-align: right; color: #00B0F0;'> نبذة عن الجامعة </h2>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> جامعة الاندلس الخاصة للعلوم الطبية هي جامعة سورية خاصة إنشئت من قبل مجموعة من الأطباء السوريين في المهجر. تقع في بلدة القدموس الواقعة في محافظة طرطوس على توسط بين محافظتي طرطوس واللاذقية. تأسست عام 2005 </h5>" , unsafe_allow_html=True)  
        st.write("---")
        st.markdown("<h2 style='text-align: right; color: #00B0F0;'> صفحات الجامعة على مواقع التواصل </h2>" , unsafe_allow_html=True)
        st.write("<a href='https://www.youtube.com/channel/UC60hB8rKV6kHckJZioIJicQ' style='text-align: right; color: #f02020; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>  YouTube-يوتيوب 🟥 </a>", unsafe_allow_html=True)
        st.write("<a href='https://www.facebook.com/andalusuni.ms' style='text-align: right; color: #0030f0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>  Facebook-فيسبوك 🟦 </a>", unsafe_allow_html=True)
        st.write("<a href='https://t.me/AndalusUni' style='text-align: right; color: #0090e0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>  Telegram-تيليغرام 🔷 </a>", unsafe_allow_html=True)
    if selectuni=="الرسوم الدراسية":
        st.markdown("<h3 style='text-align: right; color: #0070c0;'> أقساط الجامعة </h3>" , unsafe_allow_html=True)
        fees=load_workbook('c:/cp/tuition.xlsx')
        activefees=fees.active
        counter=1
        allfees=[]
        for loop in range(30):
            row=activefees[str(counter)]
            counter=counter+1
            l=[]
            for item in row:
                if item.value==".":
                        value=''
                else:
                        value=item.value
                        l.append(value)
            allfees.append(l)
        list=[]
        majors=["طب الأسنان","الصيدلة","الطب البشري","إدارة المشافي","التمريض","الهندسة الطبية"]
        for major in allfees:
            if major[0] in majors:
                list.append(major)
        cost(list)
        st.markdown("<h3 style='text-align: right; color: #00B0F0;'>(3/2024) تكاليف المواصلات 🚌</h3>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> بين 78 و280 ألف ليرة سورية شهرياً باستخدام وسائل النقل العامة حسب البعد عن الكلية </h5>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> بين 300 و800 ألف ليرة سورية شهرياً باستخدام وسائل نقل خاصة </h5>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> نقل الجامعة الرسمي يختلف حسب محافظة الإقامة </h5>" , unsafe_allow_html=True)
        st.write("<a href='https://au.edu.sy/ar/Transport' style='text-align: right; color: #0090e0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'> للمزيد من المعلومات </a>", unsafe_allow_html=True)    
    if selectuni=="المنشآت التابعة": 
        st.markdown("<h3 style='text-align: right; color: #00B0F0;'> المشافي الجامعية </h3>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'>مستشفى الأندلس</h5>" , unsafe_allow_html=True)
    if selectuni=="كليات الجامعة":
        font="""
        <style>
        html {{
        font-size: larger;
        }}
        </style>
        """
        st.markdown("<h4 style='text-align: right; color: #000000;'> كلية الطب البشري </h4>" , unsafe_allow_html=True) 
        st.markdown("<h4 style='text-align: right; color: #000000;'> كلية طب الأسنان </h4>" , unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: right; color: #000000;'> كلية الصيدلة </h4>" , unsafe_allow_html=True) 
        st.markdown("<h4 style='text-align: right; color: #000000;'> كلية الهندسة الطبية </h4>" , unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: right; color: #000000;'> كلية التمريض </h4>" , unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: right; color: #000000;'> كلية إدارة المشافي </h4>" , unsafe_allow_html=True)