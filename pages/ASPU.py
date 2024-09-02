import streamlit as st
from openpyxl import load_workbook
from PIL import Image
from streamlit_option_menu import option_menu
from st_pages import hide_pages
icon = Image.open("images/cap.png")
st.set_page_config(page_title="College Path- جامعة الشام", page_icon=icon, layout= "wide")
def cost(unicost):
    for costs in unicost:
        if len(costs)==5:  
            st.markdown("<h4 style='text-align: right; color: #0070c0;'>"+ costs[0] +"</h4>" , unsafe_allow_html=True) 
            st.markdown("<h5 style='text-align: right; color: #000000;'> رسم الساعة المعتمد للسوريين المقيمين ومن بحكمهم بالليرة السورية:"+ costs[1] +"</h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'>الحد الأعلى لرسم السنة الدراسية بالليرة السورية:"+ costs[2] +"</h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> للسوريين غير المقيمين بالدولار الأمريكي:"+ costs[3] +"</h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> للعرب والأجانب بالدولار الأمريكي :"+ costs[4] +"</h5>" , unsafe_allow_html=True)
        if len(costs)==3:  
            st.markdown("<h4 style='text-align: right; color: #0070c0;'>"+ costs[0] +"</h4>" , unsafe_allow_html=True) 
            st.markdown("<h5 style='text-align: right; color: #000000;'> رسم الساعة المعتمد للسوريين المقيمين ومن بحكمهم بالليرة السورية:"+ costs[1] +"</h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'>الحد الأعلى لرسم السنة الدراسية بالليرة السورية:"+ costs[2] +"</h5>" , unsafe_allow_html=True)
        if len(costs)==2:
            st.markdown("<h4 style='text-align: right; color: #0070c0;'>"+ costs[0] +"</h4>" , unsafe_allow_html=True) 
            st.markdown("<h5 style='text-align: right; color: #000000;'> رسم الساعة المعتمد للسوريين المقيمين ومن بحكمهم بالليرة السورية:"+ costs[1] +"</h5>" , unsafe_allow_html=True)
    return
hide_pages(["AAST","sp","majors","universities","application","DU","DU", "Website", "AU",'ANTU','MU','QAU','ASPU','EBU','HPU','ANU','ANU','JU','AUST','SU','IU','CU','WPU','YU','RU','WU','IUST','SPU','AIU','KU','HU','SVU','EU','TU','TAU','BU','HIAST'])
Page_header=f"""
<style> 
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
        menu_title="جامعة الشام الخاصة",
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
    gmap="""<p><iframe src="https://www.google.com/maps/d/embed?mid=1h7FxwY1EvIkIiMNy0edTUgY88uiIlqQ&ehbc=2E312F" width="100%" height="600" style="border:10;" allowfullscreen="True" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></p>"""
    st.markdown(gmap, unsafe_allow_html=True)
if select=="معلومات عن الجامعة":
    st.write("###")
    st.markdown("<h2 style='text-align: right; color: #00B0F0;'> جامعة الشام الخاصة </h2>" , unsafe_allow_html=True)
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
            image=Image.open("pictures/ASPU.jpeg")
            st.image(image)
        with r:
            st.write("<a href='https://www.aspu.edu.sy/site/arabic/index.php' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'> الموقع الإلكتروني🌐 </a>", unsafe_allow_html=True)
            st.write("<a href='https://www.google.com/maps/place/%D8%AC%D8%A7%D9%85%D8%B9%D8%A9+%D8%A7%D9%84%D8%B4%D8%A7%D9%85+%D8%A7%D9%84%D8%AE%D8%A7%D8%B5%D8%A9%E2%80%AD/@33.5058553,36.2854831,18.25z/data=!4m6!3m5!1s0x1518e0cbe1bca71d:0x4414acfcf9061e30!8m2!3d33.5058463!4d36.2862841!16s%2Fg%2F11c575kwhp?authuser=0&entry=ttu' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'> الموقع على الخريطة🗺  </a>", unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> نوع الجامعة : خاصة </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> ترتيب الجامعة على سوريا حسب ويبوميتريكس : 13 </h5>" , unsafe_allow_html=True)
        st.write("---")
        st.markdown("<h2 style='text-align: right; color: #00B0F0;'> نبذة عن الجامعة </h2>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> جامعة الشام الخاصة هي جامعة سورية خاصة ومقرها مدينة دمشق، أحدثت عام 2011 بموجب المرسوم التشريعي رقم (97) في تاريخ 28 يوليو 2011. ولدى الجامعة فرع في مدينة اللاذقية </h5>" , unsafe_allow_html=True)  
        st.write("---")
        st.markdown("<h2 style='text-align: right; color: #00B0F0;'> صفحات الجامعة على مواقع التواصل </h2>" , unsafe_allow_html=True)
        st.write("<a href='https://ar-ar.facebook.com/Al.Sham.University/' style='text-align: right; color: #0030f0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>  Facebook-فيسبوك 🟦 </a>", unsafe_allow_html=True)
        st.write("<a href='https://twitter.com/private_sham' style='text-align: right; color: #020209; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>  X (Twitter) - إكس (تويتر) ✖ </a>", unsafe_allow_html=True)
        st.write("<a href='https://www.youtube.com/channel/UCJ2FdU3vNAc2kd-36EErARQ?view_as=subscriber' style='text-align: right; color: #f02020; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>  YouTube-يوتيوب 🟥 </a>", unsafe_allow_html=True)
    if selectuni=="الرسوم الدراسية":
        st.markdown("<h3 style='text-align: right; color: #0070c0;'> أقساط الجامعة </h3>" , unsafe_allow_html=True)
        fees=load_workbook('c:/cp/tuition.xlsx')
        activefees=fees.active
        counter=1
        allfees=[]
        for loop in range(29):
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
        majors=["الطب البشري","طب الأسنان","الصيدلة","العلاقات الدبلوماسية","الهندسة المعلوماتية","الحقوق","العلوم الإدارية"]
        for major in allfees:
            if major[0] in majors:
                list.append(major)
        cost(list)
        st.markdown("<h3 style='text-align: right; color: #00B0F0;'>(3/2024) تكاليف المواصلات 🚌</h3>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> بين 78 و280 ألف ليرة سورية شهرياً باستخدام وسائل النقل العامة حسب البعد عن الكلية </h5>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> بين 300 و800 ألف ليرة سورية شهرياً باستخدام وسائل نقل خاصة </h5>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> نقل الجامعة الرسمي نحو 800 ألف ليرة شهرياً وهي متوفرة لفرع التل </h5>" , unsafe_allow_html=True)
        st.write("<a href='https://www.aspu.edu.sy/site/arabic/index.php?node=55175&nid=14922&' style='text-align: right; color: #0090e0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'> للمزيد من المعلومات </a>", unsafe_allow_html=True)    
    if selectuni=="المنشآت التابعة":    
        st.markdown("<h3 style='text-align: right; color: #00B0F0;'> السكن الجامعي </h3>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'>: تقييم السكن الجامعي </h5>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'>  وفرت الجامعة خدمة السكن الطلابي في مقر الجامعة الدائم (التل) </h5>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'>  يتألف مبنى السكن الطلابي من /6/ طوابق المكون من قسمين متناظرين قسم للذكور وقسم للإناث ولكل قسم مدخل خاص به كما يحتوي على /220/ غرفة  </h5>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> الطابق الأول: بمساحة /917م2/ يحتوي على /20/ غرفة بمساحة /15 م2/ تتسع لشخصين كما أن كل طابق مجهز بعدد من دورات المياه والمطابخ </h5>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> الطابق الثاني والثالث والرابع والخامس: بمساحة /1288 م2/ يحتوي على /40/ غرفة بمساحة /15 م2/ تتسع لشخصين كما أن كل طابق مجهز بعدد من دورات المياه والمطابخ </h5>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> الطابق السادس: بمساحة /1288 م2/ يحتوي على /40/ غرفة VIP تتسع لشخص واحد بمساحة /15 م2/  وكل غرفة مجهزة بدورة مياه وبوفيه ترفيهي </h5>" , unsafe_allow_html=True)
    if selectuni=="كليات الجامعة":
        font="""
        <style>
        html {{
        font-size: larger;
        }}
        </style>
        """
        st.markdown("<h4 style='text-align: right; color: #0070c0;'> فرع دمشق - البرامكة </h4>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> كلية الحقوق </h5>" , unsafe_allow_html=True) 
        st.markdown("<h5 style='text-align: right; color: #000000;'> كلية العلوم الإدارية </h5>" , unsafe_allow_html=True)  
        st.markdown("<h4 style='text-align: right; color: #0070c0;'> فرع دمشق - المزرعة </h4>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> كلية طب الأسنان </h5>" , unsafe_allow_html=True)  
        st.markdown("<h4 style='text-align: right; color: #0070c0;'> فرع دمشق - التل </h4>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> كلية الطب البشري </h5>" , unsafe_allow_html=True) 
        st.markdown("<h5 style='text-align: right; color: #000000;'> كلية الصيدلة </h5>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> كلية الهندسة </h5>" , unsafe_allow_html=True) 
        st.markdown("<h5 style='text-align: right; color: #000000;'> كلية العلاقات الدولية والدبلوماسية </h5>" , unsafe_allow_html=True)  
        st.markdown("<h4 style='text-align: right; color: #0070c0;'> فرع اللاذقية - الصليبة </h4>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> كلية طب الأسنان </h5>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> كلية الصيدلة </h5>" , unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right; color: #000000;'> كلية الحقوق </h5>" , unsafe_allow_html=True) 
        st.markdown("<h5 style='text-align: right; color: #000000;'> كلية العلوم الإدارية </h5>" , unsafe_allow_html=True)

