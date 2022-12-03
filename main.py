import streamlit as st
st.set_page_config("Projeto Stremlit Tales", layout="wide")
from streamlit_option_menu import option_menu
import streamlit_authenticator as stauth  # pip install streamlit-authenticator
import yaml

#reference https://github.com/mkhorasani/Streamlit-Authenticator
with open('./seguranca/config.yaml') as file:
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
