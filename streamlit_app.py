import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt



#First Image
image_one = Image.open("christmas card.jpg") 

#Second Image
image_two = Image.open("test.png")

st.image(image_one)
st.image(image_two)
