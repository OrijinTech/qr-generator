import qrcode
import streamlit as st
from PIL import Image
import base64
import time


# Constants
timestr = time.strftime("%Y%m%d-%H%M%S")
app_title = 'QR Code Generator'
qr_name = 'qrcode.png'

def create_qr_code(url):
    qr = qrcode.QRCode(version=5, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit = True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(qr_name)
    qr_image = Image.open('qrcode.png')
    get_img(qr_image)
    return qr_name


def create_app_instance(title):
    placeholder = 'https://'
    st.title(title)
    url = st.text_input(label='Enter URL', placeholder=placeholder)
    img_name = create_qr_code(url)
    img = open(img_name,'rb')
    st.file_uploader(label='Upload Picture', key='upload')
    st.download_button(label='Download', data=img, file_name='img.png', mime="image/png")


def get_img(file_name):
    st.image(file_name, width=300)
    



# The Actuation
create_app_instance(app_title)
