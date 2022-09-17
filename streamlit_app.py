import streamlit as st
from PIL import Image


im2 = Image.open('christmas card.jpg')
im1 = Image.open('canvas3.png')

back_im = im1.copy()
back_im.paste(im2, (50, 100))
back_im.save('frame-test.jpg', quality=95)

st.image(back_im)
