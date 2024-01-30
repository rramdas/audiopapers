from io import BytesIO
from time import sleep
import time
from gtts import gTTS
import streamlit as st

upload_pdf = st.file_uploader("Upload a pdf file to get started.")


def text_to_speech(text):
    sound_file = BytesIO()
    tts = gTTS(text, lang='en') 
    tts.write_to_fp(sound_file)
    return sound_file


if upload_pdf is not None:

    # read file as bytes
    
    bytes_data = upload_pdf.read()
    
    # check file is a pdf
    if upload_pdf.type == "application/pdf": 

        # check file has bytes
        if bytes_data is None:

            # report to user that file is empty
            st.error("File is empty. Please upload a valid pdf file.")

        else:

            with open("test.pdf", "wb") as f:
                f.write(bytes_data)

            # st.success("Saved file")
            
            #show url to the file
            
            # st.info("File location: {}".format("test.pdf"))

            progress_text = "Operation in progress. Please wait."
            my_bar = st.progress(0, text=progress_text)

            for percent_complete in range(100):
                 time.sleep(0.1)
                 my_bar.progress(percent_complete + 1, text=progress_text)

            sound_file = text_to_speech("hello world")

            st.audio(sound_file)
            



# streamlist will host the uploader
# on render we will create a parser that will extract the text from the pdf
# and then send it to a text to speech api that use coquis voice library
# to generate an audio file
# the audio file will be returned to the user via the streamlit app
# the user will be able to stream the audio file and add notes to the file

