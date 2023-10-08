import qrcode
import streamlit as st
from PIL import Image
import base64
import time


# Constants
timestr = time.strftime("%Y%m%d-%H%M%S")
app_title = 'QR Code Generator'
qr_name = 'qrcode.png'
placeholder = 'https://'
noQR = True

def create_qr_code(url, logo=None):
    if url != '':
        noQR = False
        basewidth = 100
        qr = qrcode.QRCode(version=5, box_size=10, border=5)
        qr.add_data(url)
        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        # if user upload logo, then add it to the qr code
        if logo != None:
            logo = Image.open(logo)
            wpercent = (basewidth/float(logo.size[0]))
            hsize = int((float(logo.size[1])*float(wpercent)))
            logo = logo.resize((basewidth, hsize), Image.LANCZOS)
            pos = ((img.size[0] - logo.size[0]) // 2,(img.size[1] - logo.size[1]) // 2)
            img.paste(logo, pos)
            qr.make(fit = True)
        # save img 
        img.save(qr_name)
        qr_image = Image.open('qrcode.png')
        get_img(qr_image)
    else:
        noQR = True
    return qr_name


def create_app_instance(title):
    st.title(title)
    url = st.text_input(label='Enter URL', placeholder=placeholder)
    userimg = st.file_uploader(label='Upload Picture for QR Code Decoration', key='upload')
    img_name = create_qr_code(url, userimg)
    img = open(img_name,'rb')
    st.download_button(label='Download', data=img, file_name='img.png', mime="image/png")


def get_img(file_name):
    st.image(file_name, width=300)
    



# The Actuation
create_app_instance(app_title)
