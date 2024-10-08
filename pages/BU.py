import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_option_menu import option_menu
from st_pages import hide_pages
icon = Image.open("images/cap.png")
st.set_page_config(page_title="College Path-جامعة البعث", page_icon=icon, layout= "wide")
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
        menu_title="جامعة البعث",
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
    gmap="""<p><iframe src="https://www.google.com/maps/d/embed?mid=1VvKTRQuX6GA7Xyu6lwC6N5ozXxVN2_o&ehbc=2E312F" width="100%" height="600" style="border:10;" allowfullscreen="True" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></p>"""
    st.markdown(gmap, unsafe_allow_html=True)
if select=="معلومات عن الجامعة":
    st.write("###")
    st.markdown("<h2 style='text-align: right; color: #00B0F0;'> جامعة البعث </h2>" , unsafe_allow_html=True)
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
            image=Image.open("pictures/BU.jpg")
            st.image(image)
        with r:
            st.write("<a href='https://albaath-univ.edu.sy/' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'> الموقع الإلكتروني🌐 </a>", unsafe_allow_html=True)
            st.write("<a href='https://www.google.com/maps/place/Al-Baath+University/@34.7129276,36.7096507,17z/data=!3m1!4b1!4m6!3m5!1s0x15230f242ef1d967:0xf24891cf451be34b!8m2!3d34.7129276!4d36.7096507!16s%2Fm%2F025x90j?entry=ttu' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'> الموقع على الخريطة🗺  </a>", unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> نوع الجامعة : حكومية </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> ترتيب الجامعة على سوريا حسب ويبوميتريكس : 5 </h5>" , unsafe_allow_html=True)
        st.write("---")
        st.markdown("<h2 style='text-align: right; color: #00B0F0;'> نبذة عن الجامعة </h2>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> جامعة البعث جامعة سورية تأسست في مدينة حمص عام 1979 ، ويدرس بالجامعة أكثر من مئة ألف طالب تحت إشراف أكثر من 14000 مدرس </h5>" , unsafe_allow_html=True)  
        st.write("---")
        st.markdown("<h2 style='text-align: right; color: #00B0F0;'> صفحات الجامعة على مواقع التواصل </h2>" , unsafe_allow_html=True)
        st.write("<a href='https://www.youtube.com/channel/UCWOUcHbLZwTuc8ezXMRvgcw' style='text-align: right; color: #f02020; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>  YouTube-يوتيوب 🟥 </a>", unsafe_allow_html=True)
        st.write("<a href='https://www.facebook.com/albaathunivweb' style='text-align: right; color: #0030f0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>  Facebook-فيسبوك 🟦 </a>", unsafe_allow_html=True)
        st.write("<a href='https://twitter.com/albaathunivweb' style='text-align: right; color: #020209; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>  X (Twitter) - إكس (تويتر) ✖ </a>", unsafe_allow_html=True)
    if selectuni=="الرسوم الدراسية":
        st.markdown("<h2 style='text-align: right; color: #00B0F0;'> للطلاب السوريين المقيمين ومن بحكمهم </h2>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> لا يوجد أي رسوم دراسية للطلاب المقبولين وفق التعليم العام </h5>" , unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: right; color: #0070C0;'>  الرسوم السنوية للخدمات الجامعية بالقبول الموازي  </h3>" , unsafe_allow_html=True)
        image=Image.open("pictures/paraedu.png")
        st.image(image)
        st.markdown("<h3 style='text-align: right; color: #0070C0;'>  وللمعاهد حسب القبول الموازي </h3>" , unsafe_allow_html=True)
        image=Image.open("pictures/paraedu1.png")
        st.image(image)
        st.markdown("<h3 style='text-align: right; color: #00B0F0;'> تكاليف المواصلات 🚌</h3>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> بين 60 و180 ألف ليرة سورية شهرياً باستخدام وسائل النقل العامة حسب البعد عن الكلية </h5>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> بين 100 و500 ألف ليرة سورية شهرياً باستخدام وسائل نقل خاصة أو بالاتفاق مع سائق حافلة أو أجرة حسب البعد عن الكلية </h5>" , unsafe_allow_html=True)
        st.write("---")
        st.markdown("<h2 style='text-align: right; color: #00B0F0;'> للطلاب السوريين ومن بحكمهم الحاصلين على شهادة ثانوية غير سورية </h2>" , unsafe_allow_html=True)
        image=Image.open("pictures/f1.jpg")
        st.image(image)
        st.write("---")
        st.markdown("<h2 style='text-align: right; color: #00B0F0;'> للطلاب العرب و الأجانب </h2>" , unsafe_allow_html=True)
        image=Image.open("pictures/f2.jpg")
        st.image(image)
    if selectuni=="المنشآت التابعة":
        llc,rrc=st.columns(2)
        with llc:
            st.markdown("<h3 style='text-align: right; color: #00B0F0;'> السكن الجامعي </h3>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> تكلفة السكن الجامعي(2023): 80ألف ليرة سورية سنوياً  </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> ميزات وخصائص السكن الجامعي: كهرباء دائمة وإنترنت مجاني </h5>" , unsafe_allow_html=True)
        with rrc:    
            st.markdown("<h3 style='text-align: right; color: #00B0F0;'> المشافي الجامعية </h3>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'>مستشفى جامعة البعث</h5>" , unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: right; color: #00B0F0;'> المعاهد التابعة </h3>" , unsafe_allow_html=True)
        il,ir=st.columns(2)
        with il:
            st.markdown("<h4 style='text-align: right; color: #0070C0;'>: المعاهد العليا </h4>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد العالي للغات </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد العالي لإدارة المياه </h5>" , unsafe_allow_html=True)
            
        with ir:
            st.markdown("<h4 style='text-align: right; color: #0070C0;'>: المعاهد المتوسطة </h4>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد التقاني الزراعي </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد التقاني لشؤون البادية والتصحر </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد التقاني الهندسي </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد التقاني للحاسوب </h5>" , unsafe_allow_html=True)
    if selectuni=="كليات الجامعة":
        font="""
        <style>
        html {{
        font-size: larger;
        }}
        </style>
        """
        st.markdown("<h3 style='text-align: right; color: #0070c0;'>: العلوم الطبية والصحية </h3>" , unsafe_allow_html=True)
        st.markdown(font, unsafe_allow_html=True)
        st.write("""  
        \nكلية الطب
\nكلية طب الأسنان
\nكلية الصيدلة
\nكلية التمريض
\nكلية العلوم الصحية
                        
        """)
        st.markdown("<h3 style='text-align: right; color: #0070c0;'>: العلوم الهندسية </h3>" , unsafe_allow_html=True)
        st.write("""
    \nكلية الهندسة المدنية
\nكلية الهندسة الميكانيكية والكهربائية
\nكلية الهندسة المعمارية
\nكلية الهندسة المعلوماتية
\nكلية الهندسة التطبيقة
                 \nكلية الهندسة الكيميائية والبترولية
                 \nكلية الزراعة
    """)
        st.markdown("<h3 style='text-align: right; color: #0070c0;'>: العلوم الإنسانية </h3>" , unsafe_allow_html=True)
        st.write("""
    \nكلية الآداب والعلوم الإنسانية
\nكلية التربية
\nكلية التربية(تدمر)
\nكلية الحقوق
\nكلية السياحة
\nكلية التربية الموسيقية
    """) 
        st.markdown("<h3 style='text-align: right; color: #0070c0;'>: العلوم الأساسية </h3>" , unsafe_allow_html=True)
        st.write("""
    \nكلية العلوم (حمص)
     \nكلية العلوم (تدمر)
    """) 
        st.markdown("<h3 style='text-align: right; color: #0070c0;'> كلية الاقتصاد </h3>" , unsafe_allow_html=True)  