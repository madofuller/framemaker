import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt



st.file_uploader(Frame)
st.file_uploader(Art)
#First Image
image_one = Image.open(Art) 

#Second Image
image_two = Image.open(Frame)

Image.Image.paste(image_one, image_two)

fig = plt.figure()
plt.imshow(image_one)
plt.axis("off")
st.pyplot(fig)
