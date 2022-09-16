import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt

#First Image
image_one = Image.open("Capture.PNG") 

#Second Image
image_two = Image.open("github.PNG")

Image.Image.paste(image_one, image_two)

fig = plt.figure()
plt.imshow(image_one)
plt.axis("off")
st.pyplot(fig)