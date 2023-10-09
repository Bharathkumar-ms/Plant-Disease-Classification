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

### Motive

###### For this challenge, we used the “plant_disease” dataset. This dataset contains an open access repository of images on plant health to enable the development of web disease diagnostics. The dataset contains 87,0000 images. The images span 14 crop species: Apple, Blueberry, Cherry, Grape, Orange, Peach, Bell Pepper, Potato, Raspberry, Soybean, Squash, Strawberry, and Tomato. It contains images of 17 fundal diseases, 4 bacterial diseases, 2 molds (oomycete) diseases, 2 viral diseases, and 1 disease caused by a mite. 12 crop species also have images of healthy leaves that are not visibly affected by a disease.


'''
)








