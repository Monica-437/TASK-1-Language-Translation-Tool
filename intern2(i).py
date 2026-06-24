
import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import base64
import pyperclip
import os

st.set_page_config(
    page_title="AI Smart Language Translator",
    page_icon="",
    layout="wide"
)

st.markdown("""
<style>

.main{
background:linear-gradient(135deg,#00c6ff,#0072ff);
padding:20px;
border-radius:20px;
}

.title{
font-size:48px;
font-weight:bold;
text-align:center;
color:white;
animation: glow 2s infinite;
}

.subtitle{
font-size:20px;
text-align:center;
color:white;
}

@keyframes glow{
0%{text-shadow:0 0 5px white;}
50%{text-shadow:0 0 20px yellow;}
100%{text-shadow:0 0 5px white;}
}

.stButton>button{
background:linear-gradient(90deg,#ff512f,#dd2476);
color:white;
font-size:18px;
font-weight:bold;
border-radius:12px;
height:50px;
width:100%;
border:none;
}

textarea{
border-radius:15px;
}

.result{
background:linear-gradient(90deg,#11998e,#38ef7d);
padding:20px;
border-radius:15px;
font-size:22px;
font-weight:bold;
color:white;
}

.metric{
background:#f5f5f5;
padding:15px;
border-radius:10px;
text-align:center;
}

</style>
""",unsafe_allow_html=True)

st.markdown("""
<div class="main">
<div class="title"> AI SMART LANGUAGE TRANSLATOR</div>
<div class="subtitle">
Translate into multiple languages instantly using Artificial Intelligence
</div>
</div>
""",unsafe_allow_html=True)

languages={
"English":"en",
"Tamil":"ta",
"Hindi":"hi",
"French":"fr",
"German":"de",
"Spanish":"es",
"Italian":"it",
"Portuguese":"pt",
"Japanese":"ja",
"Korean":"ko",
"Chinese":"zh-CN",
"Arabic":"ar",
"Malayalam":"ml",
"Telugu":"te",
"Kannada":"kn",
"Bengali":"bn",
"Gujarati":"gu",
"Punjabi":"pa",
"Russian":"ru"
}

st.write("")

c1,c2=st.columns(2)

with c1:
    source=st.selectbox(" Source Language",list(languages.keys()))

with c2:
    target=st.selectbox(" Target Language",list(languages.keys()))

text=st.text_area(
"✍ Enter Text",
height=180,
placeholder="Type your sentence here..."
)

col1,col2,col3=st.columns(3)

translate=col1.button("Translate")
swap=col2.button("Swap")
copybtn=col3.button(" Copy")

st.write("### Statistics")

m1,m2,m3=st.columns(3)

m1.metric("Characters",len(text))
m2.metric("Words",len(text.split()))
m3.metric("Languages",len(languages))

if swap:
    temp=source
    source=target
    target=temp
    st.success("Languages Swapped")

translation=""

if translate:

    if text.strip()=="":

        st.error("Please enter some text.")

    else:

        with st.spinner("Translating..."):

            translator=GoogleTranslator(
                source=languages[source],
                target=languages[target]
            )

            translation=translator.translate(text)

        st.balloons()

        st.success("Translation Completed Successfully")

        st.write("## ✅ Result")

        st.markdown(
        f"""
        <div class="result">
        {translation}
        </div>
        """,
        unsafe_allow_html=True
        )

        tts=gTTS(
        text=translation,
        lang=languages[target]
        )

        tts.save("voice.mp3")

        audio=open("voice.mp3","rb")
        st.audio(audio.read())

        b64=base64.b64encode(
        translation.encode()
        ).decode()

        href=f'<a href="data:file/txt;base64,{b64}" download="Translation.txt">Download Translation</a>'

        st.markdown(href,unsafe_allow_html=True)

        st.write("")

        st.info("Tip: You can translate into multiple languages instantly.")

if copybtn:

    if translation!="":

        pyperclip.copy(translation)

        st.success("Copied Successfully")

st.sidebar.title(" AI Dashboard")


st.sidebar.write("")

st.markdown("---")

st.markdown(
"""
<center>
<h3 style='color:blue;'>
Developed as an Artificial Intelligence Mini Project
</h3>

<h4 style='color:red;'>
 Smart • Fast • Beautiful • Interactive 
</h4>

</center>
""",
unsafe_allow_html=True
)

