import streamlit
import requests 
from streamlit_lottie import st_lottie 
from PIL import Image

# https://www.webfx.com/tools/emoji-cheat-sheet/ 
streamlit.set_page_config(page_title="My web page with Streamlit", page_icon="rocket", layout="wide")


# LOAD CSS
def local_css(file_name):
    with open(file_name) as f:
        streamlit.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/styles.css") # Your Route



# LOAD LOTTIE ANIMATION
# Take a look: https://lottiefiles.com/
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# IMG/LOTTIE ANIMATIONS
lottie_codding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_vbaerjlq.json")
img_contact_1 = Image.open("img/1.jpg") # From your IMG folder
img_contact_2 = Image.open("img/3.jpg") # From your IMG folder




with streamlit.container():
    streamlit.subheader("Hi there!")
    streamlit.title("I am a freelance developer")
    streamlit.write("I use different technologies like Python, HTML, CSS, and more...")
    streamlit.write("[Learn More >](http://google.com)") # Link 


# What I do 
with streamlit.container():
    streamlit.write("---") # Separator
    left_column, right_column = streamlit.columns(2)
    with left_column:
        streamlit.header("What I do")
        streamlit.write("##")
        streamlit.write(
            """
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ipsam ex necessitatibus dolor incidunt omnis sint possimus deserunt accusantium veritatis culpa quas, dolores praesentium aut nisi expedita explicabo eum corrupti reiciendis?
            Minima eum molestiae, autem, ut modi ab harum quidem sunt aliquid, deserunt corrupti amet saepe quis! Illum, tempore voluptate adipisci ut consequuntur ipsa sunt velit, fuga quaerat delectus eos vitae?
            Beatae saepe vitae quae tempora incidunt molestias quas ducimus dolorum optio omnis, iure quis nostrum itaque quo quaerat nihil porro nobis corporis illum sunt exercitationem excepturi eaque totam. Consequuntur, debitis?
            """
        )

        streamlit.write("[YouTube Chanel >] (http://youtube.com)") # Link


    with right_column:
        st_lottie(lottie_codding, height=300, key="coding")


with streamlit.container():
    streamlit.write("---")
    streamlit.header("My projects")
    streamlit.write("##")
    image_column, text_column = streamlit.columns((1, 2)) 
    with image_column:
        streamlit.image(img_contact_1)
    with text_column:
        streamlit.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        streamlit.write(
            """
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ipsam ex necessitatibus dolor incidunt omnis sint possimus deserunt accusantium veritatis culpa quas, dolores praesentium aut nisi expedita explicabo eum corrupti reiciendis?
            Minima eum molestiae, autem, ut modi ab harum quidem sunt aliquid, deserunt corrupti amet saepe quis! Illum, tempore voluptate adipisci ut consequuntur ipsa sunt velit, fuga quaerat delectus eos vitae?
            Beatae saepe vitae quae tempora incidunt molestias quas ducimus dolorum optio omnis, iure quis nostrum itaque quo quaerat nihil porro nobis corporis illum sunt exercitationem excepturi eaque totam. Consequuntur, debitis?
            """
        )

        streamlit.markdown("[Watch Video...]((http://youtube.com))") # Link



with streamlit.container():
    image_column, text_column = streamlit.columns((1,2))
    with image_column:
        streamlit.image(img_contact_2)
    with text_column:
        streamlit.subheader("How to Add a Contact Form To your Streamlit App")
        streamlit.write(
            """
            Want to add a contact form to your Streamlit App?
            In this tutorial I'm going to show you how to do it
            """
        )
        streamlit.markdown("[Watch Video...]((http://youtube.com))") # Link


with streamlit.container():
    streamlit.write("---")
    streamlit.header("Get in touch!")
    streamlit.write("##")

    contact_form = """
        <form action="https://formsubmit.co/YOUR_EMAIL" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email"  required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
    
    left_column, right_column = streamlit.columns(2)
    with left_column:
        streamlit.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        streamlit.empty()
