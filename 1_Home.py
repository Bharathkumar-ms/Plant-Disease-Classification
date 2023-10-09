import streamlit as st 
import base64
st.title("Plant Disease Detection ")

#####################Set background################
#######################################################################
from PIL import Image
image = Image.open('./show-photo/plant.jpeg')
st.image(image, caption='')


st.markdown(
    '''
    ### Introduction

###### The primary objective of this project is to detect and classify plant diseases at an early stage. Early detection can help farmers take timely action to prevent the spread of diseases and minimize crop loss.


'''
)








