from bs4 import BeautifulSoup
import shutil
import pathlib
import logging
import streamlit as st


def add_meta_tags():
    # Replace with your own meta tags
    meta_tags = '''
    <!-- Primary Meta Tags -->
    <meta name="title" content="College Path - مسار الجامعة" />
    <meta name="description" content="كل ما يحتاجه الطالب من شرح عن المفاضلة والاختصاصات الجامعية، ابحث عن الجامعة المناسبة في قائمة تضم جميع الجامعات السورية!!" />

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://collegepath.onrender.com/" />
    <meta property="og:title" content="College Path - مسار الجامعة" />
    <meta property="og:description" content="كل ما يحتاجه الطالب من شرح عن المفاضلة والاختصاصات الجامعية، ابحث عن الجامعة المناسبة في قائمة تضم جميع الجامعات السورية!!" />
    <meta property="og:image" content="https://raw.github.com/HannaJAlkhoury/CollegePath/main/images/mthumbnail.webp" />

    <!-- X (Twitter) -->
    <meta property="twitter:card" content="summary_large_image" />
    <meta property="twitter:url" content="https://collegepath.onrender.com/" />
    <meta property="twitter:title" content="College Path - مسار الجامعة" />
    <meta property="twitter:description" content="كل ما يحتاجه الطالب من شرح عن المفاضلة والاختصاصات الجامعية، ابحث عن الجامعة المناسبة في قائمة تضم جميع الجامعات السورية!!" />
    <meta property="twitter:image" content="https://raw.github.com/HannaJAlkhoury/CollegePath/main/images/mthumbnail.webp" />

'''

    # Locate Streamlit’s index.html inside site-packages
    index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
    backup_path = index_path.with_suffix(".bck")

    # Backup once
    if not backup_path.exists():
        shutil.copy(index_path, backup_path)

    # Load HTML safely
    soup = BeautifulSoup(index_path.read_text(encoding="utf-8"), "html.parser")

    # Prevent duplicate injection
    if not soup.find("meta", {"name": "description", "content": "This is my custom Streamlit app deployed on Render."}):
        html = str(soup).replace("</head>", meta_tags + "\n</head>")
        # Write to temp file first (UTF-8!)
        temp_file = index_path.with_suffix(".tmp")
        temp_file.write_text(html, encoding="utf-8")

        # Verify and replace
        if "<meta name=" in temp_file.read_text(encoding="utf-8"):
            shutil.move(temp_file, index_path)

# Run before Streamlit
add_meta_tags()