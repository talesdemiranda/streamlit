import streamlit as st
st.set_page_config("Projeto Stremlit Tales", layout="wide")
state = st.session_state

from streamlit_option_menu import option_menu
import yaml
import streamlit_authenticator as stauth  # pip install streamlit-authenticator
import os
# requirements.txt https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/app-dependencies#add-python-dependencies

import base64

st.markdown(
    """
    <style>
	 .css-ffhzg2 {
        background: url("./img/blue_abstract_background.jpg")
    }
	 .css-6qob1r {
			
			background: lightblue	
	 }
    </style>
    """,
    unsafe_allow_html=True
)

@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }

    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg(f'{os.path.dirname(os.path.realpath(__file__))}/img/blue_abstract_background.jpg')

#reference https://github.com/mkhorasani/Streamlit-Authenticator
#			  https://discuss.streamlit.io/t/new-component-streamlit-authenticator-a-secure-authenticaton-module-to-validate-user-credentials-in-a-streamlit-application/18893
#with open('./seguranca/config.yaml') as file: #Remoto
with open(os.path.dirname(os.path.realpath(__file__))+'/seguranca/config.yaml') as file: #Remoto
    config = yaml.load(file, Loader=yaml.SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:

#if seguranca.check_password():

	menu_esquerdo              = ["Cadastro", "Adesão", "Arrecadação", "Instituto", "Configuração"]
	menu_esquerdo_icone        = ['people-fill', 'card-list', 'cash-coin', 'bounding-box', 'gear']

	with st.sidebar:
		
		#image = Image.open(local_image)
		#st.image(image, width=30, )

		selected_left_menu = option_menu("Tales",
													menu_esquerdo, 
													icons=menu_esquerdo_icone,
													menu_icon="eyeglasses",
													default_index=0
									)

		authenticator.logout('Sair', 'main')
