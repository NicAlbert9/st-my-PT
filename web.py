from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title='My Webpage', page_icon=':tada:', layout='wide')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl('https://lottie.host/b6dd1398-6a4b-4305-8f71-ce33a5457ed7/ditYDZht48.json')
img_contact_form = Image.open('images/th.jfif')

with st.container():
 st.subheader('Wassup, Spreken at your Service :wave:')
 st.title('A Student from SNSU')
 st.write('I am something everyone know yet sometimes everyone doesnt know me')


with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
      st.header('Disco')
      st.write('####')
      st.write('so i do not know what to write here')
      st.write('in this side idk what to do')
    with right_column:
        st_lottie(lottie_coding, height = 300, key='coding')

with st.container():
    st.write('---')
    st.header('My projects')
    st.write('##')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader('My Waifuuu :heart_on_fire:')
        st.write(
            """
            I don't know this gal but she a beauty hehehe
            """
        )
        st.markdown('[Watch my other waifu hahah...](https://ph.images.search.yahoo.com/search/images;_ylt=AwrPqiPLwGllrRIXHJi1Rwx.;_ylu=c2VjA3NlYXJjaARzbGsDYnV0dG9u;_ylc=X1MDMjExNDczNDAwNQRfcgMyBGZyA21jYWZlZQRmcjIDcDpzLHY6aSxtOnNiLXRvcARncHJpZANxemJYQld3QlNBdTZvOS4yQS5OMUJBBG5fcnNsdAMwBG5fc3VnZwMxMARvcmlnaW4DcGguaW1hZ2VzLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzYEcXVlcnkDbmV6dWtvBHRfc3RtcAMxNzAxNDI5NDYy?p=nezuko&fr=mcafee&fr2=p%3As%2Cv%3Ai%2Cm%3Asb-top&ei=UTF-8&x=wrt&type=E210PH91215G0#id=14&iurl=https%3A%2F%2Fwww.nawpic.com%2Fmedia%2F2020%2Fnezuko-nawpic-26.jpg&action=click)')


