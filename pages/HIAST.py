import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from st_pages import hide_pages
icon = Image.open("images/cap.png")
st.set_page_config(page_title="College Path- HIAST", page_icon=icon, layout= "wide")
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
        menu_title="HIAST",
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
    gmap="""<p><iframe src="https://www.google.com/maps/d/embed?mid=1eWCXgVxTIfgNY3r9lqWyULKHP9i2Aho&ehbc=2E312F" width="100%" height="600" style="border:10;" allowfullscreen="True" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></p>"""
    st.markdown(gmap, unsafe_allow_html=True)
if select=="معلومات عن الجامعة":
    st.write("###")
    st.markdown("<h2 style='text-align: right; color: #00B0F0;'>المعهد العالي للعلوم التطبيقية والتكنولوجيا</h2>" , unsafe_allow_html=True)
    st.write("###")
    selectuni = option_menu(
          menu_icon=None,
          menu_title=None,
          options=["المنشآت التابعة","الرسوم الدراسية"," أقسام المعهد","نظرة عامة"],
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
            image=Image.open("pictures/HIAST.jpg")
            st.image(image)
        with r:
            st.write("<a href='https://hiast.edu.sy/ar' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'> الموقع الإلكتروني🌐 </a>", unsafe_allow_html=True)
            st.write("<a href='https://www.google.com/maps/place/H837%2BMP9+%D8%A7%D9%84%D9%85%D8%B9%D9%87%D8%AF+%D8%A7%D9%84%D8%B9%D8%A7%D9%84%D9%8A+%D9%84%D9%84%D8%B9%D9%84%D9%88%D9%85+%D8%A7%D9%84%D8%AA%D8%B7%D8%A8%D9%8A%D9%82%D9%8A%D8%A9+%D9%88+%D8%A7%D9%84%D8%AA%D9%83%D9%86%D9%88%D9%84%D9%88%D8%AC%D9%8A%D8%A7%D8%8C+%D8%AF%D9%85%D8%B4%D9%82%D8%8C+%D8%B3%D9%88%D8%B1%D9%8A%D8%A7%E2%80%AD/data=!4m2!3m1!1s0x1518e64f44af2a5b:0x894ad92a83899b79?utm_source=mstt_1&entry=gps&lucs=,47075915,47084387&g_ep=CAESCjExLjExNi4xMDEYACDXggMqEiw0NzA3NTkxNSw0NzA4NDM4N0ICU1k%3D' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'> الموقع على الخريطة🗺  </a>", unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> نوع الجامعة : حكومية </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> ترتيب الجامعة على العالم حسب ويبوميتريكس : 6102 </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #00b0f0;'> للمعهد مفاضلته الخاصة ولا يتبع للمفاضلة العامة لوزارة التعليم العالي وقد يتطلب امتحان قبول </h5>" , unsafe_allow_html=True)
        st.write("---")
        st.markdown("<h2 style='text-align: right; color: #00B0F0;'> نبذة عن الجامعة </h2>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> تأسس المعهد العالي للعلوم التطبيقيّة والتكنولوجيا عام 1983. يهدف المعهد إلى إعداد أطر مؤهّلة للبحث العلمي والتقاني في جميع ميادين العلوم التطبيقيّة والتكنولوجيا </h5>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> مدة الدراسة في المعهد العالي  خمس سنوات، يحصل بعدها الطالب على درجة الإجازة في الهندسة (بكلوريوس في الهندسة) وهي شهادة تعادل أي شهادة أخرى من مختلف الجامعات السورية </h5>" , unsafe_allow_html=True)  
        st.markdown("<h5 style='text-align: right; color: #000000;'> حالياً لا يقبل إلا حملة الجنسية العربية السورية أو من في حكمهم لكنه يقبل الشهادات الثانوية المعادلة للشهادة الثانوية السورية العامة العلمية </h5>" , unsafe_allow_html=True)
        st.write("---")
        st.markdown("<h2 style='text-align: right; color: #00B0F0;'> صفحات الجامعة على مواقع التواصل </h2>" , unsafe_allow_html=True)
        st.write("<a href='https://www.facebook.com/hiast.edu.sy' style='text-align: right; color: #0030f0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>  Facebook-فيسبوك 🟦 </a>", unsafe_allow_html=True)
    if selectuni=="الرسوم الدراسية":
        st.markdown("<h3 style='text-align: right; color: #0070C0;'> الطلاب الموفودين </h3>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> الطالب الموفد هو طالب متعاقد مع جهة تمول دراسته كوزارة التعليم العالي أو مركز الدراسات والبحوث العلمية وغيرهما، وذلك مقابل التزام بالخدمة كمهندس بعد التخرج في هذه الجهة. تحدد كل جهة موفدة الراتب والميزات الأخرى الممنوحة لطلابها وكذلك طبيعة الالتزامات بعد التخرج. يتقاضى الطلاب الموفدون لصالح مركز الدراسات والبحوث العلمية مثلاً راتباً طيلة فترة دراستهم بنجاح في المعهد العالي ويُقدر بـ /772.032/ ل.س خلال سنوات الدراسة الخمسة مقابل التزام بالخدمة في المركز كمهندسين بعد التخرج لمدة تساوي مثليّ مدة الدراسة بما فيها سنوات الرسوب. يستمر الراتب طيلة أشهر السنة أي حتى في فترة العطل الصيفية. يتأخر بدء صرفه بعد بدء الدوام في السنة الأولى لشهر أو شهرين ريثما تأخذ الإجراءات الرسمية وقتها الكافي </h5>" , unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: right; color: #0070C0;'> طالب دراسة خاصة </h3>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'>  يدرس على حسابه الشخصي، أي يدفع قسـطاً سـنوياً قدره / 3.000.000 / ل.س فقـط ثلاثة ملايين ليرة سورية عن كل سنة من سنوات الدراسة حيث تسدد الأقساط والرسوم عن السنة الدراسية دفعة واحدة وخلال أسبوع من تاريخ صدور لوائح القبول في المفاضلة، وإلا يعتبر قبوله لاغياً. في المقابل لا التزامات تجاه أية جهة على طالب الدراسة الخاصة بعد التخرج، كما أن المعهد العالي غير ملزم بتوظيفه، مع إمكانية حصول ذلك إن رغب الخريج واقتضت الحاجة،شأنه شأن أي مهندس يتقدم بطلب توظيف إلى المعهد العالي. لا يتضمن قسط الدراسة تكاليف السكن والطعام  </h5>" , unsafe_allow_html=True)
    if selectuni=="المنشآت التابعة":
        st.markdown("<h3 style='text-align: right; color: #00B0F0;'> السكن الجامعي </h3>" , unsafe_allow_html=True)
        llc,rrc=st.columns(2)
        with llc:
            st.markdown("<h5 style='text-align: right; color: #000000;'>: أجور السكن الجامعي الشهرية  </h5>" , unsafe_allow_html=True)
            st.write("""
\nللطالب الموفد لصالح المعهد العالي
\n· طالب هندسة من السنوات الأولى حتى الثالثة 8000 ل.س
\n· طالب هندسة من السنتين الرابعة والخامسة 8000 ل.س
\nلطالب الدراسة الخاصة ولموفدي الوزارات
\n· طالب هندسة من السنوات الأولى حتى الثالثة 10000 ل.س
\n· طالب هندسة من السنتين الرابعة والخامسة 12000 ل.س
""")
        with rrc:    
           st.markdown("<h5 style='text-align: right; color: #000000;'>: ميزات وخصائص السكن الجامعي </h5>" , unsafe_allow_html=True)
           st.write("""  
             \nالمكتبة وقاعات للمطالعة.
\nلندوة وصالة التلفزيون.
\nصالة حواسيب شخصيّة مخصصة لتحضير وظائف الطلاب ومشاريعهم.
\nقاعة غسيل وكي مركزيّة وأخرى فرعية للطالبات والطلاب.
\nصالة استقبال الزوّار.
\nعيادة طبيّة للإسعافات الليليّة.       
  الغرف إفرادية                  
                    """)  
    if selectuni==" أقسام المعهد":
        font="""
        <style>
        html {{
        font-size: 3rem;
        }}
        </style>
        """
        st.write("""
    \nقسم المعلوميات
\nقسم الاتصالات
\nقسم الرياضيات
\nقسم النظم الإلكترونية والميكانيكية
\nفرع حلب (هندسة الطيران)
\nقسم الفيزياء
\nقسم هندسة الإدارة
\nمخبر الدراسات البيئية
\nمركز تعليم اللغات
    """)
