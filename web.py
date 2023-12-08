from PIL import Image
import streamlit as st

st.set_page_config(page_title='Aspects Webpage', page_icon='😱', layout='wide')

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css.txt")

img_contact_form= Image.open('images/maxresdefault.jpg')
silop_cave= Image.open('images/silop_cave.jpg')
mabua_beach= Image.open('images/mabua_beach.jpg')
floatingvil= Image.open('images/Floatingvil.jpg')
sagisiisland= Image.open('images/sagisi.jfif')
Buenavista= Image.open('images/buenavistacave.jpg')
lakemainit= Image.open('images/Lake-Mainit.jpg')
alingkakajaw= Image.open('images/alingkakajaw.jpg')
battleofsurigao= Image.open('images/battle_of_surigao.jpg')
balingangafalls= Image.open('images/balinganga.jpeg')
songkoycoldspring= Image.open('images/songkoy-cold-spring.jpg')


with st.container():
    st.title('------------------------------Welcome to my Webpage------------------------------')
with st.container():
    column1, column2, column3 = st.columns((1, 1.1, 1))
    with column2:
     st.subheader('-----------Aspect at your service-------------')

with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
      st.header('Programming Project')
      st.write('####')
      st.write('Make Webpage using Streamlit')
      st.write('Then Host your [Streamlit](https://streamlit.io/) app on [Github](https://github.com/)')
      st.write('[Click Here for Tutorial](https://blog.streamlit.io/host-your-streamlit-app-for-free/)')
    with right_column:
        st.empty()

with st.container():
    st.write('###')
    st.write('###')
    st.write('---')
with st.container():
     left, center, right = st.columns((1.5,2,1.5))
     with center:
         st.title('Things to do in Surigao City')

with st.container():
    column, column2, colum = st.columns((0.01, 2, 0.01))
    with column2:
      st.write('###')
      st.image(img_contact_form)
    with colum:
        st.empty()
    with column:
        st.empty()

with st.container():
    st.write('---')
    st.header('Silop Multi-Caves')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(silop_cave)
    with text_column:
        st.subheader('Silop Multi_Caves')
        st.write(
            """One of Suirgao City's tourist attraction, Silop Cave is a multi cave system located just few minutes
            away from the city proper. It is composed of six cave systems of which the two are open for tourist 
            exploration.
            """
        )
        st.markdown('[Learn more...](https://www.tripadvisor.com.ph/Attraction_Review-g1459886-d2043745-Reviews-Silop_Multi_Caves-Surigao_City_Surigao_del_Norte_Province_Mindanao.html)')

with st.container():
    st.write('##')
    st.header('Mabua Pebble Beach')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(mabua_beach)
    with text_column:
        st.subheader('Mabua Pebble Beach')
        st.write(
            """Mabua Pebble Beach, located 30 minutes from the city center of Surigao, 
            stands out among Filipino beaches due to its unique shoreline composed of smooth white pebbles. 
            Unlike most beaches formed by wind and wave movements, Mabua Pebble Beach likely resulted from strong 
            forward swashing waves pushing pebbles onshore and weaker return swashing waves depositing the material. 
            The varied sizes and shapes of the pebbles, mainly oval, have a dual purpose—aside from their aesthetic 
            appeal, walking barefoot on them is considered therapeutic by reflexologists due to the feet's reflex points 
            connected to internal organs.
        """
        )
        st.markdown('[Learn more...](https://guidetothephilippines.ph/destinations-and-attractions/mabua-pebble-beach)')

with st.container():
    st.write('##')
    st.header('Day-Asan Floating Villages')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(floatingvil)
    with text_column:
        st.subheader ('Day-Asan Floating Villages')
        st.write(
            """No words can probably describe the beauty and silent charm of Day-asan Floating Village in Surigao City. 
            Hailed as the “Little Venice of Surigao City”, the village is a fishing village consisting of houses on 
            wooden stilts above the water. It is a barangay in Surigao City, the capital of the province of Surigao del 
            Norte in the Caraga Region of Mindanao.
            """
        )
        st.markdown('[Learn more...](https://www.vigattintourism.com/tourism/articles/Day-asan-Floating-Village-Little-Venice-of-Surigao-City)')

with st.container():
    st.write('##')
    st.header('Sagisi Island')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(sagisiisland)
    with text_column:
        st.subheader ('Day-Asan Floating Villages')
        st.write(
            """No words can probably describe the beauty and silent charm of Day-asan Floating Village in Surigao City. 
            Hailed as the “Little Venice of Surigao City”, the village is a fishing village consisting of houses on 
            wooden stilts above the water. It is a barangay in Surigao City, the capital of the province of Surigao del 
            Norte in the Caraga Region of Mindanao.
            """
        )
        st.markdown('[Learn more...](https://www.vigattintourism.com/tourism/articles/Day-asan-Floating-Village-Little-Venice-of-Surigao-City)')

with st.container():
    st.write('##')
    st.header('Buenavista Cave')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(Buenavista)
    with text_column:
        st.subheader ('Buenavista Cave')
        st.write(
            """Buenavista Cave is primarly a dripstone cave. The wealth of formations is named King's Court, as it 
            resembles a huge group of persons. Some 100 meters from the main entrance is an underground pool which is 
            knee deep. The cave has three different entrances. Buenavista Cave is located at Barangay Buenavista on 
            Hikdop Island and is reached from the capital in 45 minutes by pumpboat.
        """
                 )
        st.markdown('[Learn more...](https://www.traveltothephilippines.info/2020/07/05/buenavista-cave-amazing-stone-formation/)')

with st.container():
    st.write('##')
    st.header('Lake Mainit')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(lakemainit)
    with text_column:
        st.subheader ('Lake Mainit')
        st.write(
            """Lake Mainit, lake on the border of Surigao del Norte and Agusan del Sur provinces, northeastern Mindanao,
             Philippines. It is the country’s fourth largest lake and has an area of 58 sq mi (150 sq km). Its outlet is 
             the Tubay River, which flows southward before entering Butuan Bay of the Mindanao Sea. Lake Mainit is skirted 
             on the east by the Philippine–Japan Friendship Highway, connecting Surigao and Davao. The area has secondary
              forests, and rice, corn (maize), and bananas are grown.
            """
        )
        st.markdown('[Learn more...](https://lmda.wordpress.com/about-lake-mainit/)')

with st.container():
    st.write('##')
    st.header('Alingkakajaw Islands')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(alingkakajaw)
    with text_column:
        st.subheader ('Alingkakajaw Islands')
        st.write(
            """Alingkakajaw Island was a symbol of fighting little paradise behind the huge mining activities but still 
            lots of attraction from the incoming visitors whether international or local because of its presence in the 
            sea, perfectly untouched and unexploited little paradise. Those bypassing visitors when crossing the port of 
            Hayanggabon en route to Bucas Grande Islands will ever make a turn to look into something beautiful and 
            endearing that will make their day alive and thinking about something pleasant that is going to happen.
            """
        )
        st.markdown('[Learn more...](https://www.expedia.com.ph/Alingkakajaw-Island-Surigao.d553248621562598253.Place-To-Visit)')

with st.container():
    st.write('##')
    st.header('Batlle of Suirgao Strait Museum')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(battleofsurigao)
    with text_column:
        st.subheader ('Batlle of Suirgao Strait Museum')
        st.write(
            """Surigao City — The Battle of Surigao Strait (BOSS) Memorial and Museum officially opened to the public 
            here with the presence of dignitaries and ships from the Royal Australian Navy (RAN), the Philippine Navy 
            (PN) and the Philippine Coast Guard (PSG).
            """
        )
        st.markdown('[Learn more...](https://mindanaogoldstardaily.com/archives/104068)')

with st.container():
    st.write('##')
    st.header('Balinganga Falls')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(balingangafalls)
    with text_column:
        st.subheader ('Balinganga Falls')
        st.write(
            """Surigao del Sur is one of the provinces in the Philippines which is famous for its mysterious yet amazing tourist spots.

You might have heard some of the famous tourist spots in Surigao del Sur like the magical river or the breath-taking 
waterfalls. Indeed, Surigao del Sur is a blessed with beautiful destinations. Facing the Pacific Ocean, its stunning 
islands are inviting for some island-hopping activities.
            """
        )
        st.markdown('[Learn more...](https://touristspotsfinder.com/surigao-del-sur-tourist-spots/)')

with st.container():
    st.write('##')
    st.header('Songkoy Cold Spring')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(songkoycoldspring)
    with text_column:
        st.subheader ('Songkoy Cold Spring')
        st.write(
            """Surigao del Sur is one of the provinces in the Philippines which is famous for its mysterious yet amazing tourist spots.
You might have heard some of the famous tourist spots in Surigao del Sur like the magical river or the breath-taking 
waterfalls. Indeed, Surigao del Sur is a blessed with beautiful destinations. Facing the Pacific Ocean, its stunning 
islands are inviting for some island-hopping activities.
            """
        )
        st.markdown('[Learn more...](https://touristspotsfinder.com/surigao-del-sur-tourist-spots/)')


with st.container():
    st.write('---')
    st.header('Get in Touch with me!')
    st.write('##')

    contact_form = """
    <form action="https://formsubmit.co/beboyimba30@email.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email"placeholder="Your email" required>
     <textarea name="message" placeholder="Your message" required></textarea>
     <button type="submit">Send</button>
</form>
"""
    left_column, mid_column, right_column = st.columns((2, 2 , 2))
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
    with mid_column:
        st.empty()
