import streamlit as st
from streamlit_extras import add_vertical_space as avs
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

load_dotenv()

# set page config
st.set_page_config(
    page_title="crowd density detection",
    page_icon="📃",
    layout="wide",
)
st.title("crowd density detection")

# Display a message with a LinkedIn profile link
st.write("Developed by [Jitendra-Kumar](https://www.linkedin.com/in/jitendra-ky)")

avs.add_vertical_space(4)

# set genai api configuration
genai.configure(api_key="AIzaSyA7DPMBYgeuLSySIB7hDHNeF8qFahSjzB4")
# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
)

# ATS tracking application
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"], help="Please upload the image")
submit = st.button("Submit")


c1, c2 = st.columns([1, 1])
if submit:
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        with c1:
            st.image(image, caption='Uploaded Image')

        # Pass the image file path to the model
        response = model.generate_content([image, "you just have to give a number between 1 to 100, 1 means very less crowd and 100 means very high crowd density. | your response must be a int type no text | if input is invllid then it wil return 0"])
        with c2:
            upto = int(response.text.strip())
            st.write(f"## crowd level is : {upto} %")
            progress_bar = st.progress(upto/100)


    else:
        st.error("Please upload the image")



st.write("## or you can just drag and drop below sample image in the box")
st.image("sample.png", caption='Sample Image')


