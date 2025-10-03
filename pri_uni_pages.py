import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from st_pages import hide_pages
from openpyxl import load_workbook
def cost(unicost):
    for costs in unicost: 
        st.markdown("<h4 style='text-align: right; color: #0070c0;'>"+ str(costs[0]) +"</h4>" , unsafe_allow_html=True) 
        st.markdown("<h5 style='text-align: right; color: #000000;'> رسم الساعة المعتمد للسوريين المقيمين والغير مقيمين ومن بحكمهم بالدولار الأمريكي :"+ costs[1] +"</h5>" , unsafe_allow_html=True)
        if costs[2]:    
            st.markdown("<h5 style='text-align: right; color: #000000;'>الحد الأعلى لرسم السنة الدراسية بالدولار الأمريكي:"+ str(costs[2]) +"</h5>" , unsafe_allow_html=True)
            if costs[3]:    
                st.markdown("<h5 style='text-align: right; color: #000000;'> للعرب والأجانب بالدولار الأمريكي :"+ str(costs[3]) +"</h5>" , unsafe_allow_html=True)
    return
def Uni_Page(uniname,nickname,map_link,uni_image,website,location,rank,description,note,majors,social_media,colleges=[],unihospitals=[],High_inst=[],Mid_inst=[],campus_housing=True):
    icon = Image.open("images/cap.png")
    st.set_page_config(page_title="College Path-"+uniname, page_icon=icon, layout= "wide")
    hide_pages(["AAST","sp","majors","universities","application","DU","DU", "Website", "AU",'ANTU','MU','QAU','ASPU','EBU','HPU','ANU','ANU','JU','AUST','SU','IU','CU','WPU','YU','RU','WU','IUST','SPU','AIU','KU','HU','SVU','EU','TU','TAU','BU','HIAST'])
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
    p{{text-align:right}}
    h1,h2,h3,h4,h5,h6{{direction: rtl}}
    """
    textwrap=f"""
    .st-emotion-cache-1lvxfs7{{
        word-break: auto-phrase;
            text-wrap: auto
    }}"""
    st.markdown("<style>"+textwrap+Page_header+hide_img_fs+SidebarStyle+"</style>",unsafe_allow_html=True)
    with st.sidebar:
        logo = Image.open("images/logo.png")
        st.image(logo)
        st.write("###")
        select = option_menu(
            menu_icon="bank2",
            menu_title=nickname,
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
        gmap=f"""<p><iframe src={map_link} width="100%" height="600" style="border:10;" allowfullscreen="True" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></p>"""
        st.markdown(gmap, unsafe_allow_html=True)
    if select=="معلومات عن الجامعة":
        st.markdown(f"<h2 style='text-align: right; color: #00B0F0;'> {uniname} </h2>" , unsafe_allow_html=True)
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
                image=Image.open(f"pictures/{uni_image}")
                st.image(image)
            with r:
                st.write(f"<a href='{website}' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'> الموقع الإلكتروني🌐 </a>", unsafe_allow_html=True)
                st.write(f"<a href='{location}' style='text-align: right; color: #0070C0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'> الموقع على الخريطة🗺  </a>", unsafe_allow_html=True)
                st.markdown("<h5 style='text-align: right; color: #000000;'> نوع الجامعة : حكومية </h5>" , unsafe_allow_html=True)
                st.markdown(f"<h5 style='text-align: right; color: #000000;'> ترتيب الجامعة على العالم حسب ويبوميتريكس : {rank} </h5>" , unsafe_allow_html=True)        
            st.write("---")
            st.markdown("<h2 style='text-align: right; color: #00B0F0;'> نبذة عن الجامعة </h2>" , unsafe_allow_html=True)
            st.markdown(f"<h5 style='text-align: right; color: #000000;'>{description}</h5>" , unsafe_allow_html=True)  
            if note:
                st.markdown(f"<h5 style='text-align: right; color: #00b0f0;'>{note}</h5>" , unsafe_allow_html=True)              
            st.write("---")
            st.markdown("<h2 style='text-align: right; color: #00B0F0;'> صفحات الجامعة على مواقع التواصل </h2>" , unsafe_allow_html=True)
            for link in social_media:
                if "youtube" in link:
                    st.write(f"<a href='{link}' style='text-align: right; color: #f02020; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>  YouTube-يوتيوب 🟥 </a>", unsafe_allow_html=True)
                if "facebook" in link:
                    st.write(f"<a href='{link}' style='text-align: right; color: #0030f0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>  Facebook-فيسبوك 🟦 </a>", unsafe_allow_html=True)
                if "instagram" in link:
                    st.write(f"<a href='{link}' style='text-align: right; color: #d0d010; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>  Instagram-إنستاغرام 🟨 </a>", unsafe_allow_html=True)
                if "t.me" in link:    
                    st.write(f"<a href='{link}' style='text-align: right; color: #0090e0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>  Telegram-تيليغرام 🔷 </a>", unsafe_allow_html=True)
                if "twitter" in link:    
                    st.write(f"<a href='{link}' style='text-align: right; color: #020209; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>  X (Twitter) - إكس (تويتر) ✖ </a>", unsafe_allow_html=True)
                if "linkedin" in link:   
                    st.write(f"<a href='{link}' style='text-align: right; color: #0010d0; font-weight: bolder; font-weight: 600; font-size: 1.2rem;'>  LinkedIN-لينكدإن 🔷 </a>", unsafe_allow_html=True)

        if selectuni=="الرسوم الدراسية":
            fees=load_workbook('tuition.xlsx')
            activefees=fees.active
            counter=1
            allfees=[]
            for loop in range(44):
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
            for major in allfees:
                if major[0] in majors:
                    list.append(major)
            cost(list)
            st.markdown("<h3 style='text-align: right; color: #00B0F0;'> تكاليف المواصلات 🚌</h3>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> بين 60 و180 ألف ليرة سورية شهرياً باستخدام وسائل النقل العامة حسب البعد عن الكلية </h5>" , unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: right; color: #000000;'> بين 100 و500 ألف ليرة سورية شهرياً باستخدام وسائل نقل خاصة أو بالاتفاق مع سائق حافلة أو أجرة حسب البعد عن الكلية </h5>" , unsafe_allow_html=True)

        if selectuni=="المنشآت التابعة":
            llc,rrc=st.columns(2)
            with llc:
                st.markdown("<h3 style='text-align: right; color: #00B0F0;'> السكن الجامعي </h3>" , unsafe_allow_html=True)
                if campus_housing:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> زودت الغرف بأثاث متكامل مميز يتناسب مع حاجات الطالب،كما تمّ تزويد الغرف بخط إنترنت وخط هاتف مما يتيح للطلبة استمرار التواصل مع المجتمع الخارجي المرافق العامة المتوفرة في السكن الجامعي تشمل  المطابخ والأجهزة الكهربائية وقاعة لمشاهدة التلفاز، والمصاعد الكهربائية فضلاً عن التدفئة المركزية والمياه الساخنة على مدار العام </h5>" , unsafe_allow_html=True)
                    image=Image.open("pictures/KUcampus.png")
                    st.image(image) 
                else:
                    st.markdown("<h5 style='text-align: right; color: #000000;'> خدمة السكن غير متوفرة في الجامعة </h5>" , unsafe_allow_html=True)
            with rrc:
                if unihospitals:    
                    st.markdown("<h3 style='text-align: right; color: #00B0F0;'> المشافي الجامعية </h3>" , unsafe_allow_html=True)
                    for hospital in unihospitals:    
                        st.markdown(f"<h5 style='text-align: right; color: #000000;'> {hospital} </h5>" , unsafe_allow_html=True)
            il,ir=st.columns(2)
            with il:
                if High_inst:
                    st.markdown("<h4 style='text-align: right; color: #0070C0;'> المعاهد العليا :</h4>" , unsafe_allow_html=True)
                    for inst in High_inst:    
                        st.markdown(f"<h5 style='text-align: right; color: #000000;'>{inst}</h5>" , unsafe_allow_html=True)
                
            with ir:
                if Mid_inst:
                    st.markdown("<h4 style='text-align: right; color: #0070C0;'> المعاهد التقانية :</h4>" , unsafe_allow_html=True)
                    for inst in Mid_inst:    
                        st.markdown(f"<h5 style='text-align: right; color: #000000;'>{inst}</h5>" , unsafe_allow_html=True)
        if selectuni=="كليات الجامعة":
            for subject in colleges:
                title=True
                for college in subject:
                    if title:
                        st.markdown(f"<h3 style='text-align: right; color: #0070c0;'>{college}</h3>" , unsafe_allow_html=True)
                        title=False
                    else:
                        st.markdown(f"<h5 style='text-align: right; color: #000000;'>{college}</h5>" , unsafe_allow_html=True)
                    