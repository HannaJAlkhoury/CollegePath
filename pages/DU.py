import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from st_pages import hide_pages
icon = Image.open("images/cap.png")
st.set_page_config(page_title="College Path-جامعة دمشق", page_icon=icon, layout= "wide")
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
        menu_title="جامعة دمشق",
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
    gmap="""<p><iframe src="https://www.google.com/maps/d/embed?mid=16fl7NM0hOSxyUKijMvaSHefDatd9EAM&ehbc=2E312F" width="100%" height="600" style="border:10;" allowfullscreen="True" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></p>"""
    st.markdown(gmap, unsafe_allow_html=True)
if select=="معلومات عن الجامعة":
    st.write("###")
    st.markdown("<h2 style='text-align: right; color: #00B0F0;'> جامعة دمشق </h2>" , unsafe_allow_html=True)
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
            image=Image.open("pictures/DU.jpg")
            st.image(image)
        with r:
            st.write("<a href='https://www.damascusuniversity.edu.sy/' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'> الموقع الإلكتروني🌐 </a>", unsafe_allow_html=True)
            st.write("<a href='https://www.google.com/maps/place/Damascus+University/@33.5106105,36.2881338,17z/data=!3m1!4b1!4m6!3m5!1s0x1518e73351b783c3:0x81aba1f4d3154d23!8m2!3d33.5106105!4d36.2881338!16zL20vMDdwbnc2?entry=ttu' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'> الموقع على الخريطة🗺  </a>", unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> نوع الجامعة : حكومية </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> ترتيب الجامعة على سوريا حسب ويبوميتريكس : 1 </h5>" , unsafe_allow_html=True)        
        st.write("---")
        st.markdown("<h2 style='text-align: right; color: #00B0F0;'> نبذة عن الجامعة </h2>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> جامعة دمشق هي أقدم وأكبر جامعة في الجمهورية العربية السورية، تقع في العاصمة دمشق ولديها فروع في بعض المحافظات الأخرى، تعد أول جامعة حكومية في الوطن العربي. ترجع نواتها الأولى إلى العام 1903 من خلال المدرسة الطبية بفرعيها الطب البشري والصيدلة. في العام 1923 تم دمج المدرسة الطبية مع مدرسة الحقوق (التي أسست عام 1913) لتكوين الجامعة السورية. وبقيت تحمل ذاك الاسم حتى عام 1958 حيث أصبحت تدعى جامعة دمشق. </h5>" , unsafe_allow_html=True)  
        st.write("---")
        st.markdown("<h2 style='text-align: right; color: #00B0F0;'> صفحات الجامعة على مواقع التواصل </h2>" , unsafe_allow_html=True)
        st.write("<a href='https://youtube.com/@damascusuniv?si=1sfJv7Oztd0_lgfb' style='text-align: right; color: #f02020; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>  YouTube-يوتيوب 🟥 </a>", unsafe_allow_html=True)
        st.write("<a href='https://www.facebook.com/Damas.University' style='text-align: right; color: #0030f0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>  Facebook-فيسبوك 🟦 </a>", unsafe_allow_html=True)
        st.write("<a href='https://www.instagram.com/damasuniv/' style='text-align: right; color: #d0d010; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>  Instagram-إنستاغرام 🟨 </a>", unsafe_allow_html=True)
        st.write("<a href='https://t.me/damascus122021' style='text-align: right; color: #0090e0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>  Telegram-تيليغرام 🔷 </a>", unsafe_allow_html=True)
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
            st.markdown("<h5 style='text-align: right; color: #000000;'> تكلفة السكن الجامعي(2023): 80ألف ليرة سورية سنواً  </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> ميزات وخصائص السكن الجامعي: كهرباء دائمة وإنترنت مجاني </h5>" , unsafe_allow_html=True)
        with rrc:    
            st.markdown("<h3 style='text-align: right; color: #00B0F0;'> المشافي الجامعية </h3>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> مستشفى جراحة القلب الجامعي</h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> مشفى جراحة الفم والفكين</h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'>مستشفى الأسد الجامعي</h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'>مستشفى المواساة الجامعي</h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> مشفى جراحة الفم والفكين </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'>مستشفى التوليد وأمراض النساء</h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'>  مستشفى البيروني </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> مستشفى الأمراض الجلدية والزهرية </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> مشفى الأطفال الجامعي </h5>" , unsafe_allow_html=True)
            st.markdown("<h3 style='text-align: right; color: #00B0F0;'> المعاهد التابعة </h3>" , unsafe_allow_html=True)
        il,ir=st.columns(2)
        with il:
            st.markdown("<h4 style='text-align: right; color: #0070C0;'>: المعاهد العليا </h4>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد العالي للتخطيط الاقليمي </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد العالي للغات </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد العالي للتنمية الادارية </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد العالي لبحوث الليزر وتطبيقاته </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد العالي للدراسات والبحوث الزلزالية </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد العالي للترجمة والترجمة الفورية </h5>" , unsafe_allow_html=True)
            
        with ir:
            st.markdown("<h4 style='text-align: right; color: #0070C0;'>: المعاهد التقانية </h4>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد التقاني للعلوم المالية والمصرفية </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد التقاني لإدارة الأعمال والتسويق </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد التقاني الزراعي </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد التقاني للهندسة الميكانيكية والكهربائية </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد التقاني الطبي </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'>  المعهد التقاني لطب الأسنان </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد التقاني الهندسي </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد التقاني للحاسوب </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد التقاني الزراعي بدرعا </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد التقاني للعلوم المالية والمصرفية بدرعا </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد التقاني الطبي بالنبك </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد التقاني الزراعي بالسويداء </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد التقاني الزراعي بالقنيطرة </h5>" , unsafe_allow_html=True)
    if selectuni=="كليات الجامعة":
        font="""
        <style>
        html {{
        font-size: larger;
        }}
        </style>
        """
        st.markdown("<h3 style='text-align: right; color: #0070c0;'>: جامعة دمشق </h3>" , unsafe_allow_html=True)
        st.markdown(font, unsafe_allow_html=True)
        st.write("""  
        \n• كلية الآداب والعلوم الانسانية
\n• كلية الإعلام
\n• كلية الاقتصاد
\n• كلية التربية
\n• كلية الحقوق
\n• كلية الهندسة الزراعية
\n• كلية السياحة
\n• كلية الشريعة
\n• كلية العلوم الصحية
\n• كلية الصيدلة
\n• كلية الطب البشري
\n• كلية طب الأسنان
\n• كلية العلوم
\n• كلية العلوم السياسية
\n• كلية الفنون الجميلة
\n• كلية الهندسة المدنية
\n• كلية الهندسة المعلوماتية
\n• كلية الهندسة المعمارية
\n• كلية الهندسة الميكانيكية والكهربائية
\n• الكلية التطبيقية
                        
        """)
        st.markdown("<h3 style='text-align: right; color: #0070c0;'>: فرع درعا </h3>" , unsafe_allow_html=True)
        st.write("""
    \n• التربية الثالثة
    \n• الآداب الثالثة
    \n• الحقوق الثانية
    \n• الاقتصاد الثانية
    \n• الطب البيطري
    \n• العلوم الثانية
    """)
        st.markdown("<h3 style='text-align: right; color: #0070c0;'>: فرع السويداء </h3>" , unsafe_allow_html=True)
        st.write("""
    \n• الآداب والعلوم الانسانية الثانية
    \n• التربية الثانية
    \n• الزراعة الثانية
    \n• الفنون الجميلة الثانية
    \n• العلوم الرابعة
    \n• الهندسة الميكانيكية والكهربائية الثانية
    \n• كلية الاقتصاد الرابعة

    """) 
        st.markdown("<h3 style='text-align: right; color: #0070c0;'>: فرع القنيطرة </h3>" , unsafe_allow_html=True)
        st.write("""
    \n• التربية الرابعة
    \n• الاقتصاد الثالثة
    \n• الآداب والعلوم الانسانية الرابعة
    \n• الحقوق الثالثة
    \n• العلوم الثالثة
    """)   