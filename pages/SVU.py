import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from st_pages import hide_pages
icon = Image.open("images/cap.png")
st.set_page_config(page_title="College Path-الجامعة السورية الافتراضية", page_icon=icon, layout= "wide")
hide_pages(["AAST","sp","majors","universities","application","DU", "Website", "AU",'ANTU','MU','QAU','ASPU','EBU','HPU','ANU','ANU','JU','AUST','SU','IU','CU','WPU','YU','RU','WU','IUST','SPU','AIU','KU','HU','SVU','EU','TU','TAU','BU','HIAST'])
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
.st-emotion-cache-0{{
     align-items: flex-end;
    display: flex;
    flex-direction: row-reverse;
    align-content: stretch;
    flex-wrap: wrap;
    justify-content: space-evenly;
}}
.st-emotion-cache-yp5fhh{{background-color:#FFFFFF;}}
.st-emotion-cache-9hz7ad p{{text-align: end;}}
a:hover{{background-color:#E0FFFF;}}
h1,h2,h3,h4,h5,h6{{direction: rtl}}
"""
textwrap=f"""
.st-emotion-cache-1lvxfs7{{
    word-break: auto-phrase;
        text-wrap: auto
}}
"""
st.markdown("<style>"+textwrap+Page_header+hide_img_fs+SidebarStyle+"</style>",unsafe_allow_html=True)
with st.sidebar:
    logo = Image.open("images/logo.png")
    st.image(logo)
    st.write("###")
    select = option_menu(
        menu_icon="bank2",
        menu_title="الجامعة السورية الافتراضي",
        options=["معلومات عن الجامعة", "على الخريطة"],
        icons=["mortarboard","globe-europe-africa"],
        default_index=0,
        key=None,
        styles={"nav-link": {"--hover-color": "#ACD3FE"},}          
    )
    st.write("<a href='javascript:window.top.close();' target='_self' class='.st-emotion-cache-g2ydmt' style='border: 1px solid transparent; border-radius:5px; padding:5px; text-align: centered; color:#ffffff; font-weight: 400; font-size: 1rem; text-decoration: none; background-color:transparent; padding-width:100%;'><svg xmlns='http://www.w3.org/2000/svg' width='40' height='40' fill='currentColor' class='bi bi-house-door-fill' viewBox='0 0 34 34'><path d='M6.5 14.5v-3.505c0-.245.25-.495.5-.495h2c.25 0 .5.25.5.5v3.5a.5.5 0 0 0 .5.5h4a.5.5 0 0 0 .5-.5v-7a.5.5 0 0 0-.146-.354L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.354 1.146a.5.5 0 0 0-.708 0l-6 6A.5.5 0 0 0 1.5 7.5v7a.5.5 0 0 0 .5.5h4a.5.5 0 0 0 .5-.5'/><svg></a>", unsafe_allow_html=True)
if select=="معلومات عن الجامعة":
    st.write("###")
    st.markdown("<h2 style='text-align: right; color: #00B0F0;'>الجامعة السورية الافتراضي</h2>" , unsafe_allow_html=True)
    st.write("###")
    selectuni = option_menu(
          menu_icon=None,
          menu_title=None,
          options=["المنشآت التابعة","الرسوم الدراسية","اختصاصات الجامعة","نظرة عامة"],
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
            image=Image.open("pictures/SVU.jpg")
            st.image(image)
        with r:
            st.write("<a href='https://svuonline.org/ar' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'> الموقع الإلكتروني🌐 </a>", unsafe_allow_html=True)
            st.write("<a href='https://www.google.com/maps/place/Syrian+Virtual+University/@33.5113781,36.2731257,17z/data=!3m1!4b1!4m6!3m5!1s0x1518e0ae102ae53d:0xdec26d70f4423ce9!8m2!3d33.5113781!4d36.2731257!16zL20vMGQ0bHZk?entry=ttu' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'> موقع رئاسة الجامعة على الخريطة🗺  </a>", unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> نوع الجامعة : حكومية افتراضية </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> ترتيب الجامعة على العالم حسب ويبوميتريكس : 7113 </h5>" , unsafe_allow_html=True)
        st.write("---")
        st.markdown("<h2 style='text-align: right; color: #00B0F0;'> نبذة عن الجامعة </h2>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> الجامعة الافتراضية السوريّة هي جامعة افتراضية افتُتحت في 2 سبتمبر عام 2002. تأسست الجامعة الافتراضية السورية، التي كانت السباقة إلى اعتماد التعليم الافتراضي في الشرق الأوسط، بقرار من وزارة التعليم العالي السورية، والتي تهدف إلى توفير تعليم من مستوى عالمي للطلبة السوريين في بلدهم، يشمل كافة القطاعات المهنية المتوفرة حالياً </h5>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #00B0f0;'> التدريس في الجامعة يتم عبر الإنترنت لكن يتم تقديم الامتحانات في مراكز مختصة على الطالب التواجد فيها لتقديم الامتحان </h5>" , unsafe_allow_html=True)  
        st.write("---")
        st.markdown("<h2 style='text-align: right; color: #00B0F0;'> صفحات الجامعة على مواقع التواصل </h2>" , unsafe_allow_html=True)
        st.write("<a href='https://www.youtube.com/channel/UCJwPgp0tOp1ZqkzbmDvFSaw' style='text-align: right; color: #f02020; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>  YouTube-يوتيوب 🟥 </a>", unsafe_allow_html=True)
        st.write("<a href='https://www.facebook.com/svuonline.org' style='text-align: right; color: #0030f0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>  Facebook-فيسبوك 🟦 </a>", unsafe_allow_html=True)
        st.write("<a href='http://instagram.com/syrian_virtual_university' style='text-align: right; color: #d0d010; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>  Instagram-إنستاغرام 🟨 </a>", unsafe_allow_html=True)
        st.write("<a href='https://www.linkedin.com/company/syrianvirtualuniversity' style='text-align: right; color: #0010d0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>  LinkedIN-لينكدإن 🔷 </a>", unsafe_allow_html=True)
        st.write("<a href='https://twitter.com/SVU_Syria' style='text-align: right; color: #020209; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>  X (Twitter) - إكس (تويتر) ✖ </a>", unsafe_allow_html=True)
    if selectuni=="الرسوم الدراسية":
        st.markdown("<h3 style='text-align: right; color: #0070C0;'>: نظام الرسوم الدراسية </h3>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'>تتبع الجامعة الافتراضية نظام أقساط المواد بحسب الفصل حيث أنه يترتب على الطالب اختيار المواد التي يدرسها خلال الفصل وتفرض عليه رسوم بحسب عدد المواد المختارة</h5>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> الجامعة الافتراضية مأجورة كلياً حيث يترتب على كل الطلاب المسجلين دفع الرسوم الدراسية إلا إذا استطاع الطالب الحصول على منحة ولرؤية إذا كنت مؤهلاً يرجى قرائة الفقرات من الصفحة 23 إلى الصفحة 26 من الملف أدناه </h5>" , unsafe_allow_html=True)
        with open("SVU.pdf", "rb") as pdf_file1:
                         PDFbyte1 = pdf_file1.read()
                         st.download_button(label=" اضغط لتنزيل دليل الطالب ",
                         data=PDFbyte1,
                         file_name="SVU.pdf",
                         mime='application/octet-stream')
        st.markdown("<h3 style='text-align: right; color: #0070C0;'>: اللرسوم الدراسية </h3>" , unsafe_allow_html=True)
        image=Image.open("pictures/SVUcost.png")
        st.image(image)
    if selectuni=="المنشآت التابعة":
        llc,rrc=st.columns(2)
        st.markdown("<h3 style='text-align: right; color: #00B0F0;'> المعاهد التابعة </h3>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد التقاني لإدارة الأعمال  </h5>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد التقاني  للعلوم السياحية والفندقية </h5>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> المعهد التقاني للحاسوب </h5>" , unsafe_allow_html=True)
    if selectuni=="اختصاصات الجامعة":
        font="""
        <style>
        html {{
        font-size: larger;
        }}
        </style>
        """
        st.markdown("<h3 style='text-align: right; color: #0070c0;'>: كلية المعلوماتية والاتصالات</h3>" , unsafe_allow_html=True)
        st.markdown(font, unsafe_allow_html=True)
        st.write("""  
\nالهندسة المعلوماتية
\n تقانة الاتصالات
\n تقانة المعلومات                        
        """)
        st.markdown("<h3 style='text-align: right; color: #0070c0;'>: كلية العلوم الإدارية </h3>" , unsafe_allow_html=True)
        st.write("""
\n    علوم الإدارة
    """)
        st.markdown("<h3 style='text-align: right; color: #0070c0;'>: كلية العلوم الإنسانية </h3>" , unsafe_allow_html=True)
        st.write("""
\n الحقوق
\n الإعلام والاتصالات
    """) 