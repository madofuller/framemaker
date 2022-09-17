import streamlit as st
from PIL import Image


im1 = Image.open('christmas card.jpg')
im2 = Image.open('canvas3.png')

back_im = im1.copy()
back_im.paste(im2, (100, 50))
back_im.save('frame-test.jpg', quality=95)
