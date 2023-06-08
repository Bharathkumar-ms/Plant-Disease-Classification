import streamlit as st 
import base64
st.title("Plant Disease Detection ")

#####################Set background################
#######################################################################
from PIL import Image
image = Image.open('./show-photo/plant.jpeg')
st.image(image, caption='')






